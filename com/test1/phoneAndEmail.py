
import pyperclip, re


phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(\s*|ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)

phoneRegex = re.compile(r'''(
        (\d{3,4}|\(\d{3,4}\))?
        (\s|-|\.)?
        (\d{7,8})
        (\s*(\s*|ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)


emailRegex = re.compile(r'''(
           [a-zA-Z0-9._%+-]+
           @
           [a-zA-Z0-9.-]+
           (\.[a-zA-Z]{2,4})
           )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1], groups[3]])
    if groups[6] != '':
        phoneNum += ' x' + groups[6]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')


