
import json
print("***welcome to login and signup***")
user=input("we want to you login and signup")
if user=="signup":
    user_name=input("enter the user name")
    password1=input("enter the password")
    password2=input("enter rhe comfrom paasword")
    if password1==password2:
        descripation=input("enter rhe descripation")
        do_birth=input("enter the do_birth")
        gander=input("enter the gander")
        hobij=input("enter the hobij")
        dict={"user_name":user_name,"password2":password2,"descripation":descripation,"do_birth":do_birth,"gander":gander,"hobij":hobij}
        with open("text.json","w")as f:
         b=json.dump(dict,f,indent=4)
    else:
        
        print("wrong password")
else:
    if user=="login":
        user_name=input("enter the user name")
        password=input("enter the passwor")
        with open("text.json","r")as f:
            b=json.load(f)
            if password==b["password2"]:
                print("login succesfully")
                print(b)
    else:
        print("your deatils is rong")



    