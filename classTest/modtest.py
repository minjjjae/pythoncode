from mod import mod1 as m

a=m.add(2,4)
print(a)
b=m.sub(4,1)
print(b)

import sys
print(sys.path)
sys.path.append('c:\\python\\pythoncode\\classTest')
print(sys.path)
import mod2

print(mod2.div(3,5))

