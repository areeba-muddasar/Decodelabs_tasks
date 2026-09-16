"""
colors.py
ANSI color codes for beautiful terminal output.
Project 4: Image & Text Recognition — DecodeLabs AI Internship
"""

import os

# Enable ANSI colors on Windows
if os.name == 'nt':
    os.system('')


class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'


def ok(text):
    return f"{Colors.GREEN}[OK]{Colors.RESET} {text}"


def info(text):
    return f"{Colors.CYAN}[INFO]{Colors.RESET} {text}"


def warn(text):
    return f"{Colors.YELLOW}[WARN]{Colors.RESET} {text}"


def error(text):
    return f"{Colors.RED}[ERROR]{Colors.RESET} {text}"


def detected(text):
    return f"{Colors.BRIGHT_MAGENTA}[DETECTED]{Colors.RESET} {text}"


def success(text):
    return f"{Colors.BRIGHT_GREEN}{Colors.BOLD}[PASS]{Colors.RESET} {text}"


def heading(text):
    return f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{text}{Colors.RESET}"


def title(text):
    return f"{Colors.BOLD}{Colors.BRIGHT_YELLOW}{text}{Colors.RESET}"


def divider(char='=', length=55):
    return f"{Colors.BRIGHT_BLUE}{char * length}{Colors.RESET}"


def banner(text, width=62):
    pad = (width - len(text) - 2) // 2
    line = '#' * width
    return (
        f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{line}{Colors.RESET}\n"
        f"{Colors.BOLD}{Colors.BRIGHT_YELLOW}{' ' * pad}{text}{Colors.RESET}\n"
        f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{line}{Colors.RESET}"
    )