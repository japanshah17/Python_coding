#filename = 'abc.txt'
#with open(filename) as f:
#   contents = f.read()
#print(contents)

#with open(filename) as f_obj:
#    for line in f_obj:
#        print(line.strip())

filename = 'programming.txt'
with open(filename, 'w') as f:
    f.write("I love programs\n")

filename = 'programming.txt'
with open(filename, 'r') as f:
    g =  f.read()
    print(g)
