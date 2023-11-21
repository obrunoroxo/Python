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

    def verify_os_by_platform_lib( self ):
        # Get the operating system name by: » " platform " library.
        os_name = platform.system()

        # Get the operating system version by: » " platform " library.
        os_version = platform.version()

        # Get the machine type (e.g., 'x86_64' or 'AMD64') by: » " platform " library.
        machine_type = platform.machine()

        # Get additional system information by: » " platform " library.
        system_info = platform.uname()

        # Showing information logs by: » " platform " library.
        logger().info(f"Operating System: {os_name}")
        print('\n')
        logger().info(f"OS Version: {os_version}")
        print('\n')
        logger().info(f"Machine Type: {machine_type}")
        print('\n')
        logger().info(f"System Info: {system_info}")


    def verify_os_by_os_lib( self ):
        '''
            nt = Windows operational system
            posix = Linux operational system
        '''

        operational_system = os.name

        if operational_system == 'nt':
            # return os.system('cls')
            logger().info(operational_system)
        elif operational_system == 'posix':
            logger().info(operational_system)
        else:
            logger().error('Ops! The operational system is not supported...')


    def start_process( self ):
        self.verify_os_by_platform_lib()
        self.verify_os_by_os_lib()


def stand_by( milliseconds: T.Optional[ T.Union[ int, float ] ] ) -> None:
    return time.sleep( milliseconds )


def clear() -> None:
    os_name = __OperationalSystemVerification()
    os_name.start_process()
