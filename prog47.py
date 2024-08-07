# 1. write a program to calculate the electricity bill(accept number of unit from user)according to following criteria : 
# unit [first 100 units:no charges],[next 100 units :rs 5 per unit],[after 200 units:rs 10 per units] 
# for example if 350 units bil is rs2000.

def calculate_bill(units):
    
    if units <= 100:
        return 0  
    elif units <= 200:
        return (units - 100) * 5 
    else:
        return (100 * 5) + (units - 200) * 10  

units = int(input("Enter the number of units consumed: "))
print("Your electricity bill is: Rs.", calculate_bill(units))