
def collatz(number):
    if number%2==0:
        return number//2
    return 3*number + 1

def userInput():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Error: Numnber not a valid integer number.")
            print("Try Again!!");

print("Input the number.")
myNumber=userInput()
while myNumber !=1:
    myNumber=collatz(myNumber)
    print(myNumber)

