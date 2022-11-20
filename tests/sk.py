from collections import namedtuple

Point2d = namedtuple('Point2d', 'x y')

pt = Point2d(10,20)

print(pt)

pt = Point2d(100, pt.x)
print(pt)

Stock = namedtuple('Stock', 'symbol year month day open hight low close')

djia = Stock("DJIA", 2022, 7, 12, 100, 130, 90, 110)

print(djia)

*val, _ = djia

djia = Stock(*val, 120)
print(djia)

djia = djia._replace(open=50)
print(djia)

djia = djia._make(tuple(val) + (200,))
print(djia)
