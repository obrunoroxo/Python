from abc import (
    ABC,
    abstractmethod,
    abstractproperty,
    abstractclassmethod,
    abstractstaticmethod
)


class BaseHardCode(ABC):
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
        print(self.check_status)
        checked_content = self.get_response_content()
        self.manipulating_content(checked_content = checked_content)