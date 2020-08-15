#import module1
#print(dir(module1))
#print(module1.africa)

from module1 import europe
#print(module1.europe)
print(europe.greece)

#print(module1.europe.norway)

from module1 import africa
#print(africa.zimbabwe)

from module1.africa import zimbabwe