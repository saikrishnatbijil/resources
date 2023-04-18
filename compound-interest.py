
p = int(input("Enter Principle Amount : "))
n = int(input("Enter Number of Years : "))
r = int(input("Enter Rate of Interest : "))

results = p * (1 + r / 100) ** n

print("Amount need to Pay : ", results)