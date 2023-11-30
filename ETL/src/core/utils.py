import os
import time
import platform
import colorama
import typing as T

from ..core.logger import logger
from ..core.interfaces import BaseOperationalSystemVerification

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


class WinColors( __win_color_schemes ):
    def __init__( self, **kwargs ) -> None:
        super().__init__( **kwargs )


class OtherColors( __other_color_scheme ):
    def __init__( self, **kwargs ) -> None:
        super().__init__( **kwargs )


class __OperationalSystemVerification(BaseOperationalSystemVerification):
    def __init__( self ) -> None:
        pass

    @property
    def verify_os_by_platform_lib( self ) -> str:
        '''
            Windows = Windows operational system
            Linux = Linux operational system
            Darwin = macOS Operational system
        '''

        # Get the operating system name by: » " platform " library.
        os_name = platform.system()

        # Get the operating system version by: » " platform " library.
        os_version = platform.version()

        # Get the machine type (e.g., 'x86_64' or 'AMD64') by: » " platform " library.
        machine_type = platform.machine()

        # Get additional system information by: » " platform " library.
        system_info = platform.uname()

        return os_name


    @property
    def verify_os_by_os_lib( self ) -> str:
        '''
            nt = Windows operational system
            posix = Linux / macOS operational system
        '''

        operational_system = os.name

        return operational_system



def stand_by( milliseconds: T.Optional[ T.Union[ int, float ] ] ) -> T.Any:
    return time.sleep( milliseconds )



def clear() -> None:
    os_name = __OperationalSystemVerification()
    verified_os_command = os_name.start_process()
    logger().info(verified_os_command)
    stand_by(5)

    # if verified_os_command == 'cls':
    #     os.system('cls')

    # if verified_os_command == 'clear':
    #     os.system('clear')
