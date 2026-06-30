import os

num1 = int(os.environ["NUM1"])
num2 = int(os.environ["NUM2"])

result = num1 + num2

print(f"First Number : {num1}")
print(f"Second Number: {num2}")
print(f"Sum = {result}")