print("_"*107)
a="SPOTIFLY"#Heading
b=a.center(107)#Center alignment
print(b)
print("_"*107)
import pickle
import time
import emoji
c="Welcome to Spotifly! Enjoy the world of music !"#Welcome message
d=c.center(107)
print("  ")
time.sleep(1)
print(d)
time.sleep(1)
print(" ")
d1={}
username=input("Enter your username:")
password=input("Enter your password:")
d1[username]=(password)
f=open("credential.dat",'wb')
pickle.dump(d1,f)
f.close()
print(" ")
print("Please wait for a moment...")
time.sleep(3)
print("User name and password successfully created!","\nYou are good to go!")
print(' ')
load=("Loading...")
print(load.center(107))
time.sleep(1)
print(' ')
print("Hello...",username,emoji.emojize(":woman:"),'.',"I am Blaire.Your personal spotifly comapanion!")
e=input("Shall i present you a menu(yes/no):")
if e in "YyyesYES":
    time.sleep(2)
    print(' ')
    print("Please enter your desired operation:")#menu
    print("1.Create playlist")
    print("2.Search artist")
    print("3.Search according mood")
    print("4.Know about us")
    print("5.Privacy policy")
    print("6.Quit")
    
else:
     print("It seems that you are not in a mood to listen music!")
     print("Closing Spotifly...")
     time.sleep(3)
     exit()
while True :
     from newmodule import *
     print(" ")
     ch=int(input("Enter your choice:"))
     if ch==1:
          playlist()
     elif ch==2:
          artist()
     elif ch==3:
          mood()
     elif ch==4:
          kou()
     elif ch==5:
          policy()
     elif ch==6:
          import time
          import emoji
          a=input("Are you sure you want to quit the world of music?")
          if a in "yesYESyY":
               print("Closing..."),print(emoji.emojize(":musical_note:"))
               time.sleep(2)
               exit()
               break
     else:
          continue


    
