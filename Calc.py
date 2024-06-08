expression = input("Calculate: ")

x, y, z = expression.split(" ")
x = int(x)
z = float(z)

if y == "+":
    calc = x + z
elif y == "-":
    calc = x - z
elif y == "*":
    calc = x * z
elif y == "/":
    calc = x / z

print(f"{calc:.1f}")
