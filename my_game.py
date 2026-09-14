n = int(input())

print("--------------------------")
print("NUMBER GUESSING GAME")
print("--------------------------")

while True:
    guess = int(input("Enter your guess:"))
    break

if guess>n:
    print("its too high")

elif guess<n:
    print("its too low")

elif guess==n:
    print("its correct")

else:
    print("wrong guess try again")

print()    

reply = (input("do you want to replay:yes/no:"))

if reply == "yes":
    print("okay, game replaying...")
else:
    print("Thankyou 😊")    

       


