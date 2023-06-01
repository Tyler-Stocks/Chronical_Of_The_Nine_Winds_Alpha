"""
Custom Errors
InputErrors
|
|--__init__(self) -> None
|
|--length_error(self, length(int | float)) -> None
|
|--type_error(self, data_type(str)) -> None
|
|--whitespace_error(self) -> None
|
|--range_error(self, low_bound(int | float), high_bound(int | float)) -> None

"""
from utility import console as util

console = util.Console()

class InputErrors:
    """Handles Input Errors."""

    def __init__(self) -> None:
        pass

    def length(self, length: int | float) -> None:
        """
        Prints error message if input length is too long.

        Args:
        length (int, float, double): Length to be displayed in error message.
        """
        print(f'Input cannot be longer than {length}.\n')
        console.clear(1)

    def type(self, data_type: str) -> None:
        """
        Prints error if the input is of the wrong data type.

        Args:
        data_type (str): Data type to be displayed in error message
        """
        if data_type.lower() == 'str':
            print('\nInput must be alphabetic.\n')
            console.clear(1)
        elif data_type.lower() in ('int', 'float'):
            print('Input must be a real number.\n')
            console.clear(1)
        elif data_type.lower() == 'bool':
            print('Input must be a boolean value (True/False)\n')
            console.clear(1)
        else:
            raise TypeError

    def whitespace(self) -> None:
        """Prints error if there is no input."""
        print('Must provide input.\n')
        console.clear(1)

    def range(self, low_bound: int | float, high_bound: int | float) -> None:
        """
        Prints error if an input if out of range.

        Args:
            low_bound (int, float, double): The lowest value the input can be.\n
            hight_bound (int, float, double): The highest value the input can be.
        """
        print(f'Input value must be between {low_bound}, and {high_bound}.\n')
        console.clear(1)