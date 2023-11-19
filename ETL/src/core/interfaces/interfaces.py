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
    def manipulating_content(self, information_keys: list):
        pass

    def start_process(self):
        print(self.check_status)
        information_key = self.get_response_content()
        self.manipulating_content(information_keys = information_key)