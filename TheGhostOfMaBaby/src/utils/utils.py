import os
import time
import platform

import typing as T

from ..utils.logger import logger
from ..utils.interfaces import BaseOperationalSystemVerification



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


def stand_by( milliseconds: T.Union[ int, float ] ) -> T.Any:
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