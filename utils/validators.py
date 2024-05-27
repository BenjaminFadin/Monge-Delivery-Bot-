import re


def validate_date(date_text):
    pattern = r"\d{2}\.\d{2}\.\d{4}"  # Pattern to match dates in the format dd.mm.yyyy
    if re.match(pattern, date_text):
        return True
    return False


def get_phone_number(contact):
    if not (contact and contact.phone_number):
        return None
    if "+" in contact.phone_number:
        return contact.phone_number[1:]
    return contact.phone_number[1:]



