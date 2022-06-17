quantity = 0
SIZE = 4
DISCOUNTS = [0.00,0.10,0.15,0.20]
QUAN_LIMITS = [0,9,13,26]
x = 0
QUIT = -1

quantity = input("Enter quantity order or -1 to quit: ")
quantity = int(quantity)

while quantity != QUIT:
  x = SIZE - 1
  while quantity < QUAN_LIMITS[x]:
    x = x - 1
  print("Your discount rate is", str(DISCOUNTS[x]))
  quantity = input("Enter anther quantity order or -1 to quit: ")
  quantity = int(quantity)

print("End of job")