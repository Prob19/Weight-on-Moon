import math



objects_weight=float(input("Enter weight of object on Earth (in lbs)"))
moon_weight=objects_weight*.165

earth_weightkg=objects_weight*0.45359237

ounce_weight=int((moon_weight%1)*16)

moon_weightkg=earth_weightkg*.165
moon_weightg= (moon_weightkg%1)*1000
print("The objects weight on the moon is" ,float(int(moon_weight)), "lbs", float(ounce_weight), "oz")
print("The objects weight on the moon is" , int(moon_weightkg), "kgs", int(moon_weightg), "g")




pythoid_lbs= math.sqrt(((objects_weight**2-13)/8)+22)*4

pythoid_oz=(pythoid_lbs%1)*100

print("The objects weight on Pythoid is", int(pythoid_lbs), "lbs", int(pythoid_oz), "oz")

