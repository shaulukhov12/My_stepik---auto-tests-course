f = open("list.txt", "r")
#y = f.readline().rstrip()
#y = y.splitlines()
#print(repr(y))

for line in f:
    line = line.rstrip()
    print(repr(line))
x = f.read()
print(repr(x))
f.close()