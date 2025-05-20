## total input we need from user
# total rent
# electricity units
# bill per unit
# meal
# number of person

## output
# total amount one has to pay 

rent=int(input("Enter your flat/hostel rent : "))
meal=int(input("Enter total meal cost : "))
elec_un=int(input("Enter total unit of electricity : "))
bill_pu=int(input("Enter per unit cost : "))
person=int(input("Enter total person : "))

total_elec_bill=elec_un*bill_pu
total_cost=total_elec_bill+rent+meal
per_person_cost=total_cost/person
print("Per person Cost is : ",per_person_cost)