import re


def check(password):
    # regex1 = re.compile(r'[a-z]{1,}')
    regex1 = re.compile(r'[A-Z]{1,}')
    regex2 = re.compile(r'[a-z]{1,}')
    regex3 = re.compile(r'\d+')
    print(regex1.search(password))
    print(regex2.search(password))
    print(regex3.search(password))

    if len(password) > 7 and regex1.search(password) \
            and regex2.search(password) and regex3.search(password):
        return True
    else:
        return False


if __name__ == '__main__':
    # print(check("123"))
    # print(check("Q123dsdsfsfsd"))
    # print(check("123456789"))
    print(check("Qwewqeqe1213"))
    # print(check("AHJHJHHJHJHJHJ"))
    # print(check("ASSDDzzasdsadadASSS"))
