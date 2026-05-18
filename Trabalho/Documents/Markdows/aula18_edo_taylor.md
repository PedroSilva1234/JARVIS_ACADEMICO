# Solução Numérica de equações diferenciais ordinárias

# Lilian Berti

# Métodos Numéricos

# Solução Numérica de equações diferenciais ordinárias

# Lilian Berti

# Equação diferencial

Equação envolvendo derivadas de uma função incógnita.

# Exemplos:

- u = u u(t) = cet
- v" + v = 0 v(t) = α cos t + βsen t
- ∂2u + ∂2u = 0 u = u(x, y)
- ∂x2 ∂y2

# Aplicações:

estudo das redes elétricas, curvatura de vigas, estabilidade de aviões e etc.

# Lilian Berti

# Solução Numérica de equações diferenciais ordinárias

# Equação diferencial ordinária (EDO)

a equação diferencial que tem apenas uma variável independente.

# Exemplo:

y (x) = −xy(x)

Temos:

dy = −xy
dx

1 dy = −x dx
y

1 dy = − x dx
y

ln |y| = − x² + c

|y| = e−ˣ₂² +c = ece−ˣ₂²

y = k e−ˣ₂² para k ∈ R

Considerando a condição inicial y(0) = 1, então: 1 = ke0 = k.

Dessa forma, a solução é dada por y = e−ˣ₂².

Lilian Berti Solução Numérica de equações diferenciais ordinárias

# Solução Numérica de Equações Diferenciais Ordinárias

Estudaremos métodos numéricos para resolver o problema de valor inicial (PVI)

y (x) = f(x, y(x)), x > x0

y(x0) = y0

Lilian Berti

# Resolver numericamente um PVI

Resolver numericamente um PVI consiste em calcular aproximações para y = y(x) em pontos discretos x0, x1, · · ·, xN em um intervalo [a,b].

Discretizamos o intervalo [a,b] tomando N subintervalos (N ≥ 1) e fazemos

xi = x0 + ih, i = 0, 1, · · · N,

x0 = a, xN = b e h = (b − a) / N,

sendo

- h = tamanho do passo,
- xi = pontos da malha e
- N = número de passos.

Lilian Berti

Solução Numérica de equações diferenciais ordinárias

# Método de Taylor de ordem q

Considere o PVI, f sendo contínua suficientemente derivável até a ordem (q + 1) em relação a x e y. Seja y(x) a solução exata do PVI. A expansão em série de Taylor, para y(xi+1) em torno do ponto xi é dado por:

y(xi+1) = y(xi) + hy'(xi) + h² y''(xi) + · · · + hq y(q)(xi) + (hq+1 y(q+1)(ξx))/(q + 1)!

em que ξx está entre xi e xi+1 e além disso,

ei = (hq+1 y(q+1)(ξx))/(q + 1)! é o erro de truncamento local.

Lilian Berti Solução Numérica de equações diferenciais ordinárias

# Temos:

y = f(x, y)

y = f = ∂f dx + ∂f dy = f + f f

∂x dx ∂y dx x y

y = f = ∂fx + ∂fx dy + ∂fy + ∂fy dy f + fy ∂f + ∂f dy

∂x ∂y dx ∂x ∂y dx ∂x ∂y dx

= fxx + fxy f + fyxf + fyy f2 + fy fx + fy2f

Continuando, podemos expressar qualquer derivada de y em torno de f(x, y) e de suas derivadas parciais.

Lilian Berti Solução Numérica de equações diferenciais ordinárias

Limitando (1) após (q + 1) termos, obtemos:

y(xi+1) = y(xi) + hf (xi, y(xi)) + h2 f (xi, y(xi)) + · · · + hq f(q−1)(xi, y(xi))

2! q!

Substituindo y(xi) por yi, temos:

yi+1 = yi + hf(xi, yi) + h2 f (xi, yi) + · · · + hq f(q−1)(xi, yi)

2! q!

em que i = 0, 1, · · · , N − 1, é denominado de método de Taylor de ordem q.

Quando q = 1:

yi+1 = yi + hf(xi, yi)

para i = 0, 1, · · · , N − 1. Este método é conhecido como método de Euler.

Lilian Berti Solução Numérica de equações diferenciais ordinárias

# Exemplo: Determine aproximações para a solução do PVI

y = x − y + 2

y(0) = 2

na malha [0; 0, 2] com h = 0, 1.

Lilian Berti

# Solução Numérica de equações diferenciais ordinárias

# Método de Euler

Temos:

x0 = 0, x1 = 0,1, x2 = 0,2 y0 = 2, f(x, y) = x − y + 2

# Método de Euler

yi+1 = yi + hf(xi, yi) para i = 0, 1

# i = 0

y1 = y0 + hf(x0, y0) = 2 + 0,1 · 0 = 2 ⇒ y(0, 1) ≈ 2

# i = 1

y2 = y1 + hf(x1, y1) = 2 + 0,1 · 0,1 = 2,01 ⇒ y(0, 2) ≈ 2,01

Lilian Berti Solução Numérica de equações diferenciais ordinárias

# b) utilizando o método de Taylor de ordem 2.

Pontos da malha:

- x0 = 0
- x1 = 0,1
- x2 = 0,2
- y0 = 2

f(x, y) = x − y + 2

# Método de Taylor de ordem 2

yi+1 = yi + hf(xi, yi) + h2 f(2)(xi, yi) para i = 0, 1

i = 0

y1 = y0 + hf(x0, y0) + h2 f(2)(x0, y0)

= 2 + 0,1 · 0 + (0,1)2 · 1 = 2,005 ⇒ y(0, 1) ≈ 2,005

i = 1

y2 = y1 + hf(x1, y1) + h2 f(2)(x1, y1)

= 2 + 0,1 · 0,095 + (0,1)2 · 0,905 = 2,019 ⇒ y(0, 2) ≈ 2,019

Lilian Berti

Solução Numérica de equações diferenciais ordinárias

# Método de Euler

# Método de Taylor

# Solução exata de ordem 2

y = e−x + x + 1

| xi | yi |
| --- | ---- |
| 0 | 2 |
| 0,1 | 2 |
| 0,2 | 2,01 |

| yi | y(xi) |
| ----- | ------ |
| 2 | 2 |
| 2,005 | 2,0048 |
| 2,019 | 2,0187 |

# Lilian Berti

# Solução Numérica de equações diferenciais ordinárias

# Exemplo:

Encontre uma aproximação para y(1) pelo método de Euler utilizando passo h = 0,5 sendo

y = −xy

y(0) = 1

Temos:

x0 = 0, x1 = 0,5, x2 = 1 e y0 = 1

f(x, y) = −xy

# Método de Euler

yi+1 = yi + hf(xi, yi) para i = 0, 1

i = 0

y1 = y0 + hf(x0, y0) = 1 + 0,5 · 0 = 1

i = 1

y2 = y1 + hf(x1, y1) = 1 + 0,5 · (−0,5) = 0,75

Portanto, y(1) ≈ 0,75

Lilian Berti

Solução Numérica de equações diferenciais ordinárias