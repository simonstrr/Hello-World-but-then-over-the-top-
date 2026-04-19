import asyncio
import fcntl
import json
import os
import pty
import struct
import sys
import termios
from pathlib import Path

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).parent
app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


@app.get("/")
async def root():
    return HTMLResponse((BASE_DIR / "static" / "index.html").read_text())


@app.websocket("/ws")
async def terminal_ws(websocket: WebSocket):
    await websocket.accept()

    master_fd, slave_fd = pty.openpty()
    _set_winsize(master_fd, rows=50, cols=220)

    proc = await asyncio.create_subprocess_exec(
        sys.executable, "-u", str(BASE_DIR / "main.py"),
        stdin=slave_fd,
        stdout=slave_fd,
        stderr=slave_fd,
        env={**os.environ, "TERM": "xterm-256color", "PYTHONUNBUFFERED": "1"},
        close_fds=True,
    )
    os.close(slave_fd)

    loop = asyncio.get_event_loop()
    stop = asyncio.Event()

    async def pty_to_ws():
        while not stop.is_set():
            try:
                data = await loop.run_in_executor(None, _read_pty, master_fd)
                if data is None:
                    break
                await websocket.send_bytes(data)
            except Exception:
                break
        stop.set()

    async def ws_to_pty():
        while not stop.is_set():
            try:
                text = await asyncio.wait_for(websocket.receive_text(), timeout=1.0)
                msg = json.loads(text)
                if msg.get("type") == "resize":
                    _set_winsize(master_fd, rows=msg.get("rows", 50), cols=msg.get("cols", 220))
            except asyncio.TimeoutError:
                continue
            except (WebSocketDisconnect, Exception):
                break
        stop.set()

    try:
        await asyncio.gather(pty_to_ws(), ws_to_pty())
    finally:
        stop.set()
        try:
            proc.kill()
        except ProcessLookupError:
            pass
        try:
            os.close(master_fd)
        except OSError:
            pass


def _read_pty(fd: int, size: int = 4096) -> bytes | None:
    try:
        return os.read(fd, size)
    except OSError:
        return None


def _set_winsize(fd: int, rows: int, cols: int) -> None:
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", rows, cols, 0, 0))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")
