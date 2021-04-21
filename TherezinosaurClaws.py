import time

times = 0
strength = 0
stamina = 100

def slash(times, strength, stamina):
    can_slash = True
    for n in range(times):
       if can_slash == True:
           if stamina >= 0 and strength <= 10:
               print("Therezinosaurus has slashed with a strength of", strength)
               stamina -= strength
           elif stamina <= 0:
               print("Stamina ran out")
               print("Unable to continue")
               can_slash = False
       else:
           time.sleep(3)
           exit()


       time.sleep(0.5)

    print("Process Finished Successfully!")
    time.sleep(3)
    exit()


print('''
  _______ _                       _                                            
 |__   __| |                     (_)                                           
    | |  | |__   ___ _ __ ___ _____ _ __   ___  ___  __ _ _   _ _ __ _   _ ___ 
    | |  | '_ \ / _ \ '__/ _ \_  / | '_ \ / _ \/ __|/ _` | | | | '__| | | / __|
    | |  | | | |  __/ | |  __// /| | | | | (_) \__ \ (_| | |_| | |  | |_| \__ \\
    |_|  |_| |_|\___|_|  \___/___|_|_| |_|\___/|___/\__,_|\__,_|_|   \__,_|___/
    ''')
times = int(input("Input Times You want to Attack: "))
strength = int(input("Input Therezinosaur Strength: "))
print("\n")

if strength > 10:
    print("That is to strong! it will injure your dino.")
else:
    slash(times, strength, stamina)
