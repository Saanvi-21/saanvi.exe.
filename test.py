f = open("file.txt")
f.read()

f = open("file.txt")
filelines = f.readlines()
for line in filelines:
    print(line)

f = open("file2.txt")
f.read()

f = open("file2.txt")
filelines = f.readlines()
for line in filelines:
    print(line)

file = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

def swapData(file, file2):
    try:
        with open(file, 'r') as f:
            data_1 = f.read()

        with open(file2, 'r') as f:
            data_2 = f.read()


        with open(file, 'w') as f:
            f.write(data_2)
            f.close()

        with open(file2, 'w') as f:
            f.write(data_1)
            f.close()

    except FileNotFoundError:
        print("[-] No such file(s) found!")

swapData(file, file2)