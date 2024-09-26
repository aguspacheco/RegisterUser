from django.core.validators import RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError
from utils.constants import *
from django.core.validators import RegexValidator

#Expresiones regulares y mensajes genéricos
DIGITS_REGEX = r'^\d+$'
EXACT_LENGTH_8_REGEX = r'^\d{8}$'
EXACT_LENGTH_10_REGEX = r'^\d{10}$'
EXACT_LENGTH_11_REGEX = r'^\d{11}$'

DIGITS_ONLY_MESSAGE = 'solo se admiten datos numéricos.'
EXACT_LENGTH_8_MESSAGE = 'Tiene que tener solo 8 dígitos.'
EXACT_LENGTH_10_MESSAGE = 'Tiene que tener solo 10 dígitos.'
EXACT_LENGTH_11_MESSAGE = 'Tiene que tener solo 11 dígitos.'

# Valida números y longitudes específica
numeric_validator = RegexValidator(
    regex=DIGITS_REGEX,
    message=DIGITS_ONLY_MESSAGE,
    code='invalid_numeric'
)

exact_length_8_validator = RegexValidator(
    regex=EXACT_LENGTH_8_REGEX,
    message=EXACT_LENGTH_8_MESSAGE,
    code='invalid_length_8'
)

exact_length_10_validator = RegexValidator(
    regex=EXACT_LENGTH_10_REGEX,
    message=EXACT_LENGTH_10_MESSAGE,
    code='invalid_length_8'
)

exact_length_11_validator = RegexValidator(
    regex=EXACT_LENGTH_11_REGEX,
    message=EXACT_LENGTH_11_MESSAGE,
    code='invalid_length_11'
)

numeric_validator = RegexValidator(
        regex=r'^\d+$',
        message=f'Solo tiene que tener datos numéricos.',
        code='invalid_numeric'
)