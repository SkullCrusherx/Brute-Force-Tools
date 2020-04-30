from  colored import fg,attr
color_1 = fg("#0be313")
color_2 = fg('#ed45e2')
reset = attr('reset')
print(color_1+" ________                                      ___  ")
print(" `MMMMMMMb.                                    `MM  ")
print("  MM    `Mb                     /               MM  ")
print("  MM     MM ___  __ ___   ___  /M        ___    MM  ")
print("  MM    .M9 `MM 6MM `MM    MM /MMMMM   6MMMMb   MM  ")
print("  MMMMMMM(   MM69    MM    MM  MM     8M'  `Mb  MM   ")
print("  MM    `Mb  MM'     MM    MM  MM         ,oMM  MM  ")
print("  MM     MM  MM      MM    MM  MM     ,6MM9'MM  MM  ")
print("  MM     MM  MM      MM    MM  MM     MM'   MM  MM  ")
print("  MM    .M9  MM      YM.   MM  YM.  , MM.  ,MM  MM  ")
print(" _MMMMMMM9' _MM_      YMMM9MM_  YMMM9 `YMMM9'Yb_MM_ "+reset)
print("\n\t\t\t\t\t\t\tscripted by Sh4d0w1729")

#print("\n\t\t\t\t\t\t\t\t")
#os call

import os

print("1.RuN!")
print("2.PaSS list generate")

choose = input("please select your options : ")

if choose == "1":
    os.system("clear")
    os.system('python3 668.py')
    os.system('python3 345.py')

elif choose == "2":
    os.system('clear')
    os.system('python3 678.py')
    try:
        need = int(input("how much you 1st number : "))
        need2 = int(input("how much you 2nd number : "))
        string = input('enter string : ')
    except:
        print(color_2+"VALUE ERROR"+reset)

    def generate():
        try:
            passfile = open('pass.txt','w')
            for x in range(need,need2):
                passfile.write(str(x)+ string +'\n')
            print("success full !")
            passfile.close()
        except:
            print("THANKS FOR USING TRYING AGAIN")
    generate()
else:
    print("try again!")