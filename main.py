import math

def main():
  phases = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous", "Third Quarter", "Waning Crescent"]
  print("Enter your birthdays in this format: MM/DD/YYYY")
  moon1 = input("Enter your birthday: ")
  moon2 = input("Enter partners birthday: ")
  p1 = (splitAndCalc(moon1,phases))
  p2 = (splitAndCalc(moon2,phases))
  percent = (compat(phases,p1,p2))
  print("You guys are ", percent, "% compatable!")

def splitAndCalc(moon,sp):
  m, d, y = moon.split("/")
  d = int(d)
  m = int(m)
  y = int(y)

  if m <= 1:
    y -= 1
    m += 12

  a = y/100
  b = a/4
  c = 2-a+b
  e = int(365.25 * (y + 4716))
  f = int(30.6001 * (m + 1))
  jd = c+d+e+f-1524.5
  nd = (jd - 2451549.5) 
  nm=nd/29.53
  nm1 = math.trunc(nm)
  nm=nm-nm1
  dic = nm * 29.53

  if dic <= 3.6875:
    return sp[0]
  elif dic <= 7.375:
    return sp[1]
  elif dic <= 11.0625:
    return sp[2]
  elif dic <= 14.75:
    return sp[3]
  elif dic <= 18.4375:
    return sp[4]
  elif dic <= 22.125:
    return sp[5]
  elif dic <= 25.8125:
    return sp[6]
  elif dic <= 29.5:
    return sp[0]



def compat(phs,p1,p2):
  index_p1 = phs.index(p1)
  index_p2 = phs.index(p2)
  compat = abs(index_p1-index_p2)
  if compat == 4:
   return "100"
  if compat == 3:
    return "75"
  if compat == 2:
    return "50"
  if compat == 1:
    return "25"
  if compat == 0:
   return "0"





main()

