#  
#     









import re
import json
import os
file = os.path.exists('name.json')
if file ==False:
    user=input("what you want to login ya signup ")
    if user=="signup":
        list=[]
        dic={}
        name=input("enter the name : ")
        passward=input("enter the passward : ")
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passward):
            print("strong passward")
            confurm_passward=input("enter the confurm_passward : ")
            if confurm_passward==passward:
                print("right") 
                desserpetions=input("enter the desserpetions : ")
                date_of_birth=input("enter the date_of_birth : ")
                habits=input("enter the habits : ")
                dict={"name":name,"passward":passward,"descripation":desserpetions,"do_birth":date_of_birth,"hobit":habits}
                list.append(dict)
                dic.update({passward:list})
                with open("name.json","a")as f:
                    b=json.dump(dic,f,indent=4)                
            
        else:
            print("wrong password")
elif file==True:
    user=input("what you want to login ya signup ")
    if user=="signup":
        list=[]
        dic={}
        name=input("enter the name : ")
        a=os.path.exists("name.json")
        # for a in name:
        #     print("aalready hai")
        #    print("allready hai")
        # else:
        passward=input("enter the passwars : ")
        if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', passward):
            print("strong passward")
            confurm_passward=input("enter the confurm_passward : ")
            if confurm_passward==passward:
                print("right")                   
                desserpetions=input("enter the desserpetions : ")
                date_of_birth=input("enter the date_of_birth : ")
                habits=input("enter the habits : ")
                dict={"name":name,"passward":passward,"descripation":desserpetions,"do_birth":date_of_birth,"hobit":habits}
                list.append(dict)
                dic.update({passward:list})
                with open("name.json","a")as f:
                    b=json.dump(dic,f,indent=4)
                
            
        else:
            print("wrong password")
    else:
        
        if user=="login":
            user_name=input("enter the user name")  
            conform_passward=input("enter the passwor")
            with open("name.json","r")as f:
                b=json.load(f)
                if conform_passward==b['Monika@123'][0]["passward"]:
                    print("login succesfully")
                    print(b)
        else:
            print("your deatils is wrong")