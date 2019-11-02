def calc(string):
    res = re.findall('([+-]?[0-9]+[.][0-9]*)(\s?[+*/÷×-]{1}\s?)([+-]?[0-9]+[.][0-9]*)',string)[0]
    num1 = float(res[0])
    num2 = float(res[2])
    oper = res[1]
    op = {'÷':num1/num2,
          '/':num1/num2,
          '+':num1+num2,
          '×':num1*num2,
          'X':num1*num2,
          'x':num1*num2,
          '*':num1*num2,
         }
    return op[oper]
print(calc('1.5+-3.0'))
print(calc('1.5*-3.0'))