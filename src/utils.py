import re

def extract_ingredients(text):

    text = str(text)

    match = re.search(
        r'ingredients[:\-]?(.*)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return text