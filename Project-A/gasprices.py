def avg(lyst):
  total = 0.00
  for num in lyst:
    total += num
  return total/len(lyst)

def lowest(lyst):
  low = 1000.00
  for num in lyst:
    if num < low:
      low = num
  return low

def highest(lyst):
  high = -1000.00
  for num in lyst:
    if num > high:
      high = num
  return high

with open("gas_prices.txt", "r") as file:
  file = file.readlines()
  monthref = {"01":"January", "02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
  for line in file:
    line = line.strip()
    line = line.split(":")