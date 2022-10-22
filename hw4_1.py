LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> str(encode('sos')) #doctest: -FAIL_FAST
    '... --- ...'
    >>> str(encode("SOS")) #doctest: -FAIL_FAST
    '... --- ...'
    >>> str(encode("SOS"))
    '... --- ...'
    >>> str(encode("SOS"))
    '... --- ...'
    >>> str(encode(123))
    Traceback (most recent call last):
    ...
    TypeError: 'int' object is not iterable

    """

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


# testdata = [
#     ('SOS', '... --- ...'),
#     ('GE', '--. .'),
#     ('QRZ?', '--.- .-. --.. ..--..')
#     ]
#
# @pytest.mark.parametrize('source_string,result', testdata)
# def test_encode(source_string, result):
#     assert encode(source_string) == result
#
#
# testdata_exception = [
#     ('sos',  pytest.raises(KeyError)),
#     (123, pytest.raises(TypeError))
#     ]
#
# @pytest.mark.parametrize('source_string,result', testdata_exception)
# def test_encode_e(source_string, result):
#     with result:
#         assert encode(source_string) == result
