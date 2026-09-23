def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for char in s:
        if char.isdigit() == False and char.isalpha() == False:
            return False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            if not s[i:].isdigit():
                return False
            break
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    else:
        return True
main()
