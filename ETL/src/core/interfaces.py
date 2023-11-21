
from ..core.logger import logger

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

    def start_process(self):
        # self.verify_os()
        pass


class BaseOperationalSystemVerification(ABC):

    @abstractmethod
    def verify_os_by_platform_lib(self):
        pass

    @abstractmethod
    def verify_os_by_os_lib(self):
        pass

    def start_process(self):
        platform_os_name = self.verify_os_by_platform_lib()
        os_os_name = self.verify_os_by_os_lib()
        logger().info(platform_os_name)
        logger().info(os_os_name)