import random
import time as tm
import sys
import os
from Resources.Var import *
from Resources.Functions import *
from replit import db
import psutil

Clear()
process = psutil.Process(os.getpid())
memory_used = process.memory_info().rss/1000000

name = str(input("Hello, What is your first and last name?\n"))

if name in db:
  Clear()
  print("Good to see you again! It looks like you have used this before!")
  tm.sleep(3)
elif name not in db:
  Clear()
  print("I see this is your first time using this software. Have fun!  Just a disclaimer, your name will be added to my repl.it database, but we will never share anyone's name!")
  tm.sleep(5)
  db[name] = name
  new_user = db[name]

Clear()
print(yellow, "Hello! Thank you for using our Beta version of the Distance Conversion Calculator!  Please report any bugs or fixes that should be made to me.  Created by me, @ThePythonFury, and my helper, Mr. Baumgardner.\n\n", red, "Version 1.1.0")
tm.sleep(5)
Clear()

print(white)
print("\n")

print(yellow)



def Main():
  def conversionprocess():
    Clear()
    print(cyan, 'The available units include miles, kilometers, meters, millimeters, centimeters, inches, yards, and feet.\n\n')
    whattoconvert = input('What unit would you like to convert? PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
    if whattoconvert == 'miles':
      print(blue)
      milesto = input('Ok. what would you like to convert miles to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if milesto == 'kilometers':
        main_func("miles", milestokilo, "kilometers")
      elif milesto == 'meters':
        main_func("miles", milestometer, "meters")
      elif milesto == 'yards':
        main_func("miles", milestoyard, "yards")
      elif milesto == 'feet':
        main_func("miles", milestofoot, "feet")
      elif milesto == 'millimeters':
        main_func("miles", milestomm, "millimeters")
      elif milesto == 'inches':
        main_func("miles", milestoinch, "inches")
      elif milesto == 'centimeters':
        main_func("miles", milestocm, "centimeters")
    elif whattoconvert == 'kilometers':
      print(blue)
      kiloto = input('Ok. what would you like to convert kilometers to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if kiloto == 'miles':
        main_func("kilometers", kilotomile, "miles")
      elif kiloto == 'meters':
        main_func("kilometers", kilotometer, "meters")
      elif kiloto == 'yards':
        main_func("kilometers", kilotoyard, "yards")
      elif kiloto == 'feet':
        main_func("kilometers", kilotofoot, "feet")
      elif kiloto == 'millimeters':
        main_func("kilometers", kilotomm, "millimeters")
      elif kiloto == 'inches':
        main_func("kilometers", kilotoinch, "inches")
      elif kiloto == 'centimeters':
        main_func("kilometers", kilotocm, "centimeters")
    elif whattoconvert == "km":
      print(blue)
      kiloto = input('Ok. what would you like to convert kilometers to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if kiloto == 'miles':
        main_func("kilometers", kilotomile, "miles")
      elif kiloto == 'meters':
        main_func("kilometers", kilotometer, "meters")
      elif kiloto == 'yards':
        main_func("kilometers", kilotoyard, "yards")
      elif kiloto == 'feet':
        main_func("kilometers", kilotofoot, "feet")
      elif kiloto == 'millimeters':
        main_func("kilometers", kilotomm, "millimeters")
      elif kiloto == 'inches':
        main_func("kilometers", kilotoinch, "inches")
      elif kiloto == 'centimeters':
        main_func("kilometers", kilotocm, "centimeters")
    elif whattoconvert == "meters":
      print(cyan)
      meterto = input('Ok. what would you like to convert meters to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if meterto == 'miles':
        main_func("meters", metertomile, "miles")
      elif meterto == "kilometers":
        main_func("meters", metertokilo, "kilometers")
      elif meterto == "millimeters":
        main_func("meters", metertomm, "millimeters")
      elif meterto == "mm":
        main_func("meters", metertomm, "millimeters")
      elif meterto == "centimeters": 
        main_func("meters", metertocm, "centimeters")
      elif meterto == "cm":
        main_func("meters", metertocm, "centimeters")
      elif meterto == "inches":
        main_func("meters", metertocm, "inches")
      elif meterto == "yards":
        main_func("meters", metertoyard, "yards")
      elif meterto == "feet" or "ft":
        main_func("meters", metertofoot, "feet")
    elif whattoconvert == "millimeters":
      print(red)
      mmto = input('Ok. what would you like to convert millimeters to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if mmto == "miles":
        main_func("millimeters", mmtomile, "miles")
      elif mmto == "kilometers":
        main_func("millimeters", mmtokilo, "kilometers")
      elif mmto == "km":
        main_func("millimeters", mmtokilo, "kilometers")
      elif mmto == "meters":
        main_func("millimeters", mmtometer, "meters")
      elif mmto == "centimeters":
        main_func("millimeters", mmtocm, "centimeters")
      elif mmto == "cm":
        main_func("millimeters", mmtocm, "centimeters")
      elif mmto == "inches":
        main_func("millimeters", mmtoinch, "inches")
      elif mmto == "yard" or "yards":
        main_func("millimeters", mmtoyard, "yards")
      elif mmto == "foot" or "feet":
        main_func("millimeters", mmtofoot, "feet")
    elif whattoconvert == "mm":
      print(red)
      mmto = input('Ok. what would you like to convert millimeters to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if mmto == "miles":
        main_func("millimeters", mmtomile, "miles")
      elif mmto == "kilometers":
        main_func("millimeters", mmtokilo, "kilometers")
      elif mmto == "km":
        main_func("millimeters", mmtokilo, "kilometers")
      elif mmto == "meters":
        main_func("millimeters", mmtometer, "meters")
      elif mmto == "centimeters":
        main_func("millimeters", mmtocm, "centimeters")
      elif mmto == "cm":
        main_func("millimeters", mmtocm, "centimeters")
      elif mmto == "inches":
        main_func("millimeters", mmtoinch, "inches")
      elif mmto == "yard" or "yards":
        main_func("millimeters", mmtoyard, "yards")
      elif mmto == "foot" or "feet":
        main_func("millimeters", mmtofoot, "feet")
    elif whattoconvert == "cm":
      print(red)
      cmto = input('Ok. what would you like to convert centimeters to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if cmto == "miles":
        main_func("centimeters", cmtomile, "miles")
      elif cmto == "kilometers":
        main_func("centimeters", cmtokm, "kilometers")
      elif cmto == "km":
        main_func("centimeters", cmtokilo, "kilometers")
      elif cmto == "meters":
        main_func("centimeters", cmtometer, "meters")
      elif cmto == "millimeters":
        main_func("centimeters", cmtomm, "millimeters")
      elif cmto == "mm":
        main_func("centimeters", cmtomm, "millimeters")
      elif cmto == "inches":
        main_func("centimeters", cmtoinch, "inches")
      elif cmto == "yards":
        main_func("centimeters", cmtoyard, "yards")
      elif cmto == "feet":
        main_func("centimeters", cmtofoot, "feet")
    elif whattoconvert == "centimeters":
      print(red)
      cmto = input('Ok. what would you like to convert centimeters to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if cmto == "miles":
        main_func("centimeters", cmtomile, "miles")
      elif cmto == "kilometers":
        main_func("centimeters", cmtokm, "kilometers")
      elif cmto == "km":
        main_func("centimeters", cmtokilo, "kilometers")
      elif cmto == "meters":
        main_func("centimeters", cmtometer, "meters")
      elif cmto == "millimeters":
        main_func("centimeters", cmtomm, "millimeters")
      elif cmto == "mm":
        main_func("centimeters", cmtomm, "millimeters")
      elif cmto == "inches":
        main_func("centimeters", cmtoinch, "inches")
      elif cmto == "yards":
        main_func("centimeters", cmtoyard, "yards")
      elif cmto == "feet":
        main_func("centimeters", cmtofoot, "feet")
    elif whattoconvert == "inches":
      inchto = input("Ok. What would you like to convert inches to?  PLEASE ANWER WITH NO CAPITAL LETTERS!:")
      if inchto == "miles":
        main_func("inches", inchtomile, "miles")
      elif inchto == "kilometers":
        main_func("inches", inchtokilo, "kilometers")
      elif inchto == "km":
        main_func("inches", inchtokilo, "kilometers")
      elif inchto == "meters":
        main_func("inches", inchtometer, "meters")
      elif inchto == "millimeters":
        main_func("inches", inchtomm, "millimeters")
      elif inchto == "mm":
        main_func("inches", inchtomm, "millimeters")
      elif inchto == "centimeters":
        main_func("inches", inchtocm, "centimeters")
      elif inchto == "cm":
        main_func("inches", inchtocm, "centimeters")
      elif inchto == "yards":
        main_func("inches", inchtoyard, "yards")
      elif inchto == "feet":
        main_func("inches", inchtofoot, "foot")
    elif whattoconvert == "yards":
      print(green)
      yto = input('Ok. what would you like to convert yards to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if yto == "miles":
        main_func("yards", yardtomile, "miles")
      elif yto == "kilometers":
        main_func("yards", yardtokilo, "kilometers")
      elif yto == "km":
        main_func("yards", yardtokilo, "kilometers")
      elif yto == "meter" or "meters":
        main_func("yards", yardtometer, "meters")
      elif yto == "millimeters":
        main_func("yards", yardtomm, "mm")
      elif yto == "mm":
        main_func("yards", yardtomm, "mm")
      elif yto == "centimeters":
        main_func("yards", yardtocm, "cm")
      elif yto == "cm":
        main_func("yards", yardtocm, "cm")
      elif yto == "inches":
        main_func("yards", yardtoinch, "inches")
      elif yto == "feet":
        main_func("yards", yardtofoot, "feet")
    elif whattoconvert == "foot" or "feet":
      print(magenta)
      ftto = input('Ok. what would you like to convert inches to?  PLEASE ANSWER WITH NO CAPITAL LETTERS!:\n')
      if ftto == "miles":
        main_func("feet", feettomile, "miles")
      elif ftto == "km":
        main_func("feet", feettokilo, "kilometers")
      elif ftto == "kilometers":
        main_func("feet", feettokilo, "kilometers")
      elif ftto == "meter" or "meters":
        main_func("feet", feettometer, "meters")
      elif ftto == "mm":
        main_func("feet", feettomm, "millimeters")
      elif ftto == "millimeters":
        main_func("feet", feettomm, "millimeters")
      elif ftto == "cm":
        main_func("feet", feettocm, "centimeters")
      elif ftto == "centimeters":
        main_func("feet", feettocm, "centimeters")
      elif ftto == "inches":
        main_func("feet", feettoinch, "inches")
      elif ftto == "yard" or "yards":
        main_func("feet", feettoyard, "yards")
    else:
      print(red, "Please put a valid input.")
      tm.sleep(3)
      conversionprocess()
 

        






  conversionprocess()
  
  tm.sleep(5)
  print(yellow)
  Again = input('\n\n\n\nWould you like to convert another unit? [Y/N]\n')
  if Again == 'Y':
    print('Ok!')
    tm.sleep(2)
    Clear()
    Main()
  if Again == 'y':
    print('Ok!')
    tm.sleep(2)
    Clear()
    Main()
  if Again == 'N':
    Clear()
    print('Ok, See you later!')
    tm.sleep(2)
    Clear()
    rounded = round(memory_used)
    print(int(rounded) + " kilobytes were used to run this project!")
    sys.exit()
  if Again == 'n':
    Clear()
    print('Ok, See you later!')
    tm.sleep(2)
    Clear()
    rounded = round(memory_used)
    print(str(rounded) + " kilobytes were used to run this program!")
    sys.exit()

Main()
