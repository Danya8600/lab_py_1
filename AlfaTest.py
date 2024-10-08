from modulZ1 import fp

x = float(input('x = '))
y = float(input('y = '))
with open('ResAlfa.txt', 'a') as file:
    file.writelines(f'x = {x}, y = {y}, res = {fp(x, y)}' + '\n')
print(fp(x, y))
