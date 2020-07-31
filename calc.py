def cal(n1, op, n2):
    global result
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        result = n1 / n2
    return result

def binary(list1):
    bin_val = ['0', '1']
    for b in list1:
        if b in bin_val:
            pass
        elif b not in bin_val:
            print("잘못 입력하셨습니다.")
            return num_input()

def octal(list1):
    oct_val = ['0', '1', '2', '3', '4', '5', '6', '7']
    for o in list1:
        if o in oct_val:
            pass
        elif o not in oct_val:
            print("잘못 입력하셨습니다.")
            return num_input()

def hexadecimal(list1):
    hex_val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for h in list1:
        if h in hex_val:
            pass
        elif h not in hex_val:
            print("잘못 입력하셨습니다.")
            return num_input()

def num_input():
    global com, num1, operator, num2
    num1, operator, num2 = input("연산자와 피연산자를 입력하시오. : ").split()
    num1_com = list(num1)
    num2_com = list(num2)
    com = num1_com + num2_com
    return com

if __name__ == '__main__': 

    num_type = 3
    
    while num_type != 0:
        num_type = input("진수를 입력하세요. (bin: 1, oct: 2, dec : 3, hex: 4, 종료: 0) : " )
        if num_type == '1':
            num_input()
            binary(com)
            num1 = int(num1, 2)
            num2 = int(num2, 2)
            cal(num1, operator, num2)
            print(bin(num1), operator, bin(num2), '=', bin(result))
        elif num_type == '2':
            num_input()
            octal(com)
            num1 = int(num1, 8)
            num2 = int(num2, 8)
            cal(num1, operator, num2)
            print(oct(num1), operator, oct(num2), '=', oct(result))
        elif num_type == '3':
            num_input()
            num1 = int(num1)
            num2 = int(num2)
            cal(num1, operator, num2)
            print(num1, operator, num2, '=', result)
        elif num_type == '4':
            num_input()
            hexadecimal(com)
            num1 = int(num1, 16)
            num2 = int(num2, 16)
            cal(num1, operator, num2)
            print(hex(num1), operator, hex(num2), '=', hex(result))
        elif num_type == '0':
            break
