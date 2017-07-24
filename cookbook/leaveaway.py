record = ('ACME', 50, 123.45, (12, 18, 2012))
name,*_,(*_,year) = record

print(name)
print(year)
print(*_)