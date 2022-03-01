import datetime

#d1 = datetime.strptime(input(), "%Y-%m-%d")
a1,b1,c1 = map(int, (input().split()))
a2,b2,c2 = map(int, (input().split()))
d1 = datetime.date(a1, b1, c1)
d2 = datetime.date(a2, b2, c2)
print(abs((d2-d1).days)*24*3600)