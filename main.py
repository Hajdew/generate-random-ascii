from strgen import StringGenerator as SG
import random
import string
import uuid

#lenght of random generated ascii
ascii_lenght = 100

#random generate not an ascii i want but it is close
a = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(ascii_lenght))

print(a+"\n")

#generate random uuid not what i want
a = uuid.uuid4()

print(str(a)+"\n")


#very close to generate ascii for some reason \a doesnt work
a = SG("[\w]{"+str(ascii_lenght)+"}").render()

print(a)