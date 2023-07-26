#--------------------------------------------------------------------------
#imports
from ColorO import Zen
import time
import Classes
import clear
import Data
import er_handler
import random
import requests
import os
#--------------------------------------------------------------------------
# Data
__Hammerequire__ = Data.__Hammerequire__
__tvrequire__ = Data.__tvrequire__
__fanreqire__ = Data.__fanreqire__
__doorreqire__ = Data.__doorreqire__
__cupreqire__ = Data.__cupreqire__
__phonereqire__ = Data.__phonereqire__
__Version__ = Data.__Version__
cmds = Data.cmds
Store = Data.Store
weeklytimeleft = Data.weeklytimeleft
Admin = Data.Admin
Year = 1
total_days = 0
items=['phone body','phone screen','phone','apple', 'fan', 'car', 'tv', 'house', 'hammer', 'tree', 'door', 'cup', 'window:', 'water', 'metal', 'stick', 'glue', 'motherboard', 'tv screen', 'power cord', 'plastic', 'motor', 'wood', 'rope', 'clay']
#--------------------------------------------------------------------------
# Start Menu
clear.ScreenClearer().clear_screen()
print("--Note: If you don't have any data in the saves, it will print an error.")
print("--Note: There might be bugs.")
print("--Note: Only use lowercase when typing.")

print("Would you like to load your save? (y/n)")
start_menu = input("> ")

if start_menu == "y":
    Day = int(Classes.DayLoad.Dayo)
    Cash = int(Classes.CashLoad.Casho)
    Name = str(Classes.NameLoad.Nameo)
    Job = str(Classes.JobLoad.Jobo)
    inv = eval(Classes.Invload.invo)
    __skill_level__ = int(Classes.Nonload.__skill_level__)
    used_load = True
else:
   Day = int(Classes.Nonload.Day1)
   Cash = int(Classes.Nonload.Cash1)
   Name = str(Classes.Nonload.Name1)
   Job = str(Classes.Nonload.Job1)
   inv = list(Classes.Nonload.inv1)
   __skill_level__ = int(Classes.Nonload.__skill_level__)
   used_load = False
#--------------------------------------------------------------------------
# Game
if not used_load:
   er_handler.LoadError(Day, Cash, Name, Job, __skill_level__)
else:
   pass
clear.ScreenClearer().clear_screen()
print(f"Version: {__Version__}")
print("Type Help To See The Commands.")
print("Start Playing.")
while True:
    Play = input(Zen.RESET+"> ")
    if Play.lower() == "stats":
        print("------------------------------")
        print(f"Cash: {Cash}")
        print(f"Day: {Day}")
        print(f"Job: {Job}")
        print(f"Name: {Name}")
        print(f"Skill Level: {__skill_level__}")
        print(f"Total Days: {total_days}")
        print(f"Year: {Year}")
        print("------------------------------")
    elif Play.lower() in ['clearmessages', 'clear']:
      clear.ScreenClearer().clear_screen()
      print(f"Version: {__Version__}")
      print("Type Help To See The Commands.")
      print("Start Playing.")
      print("Your Save Has Been Updated")
    elif Play.lower() in ['lb', 'leaderboard']:
      print("Name for Leaderboard.")
      Nameforlb = input("> ")
      message = f'Name: {Nameforlb}, Cash: {Cash} Day: {Day}, Skill Level: {__skill_level__}, Year: {Year}, Total Days: {total_days}'
      response = requests.post("https://api.cluefixx.repl.co", headers={'API-Key': "Jc81LOppnnm25h5fw47jreh"}, data={'message': message})
      if response.status_code == 200:
        print('Data saved successfully!')
        print(F'Leaderboard: {Zen.BLUE}https://api.cluefixx.repl.co')
      else:
        print('Error:', response.text)
    elif Play.lower() == "craft":
       while True:
         print(Zen.RESET+"------------------------------")
         print(f"Hammer: {__Hammerequire__}")
         print(f"Tv: {__tvrequire__}")
         print(f"Fan: {__fanreqire__}")
         print(f"Door:  {__doorreqire__}")
         print(f"Cup:  {__cupreqire__}")
         print(f"Phone:  {__phonereqire__}")
         print("------------------------------")
         Craftinput = input("Enter the item you want to Craft (or 'exit' to return to the main menu):")
         if Craftinput.lower() == 'exit':
            break
         if Craftinput.lower() == "hammer":
             if all(inv.count(item) >= __Hammerequire__.count(item) for item in __Hammerequire__):
                 for item in __Hammerequire__:
                    inv.remove(item)
                 inv.append("hammer")
                 print(Zen.YELLOW+"You successfully Crafted a Hammer!")
             else:
                 print(f"{Zen.RED}Cant Craft: %s" % Craftinput.lower())
         if Craftinput.lower() == "tv":
            if all(inv.count(item) >= __tvrequire__.count(item) for item in __tvrequire__):
                 for item in __tvrequire__:
                    inv.remove(item)
                 inv.append("tv")
                 print(Zen.YELLOW+"You successfully Crafted a Tv!")
            else:
                 print(f"{Zen.RED}Cant Craft: %s" % Craftinput.lower())
         if Craftinput.lower() == "fan":
             if all(inv.count(item) >= __fanreqire__.count(item) for item in __fanreqire__):
                 for item in __fanreqire__:
                    inv.remove(item)
                 inv.append("fan")
                 print(Zen.YELLOW+"You successfully Crafted a Fan!")
             else:
                 print(f"{Zen.RED}Cant Craft: %s" % Craftinput.lower())
         if Craftinput.lower() == "door":
             if all(inv.count(item) >= __doorreqire__.count(item) for item in __doorreqire__):
                 for item in __doorreqire__:
                    inv.remove(item)
                 inv.append("door")
                 print(Zen.YELLOW+"You successfully Crafted a Door!")
             else:
                 print(f"{Zen.RED}Cant Craft: %s" % Craftinput.lower())
         if Craftinput.lower() == "cup":
             if all(inv.count(item) >= __cupreqire__.count(item) for item in __cupreqire__):
                 for item in __cupreqire__:
                    inv.remove(item)
                 inv.append("cup")
                 print(Zen.YELLOW+"You successfully Crafted a Cup!")
             else:
                 print(f"{Zen.RED}Cant Craft: %s" % Craftinput.lower())
         if Craftinput.lower() == "Phone":
             if all(inv.count(item) >= __phonereqire__.count(item) for item in __phonereqire__):
                 for item in __phonereqire__:
                    inv.remove(item)
                 inv.append("Phone")
                 print(Zen.YELLOW+"You successfully Crafted a Phone!")
             else:
                 print(f"{Zen.RED}Cant Craft: %s" % Craftinput.lower())
    elif Play in cmds:
      pass
    else:
      if Day >= 365:
        Day = 0
        Year += 1 
        print("It's been a whole year. Here is a random item.")
        weights = [1] * len(items)
        item = random.choices(items, weights=weights, k=1)
        inv.extend(item)
      else:
        pass
      Day += 1
      total_days += 1
      save_updater = Classes.SaveUpdate()
      save_updater.update_save_files(Cash, Name, Job, inv, Day, __skill_level__)
      if weeklytimeleft > 0:
        weeklytimeleft -= 1
      if not Admin:
        if Cash >= 1000000000:
          print(f"You have been Wiped for Having {Cash} : Cash")
          time.sleep(1.5)
          clear.ScreenClearer().clear_screen()
          wipe_saver = Classes.WipeSave()
          wipe_saver.update_save_files()
          Cash = int(Classes.CashLoad.Casho)
          Name = str(Classes.NameLoad.Nameo)
          Job = str(Classes.JobLoad.Jobo)
          inv = eval(Classes.Invload.invo)
          Day = int(Classes.DayLoad.Dayo)
          print(Zen.RESET+f"Version: {__Version__}")
          print(Zen.RESET+"Type Help To See The Commands.")
          print(Zen.RESET+"Start Playing.")
      else:
        pass
    if Play.lower() in ['w', 'wipe']:
      if used_load:
        print(Zen.RED+"Are you Sure y/n")
        Wipe_Ask=input(Zen.MAGENTA+"> ")
        if Wipe_Ask in ['yes', 'y']:
          print("Wiping...")
          time.sleep(1.5)
          clear.ScreenClearer().clear_screen()
          wipe_saver = Classes.WipeSave()
          wipe_saver.update_save_files()
          Cash = int(Classes.CashLoad.Casho)
          Name = str(Classes.NameLoad.Nameo)
          Job = str(Classes.JobLoad.Jobo)
          inv = eval(Classes.Invload.invo)
          Day = int(Classes.DayLoad.Dayo)
          print(Zen.RESET+f"Version: {__Version__}")
          print(Zen.RESET+"Type Help To See The Commands.")
          print(Zen.RESET+"Start Playing.")
      else:
        print("You Can't Wipe A Save That does not exist")
    elif Play.lower() == "help":
        print(f'Commands: {cmds}')
        print('Our Devs Will Add More')
    elif Play.lower() == "inv":
      print(inv)
    elif Play.lower() == "job":
      if Job in ['', 'None']:
        print("You Dont Have A Job")
        print("Jobs:")
        print("Computer Programmer, 5k - 1")
        print("Doctor, 8k - 2")
        print("Cook, 100$ - 3")
        print("Graphics Developer, 6k - 4")
        print("Discord Mod:, 1k - 5")
        acs=input(Zen.RESET+"> ")
        if acs.lower() in ["discord mod", "1"]:
          if __skill_level__ >= 1:
            print("Your Now A Discord Mod, Pay - 1k Per Week")
            print('First Pay Check - 1k')
            Cash+=1000
            weeklytimeleft+=7
            Job="Discord Mod"
        if acs.lower() in ["computer programmer", "1"]:
          if __skill_level__ >= 3:
            print("Your Now A Computer Programmer, Pay - 5k Per Week")
            print('First Pay Check - 5k')
            Cash+=5000
            weeklytimeleft+=7
            Job="Computer Programmer"
          else:
             print(Zen.RED+"You Dont Have A high enough skill")
        if acs.lower() in ["doctor", "2"]:
          if __skill_level__ >= 10:
            print("Your Now A Doctor, Pay - 8k Per Week")
            print('First Pay Check - 8k')
            Cash+=8000
            weeklytimeleft+=7
            Job="Doctor"
        if acs.lower() in ["cook", "3"]:
          if __skill_level__ >= 0:
            print("Your Now A Game Cook, Pay - 100$ Per Week")
            print('First Pay Check - 100$')
            Cash+=100
            weeklytimeleft+=7
            Job="cook"
        if acs.lower() in ["graphics Developer", "4"]:
          if __skill_level__ >= 5:
            print("Your Now A Graphics Developer, Pay - 6k Per Week")
            print('First Pay Check - 6k')
            Cash+=6000
            weeklytimeleft+=7
            Job="Graphics Developer"
      else:
        print(f"Your Job Is {Job}")
    elif Play.lower() =='pay':
      if weeklytimeleft==0:
        if Job in ['', 'None']:
          print("You Dont Have a Job So You Only Get 500$")
          Cash+=500
          weeklytimeleft+=7
        else:
          if Job == "Discord Mod":
            print("Good PayCheck - 1k")
            Cash+=1000
            weeklytimeleft+=7
            __skill_level__+= 00.9
          if Job == "Computer Programmer":
            print("Good PayCheck - 5k")
            Cash+=5000
            weeklytimeleft+=7
            __skill_level__+= 0.10
          if Job == "Doctor":
            print("Good PayCheck - 8k")
            Cash+=8000
            weeklytimeleft+=7
            __skill_level__+= 0.30
          if Job == "cook":
            __skill_level__
            print("Good PayCheck - 100$")
            Cash+=100
            weeklytimeleft+=7
            __skill_level__+= 00.1
          if Job == "Graphics Developer":
            print("Good PayCheck - 6k")
            Cash+=6000
            weeklytimeleft+=7
            __skill_level__+= 0.3
      else:
        print("You Have To Wait To Get Your PayCheck")
    elif Play.lower() == 'quit job':
      if Job == 'None' or '':
        print('You dont have a job.')
      else:
        print('You quit your Job.')
        Job = "None"
        
    
    if Play.lower() in ['store', 'shop']:
        print("The Store Has")
        print(f"Money: {Cash}")
        print("----------------------------")
        for item in Store:
            name, price = item.split(':')
            price = int(price)
            print(f"{name.capitalize()}: {price}$")
        print("----------------------------")

        while True:
            aga = input(Zen.RESET + "Enter the item you want to buy (or 'exit' to return to the main menu): ")
            if aga.lower() == 'exit':
                break
            found = False
            for item in Store:
                name, price = item.split(':')
                if aga.lower() == name.lower():
                    found = True
                    if int(price) <= int(Cash):
                        print(f"{Zen.YELLOW}You Bought an {name.capitalize()}! {Zen.RESET}")
                        inv.append(name)
                        Cash -= int(price)
                    else:
                        print(f"{Zen.RED}You don't have enough money to buy that item. {Zen.RESET}")
                    break

            if not found:
                print(f"{Zen.RED}That is not an item in this store {Zen.RESET}")
#--------------------------------------------------------------------------
#Admin
    if Play.lower() == "admin":
        if Admin:
            print(Zen.MAGENTA + "Admin Room")
            askr = input(Zen.RESET + "> ")
            if askr.startswith("addmoney"):
                addmoney = askr.removeprefix("addmoney")
                Cash += int(addmoney)
                print(f"Added {addmoney} to the Money Value")
            elif askr.startswith('acis'):
                print("--Note Example Apple:5")
                acis = askr.removeprefix("acis ")
                Store.append(acis)
                print(f"Added {acis} to the Store")
            elif askr.startswith("adday"):
                adday = askr.removeprefix("adday")
                Day += int(adday)
                print(f"Added {adday} to the Day Value")
            elif askr.startswith("changename"):
                xName = Name
                changedname = askr.removeprefix("changename ")
                Name = changedname
                print(f"Changed Your name From {xName} to {changedname}")
            elif askr.startswith("setjob"):
                setjob = askr.removeprefix("setjob ")
                Job = setjob
                print(f"Set Your Job to {setjob}")
            elif askr.startswith("setversion"):
               setversion = askr.removeprefix("setversion ")
               __Version__= setversion
               print(f"Set the Version to {setversion}")
            elif askr.startswith("weeklytimerest"):
               addtimeleft = askr.removeprefix("weeklytimerest")
               weeklytimeleft = int(addtimeleft)
               print(f"Rest Weekly Time Left: {weeklytimeleft}")
            elif askr.startswith("allitems"):
               inv.extend(items)
               print("Added all the items to your inventory")
            elif askr.startswith("additem"):
               additem = askr.removeprefix("additem ")
               inv.append(additem)
               print(f"added {additem} to your inventory")
            elif askr.startswith("setskill"):
                setskill = askr.removeprefix("setskill")
                __skill_level__ += int(adday)
                print(f"Added {setskill} to the __skill_level__ Value")
            elif askr.startswith('setyear'):
              timetoadd = askr.removeprefix("setyear")
              Year += timetoadd
            elif askr.startswith('settotaldays'):
              td = askr.removeprefix("settotaldays")
              total_days += td
              
        else: 
            print("You're Not An Admin")
