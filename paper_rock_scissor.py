{\rtf1\ansi\ansicpg1252\deff0\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Msftedit 5.41.21.2509;}\viewkind4\uc1\pard\sa200\sl276\slmult1\lang9\f0\fs22 import random\par
print("**************************************************")\par
print("*          *SCISSOR * ROCK  * PAPER  *            *")\par
print("****************************************************")\par
print(" Less start the game!!..........")\par
point=0\par
ai=0\par
hs=0\par
cs=0\par
ma=0\par
while(True):\par
    if(ma>5):\par
      print("************************************")\par
      print("total match:",ma,)\par
      print("human score",hs,)\par
      print("Ai score:" ,cs,)\par
      if(hs>cs):\par
        print(" congrats you won ")\par
      elif(cs>hs):\par
        print("Ai won.......better luck next time")\par
      else:\par
        print("match drawn")\par
      print("************************************")\par
      break\par
    c=input(" choose the option scissor->s rock->r  paper->p stop->stop ")\par
    if(c=="s"):\par
      point=10+random.randint(1,3)\par
      match point:\par
        case 11:\par
               ma=ma+1\par
               hs=hs+1\par
               print(" human paper", "Ai:rock ")\par
               print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
               print("Human:win","Ai: lost")\par
               print(" ------------------------------ ")\par
        case 12:\par
                ma=ma+1\par
                cs=cs+1\par
                print(" human paper", "Ai:paper ")\par
                print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
                print(" human wins","Ai: wins ")\par
                print(" ------------------------------ ")\par
        case 13:\par
                ma=ma+1\par
                hs=hs+1\par
                cs=cs+1\par
                print("human paper"," Ai:scissor ")\par
                print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
                print("match draw ")\par
                print(" ----------------------------- ")\par
    elif(c=="R"):\par
       print("rock")\par
       point=20+random.randint(1,3)\par
       match point:\par
            case 21:\par
               ma=ma+1\par
               hs=hs+1\par
               print(" human rock", "Ai:paper ")\par
               print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
               print(" human wins","Ai: lost  ")\par
               print(" ------------------------------ ")\par
            case 22:\par
               ma=ma+1\par
               cs=cs+1\par
               print(" human rock", "Ai:rock ")\par
               print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
               print(" human wins","Ai: wins ")\par
               print(" ------------------------------ ")\par
            case 23:\par
               ma=ma+1\par
               hs=hs+1\par
               cs=cs+1\par
               print("human rock"," Ai:scissor ")\par
               print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
               print("match draw ")\par
               print(" ----------------------------- ")    \par
    elif(c=="p"):\par
        print("paper")\par
        point=30+random.randint(1,3)\par
        match point:\par
            case 31:\par
               ma=ma+1\par
               hs=hs+1\par
               print(" human scissor", "Ai:paper ")\par
               print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
               print(" human wins","Ai: lost  ")\par
               print(" ------------------------------ ")\par
            case 32:\par
                ma=ma+1\par
                cs=cs+1\par
                print(" human scissor", "Ai:rock ")\par
                print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
                print(" human wins","Ai: wins ")\par
                print(" ------------------------------ ")\par
            case 33:\par
                ma=ma+1\par
                hs=hs+1\par
                cs=cs+1\par
                print("human scissor"," Ai:scissor ")\par
                print(" match:",ma," Human score:",hs,"Ai:score  ",cs,)\par
                print("match draw ")\par
                print(" ----------------------------- ")     \par
    elif(c=="stop"):\par
        break\par
print("program end")\par
}
