expression = input("Expression: ").strip()
x_str, y, z_str = expression.split(" ")

x = int(x_str)
z = int(z_str)

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z
else:
    print("invalid")

print(f"{answer:.1f}")
