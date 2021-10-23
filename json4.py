# import json
# j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
# with open("myfile.json","w") as f:
#     json.dump(j_str,f,sort_keys=True,indent=4)
# # print(b)

import requests
import json
URl=requests.get("https://api.merakilearn.org/courses") 
meraki_URl=URl.json() 
# print(meraki_URl)
with open("tex.json","w")as file_deta :
    file=json.dump(meraki_URl,file_deta,indent=3)
serial_number=1
for i in meraki_URl:
    print(serial_number,i["name"],i["id"])
    serial_number+=1
course_no=int(input("enter the courses"))
print(meraki_URl[course_no-1]["name"])
var1=meraki_URl[course_no-1]["id"]
url_1=requests.get("http://api.merakilearn.org/courses/"+str(var1)+"/exercises")
var=url_1.json()
# print(url_1)
with open("monika.json","w")as t:
    json.dump(var,t,indent=4)
    serial_number2=1
    list1=[]
    list2=[]
for j in var["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(serial_number2,j["name"])
        print("   ",serial_number2,j["slug"])
        serial_number2+=1
        # print(j)
        new_no=1
        list1.append(j)
        list2.append(j)
        # print(list1,list2)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial_number2,j["name"])
        serial_number2+=1
        new_no=1
        list1.append(j)
        print(list1)
    for l in var["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print(" ",new_no,j["name"])
            new_no+=1
            list2.append(j)
            # print(list2)
            break
with open("monika_prjapt.json","w")as f:
    json.dump(list1,f,indent=4)
    # print(list1)
    # parent=int(input())







