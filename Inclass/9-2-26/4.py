s = "sai university"
c = input("Enter a character: ")
sub_string = input("Enter a sub string: ")
if c in s:
    print(True)
else:
    print(False)

if sub_string not in s:
    print(False)
else:
    print(True)