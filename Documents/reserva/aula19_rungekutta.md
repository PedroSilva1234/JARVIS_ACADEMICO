
Solu¸c˜ao Num´erica de Equa¸c˜oes Diferenciais Ordin´arias - M´etodo de Runge Kutta

# Métodos Numéricos

# Lilian Berti

# Solu¸c˜ao Num´erica de Equa¸c˜oes Diferenciais Ordin´arias - M´etodo de Runge Kutta



# Método de Runge Kutta

não é necessário o cálculo de derivadas múltiplas avaliações de f

# Forma geral dos métodos de Runge Kutta

yi+1 = yi + hφ

O que muda de um método para outro é a inclinação φ.

Lilian Berti  Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta



# Runge Kutta de 1a ordem

# Método de Euler

yi+1 = yi + hf(xi, yi)

para i = 0, 1, · · · , N − 1.

Lilian Berti Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta



# Runge Kutta de 2a ordem

# Método de Euler Modificado (Método do ponto médio)

| y    | h | f( )                     |
| ---- | - | ------------------------ |
| ŷi+1 | = | yi + 2 h f(xi, yi)       |
| yi+1 | = | yi + h f(xi + h/2, ŷi+1) |

Lilian Berti

Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta



# Exemplo

y = 1 + y

x

y(1) = 2

# Encontre uma aproximação para y(1, 5) com h = 0, 25

Lilian Berti

Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta




# Método de Euler Modificado

Temos:

- x0 = 1, x1 = 1, 25, e x2 = 1, 5;
- f(x, y) = 1 + y e y(x0) = 2 = y0

yˆi+1 = yi + h f( xi, yi) para i = 0, 1

yˆi+1 = yi + hf(x + h, yi) para i = 0

yˆ1 = y0 + h f( x0, y0) = 2 + h f(1, 2)

= 2 + 0, 25 * 3 = 2, 375

y1 = y0 + hf(x + h, y0) = 2 + 0, 25 * f(1, 375)

= 2 + 0, 25 * 3, 1111 = 2, 7778

Lilian Berti

Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta






para i = 1

y      h f(  )      0, 25 f(1




Método de Euler Aperfeiçoado

# Método de Euler Aperfeiçoado

yi+1 = yi + h f( xi, yi )

yi+1 = yi + h [f(xi, yi) + f(xi+1, yi+1)]

Lilian Berti

Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta





# Exemplo

y = 1 + y

x

y(1) = 2

# Encontre uma aproximação para y(1, 5) com h = 0, 25

Lilian Berti

Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta





# Método de Euler Aperfeiçoado

Temos:

- x0 = 1
- x1 = 1, 25
- x2 = 1, 5

f(x, y) = 1 + y e y(x0) = 2 = y0

yi+1 = yi + h f( xi, yi )

yi+1 = yi + h [f(xi, yi) + f(xi+1, yi+1)]

Lilian Berti

Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta






# Solu¸c˜ao Num´erica de Equa¸c˜oes Diferenciais Ordin´arias - M´etodo de Runge Kutta

para i = 0

y          hf(  )

ˆ1 = y0 +       x0, y0

= 2 + 0, 25 f(1, 2)

2

= 2 + 0, 25 · 3 = 2, 75

y  = y + h [f(x , y ) + f(x , y )]

1  0       2    0     0    1 ˆ1

= 2 + 0, 25 [f(1, 2) + f(1, 25; 2, 75)]

2

= 2 + 0, 25 [3 + 3, 2] = 2, 775

2






para i = 1

y                hf(  )

ˆ2 = y1 +             x1, y1

= 2, 775 + 0, 25f(1, 25; 2, 775)

= 2 + 0, 25 · 3, 22 = 3, 58

y         = y + h [f(x , y ) + f(x , y )]

2         1      2    1     1    2   ˆ2

= 2, 775 + 0, 25 [f(1, 25; 2, 775) + f(1, 5; 3, 58)]

2

= 2, 775 + 0, 25 [3, 22 + 3, 3867] = 3, 6008

2

y(1, 5) ≈ 3, 6008

Lilian Berti  Solu¸c˜ao Num´erica de Equa¸c˜oes Diferenciais Ordin´arias - M´etodo de Runge Kutta






# Exemplo

y = 1 + y

x

y(1) = 2

Encontre uma aproximação para y(1, 5) com h = 0, 25 usando o método de Euler.

x0 = 1, x1 = 1, 25, e x2 = 1, 5 ; f(x, y) = 1 + y e y(x0) = 2 = y0

y1 = y0 + hf(x0, y0) = 2 + 0, 25f(1, 2) = 2 + 0, 25 · 3 = 2, 75

y2 = y1 + hf(x1, y1) = 2, 75 + 0, 25f(1, 25; 2, 75) = 2, 75 + 0, 25 · 3, 2 = 3, 55

Lilian Berti Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta





# Comparando os resultados, sabendo que a solução exata é

# y = 2x + xln x

| x    | Euler | Euler Modificado | Euler Aperfeiçoado | Exata  |
| ---- | ----- | ---------------- | ------------------ | ------ |
| 1,25 | 2,75  | 2,7778           | 2,775              | 2,7789 |
| 1,5  | 3,55  | 2,6061           | 3,6008             | 2,6082 |

Lilian Berti  Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta



# Runge Kutta de 4aordem (clássico)

yi+1 = yi + h (K1 + 2k2 + 2k3 + k4)

6

em que

k1 = f(xi, yi)

k2 = f(xi + h , yi + h k1)

2

k3 = f(xi + h , yi + h k2)

2

k4 = f(xi + h, yi + hk3)

Lilian Berti Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta



# Exemplo

Suponha que a densidade populacional p de lagartas seja descrita pelo PVI

dp = 3p(1 − p) −  p2 2

dt                   1 + p

p(0) = 0.1

Utilizar um método numérico para estimar p para 0 ≤ t ≤ 10.

Lilian Berti  Solução Numérica de Equações Diferenciais Ordinárias - Método de Runge Kutta