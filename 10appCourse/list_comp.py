'''
def foo(x):
    new_list = [item for item in x if isinstance(item, int)]
    print(new_list)

#foo([99, 89, 0, 1,2,4,"qwe"])


def foo2(x):
    new_list = [item for item in x if item > 0]
    return new_list

#print(foo2([-1,-2,-3, 3,45,6]))


def foo3(x):
    new_list = [item if isinstance(item, int) else 0 for item in x]
    return new_list

#print(foo3([2,3,1,4,"qwe","qwee"]))

def foo4(x):
    new_list = [float(item) for item in x]
    return sum(new_list)

#print(foo4(['2.2','2.1','2.3']))

def foo5(a,b):
    return a + b

#print(foo5("asd","zxc"))

def mean(*args):
    return sum(args) / len(args)

#print(mean(1,2,3))

def foo6(*args):
    new_list = [item.upper() for item in args]
    return sorted(new_list)

#print(foo6("z","x","a","b","c"))
'''

with open("text.txt", 'r+') as file:
    content = file.read()
    print(content)
    for i in range(2):
        file.write(content)
