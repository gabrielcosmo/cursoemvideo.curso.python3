# Sequencia de Fibonacci
print('='*10,'Sequnecia de Fibonacci','='*10)

p_num = 0
s_num = 1
t_num = 0

n = int(input('\nDigite um número: '))
x = 0

print(f'\nOs {n} primeiros números dessa sequencia são: 0 1 ', end='')
while x < n-2:
    t_num = p_num + s_num
    p_num = s_num
    s_num = t_num
    x += 1
    print(t_num, end=' ')
