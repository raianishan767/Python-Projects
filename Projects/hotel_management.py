Menu={
    "Burger":250,
    "Rice Bowl":330,
    "Pasta":380,
    "Meat Box":490,
    "Pizza":550,   
}
 
print("Welcome to XYZ restaurant")
print("Our available items to serve you are,")
print(" Burger 250/-\n Rice Bowl 330/-\n Pasta 380/-\n Meat Box 490/-\n Pizza 550/-")
item_1=input("Which item do you want to choose :")

bill=0

if item_1 in Menu:
     bill += Menu[item_1]
     print(f"Your item {item_1} is added")
else:
     print(f"Your ordered item {item_1} is not available for now")

get=input("Do you want to order more?")
if get=="yes":
  item_2=input("Which item do you want to choose :")
  bill += Menu[item_2]
  print("Your Bill is ",bill)
else:
  print("Your Bill is ",bill)
  

