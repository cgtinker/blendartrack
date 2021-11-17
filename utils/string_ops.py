
def set_lower_letter_only_string(string):
    s = set_letter_only_string(string)
    s = set_string_lowercase(s)
    return s


def string_contains(value, string):
    if value in string:
        return True
    else:
        return False


def set_string_lowercase(string):
    return string.lower()


def set_string_uppercase(string):
    return string.upper()


def set_string_camelcase(string):
    return string.title()


def remove_numbers_from_string(string):
    return ''.join([i for i in string if not i.isdigit()])


def set_letter_only_string(string):
    return ''.join(i for i in string if i.isalpha())
