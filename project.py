import ephem
def main():
  print("Enter bdays: DD/MM/YYYY")
  moon1 = input("Enter your bday: ")
  moon2 = input("Enter partners bday: ")
  print(splitAndCalc(moon1))
  print(splitAndCalc(moon2))

def splitAndCalc(moon):
  d, m, y = moon.split("/")
  d = int(d)
  m = int(m)
  y = int(y)

main()

