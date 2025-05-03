from colorama import Fore, Style, init

init(autoreset=True)

def colored(text: str, color: str) -> str:
    color_map = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "white": Fore.WHITE
    }

    return color_map.get(color.lower(), Fore.WHITE) + text + Style.RESET_ALL
