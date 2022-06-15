
def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mul(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    num1=float(input("first num?"))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operation_symbol=input("pick an operation:")
        num2=float(input("num two?"))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1, num2)

        print(f"{num1} {operation_symbol}{num2}={answer}")
        decide= input("make a choice\n1. more calculate\n2. new calculate\n3.stop calculate\n answer:")
        if decide=="1":
            num1=answer
        elif decide=="2":
            should_continue=False
            calculator()
        else:
            should_continue=False
calculator()





