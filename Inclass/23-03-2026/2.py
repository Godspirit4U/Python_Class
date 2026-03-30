#  Replace the word "anything" with "something" in the text file.
with open("text.txt","r") as f1:
    data = f1.readlines()

data1 = []
for line in data:
    line1 = ""
    i = 0
    while i < len(line) - 8:
        if line[i: i + 8] == "anything":
            line1 += "something"
            i += 8
        else:
            line1 += line[i]
            i += 1
    data1.append((line1 + "\n"))



with open("4.txt","w") as f:
    f.writelines(data1)