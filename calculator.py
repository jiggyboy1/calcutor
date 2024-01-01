class Calculator():
    def __init__(self,number1,number2) -> None:
        self.number1 = number1
        self.number2 = number2
        
    def add(self):
        return self.number1 + self.number2
    
    def sub(self):
        return self.number1 - self.number2
    
    def multiplication(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1  / self.number2
    


print("________________________")
print(" Enter which operation ")
print(" 1.Add")
print(" 2.Subtraction")
print(" 3.multiplication")
print(" 4.division")


while True:
    try:
        choice = int(input("Enter Which You Want Perform: "))

        number1 = int(input("Enter a number: "))
        number2 = int(input("Enter another number: "))
        calculator = Calculator(number1,number2)

        if choice == 1:
            print(f" {number1} + {number2} = {calculator.add()}")

        elif choice == 2 :
            print(f" {number1} - {number2} = {calculator.sub()}")

        elif choice == 3 :
            print(f" {number1} x {number2} = {calculator.multiplication()}")

        elif choice == 4:
            print(f" {number1} / {number2} = {calculator.division()}")

        else:
            print(" Invalid Request")
            
        again = input('Do You Wish Perform Another: ')
        if again == "no":
            break
    except Exception as e:
        print(e)






