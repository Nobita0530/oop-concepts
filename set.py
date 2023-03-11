# a={"sunny","prasad","krushna","chetan","yash"}
# print (a)

# a={"sunny","prasad","krushna","chetan","yash"}
# for i in a:
#     print(i)
    
# set= unorder data , unchngebale and duplicate not allow set is collection is unchangeable and un index and no duplicate member     
# a={"sunny","prasad","krushna","chetan","yash","sunny","prasad"}
# b=set(a)
# print(b)

# a={"sunny","prasad","krushna","chetan","yash"}
# a.apend("sunny")
# print(a)

# dictinoray

# a={"fy":"80","sy":"60","ty":"70"}
# print(a)


# a={"fy":"80","sy":"60","ty":"70"}
# a["sy"]="100"
# print(a)

# a={"fy":"80","sy":"60","ty":"70"}
# k=a.keys()
# print(k)

# a={"fy":"80","sy":"60","ty":"70"}
# v=a.values()
# print(v)

# a={"fy":"80","sy":"60","ty":"70"}
# i=a.items()
# print(i)

# a={"color":"red","name":"yash","bike":"hf"}
# if "color" in a:
#     print(a["color"])
# else:
#     print("not available")


# a={"fy":"80","sy":"60","ty":"70"}
# a.update({"fy":"100","sy":"200"})
# print(a)    
# a["year"]=2022
# print(a)

# a={"color":"red","name":"yash","bike":"hf"}
# a.popitem()
# print(a)

# a={"color":"red","name":"yash","bike":"hf"}
# for x in a:
#     print(a[x])


# a={"color":"red","name":"yash","bike":"hf"}
# for x in a.keys():
#     print(x)


# a={"color":"red","name":"yash","bike":"hf"}
# for x in a.values():
#     print(x)

# a={"color":"red","name":"yash","bike":"hf"}
# for x,y in a.items():
#     print(x,y)


# a={"color":"red","name":"yash","bike":"hf"}
# b=a.copy()
# print(b)


# a={"color":"red","name":"yash","bike":"hf"}
# b=dict (a)
# print(b)



a={"color":"red"}
b={"name":"yash"}
c={"bike":"hf"}
z={"first":a,"second":b,"third":c}
print(z["second"]["name"])