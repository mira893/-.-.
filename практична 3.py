dict = {1:"6", 2:"64", 3:"4", 4:"1", 5:"32", 6:"12", 7:"98", 8:"21", 9:"7", 10:"50"}
print(dict)
dict.update({2:63})
dict.update({7:99})
dict.pop(3)
dict[4] = ""
print(dict)