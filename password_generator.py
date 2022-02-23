import random
import string

di = list(string.ascii_letters + string.digits + "`~!@#$%&*()_+-={}[]\|;:''<,>./?")
length=random.randint(31,64)

random.shuffle(di)
password = []
for i in range(length):
    password.append(random.choice(di))
random.shuffle(password)
print("".join(password))
