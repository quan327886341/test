import re


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242666666.")
print(mo)

print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode + "  " + mainNumber)

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search(('HaHaHaHaHa'))
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search(('HaHaHaHaHa'))
print(mo2.group())

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Han Last Name: YouQuan')
print(mo.groups())

nameRegex = re.compile(r'Agent \w+')
print(nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))



regex1 = re.compile(r'[a-z]{1,}')
if regex1.search("Qwewqeqe1213"):
    print("------")
else:
    print("=======")

regex2 = re.compile(r'[A-Z]{1,}')
if regex2.search("Qwewqeqe1213"):
    print("---A---")
else:
    print("===A====")

regex1 = re.compile(r'\d+')
if regex1.search("Qwewqeqe1213"):
    print("---d---")
else:
    print("===d====")

# print("  --- "+regex1.findall("password").groups())
# print("  --- "+regex1.search("password").group())



# import pyperclip
#
# pyperclip.copy('Hello world!')
# print([pyperclip.paste])







