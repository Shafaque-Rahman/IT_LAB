a,b=(int (x) for x in input("Enter two comma separated numbers to perform arithmetic operation").split(","))
print(f"Addition={a+b}\nSubtraction={abs(a-b)}\nMultiplication={a*b}")
print(f"Division={a/b}\nModulus={a%b}\nFloorDivision={a//b}\nExponent={a**b}")


