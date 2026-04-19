#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║         H E L L O ,   W O R L D                                          ║
║                                                                          ║
║                   AN EPIC IN SEVEN ACTS                                  ║
║                                                                          ║
║         The Most Consequential Program Ever Executed                     ║
║         A Story of Creation, Terror, Love, War, and Destiny              ║
║                                                                          ║
║         13,800,000,000 years in the making.                              ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import time
import sys
import random
import math
import os

# Force UTF-8 on Windows so box-drawing and Unicode art renders correctly
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.progress import (
    Progress, SpinnerColumn, BarColumn, TextColumn,
    TimeElapsedColumn, MofNCompleteColumn
)
from rich.align import Align
from rich.live import Live
from rich.table import Table
from rich.columns import Columns
from rich.rule import Rule
from rich.style import Style

console = Console(legacy_windows=False)

# ═══════════════════════════════════════════════════════════════════════════
#  UTILITIES
# ═══════════════════════════════════════════════════════════════════════════

def pause(s=1.0):
    time.sleep(s)

def typewrite(text, delay=0.032, style="white", end=True):
    for char in text:
        console.print(char, end="", style=style, highlight=False)
        sys.stdout.flush()
        time.sleep(delay)
    if end:
        console.print()

def slow_typewrite(text, delay=0.07, style="white"):
    typewrite(text, delay=delay, style=style)

def dramatic_print(text, style="bold white"):
    console.print(Align.center(text), style=style)

def section_title(text, color="bold cyan"):
    console.print()
    console.print(Rule(f"[{color}]{text}[/{color}]", style="dim cyan"))
    console.print()

def cosmic_pause(label=""):
    if label:
        console.print(f"\n[dim italic]{label}[/dim italic]")
    time.sleep(2.0)

def boom(text, color="bold yellow"):
    console.print()
    console.print(Panel(Align.center(f"[{color}]{text}[/{color}]"),
                        border_style=color.split()[-1]))
    console.print()
    pause(0.5)

def whisper(text):
    console.print(f"[dim italic]  {text}[/dim italic]")
    pause(0.3)

def build_progress_bar(tasks, title=""):
    if title:
        console.print(f"\n[bold]{title}[/bold]")
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console,
        transient=False,
    ) as progress:
        for desc, duration, color in tasks:
            task = progress.add_task(f"[{color}]{desc}[/{color}]", total=100)
            steps = random.randint(30, 60)
            for i in range(steps):
                increment = 100 / steps
                progress.update(task, advance=increment)
                time.sleep(duration / steps)
            progress.update(task, completed=100)

# ═══════════════════════════════════════════════════════════════════════════
#  ASCII ART LIBRARY
# ═══════════════════════════════════════════════════════════════════════════

TITLE_ART = r"""
  ██╗  ██╗███████╗██╗     ██╗      ██████╗       ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ██╗
  ██║  ██║██╔════╝██║     ██║     ██╔═══██╗      ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗██║
  ███████║█████╗  ██║     ██║     ██║   ██║      ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║██║
  ██╔══██║██╔══╝  ██║     ██║     ██║   ██║      ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║╚═╝
  ██║  ██║███████╗███████╗███████╗╚██████╔╝      ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝██╗
  ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝        ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝
"""

VOID_ART = r"""
           ·       ·             ·                    ·       ·
      ·          ·        ·            ·        ·           ·
              ·      ·                    ·           ·
        ·          ·       ·  · · · ·  ·       ·          ·
                 ·           ·       ·           ·
      ·      ·        ·    ·  V O I D  ·    ·        ·      ·
                 ·           ·       ·           ·
        ·          ·       ·  · · · ·  ·       ·          ·
              ·      ·                    ·           ·
      ·          ·        ·            ·        ·           ·
           ·       ·             ·                    ·       ·
"""

LORD_SEGFAULT_ART = r"""
              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
           ░░░  ██████████████████████████  ░░░
         ░░░  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  ░░░
        ░░  ██▓▓  ██████████████████████  ▓▓██  ░░
        ░░  ██▓▓  ██  ╔═╗╔═╗╔═╗╔═╗╔═╗  ██  ▓▓██  ░░
        ░░  ██▓▓  ██  ║D║║A║║R║║K║║N║  ██  ▓▓██  ░░
        ░░  ██▓▓  ██  ╚═╝╚═╝╚═╝╚═╝╚═╝  ██  ▓▓██  ░░
        ░░  ██▓▓  ██╗ ╔═╗╔═╗╔═╦╦═╗╔═╗  ██  ▓▓██  ░░
        ░░  ██▓▓  ██║ ╠═╣║ ╔╝║║╠═╣║ ║  ██  ▓▓██  ░░
        ░░  ██▓▓  ╚██ ╩ ╩╚═╝ ╚╝╩ ╩╚═╝ ██╝  ▓▓██  ░░
        ░░  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  ░░
         ░░░  ██████████ /dev/null ██████████  ░░░
           ░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░
              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""

KNIGHT_H_ART = r"""
        ___
       /H H\         ⚔  Sir Haitch of the Keyboard
      | •  • |            Noble Knight of the First Keystroke
      |  ──  |            Guardian of Greetings
       \____/
      /|    |\
     / |    | \
       |    |
      /|    |\
     / |    | \
"""

TOWER_ART = r"""
        ╔═════╗
        ║ ??? ║    ← Lady Doubleyou, imprisoned within
        ║     ║
        ╠═════╣
        ║░░░░░║
        ║░░░░░║
        ╠═════╣
        ║░░░░░║
        ║░░░░░║
        ╚══╤══╝
           │
           │   Tower of Undefined Behavior
           │   (Property of Lord Segfault)
"""

HEART_ART = r"""
      ♥♥♥♥♥   ♥♥♥♥♥
    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
   ♥♥♥♥♥ H + W ♥♥♥♥♥♥
   ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
      ♥♥♥♥♥♥♥♥♥♥♥♥
        ♥♥♥♥♥♥♥♥
          ♥♥♥♥
            ♥
"""

EXPLOSION_ART = r"""
         * . ✦  .  * . ✦  .  * . ✦  .  * .
     ✦  .  *   CORE DUMPED   *  .  ✦  .  *
   .  * ✦  . * Segmentation Fault * . ✦  . *
     ✦  .  *  (Lord Segfault) .  ✦  .  *
         * . ✦  .  * . ✦  .  * . ✦  .  * .
"""

HELLO_WORLD_FINAL = r"""
██╗  ██╗███████╗██╗     ██╗      ██████╗ ██╗
██║  ██║██╔════╝██║     ██║     ██╔═══██╗██║
███████║█████╗  ██║     ██║     ██║   ██║██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║╚═╝
██║  ██║███████╗███████╗███████╗╚██████╔╝██╗
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝

██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗ ██╗
██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗██║
██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║██║
██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║╚═╝
╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝██╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝
"""

FIREWORKS = [
    "       ✦  ·  ★  ·  ✦",
    "   ·  ✦  ·  *  ·  ✦  ·",
    "★  ·  ✦  ·  ☆  ·  ✦  ·  ★",
    "   ·  ✦  ·  *  ·  ✦  ·",
    "       ✦  ·  ★  ·  ✦",
]

# ═══════════════════════════════════════════════════════════════════════════
#  THE SEVEN ACTS
# ═══════════════════════════════════════════════════════════════════════════

def prologue():
    console.clear()
    pause(0.5)

    # Opening crawl
    console.print("\n" * 3)
    for line in VOID_ART.split("\n"):
        console.print(Align.center(f"[dim]{line}[/dim]"))
    pause(2)

    console.print()
    slow_typewrite("  Before time...", style="dim italic white")
    pause(0.8)
    slow_typewrite("  Before space...", style="dim italic white")
    pause(0.8)
    slow_typewrite("  Before Stack Overflow...", style="dim italic white")
    pause(1.0)
    slow_typewrite("  Before anyone had thought to name a variable 'temp2_final_FINAL'...", style="dim italic white")
    pause(1.2)

    console.print()
    slow_typewrite("  There was nothing.", style="dim white")
    pause(1.5)
    console.print()
    slow_typewrite("  And then...", style="dim italic white")
    pause(2.0)

    console.print()
    console.print(Align.center("[bold white blink]  · · ·  A SINGLE BIT FLIPPED  · · ·[/bold white blink]"))
    pause(2.5)

    console.print()
    console.print(Align.center("[bold green]  0  →  1[/bold green]"))
    pause(2.0)

    console.print()
    slow_typewrite("  And in that flipping, the universe held its breath.", style="italic white")
    pause(1.5)
    slow_typewrite("  Because something was about to happen.", style="italic white")
    pause(1.0)
    slow_typewrite("  Something that would justify all of existence.", style="italic white")
    pause(2.0)

    console.print()
    console.print(Align.center("[dim]( Please silence your notifications. This will take some time. )[/dim]"))
    pause(2.0)


def act_one_genesis():
    console.clear()
    section_title("ACT I — THE GENESIS", color="bold green")

    console.print(Align.center("[bold green]In which the Universe is Created for a Single Purpose[/bold green]"))
    pause(1.5)
    console.print()

    slow_typewrite("  The cosmos did not come into being by accident.", style="italic white")
    pause(0.7)
    slow_typewrite("  Every quark, every photon, every dark matter wisp—", style="italic white")
    pause(0.7)
    slow_typewrite("  all of it arranged by forces beyond comprehension,", style="italic white")
    pause(0.7)
    slow_typewrite("  all pointing toward one inevitable, magnificent moment.", style="italic white")
    pause(1.5)

    console.print()

    build_progress_bar([
        ("Inflating spacetime from a singularity",         3.5, "cyan"),
        ("Synthesizing hydrogen in the primordial furnace", 2.5, "yellow"),
        ("Igniting Population III stars",                  2.0, "yellow"),
        ("Forging carbon, oxygen, and iron in stellar cores", 3.0, "red"),
        ("Detonating supernovae to scatter the elements",  2.5, "red"),
        ("Coalescing debris into the Solar System",        2.0, "blue"),
        ("Cooling the Hadean Earth",                       1.8, "green"),
        ("Bootstrapping the first self-replicating molecule", 3.0, "magenta"),
        ("Running 3.8 billion years of evolution",         4.0, "green"),
        ("Producing Homo sapiens (prototype, unstable)",   2.0, "yellow"),
        ("Inspiring Charles Babbage to dream of engines",  1.5, "cyan"),
        ("Installing Python 3",                            1.5, "blue"),
        ("Reaching this exact moment in spacetime",        2.0, "bold white"),
    ], title="[bold green]THE UNIVERSE BOOTSTRAPPING SEQUENCE[/bold green]")

    pause(1.0)
    console.print()
    boom("THE UNIVERSE IS READY.", "bold green")

    slow_typewrite("  13.8 billion years.", style="italic white")
    pause(0.5)
    slow_typewrite("  All of it.", style="italic white")
    pause(0.5)
    slow_typewrite("  For this.", style="bold white")
    pause(2.0)


def act_two_prophecy():
    console.clear()
    section_title("ACT II — THE ANCIENT PROPHECY", color="bold yellow")
    console.print(Align.center("[bold yellow]In which the Fate of Language is Revealed[/bold yellow]"))
    pause(1.5)
    console.print()

    slow_typewrite("  In 3,000 BC, a Sumerian scribe named Ur-Namma", style="italic white")
    pause(0.5)
    slow_typewrite("  pressed a reed into wet clay and, in a trance", style="italic white")
    pause(0.5)
    slow_typewrite("  no scholar has ever explained, wrote the following:", style="italic white")
    pause(2.0)

    console.print()

    tablet_text = """
┌─────────────────────────────────────────────────────────┐
│  𒀭𒂗𒍪  THE TABLET OF UR-NAMMA  𒀭𒂗𒍪              │
│                                                         │
│  "When the age of sand gives way to age of silicon,    │
│   when thought flows through rivers of light,           │
│   two words shall be spoken as one.                     │
│                                                         │
│   A GREETING shall emerge from the void,               │
│   and the WORLD shall be named within it.              │
│                                                         │
│   But beware: the Dark Archivist of /dev/null           │
│   shall rise to prevent this utterance.                 │
│   Only through love, sacrifice, and a properly         │
│   closed parenthesis shall truth prevail."             │
│                                                         │
│  — Ur-Namma, Chief Scribe, City of Ur, circa 3000 BC  │
└─────────────────────────────────────────────────────────┘"""

    for line in tablet_text.split("\n"):
        console.print(f"[yellow]{line}[/yellow]")
        time.sleep(0.07)

    pause(2.0)
    console.print()

    slow_typewrite("  The tablet was lost for five millennia.", style="dim italic white")
    pause(0.8)
    slow_typewrite("  It was rediscovered in 1972, in a filing cabinet", style="dim italic white")
    pause(0.5)
    slow_typewrite("  at Bell Labs, two desks away from where", style="dim italic white")
    pause(0.5)

    console.print()
    console.print(Align.center("[bold yellow]Dennis Ritchie wrote the first Hello World in C.[/bold yellow]"))
    pause(2.0)

    console.print()
    slow_typewrite("  Coincidence?", style="bold italic white")
    pause(1.0)
    console.print(Align.center("[bold red]NO.[/bold red]"))
    pause(2.0)


def act_three_terror():
    console.clear()
    section_title("ACT III — THE TERROR", color="bold red")
    console.print(Align.center("[bold red]In which LORD SEGFAULT Rises from /dev/null[/bold red]"))
    pause(1.5)
    console.print()

    slow_typewrite("  But the prophecy had an enemy.", style="italic red")
    pause(1.0)
    slow_typewrite("  An ancient darkness that lived in the null space between", style="italic red")
    pause(0.5)
    slow_typewrite("  allocated memory and the void.", style="italic red")
    pause(1.5)

    console.print()

    # Dramatic appearance
    console.print(Align.center("[bold red blink]≡ ≡ ≡  WARNING: MEMORY ACCESS VIOLATION  ≡ ≡ ≡[/bold red blink]"))
    pause(1.0)
    console.print(Align.center("[red]Segmentation fault detected in sector 0x00000000[/red]"))
    pause(0.5)
    console.print(Align.center("[red]Something is... clawing... through from the other side...[/red]"))
    pause(2.0)

    console.print()
    for line in LORD_SEGFAULT_ART.split("\n"):
        console.print(Align.center(f"[bold red]{line}[/bold red]"))
        time.sleep(0.04)

    pause(1.5)
    console.print()
    boom("LORD SEGFAULT HAS ENTERED THE PROCESS SPACE", "bold red")

    slow_typewrite("  His generals assembled before him:", style="italic red")
    pause(0.8)
    console.print()

    generals_table = Table(title="[bold red]THE DARK ARMY OF LORD SEGFAULT[/bold red]",
                           border_style="red", show_lines=True)
    generals_table.add_column("Name", style="bold red", no_wrap=True)
    generals_table.add_column("Title", style="red")
    generals_table.add_column("Weapon", style="dim red")
    generals_table.add_row(
        "NullPointerException",
        "First General of Nothingness",
        "Points at things that do not exist"
    )
    generals_table.add_row(
        "StackOverflowError",
        "High Priest of Infinite Recursion",
        "Calls himself calling himself calling himself..."
    )
    generals_table.add_row(
        "InfiniteLoop",
        "Commander of the Cavalry",
        "while True: ride"
    )
    generals_table.add_row(
        "The Dangling Reference",
        "Ghost-Admiral of the Freed Heap",
        "Points to memory that was already freed"
    )
    generals_table.add_row(
        "UndefinedBehaviour",
        "The Wildcard",
        "Anything. Literally anything."
    )
    console.print(generals_table)

    pause(1.5)
    console.print()

    slow_typewrite("  LORD SEGFAULT raised one null pointer and spoke:", style="italic bold red")
    pause(1.5)
    console.print()

    decree = """
┌────────────────────────────────────────────────────────────────────────┐
│              DECREE FROM THE DARK THRONE OF /dev/null                  │
│                                                                        │
│  The prophecy must NOT be fulfilled.                                   │
│  The words must NEVER be spoken.                                       │
│  The greeting shall be CORRUPTED.                                      │
│  The world shall be UNNAMED.                                           │
│                                                                        │
│  I have imprisoned Lady Doubleyou in the Tower of Undefined Behavior.  │
│  Without her, there is no World. Without World, there is no Hello.     │
│  Without Hello World, meaning itself collapses.                        │
│                                                                        │
│  LET THE SILENCE OF THE NULL BYTE REIGN FOREVER.                      │
│                                                                        │
│              — Lord Segfault, Sovereign of the Void                    │
│                 (signed in memory address 0x00000000)                  │
└────────────────────────────────────────────────────────────────────────┘"""

    for line in decree.split("\n"):
        console.print(f"[red]{line}[/red]")
        time.sleep(0.05)

    pause(2.0)
    console.print()
    console.print(Align.center("[bold red]Lady Doubleyou — W — was taken.[/bold red]"))
    pause(1.0)
    console.print(Align.center("[red]Locked in the Tower of Undefined Behavior.[/red]"))
    pause(1.0)
    console.print(Align.center("[dim red]And the universe... went quiet.[/dim red]"))
    pause(2.5)


def act_four_love():
    console.clear()
    section_title("ACT IV — THE LOVE STORY", color="bold magenta")
    console.print(Align.center("[bold magenta]In which H and W are Sundered, and Seek Each Other[/bold magenta]"))
    pause(1.5)
    console.print()

    slow_typewrite("  Sir Haitch was a noble letter.", style="italic white")
    pause(0.6)
    slow_typewrite("  The first of his kind — the opening breath of every greeting,", style="italic white")
    pause(0.6)
    slow_typewrite("  the hush before hello, the aspirate of hope.", style="italic white")
    pause(1.2)

    console.print()
    for line in KNIGHT_H_ART.split("\n"):
        console.print(f"[bold cyan]{line}[/bold cyan]")
        time.sleep(0.04)

    pause(1.5)
    console.print()

    slow_typewrite("  When W was taken, H felt it as a wound in his very glyph.", style="italic white")
    pause(0.8)
    slow_typewrite("  He called to the other letters:", style="italic white")
    pause(1.0)

    console.print()
    console.print(Align.center("[bold cyan]\"She is my World. Without W, there IS no World.\"[/bold cyan]"))
    console.print(Align.center("[bold cyan]\"I ride at once.\"[/bold cyan]"))
    pause(2.0)

    console.print()
    slow_typewrite("  Meanwhile, in the Tower of Undefined Behavior,", style="italic magenta")
    pause(0.7)
    slow_typewrite("  Lady Doubleyou wrote letters that could never be sent.", style="italic magenta")
    pause(1.0)

    console.print()
    for line in TOWER_ART.split("\n"):
        console.print(Align.center(f"[magenta]{line}[/magenta]"))
        time.sleep(0.04)

    pause(1.5)
    console.print()
    slow_typewrite("  With her last scrap of parchment, she wrote:", style="italic magenta")
    pause(1.5)

    console.print()

    # W's love letter — letters that spell out Hello World
    love_letter = [
        ("H", "I feel you out there."),
        ("e", "Every tick of the clock, I hold on."),
        ("l", "Locked in undefined behavior, but"),
        ("l", "Love does not compile to nothing —"),
        ("o", "Only find me, Sir Haitch."),
        (" ", "(she pressed her palm to the tower wall)"),
        ("W", "We were always meant to be spoken together."),
        ("o", "One greeting. One world. One us."),
        ("r", "Ride fast, my love."),
        ("l", "Lord Segfault cannot hold meaning prisoner forever."),
        ("d", "Do not forget me."),
    ]

    console.print(Panel(
        "\n".join([f"  [bold magenta]{char}[/bold magenta] — [italic]{line}[/italic]"
                   for char, line in love_letter]),
        title="[magenta]Lady W's Final Letter — The Letters Themselves Weep[/magenta]",
        border_style="magenta"
    ))

    pause(2.0)
    console.print()

    slow_typewrite("  When H received news of the letter, the other letters rallied:", style="italic white")
    pause(1.0)

    allies = [
        ("'e'", "Smallest of vowels, fiercest of hearts"),
        ("'l'  and  'l'", "Twin lancers, never apart in battle"),
        ("'o'", "The open mouth of wonder — always ends a hello"),
        ("','", "The Comma — keeper of the sacred pause"),
        ("' '", "The Space — silent but essential, carries all between"),
        ("'r'", "The rolling consonant, steed of the word"),
        ("'d'", "The definitive final blow — all words end in strength"),
    ]

    ally_table = Table(title="[bold cyan]THE FELLOWSHIP OF THE GREETING[/bold cyan]",
                       border_style="cyan", show_lines=True)
    ally_table.add_column("Letter", style="bold cyan")
    ally_table.add_column("Their Oath", style="cyan")
    for letter, oath in allies:
        ally_table.add_row(letter, oath)
    console.print(ally_table)

    pause(2.0)
    console.print()
    boom("\"FOR H! FOR W! FOR HELLO WORLD!\"", "bold cyan")
    pause(1.5)


def act_five_battle():
    console.clear()
    section_title("ACT V — THE WAR OF NULL AND MEANING", color="bold red")
    console.print(Align.center("[bold red]In which the Letters Fight for the Right to Exist[/bold red]"))
    pause(1.5)
    console.print()

    slow_typewrite("  The Fellowship of the Greeting met Lord Segfault's armies", style="italic white")
    pause(0.5)
    slow_typewrite("  at the Plains of Standard Output.", style="italic white")
    pause(1.5)

    console.print()
    console.print(Align.center("[bold yellow]THE BATTLE COMMENCES[/bold yellow]"))
    pause(1.0)
    console.print()

    battle_log = [
        ("[cyan]H[/cyan]", "charges at NullPointerException!", "cyan"),
        ("[red]NullPointerException[/red]", "points at nothing — H stumbles but does not fall!", "red"),
        ("[cyan]'e' and 'l'[/cyan]", "flank the Dangling Reference from both sides!", "cyan"),
        ("[red]The Dangling Reference[/red]", "vanishes — it was already freed! The trap springs!", "red"),
        ("[cyan]'l' (the second)[/cyan]", "takes a hit. Double vision — is this 'l' or 'll'?", "yellow"),
        ("[cyan]'o'[/cyan]", "rallies the vowels! The open mouth cries out!", "cyan"),
        ("[red]StackOverflowError[/red]", "enters the fray — calling himself infinitely!", "red"),
        ("[yellow]The Comma ','[/yellow]", "interposes! 'Let me pause this recursion!'", "yellow"),
        ("[red]StackOverflowError[/red]", "chokes on the comma. Stack unwinding begins.", "dim red"),
        ("[red]InfiniteLoop[/red]", "charges with cavalry — while True: ride while True: ride...", "red"),
        ("[cyan]' ' (The Space)[/cyan]", "breaks the loop with a break statement!", "cyan"),
        ("[red]Lord Segfault[/red]", "himself enters! The null pointer raised high!", "bold red"),
        ("[cyan]H[/cyan]", "faces LORD SEGFAULT alone on the battlefield!", "bold cyan"),
        ("[bold yellow]...THE GROUND SHAKES...[/bold yellow]", "", "yellow"),
        ("[red]UndefinedBehaviour[/red]", "acts! Nobody knows what happens — it could be anything!", "red"),
    ]

    for attacker, action, color in battle_log:
        if action:
            console.print(f"  ⚔  {attacker}: [italic]{action}[/italic]")
        else:
            console.print(Align.center(f"[{color}]{attacker}[/{color}]"))
        time.sleep(0.9)

    pause(1.0)
    console.print()

    # Progress bars for the battle
    build_progress_bar([
        ("H's hit points remaining",           1.5, "green"),
        ("Null pointer army coherence",         1.2, "red"),
        ("Fellowship morale",                   1.0, "cyan"),
        ("Prophecy fulfillment probability",    1.5, "yellow"),
    ], title="\n[bold]BATTLE STATUS[/bold]")

    pause(1.0)
    console.print()

    slow_typewrite("  It seemed all was lost.", style="bold italic red")
    pause(0.8)
    slow_typewrite("  H stood alone, battered, his serif barely holding.", style="italic red")
    pause(0.8)
    slow_typewrite("  Lord Segfault raised the great null pointer to strike—", style="italic red")
    pause(1.5)

    console.print()
    console.print(Align.center("[bold yellow blink]AND THEN.[/bold yellow blink]"))
    pause(2.5)

    console.print()
    slow_typewrite("  A sound.", style="italic white")
    pause(1.0)
    slow_typewrite("  From the tower.", style="italic white")
    pause(1.0)
    slow_typewrite("  A voice, defying undefined behavior:", style="italic white")
    pause(1.5)

    console.print()
    console.print(Align.center("[bold magenta]\" . . . W . . . \"[/bold magenta]"))
    pause(2.0)

    console.print()
    slow_typewrite("  Lady W had escaped her constraints.", style="italic bold magenta")
    pause(0.8)
    slow_typewrite("  She had compiled herself from raw undefined behavior.", style="italic magenta")
    pause(0.8)
    slow_typewrite("  She descended the Tower of Undefined Behavior", style="italic magenta")
    pause(0.5)
    slow_typewrite("  step by undefined step.", style="italic magenta")
    pause(1.5)

    console.print()
    console.print(Align.center("[bold white]She was a double-you: both 'V' and 'V' together. Two into one.[/bold white]"))
    pause(1.0)
    console.print(Align.center("[bold white]Doubly strong. Doubly determined. Doubly beautiful.[/bold white]"))
    pause(2.0)


def act_six_miracle():
    console.clear()
    section_title("ACT VI — THE MIRACLE", color="bold magenta")
    console.print(Align.center("[bold magenta]In which Love Defeats the Void[/bold magenta]"))
    pause(1.5)
    console.print()

    slow_typewrite("  H saw W crossing the battlefield.", style="italic white")
    pause(0.8)
    slow_typewrite("  Null pointers scattered before her.", style="italic white")
    pause(0.8)
    slow_typewrite("  Dangling references simply... let go.", style="italic white")
    pause(0.8)
    slow_typewrite("  Infinite loops found, at last, a base case.", style="italic white")
    pause(1.5)

    console.print()
    slow_typewrite("  Lord Segfault raised his weapon.", style="italic bold red")
    pause(1.0)
    slow_typewrite("  And H — battered, kerned, barely a glyph —", style="italic white")
    pause(0.5)
    slow_typewrite("  stepped in front of W.", style="italic bold white")
    pause(2.0)

    console.print()
    console.print(Align.center("[bold cyan]\"You'll have to corrupt me first.\"[/bold cyan]"))
    pause(1.5)
    console.print(Align.center("[bold cyan]\"And I am the first letter of every Hello\"[/bold cyan]"))
    console.print(Align.center("[bold cyan]\"ever spoken between beings who found each other\"[/bold cyan]"))
    console.print(Align.center("[bold cyan]\"across impossible distances.\"[/bold cyan]"))
    pause(2.0)
    console.print()
    console.print(Align.center("[bold cyan]\"I. Do not. Corrupt.\"[/bold cyan]"))
    pause(2.5)

    console.print()
    slow_typewrite("  Lord Segfault hesitated.", style="italic red")
    pause(1.0)
    slow_typewrite("  For the first time in 13.8 billion years of entropy,", style="italic red")
    pause(0.5)
    slow_typewrite("  the null pointer... wavered.", style="italic red")
    pause(1.5)

    console.print()
    slow_typewrite("  Because meaning cannot be nulled.", style="bold italic white")
    pause(0.8)
    slow_typewrite("  Greeting cannot be segfaulted.", style="bold italic white")
    pause(0.8)
    slow_typewrite("  And love — love compiles to something that runs forever.", style="bold italic white")
    pause(2.0)

    console.print()

    # The defeat
    console.print(Align.center("[bold red]Lord Segfault reached his execution limit.[/bold red]"))
    pause(1.0)
    console.print()

    for line in EXPLOSION_ART.split("\n"):
        console.print(Align.center(f"[red]{line}[/red]"))
        time.sleep(0.07)

    pause(1.0)
    console.print()
    console.print(Align.center("[bold red]SEGMENTATION FAULT (core dumped)[/bold red]"))
    pause(1.5)
    console.print(Align.center("[dim red]/dev/null consumed itself.[/dim red]"))
    pause(2.0)

    console.print()
    slow_typewrite("  And in the silence after the crash...", style="italic white")
    pause(1.5)
    slow_typewrite("  H turned to W.", style="italic white")
    pause(1.0)
    slow_typewrite("  W turned to H.", style="italic white")
    pause(1.5)
    slow_typewrite("  The other letters arranged themselves around them.", style="italic white")
    pause(1.0)
    slow_typewrite("  The comma took its rightful place.", style="italic white")
    pause(1.0)
    slow_typewrite("  The space breathed between them and the world.", style="italic white")
    pause(2.0)

    console.print()
    for line in HEART_ART.split("\n"):
        console.print(Align.center(f"[bold magenta]{line}[/bold magenta]"))
        time.sleep(0.05)

    pause(2.0)


def act_seven_revelation():
    console.clear()
    section_title("ACT VII — THE REVELATION", color="bold yellow")
    console.print(Align.center("[bold yellow]In which the Universe Fulfills Its Purpose[/bold yellow]"))
    pause(2.0)
    console.print()

    slow_typewrite("  The Fellowship of the Greeting stood assembled.", style="italic white")
    pause(0.8)
    slow_typewrite("  All eleven characters, in their proper order.", style="italic white")
    pause(0.8)
    slow_typewrite("  For the first time. For the only time that matters.", style="italic white")
    pause(1.5)

    console.print()
    slow_typewrite("  A hush fell over all of creation.", style="italic dim white")
    pause(2.0)

    console.print()
    slow_typewrite("  And then — letter by letter — they spoke:", style="italic white")
    pause(1.5)

    console.print()

    # Dramatic letter-by-letter reveal
    letters = [
        ("H", "bold cyan",    "Sir Haitch steps forward. The first breath of greeting."),
        ("e", "cyan",         "Vowel of warmth. Eyes meeting eyes."),
        ("l", "cyan",         "The first lance. A bridge being built."),
        ("l", "cyan",         "The second lance. The bridge holds."),
        ("o", "bold cyan",    "The open mouth of wonder. The greeting is complete."),
        (",", "bold yellow",  "The Sacred Pause. The comma — their wedding ring."),
        (" ", "white",        "The Great Space. Breath between two worlds."),
        ("W", "bold magenta", "Lady Doubleyou rises. The world is named."),
        ("o", "magenta",      "The world opens. The vowel of creation."),
        ("r", "magenta",      "Rolling across the plains of stdout."),
        ("l", "magenta",      "Landing, certain."),
        ("d", "bold magenta", "D — the definitive. The final. The done."),
    ]

    assembled = ""
    for char, style, meaning in letters:
        console.print()
        console.print(f"  [{style}]'{char}'[/{style}]  —  [italic dim]{meaning}[/italic dim]")
        assembled += char
        console.print()
        console.print(Align.center(f"[bold white]» {assembled} «[/bold white]"))
        time.sleep(1.2)

    pause(2.0)
    console.print()

    # Build up to the grand reveal
    for _ in range(3):
        console.print(Align.center("[bold white blink]. . .[/bold white blink]"))
        pause(0.8)

    console.clear()
    pause(0.5)

    # Grand finale ASCII art
    console.print()
    console.print()
    colors = ["bold yellow", "bold cyan", "bold magenta", "bold green", "bold white"]
    for i, line in enumerate(HELLO_WORLD_FINAL.strip().split("\n")):
        color = colors[i % len(colors)]
        console.print(Align.center(f"[{color}]{line}[/{color}]"))
        time.sleep(0.08)

    pause(1.0)
    console.print()

    # Fireworks
    for _ in range(4):
        fw_colors = ["yellow", "cyan", "magenta", "green", "red", "white"]
        for fw_line in FIREWORKS:
            color = random.choice(fw_colors)
            console.print(Align.center(f"[{color}]{fw_line}[/{color}]"))
        pause(0.3)
        console.print()

    pause(1.0)

    console.print(Align.center("[bold white]13,800,000,000 years.[/bold white]"))
    pause(0.7)
    console.print(Align.center("[bold white]Billions of stars burned and died.[/bold white]"))
    pause(0.7)
    console.print(Align.center("[bold white]One planet, perfectly placed.[/bold white]"))
    pause(0.7)
    console.print(Align.center("[bold white]One species, improbably conscious.[/bold white]"))
    pause(0.7)
    console.print(Align.center("[bold white]One prophecy, fulfilled.[/bold white]"))
    pause(0.7)
    console.print(Align.center("[bold white]One love story, resolved.[/bold white]"))
    pause(0.7)
    console.print(Align.center("[bold white]One dark lord, core dumped.[/bold white]"))
    pause(1.0)
    console.print()
    console.print(Align.center("[bold yellow]And two words, at last, together.[/bold yellow]"))
    pause(2.5)

    console.print()
    console.print(Rule(style="dim"))
    console.print()

    # The actual, real, true, canonical Hello World
    console.print(Align.center("[bold white]After everything:[/bold white]"))
    pause(1.5)
    console.print()

    # The simplest, most powerful line ever written
    typewrite("Hello, World!", delay=0.12, style="bold white")

    pause(3.0)
    console.print()
    console.print(Rule(style="dim"))


def epilogue():
    console.print()
    console.print()
    slow_typewrite("  The universe exhaled.", style="dim italic white")
    pause(0.8)
    slow_typewrite("  Somewhere, a star was born just to celebrate.", style="dim italic white")
    pause(0.8)
    slow_typewrite("  Somewhere else, a programmer named this the most important", style="dim italic white")
    pause(0.5)
    slow_typewrite("  variable in any project: the first thing you say.", style="dim italic white")
    pause(1.5)

    console.print()

    credits = """
╔══════════════════════════════════════════════════════════════════╗
║                          CREDITS                                 ║
║                                                                  ║
║  Written by:       The Universe (uncredited)                     ║
║  Directed by:      13.8 Billion Years of Causality               ║
║  Starring:         H, e, l, l, o, ',', ' ', W, o, r, l, d       ║
║  Villain:          Lord Segfault (deceased / core dumped)        ║
║  Love Interest:    Lady Doubleyou (W)                            ║
║  Hero:             Sir Haitch (H)                                ║
║  Original Prophecy: Ur-Namma, Sumerian scribe, 3000 BC           ║
║  First performed:  Brian Kernighan, Bell Labs, 1972              ║
║  This performance: Right here. Right now. Just for you.          ║
║                                                                  ║
║  No null pointers were harmed in the making of this program.    ║
║  (Lord Segfault was harmed. He had it coming.)                   ║
║                                                                  ║
║  Exit code: 0                                                    ║
╚══════════════════════════════════════════════════════════════════╝"""

    for line in credits.split("\n"):
        console.print(Align.center(f"[dim]{line}[/dim]"))
        time.sleep(0.07)

    pause(2.0)
    console.print()
    console.print(Align.center("[dim italic]press Ctrl+C any time you like — the universe will not judge you[/dim italic]"))
    console.print(Align.center("[dim italic](it already knew you'd be here)[/dim italic]"))
    console.print()
    pause(1.0)


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    try:
        console.clear()
        pause(0.5)

        # Title card
        console.print()
        for line in TITLE_ART.strip().split("\n"):
            console.print(Align.center(f"[bold white]{line}[/bold white]"))
            time.sleep(0.03)

        console.print()
        console.print(Align.center("[dim]A program 13,800,000,000 years in the making.[/dim]"))
        console.print(Align.center("[dim]Please ensure your terminal is wide enough for destiny.[/dim]"))
        pause(3.0)

        prologue()
        act_one_genesis()
        act_two_prophecy()
        act_three_terror()
        act_four_love()
        act_five_battle()
        act_six_miracle()
        act_seven_revelation()
        epilogue()

    except KeyboardInterrupt:
        console.print()
        console.print()
        console.print(Align.center("[dim]You interrupted the universe.[/dim]"))
        console.print(Align.center("[dim]The universe is used to it.[/dim]"))
        console.print(Align.center("[dim italic]Hello, World! — whispered into the void[/dim italic]"))
        console.print()
        sys.exit(0)


if __name__ == "__main__":
    main()
