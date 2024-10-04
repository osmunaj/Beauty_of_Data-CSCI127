


homeruns = {}
homeruns["Babe Ruth"] = 714
homeruns["Mickey Mantle"] = 536
homeruns["Ari Osmun"] = 0
#Dictionaries contain keys and values

# {'C':3,'I':9,'D':4,'T':20}
#KEYS ARE NOT MUTABLE

print(type(homeruns))
print("homeruns => ", homeruns)
print("\nhomerun.keys => ", homeruns.keys())
print("\nhomerun.values() => ", homeruns.values())
print("\nhomerun.items() => ",homeruns.items())
temp = "Mickey Mantle"
print("\nhomeruns.get('Mickey Mantle') => ",homeruns.get("Mickey Mantle")) #Uses key as parameter, gets the value
print(homeruns.get(temp))

myRect = {'width':10,'height':7.5,'color':"blue"}
print(myRect.get('width'))
area = myRect.get('width')*myRect.get('height')
print("Area = ", area)