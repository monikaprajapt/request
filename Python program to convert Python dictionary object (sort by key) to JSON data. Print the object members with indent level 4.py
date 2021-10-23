# import json
# j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
# # print("Original String:")
# # print(j_str)
# # print("\nJSON data:")
# print(json.dumps(j_str, sort_keys=True))


# a=["monika"]
# l =[]
# dic = {}
# for i in a: 
#     for j in i:
#         l.append(j)
# # print(l)
# i = 0
# for x in l:
#     dic.update({x:i})
#     i+=1
# print(dic)










import json
def is_complex_num(objct):
    if 'complex' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object =json.loads('{"complex": true, "real": 4, "img": 5}', object_hook = is_complex_num)
simple_object =json.loads('{"real": 4, "img": 5}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)
print("Without complex object: ",simple_object)