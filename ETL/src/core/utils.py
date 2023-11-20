import colorama
import typing as T

class __win_color_schemes:
    def __init__(self) -> None:
        self.RESET_ALL = colorama.Style.RESET_ALL
        self.BRIGHT = colorama.Style.BRIGHT
        self.DIM = colorama.Style.DIM
        self.RED = colorama.Fore.RED
        self.BLUE = colorama.Fore.BLUE
        self.CYAN = colorama.Fore.CYAN
        self.MAGENTA = colorama.Fore.MAGENTA
        self.YELLOW = colorama.Fore.YELLOW
        self.GREEN = colorama.Fore.GREEN
        self.RED_BACK = colorama.Back.RED

class __other_color_scheme:
    def __init__(self) -> None:
        self.RESET_ALL = r"\033[0m",
        self.BRIGHT = r"\033[1m",
        self.DIM = r"\033[2m",
        self.RED = r"\033[31m",
        self.BLUE = r"\033[34m",
        self.CYAN = r"\033[36m",
        self.MAGENTA = r"\033[35m",
        self.YELLOW = r"\033[33m",
        self.GREEN = r"\033[32m",
        self.RED_BACK = r"\033[41m"

class WinColors(__win_color_schemes):
    def __init__( self, **kwargs) -> None:
        super().__init__(**kwargs)

class OtherColors(__other_color_scheme):
    def __init__( self, **kwargs) -> None:
        super().__init__(**kwargs)