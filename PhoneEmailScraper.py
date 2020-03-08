import re

import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(
    r"""
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(\d\d\d)|(\(\d\d\d\))?   # area code(optional)
(\s|-)                   # separator
\d\d\d                   # first 3 digits
-                        # separator
\d\d\d\d                 # last 4 digits
(((ext(\.)?\s)|x)        # extension word-part(optional)
(\d{2,5}))?              # extension number-part(optional)
""",
    re.VERBOSE,
)

# TODO: Create a regex for email addresses
emailRegex = re.compile(
    r"""
# some.+_thing@some.+_thing.com

[a-zA-Z0-9_.+]+        # name part
@                      # @symbol
[a-zA-Z0-9_.+]+        # domain name part
"""
)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)


# TODO: Copy the extracted email/phone to the clipboard
