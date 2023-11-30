class OperationalSystemValueError(Exception):
    def __init__(
        self,
        value: str | None = None,
        message: str | None = None
    ) -> str:
        self.value = value
        self.message = message or " Oops! Operating system found is invalid or unknown..." if self.value is None else f"Oops! The [ {self.value} ] Operating system found is invalid..."
        super().__init__(message)


class OperationalSystemUnknownValueError(Exception):
    def __init__(
        self,
        value: str | None = None,
        message: str | None = None
    ) -> str:
        self.value = value
        self.message = message or " Oops! Operating system found is unknown..." if self.value is None else f"Oops! The [ {self.value} ] Operating system found is unknown..."
        super().__init__(message)


class ImpossibleToContinueError(Exception):
    def __str__(self) -> str:
        return " Oops! Something went wrong and was impossible to continue... Please verify the operation!"