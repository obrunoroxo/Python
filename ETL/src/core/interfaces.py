
from ..core.logger import logger
from ..core.treatments import treatment
from ..core.exceptions import (
    OperationalSystemValueError,
    OperationalSystemUnknownValueError
)

from abc import (
    ABC,
    abstractmethod,
    abstractproperty,
    abstractclassmethod,
    abstractstaticmethod
)


class BaseHardCode(ABC):
    '''
        [ INFORMATION IS REQUIRED ABOUT WHAT THIS CLASS AND YOUR FUNCTIONS DOES, ITS EXECUTION ORDER, AMONG OTHERS... ]
    '''

    @abstractmethod
    @abstractproperty
    def check_status(self) -> int:
        pass


    @abstractmethod
    def get_response_content(self) -> list:
        pass


    @abstractmethod
    def manipulating_content(self, checked_content: dict):
        pass


    def start_process(self):
        logger().info(self.check_status)
        checked_content = self.get_response_content()
        self.manipulating_content(checked_content = checked_content)


class BaseColorUtils(ABC):
    '''
        [ INFORMATION IS REQUIRED ABOUT WHAT THIS CLASS AND YOUR FUNCTIONS DOES, ITS EXECUTION ORDER, AMONG OTHERS... ]
    '''

    

    def start_process(self):
        # self.verify_os()
        pass


class BaseOperationalSystemVerification(ABC):

    @property
    @abstractmethod
    def verify_os_by_platform_lib( self ) -> None:
        pass


    @property
    @abstractmethod
    def verify_os_by_os_lib( self ) -> None:
        pass


    def verification_os( self, operational_system_os_lib, operational_system_platform_lib ) -> str:
        boolean_os_lib, boolean_platform_lib = treatment( f_value = operational_system_os_lib, f_type = str, s_value = operational_system_platform_lib, s_type = str)
        print( boolean_os_lib, boolean_platform_lib )
        # if ( isinstance( operational_system_os_lib, str ) and not str( operational_system_os_lib ).isalpha() ) or (isinstance( operational_system_platform_lib, str ) and not str(operational_system_platform_lib).isalpha()):
        #     try:
        #         operational_system_os_lib = str(operational_system_os_lib)
        #         operational_system_platform_lib = str(operational_system_platform_lib) 
        #     except Exception as e: # Create a single and specific error exception
        #         logger().error(e)
        #         raise OperationalSystemUnknownValueError( value = str(e) if e else None )
        # elif isinstance( operational_system_os_lib, str ) and isinstance( operational_system_platform_lib, str ):
        #     if operational_system_os_lib == 'posix' and operational_system_platform_lib == 'Linux' or operational_system_platform_lib == 'Darwin':
        #         return 'clear'
        #     elif operational_system_os_lib == 'nt' and operational_system_platform_lib == 'Windows':
        #         return 'cls'
        # else:
        #     raise OperationalSystemValueError( value = str(operational_system_platform_lib, operational_system_os_lib))

        if operational_system_os_lib == 'nt' and operational_system_platform_lib == 'Windows':
            return 'cls'
        elif operational_system_os_lib == 'posix' and operational_system_platform_lib == 'Linux' or 'Darwin':
            return 'clear'
 
        else:
            return logger().error(' Oops! Operating system found is invalid or unknown...')


    def start_process( self ):
        os_os_name = self.verify_os_by_os_lib
        platform_os_name = self.verify_os_by_platform_lib
        logger().info(platform_os_name)
        logger().info(os_os_name)
        verified_os_command = self.verification_os( operational_system_os_lib = 14, operational_system_platform_lib = platform_os_name )

        return verified_os_command