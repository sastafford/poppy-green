import re

def is_zip_code_valid(zip: str) -> bool:
    zip_code_regex = "(^\\d{5}$)|(^\\d{9}$)|(^\\d{5}-\\d{4}$)"
    pattern = re.compile(zip_code_regex)
    if (re.match(zip_code_regex, zip)): 
        return True
    else:
        return False

