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

if __name__ == '__main__': 

    num_type = 3
    
    while num_type != 0:
        num_type = input("진수를 입력하세요. (bin: 1, oct: 2, dec : 3, hex: 4, 종료: 0) : " )
        num1, operator, num2 = input("연산자와 피연산자를 입력하시오. : ").split()
        if num_type == '1':
            num1_com = list(num1)
            num2_com = list(num2)
            com = num1_com + num2_com
            for b in com:
                i = 0
                while i < len(b):
                    if '0' in b[i]:
                        break
                    elif '1' in b[i]:
                        break
                    else:
                        print("잘못 입력하셨습니다.")
                        num1, operator, num2 = input("연산자와 피연산자를 입력하시오. : ").split()
                        break
                    i = i + 1
                break
            num1 = int(num1, 2)
            num2 = int(num2, 2)
            cal(num1, operator, num2)
            print(bin(num1), operator, bin(num2), '=', bin(result))
        elif num_type == '2':
            num1_com = list(num1)
            num2_com = list(num2)
            com = num1_com + num2_com
            for o in com:
                i = 0
                while i < len(o):
                    if '0' in o[i]:
                        break
                    elif '1' in o[i]:
                        break
                    elif '2' in o[i]:
                        break
                    elif '3' in o[i]:
                        break
                    elif '4' in o[i]:
                        break
                    elif '5' in o[i]:
                        break
                    elif '6' in o[i]:
                        break
                    elif '7' in o[i]:
                        break
                    else:
                        print("잘못 입력하셨습니다.")
                        num1, operator, num2 = input("연산자와 피연산자를 입력하시오. : ").split()
                        break
                    i = i + 1
                break
            num1 = int(num1, 8)
            num2 = int(num2, 8)
            cal(num1, operator, num2)
            print(oct(num1), operator, oct(num2), '=', oct(result))
        elif num_type == '3':
            num1 = int(num1)
            num2 = int(num2)
            cal(num1, operator, num2)
            print(num1, operator, num2, '=', result)
        elif num_type == '4':
            num1_com = list(num1)
            num2_com = list(num2)
            com = num1_com + num2_com
            for h in com:
                i = 0
                while i < len(h):
                    if '0' in h[i]:
                        break
                    elif '1' in h[i]:
                        break
                    elif '2' in h[i]:
                        break
                    elif '3' in h[i]:
                        break
                    elif '4' in h[i]:
                        break
                    elif '5' in h[i]:
                        break
                    elif '6' in h[i]:
                        break
                    elif '7' in h[i]:
                        break
                    elif '8' in h[i]:
                        break
                    elif '9' in h[i]:
                        break
                    elif 'a' in h[i]:
                        break
                    elif 'b' in h[i]:
                        break
                    elif 'c' in h[i]:
                        break
                    elif 'd' in h[i]:
                        break
                    elif 'e' in h[i]:
                        break
                    elif 'f' in h[i]:
                        break
                    else:
                        print("잘못 입력하셨습니다.")
                        num1, operator, num2 = input("연산자와 피연산자를 입력하시오. : ").split()
                        break
                    i = i + 1
                break
            num1 = int(num1, 16)
            num2 = int(num2, 16)
            cal(num1, operator, num2)
            print(hex(num1), operator, hex(num2), '=', hex(result))
        elif num_type == '0':
            break
