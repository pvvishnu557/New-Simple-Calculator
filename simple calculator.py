def print_menu():
    print("1.addition")
    print("2.subtration")
    print("3.multiplication")
    print("4.divition")

choice=True
while(choice):
    num=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    print_menu()
    z=int(input("enter your choice:"))
    if z==1:
        print("the answer is",num+num2)
    elif z==2:
        print("the answer is",num-num2)
    elif z==3:
        print("the answer is",num*num2)
    elif z==4:
        try:
            print("the answer is",num/num2)
        except:
            print("not divisible by zero")
    else:
        print("enter a valid input")
        continue
    again=input("want to do again:\n"
            +"yes or no:")
    if again=="n":
        choice=False
