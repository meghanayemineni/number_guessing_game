n = int(input("Enter secret number:"))

print("--------------------------")
print("NUMBER GUESSING GAME")
print("--------------------------")

while True:
    guess = int(input("Enter your guess:"))

if guess>n:
    print("its too high")

elif guess<n:
    print("its too low")
    
else:
    print("correct")
    break

reply = input("do you want to replay:yes/no:")

if reply == "yes":
    print("okay, game replaying...")
else:
    print("Thankyou 😊")    

       


