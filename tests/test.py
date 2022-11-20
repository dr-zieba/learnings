from collections import namedtuple

Point2 = namedtuple("Point2", ['x', 'y'])

p1 = Point2(1,2)

print(p1._asdict())
print(p1.x)
print(p1.y)

def dec(fn):
    def inner(*args, **kwargs):
        print("Before fn")
        result = fn(*args, **kwargs)
        print("After fn")
        return result
    return inner

@dec
def suma(a,b):
    return print(f"SUma: {a+b}")

#suma(1,2)

print("********************")

def sum_points(todos):
    count = [item['points'] for item in todos]
    sum_ = 0
    for i in count:
        sum_ += int(i)
    return sum_

todo1 = {'name': 'Example 1', 'body': 'This is a test task', 'points': '3'}
todo2 = {'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'}

todos = [{'name': 'Example 1', 'body': 'This is a test task', 'points': '3'},
{'name': 'Task 2', 'body': 'Yet another example task', 'points': '2'},
{'name': 'Task 3', 'body': 'Third task', 'points': '5'}]


result = sum_points(todos)

print(result)

