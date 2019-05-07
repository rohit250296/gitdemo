n = int(input('Enter how many lines : '))
with open("sample2.txt", "r") as f:
    i = 0
    for line in f:
        print(line)
        i += 1
        if i == n: break