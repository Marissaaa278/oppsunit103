# Write a program in python that splits the bill evenly between group.
# Ask how much they want to tip and how many people


#Example
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill=float(input("Enter the cost of the bill"))
people= int(input("Enter the amount of people paying"))
tip=float(input("Enter the tip percentage"))

answer=(bill/people) *1 + (tip/100)

total= round(answer)

print("everyone has to pay")
print(total)



