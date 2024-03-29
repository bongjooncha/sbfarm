from time import localtime

t = localtime()
print(t.tm_hour)

if t.tm_hour >= 21 or t.tm_hour <7:
    print(t)