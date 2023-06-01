"""
Module to get the users gender.
Structure:
    Gender
    |
    |--__init__(self) -> None
    |
    |--input_gender(self) -> None
    |
    |--input_custom_gender(self) -> None
    |
    |--input_first_pronoun(self) -> None
    |
    |--input_second_pronoun(self) -> None
    |
    |--get_gender(self) -> None
    |
    |--assign_pronouns(self) -> None
    |
    |--format(self) -> None
    |
    |--save(self) -> None
"""
from utility import input_values
from utility import console as Console
from utility import input_formatting
from utility import error_handling
from utility import input_handling
from player import player_information

inputFormat = input_formatting.InputUtility()
inputValues = input_values.InputValues()
console = Console.Console()
errors = error_handling.ErrorHandling()
inputs = input_handling.HandleUserInput()

class Gender:
    """Get, Format, then Store users gender."""

    def __init__(self):

        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.declaration = ''
        self.confirm = ''

    def input_gender(self) -> None:
        """Have user input their first name"""
        console.clear()

        error_occured = True

        while error_occured:
            self.gender = input('What gender are you? Boy, Girl, or Other: ')
            error_occured = errors.string_error_handler(self.gender, 20)


    def input_custom_gender(self) -> None:
        """Have user input custom gender."""
        console.clear()

        error_occured = True

        while error_occured:
            self.gender = input('What is the name of your gender? ')
            error_occured = errors.string_error_handler(self.gender, 20)

    def input_first_pronoun(self) -> None:
        """Have user input first pronouns."""
        console.clear()

        error_occured = True

        while error_occured:
            self.pronoun_one = input('What is your fist pronoun? ')
            error_occured = errors.string_error_handler(self.pronoun_one, 20)

    def input_second_pronoun(self):
        """Have user input second pronoun"""
        console.clear()

        error_occured = True

        while error_occured:
            self.pronoun_two = input('What is your second pronoun? ')
            error_occured = errors.string_error_handler(self.pronoun_two, 20)

    # Goofy ahh function, pls fix soon, also fix check_for_valid_input cause it kinda sucks ass and probably doesn't even work.
    def get_gender(self) -> None:
        """Function to get the users gender."""
        console.clear()

        valid_gender_values = [inputValues.valid_boy_values, inputValues.valid_girl_values, 'other']

        while True:
            self.input_gender()
            if inputs.check_for_valid_input(self.gender, valid_gender_values, 'Input must be boy girl or other') and self.gender == 'Other':
                self.input_custom_gender()
                if inputs.confirmation(self.gender):
                    self.input_first_pronoun()
                    if inputs.confirmation(self.pronoun_one):
                        self.input_second_pronoun()
                        if inputs.confirmation(self.pronoun_two):
                            self.format()
                            self.save()
                            break
            elif inputs.check_for_valid_input(self.gender, valid_gender_values, 'Input must be boy girl or other') and self.gender != 'Other':
                if inputs.confirmation(self.gender):
                    self.assign_pronouns()
                    self.format()
                    self.save()
                    break
            elif not inputs.check_for_valid_input(self.gender, valid_gender_values, 'Input must be boy girl or other'):
                continue
            else:
                raise TypeError

    def assign_pronouns(self) -> None:
        """Assign pronouns based on user input."""
        if self.gender.lower() == 'boy':
            self.pronoun_one = 'He'
            self.pronoun_two = 'Him'
        elif self.gender.lower() == 'girl':
            self.pronoun_one = 'She'
            self.pronoun_two = 'Her'
        else:
            pass

    def format(self) -> None:
        """Format Gender, and Pronouns"""
        inputFormat.string(self.gender)
        inputFormat.string(self.pronoun_one)
        inputFormat.string(self.pronoun_two)
        inputFormat.string(self.declaration)

    def save(self) -> None:
        """
        Save gender in player_information dictionary
        """
        player_information['Gender']['Name'] = self.gender
        player_information['Gender']['First Pronoun'] = self.pronoun_one
        player_information['Gender']['Second Pronoun'] = self.pronoun_two


Gender_Instance = Gender()
Gender_Instance.get_gender()
