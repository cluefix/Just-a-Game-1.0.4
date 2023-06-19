import random
xx="Cash"
vv="Inv"
bb="Job"
mm="Name"
cc=""
dd="Day"
Job1="None"
inv1=['phone', 'apple']
Name1 = 'Player' + str(random.randint(1000, 9999))
Cash1=150
Day1=0
__Version__="1.0.3"
class DayLoad():
  with open("Data/Day.txt", "r") as f:
    line1 = f.read()
    Dayo = str(line1.removeprefix("Day:"))
class CashLoad():
    with open("Data/Cash.txt", "r") as f:
      line1 = f.read()
      Casho = str(line1.removeprefix("Cash:"))
class NameLoad():
    with open("Data/Name.txt", "r") as f:
      line1 = f.read()
      Nameo = str(line1.removeprefix("Name:"))
      Nma=Nameo
class JobLoad():
    with open("Data/Job.txt", "r") as f:
      line1 = f.read()
      Jobo = str(line1.removeprefix("Job:"))
class Invload():
  with open("Data/Inv.txt", "r") as f:
    line1 = f.read()
    invo = str(line1)
class SaveUpdate():
    def update_save_files(self, cash, name, job, inv, day):
        with open("Data/Cash.txt", "w") as f:
            f.write(f"{xx}{cc}:{cash}")

        with open("Data/Name.txt", "w") as g:
            g.write(f"{mm}{cc}:{name}")

        with open("Data/Job.txt", "w") as h:
            h.write(f"{bb}{cc}:{job}")

        with open("Data/Inv.txt", "w") as j:
            j.write(f"{inv}")

        with open("Data/Day.txt", "w") as k:
            k.write(f"{dd}{cc}:{day}")

class WipeSave():
    def update_save_files(self):
        with open("Data/Cash.txt", "w") as f:
            f.truncate(0)
            f.write(f"{xx}{cc}:0")

        with open("Data/Name.txt", "w") as g:
            g.truncate(0)
            g.write(f"{mm}{cc}:None")

        with open("Data/Job.txt", "w") as h:
            h.truncate(0)
            h.write(f"{bb}{cc}:None")

        with open("Data/Inv.txt", "w") as j:
            j.truncate(0)
            j.write("[]")

        with open("Data/Day.txt", "w") as k:
            k.truncate(0)
            k.write(f"{dd}{cc}:0")
class Nonload():
  Job1="None"
  inv1=['Apple', 'Phone']
  Name1 = 'Player#' + str(random.randint(1000, 9999))
  Cash1 = 200
  Day1= 0