from operator import truediv

print ("inizio programma")
foo = False
assert not bool (0)
assert foo is False
assert True is True
assert True != False
assert None is None

bar = 1
baz = 1
result = baz / bar
print (result)
result += 1
result -= 1
assert result >= 0

normal_string = "hello" #stringa normale
byte_string = b"world" #stringa byte
decode_string = byte_string.decode ('utf8')
message = normal_string + decode_string
print (message)

li1 = [1, 2]
li1 +=[3]
print (li1)
li1. insert (0, 1)
print (li1)
assert li1 == [1, 1, 2, 3]

tu1 = (1,2)
print (tu1)
tu1 += (3,)
print (tu1)
assert tu1 == (1,2,3)

d1 = {}
d1["a"] = 1
d1["b"] = 2
d1 = {"a" : 1, "b" : 2}
assert d1 ["a"] == 1
assert d1 == {"a" :1, "b": 2}
del d1 ["b"]
assert "b" not in d1

if "b" not in d1:
    if "a" in d1:
        assert True
    else:
        assert False
else:
    assert False

count = 0
for idx in [1, 2, 3]:
    count += 1
    print ("CIAO")
assert count == 3
num = 3
while num > 0 :
    print ("CIAO")
    num -= 1

print ("Fine programma")

import math
assert math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9)



















