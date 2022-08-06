import re

CHINESE_PATTERN = r'\u4e00-\u9fa5\u3007'
ENGLISH_PATTERN = r'a-zA-Z'
NUMBER_PATTERN = r'0-9'
PUNCTUATION_PATTERN = r'\s\$\(\)\*\+\.\]\[\?\\\^\{\}\|\<\>\°\-\=\,\"\/\‘\’\''


def cleaner(text: str) -> str:
    text = re.sub(f'[^{CHINESE_PATTERN}{ENGLISH_PATTERN}{NUMBER_PATTERN}{PUNCTUATION_PATTERN}]', '', text)
    return text
