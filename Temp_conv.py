temperature=float(input("Enter valid temperature:"))
print("Enter  valid units")
print("1 for celsius to fahrenheit")
print("2 for fahrenheit to celsius")
choice=int(input("chose 1 (or) 2 -> "))
def cel_to_fah(temp):
    return (temp*(9/5))+32
def fah_to_cel(temp):
    return (temp-32)*(5/9)
if(choice==1):
    print("Conversion result:",cel_to_fah(temperature),"°F")
elif(choice==2):
    print("Conversion result:",fah_to_cel(temperature),"°C")
else:
    print("Invalid choice")