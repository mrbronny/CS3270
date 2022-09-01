def avg(lyst):
#takes list of floats and returns average
  total = 0.00
  for num in lyst:
    total += num
  return total/len(lyst)

def lowest(lyst):
#takes list of floats and returns lowest
  low = 1000.00
  for num in lyst:
    if num < low:
      low = num
  return low

def highest(lyst):
#takes list of floats and returns highest
  high = -1000.00
  for num in lyst:
    if num > high:
      high = num
  return high

with open("gas_prices.txt", "r") as file:
  file = file.readlines()
  monthref = {"01":"January\t\t", "02":"February\t","03":"March\t\t","04":"April\t\t","05":"May\t\t\t","06":"June\t\t","07":"July\t\t","08":"August\t\t","09":"September\t","10":"October\t\t","11":"November\t","12":"December\t"}
  currmonth = "00"
  curryear = "0000"
  monthlist = []
  yearlist = []
  summary = f""
  for line in file:
    line = line.strip()
    line = line.split(":")
    date = line[0].split("-")
    if currmonth == "00": #if just starting
      currmonth = date[0]
      curryear = date[2]
    if curryear != date[2]: #if new year, print year stuff
      summary += f"\t{monthref[currmonth]}${avg(monthlist):.2f}\n"
      currmonth = "01"
      summary = f"{curryear}:\n\tLow: ${lowest(yearlist):.2f}, Avg: ${avg(yearlist):.2f}, High: ${highest(yearlist):.2f}\n" + summary
      print(summary)
      summary = ""
      yearlist = []
    elif currmonth != date[0]: #if new month, append month stuff
      summary += f"\t{monthref[currmonth]}${avg(monthlist):.2f}\n"
      monthlist = []
    monthlist += [float(line[1])]
    yearlist += [float(line[1])]
    currmonth = date[0]
    curryear = date[2]
  summary += f"\t{monthref[currmonth]}${avg(monthlist):.2f}\n"
  print(f"{curryear}:\n\tLow: ${lowest(yearlist):.2f}, Avg: ${avg(yearlist):.2f}, High: ${highest(yearlist):.2f}\n" + summary)