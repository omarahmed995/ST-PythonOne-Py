print("HEllo World")


# This a comment

# define a variable
# x = 10  # interpreted lang
# print(x)
#
# # # python is interpreted lang. ---> loosly dynamically typed lang
# # interpreter detect datatype of  varibale in the runtime
# # you change the datatype of the variable
#
# x = 'python'
#
# # ######### primitive datatypes ---->
# ### non primitive datatype
#
# l = ["iti", "python", "django", 2022, 9, 11, True ]
# # list is mutable datatype ---> can be changed in the run time
# print(l[0])
# ## list
# t = ("Saturday", "Sunday", "Monday", 9, False, ["abc", "python"])
# ## immutable datatype cannot be change in the runtime
# print(t[2])
# # ## non primitive datatype dictionary ---
# info = {"name":"noha", "works_at":"iti"}
# print(info["name"])
# # ####################################################
#
# for i in t:
#     print(i)
##########################################


# # function --> write code once use many


# def sumnum(num1, num2):
#     sum = num1 + num2
#     return sum
#
#
# z = sumnum(10, 10)
# print(z)
#
# print("-------------------------")
#
# m = sumnum(100, 100)
# print(m)

################## None ----> nothing

def sayhello(name):
    print(f"Hello {name}")
    return


res = sayhello("Ahmed")
print(res)