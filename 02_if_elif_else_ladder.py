a = int(input("Enter your age: "))

# If elif alse ladder
if(a>18):
    print("tou are above the age of consent")
    print("Good for you")

elif(a<0):
    print("your are entering an invalid age")

elif(a==0):
    print("you are entering 0 which is not a valed age")
    
else:
    print("you areblow the page of consent")


print("ENd of program")