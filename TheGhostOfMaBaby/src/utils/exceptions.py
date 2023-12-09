class ImpossibleToContinueError(Exception):
    def __str__(self) -> str:
        return " Oops! Something went wrong and was impossible to continue... Please verify the operation!"