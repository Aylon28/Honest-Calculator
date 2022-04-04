class OperationError(Exception):
    pass


def perform_operation(a, b, operation):
    if operation == '+':
        return float(a + b)
    elif operation == '-':
        return float(a - b)
    elif operation == '*':
        return float(a * b)
    elif operation == '/':
        return float(a / b)


def check(a, b, operation):
    printing = ''
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    if is_one_digit(a) and is_one_digit(b):
        printing += msg_6
    if (a == 1 or b == 1) and operation == '*':
        printing += msg_7
    if (a == 0 or b == 0) and (operation == '*' or operation == '+' or operation == '-'):
        printing += msg_8
    if printing != '':
        printing = msg_9 + printing
    print(printing)


def is_one_digit(digit):
    if -10 < digit < 10 and digit == int(digit):
        return True
    return False


def moke_the_user(digit, mem):
    if is_one_digit(digit):
        print('Are you sure? It is only one digit! (y / n)')
        svar = input()
        if svar == 'y':
            print('Don\'t be silly! It\'s just one number! Add to the memory? (y / n)')
            svar = input()
            if svar == 'y':
                print('Last chance! Do you really want to embarrass yourself? (y / n)')
                svar = input()
                if svar == 'y':
                    return digit
    else:
        return digit
    return mem


def main():
    operations = ['-', '+', '*', '/']
    mem = 0
    svar = ''
    while svar != 'n':
        while True:
            print('Enter an equation')
            inputs = input().split()
            try:
                if inputs[0] == 'M' and inputs[2] == 'M':
                    a = mem
                    b = mem
                elif inputs[0] == 'M':
                    a = mem
                    b = float(inputs[2])
                elif inputs[2] == 'M':
                    a = float(inputs[0])
                    b = mem
                else:
                    a = float(inputs[0])
                    b = float(inputs[2])
                if inputs[1] not in operations:
                    raise OperationError
                elif inputs[1] == operations[3] and b == 0:
                    check(a, b, inputs[1])
                    raise ZeroDivisionError
                break
            except OperationError:
                print('Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?')
            except ZeroDivisionError:
                print('Yeah... division by zero. Smart move...')
            except:
                print('Do you even know what numbers are? Stay focused!')
        check(a, b, inputs[1])
        rez = perform_operation(a, b, inputs[1])
        print(rez)
        print('Do you want to store the result? (y / n):')
        svar1 = input()
        if svar1 == 'y':
            mem = moke_the_user(rez, mem)
        print('Do you want to continue calculations? (y / n):')
        svar = input()


if __name__ == '__main__':
    main()
