import random
import time
print("--Your Omnitrix--\n")

list = ["Clomastone", "Diamondhead", "Spidermonkey" ,"Swampfire", "Jetray" , "Humungousaur" , "Spidermonkey"  , "Brainstorm" ,  "Bigchill" , "Goop"  ,"Cannonbolt" , 'Rath' , "Upchuck", "NRG", "Armodrillo" ,"Terraspin", "Ampfibian", "Fourarms", "Nanomech", "Waybig", "Ripjaws", "Heatblast", "Wildmutt"]

a = None 

aliens =[ ]

while len(aliens) <= 4:
	a = random.choice(list)
	if a in aliens:
		continue
	else:
                aliens.append(a)
                time.sleep(0.3)
                print(a)
        
        

time.sleep(0.5)
print("Now vilgax is comming .Hurry up !! Select any alien to defeat vilgax\n")

alien = None
while alien not in aliens:
        x = input("Select alien: ")
        alien = x.capitalize()

randomAliens = random.choice(aliens)

print("Now Vilgax has Arrived\n")
time.sleep(2)
print("Now Vigax is comming to kill you\n")
if alien in randomAliens:
        print(f"congratulation! your {alien} kick on Vilgax ass you Defeat him")

else:
        print(f"Ahh you lose , Vilgax kill your {alien} \n if you select  {randomAliens} that might defeat Villgax")