
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""

temp = float(input("Give me a temperature: "))

def check_fever(temp):
  if 100.4<=temp<104:
    print("You have a fever.")
  elif temp>= 104:
    print("You have a realy really high fever, go help yourself please I beg you")
  elif temp<=98.5:
    print("You are a little chilly right now, maybe put on a sweater")
  else:
    print("You don't have a fever, congratulations!.")
check_fever(temp)