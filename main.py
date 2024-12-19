import random

password = ''

for i in range(10):
    ce = random.choice(".,;:?!'()[]{}-0123456789abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password = password + ce
print(password)
