# Problema de Valor de Contorno

# Lilian Berti

# Métodos Numéricos

# Lilian Berti

# Problema de Valor de Contorno

# Problema de Valor de Contorno (PVC)

y'' = f(x, y(x), y'(x)) a ≤ x ≤ b

y(a) = α

y(b) = β

# Lilian Berti

# Problema de Valor de Contorno

# Resolvendo o PVC por Diferenças finitas

# Discretização

a = x0 < x1 < x2 < · · · < xn = b

h = xi − xi−1 = (b−a) / n

Queremos encontrar yi ≈ y(xi).

Vamos aproximar y(xi) e y'(xi) por diferenças finitas usando apenas o valor da função.

Lilian Berti Problema de Valor de Contorno

# Expansão de Taylor

Se y tem (n + 1) derivadas

y(x+h) = y(x)+hy'(x)+h²y''(x)+· · ·+ hⁿyⁿ(x)+(hⁿ⁺¹yⁿ⁺¹(γ))

em que γ ∈ (x, x + h).

Lilian Berti

# Problema de Valor de Contorno

# Temos:

y(xi+1) = y(xi) + hy (xi) + h2 y (xi) + h3 y (γ)

y(xi−1) = y(xi) − hy (xi) + h2 y (xi) − h3 y (γ)

Subtraindo as duas equações acima, obtemos:

y(xi+1) − y(xi−1) = 2hy (xi) + 2 h3 y (γ)

y(xi+1) − y(xi−1) − 2 h3 y (γ) = 2hy (xi)

y(xi+1) − y(xi−1) − h2 y (γ) =   y (xi)

2h             3!

Lilian Berti Problema de Valor de Contorno

Então, a Diferença centrada é dada por:

y (xi) ≈ yi+1 − yi−1

2h

Outras formas:

Diferença atrasada

y (xi) ≈ yi − yi−1

h

Diferença avançada

y (xi) ≈ yi+1 − yi

h

Lilian Berti Problema de Valor de Contorno

Obtendo y, temos:

y(xi+1) = y(xi) + h y (xi) + h2 y (xi) + h3 y (x) + h4 y (γ)

# Exemplo:

y + 2y + y = x

y(0) = 2

y(1) = 0

Resolva pelo método das diferenças finitas usando h = 0, 25.

# Pontos da malha:

| x0 = 0 | x1 = 0, 25 | x2 = 0, 5 | x3 = 0, 75 | x4 = 1 |
| ------ | ---------- | --------- | ---------- | ------ |
| y0 = 2 | | | | y4 = 0 |

# Lilian Berti

Problema de Valor de Contorno

# Temos:

yi+1 − 2yi + yi−1 + 2 yi+1 − yi−1 + yi = xi

h2 2h

yi+1 − 2yi + yi−1 + 2 yi+1 − yi−1 + yi = xi (×(0, 25)2)

(0, 25)2 2.(0, 25)

yi+1 − 2yi + yi−1 + 0, 25yi+1 − 0, 25yi−1 + 0, 0625yi = 0, 0625xi

0, 75yi−1 − 1, 9375yi + 1, 25yi+1 = 0, 0625xi

i = 1

0, 75y0 − 1, 9375y1 + 1, 25y2 = 0, 0625x1

1, 5 − 1, 9375y1 + 1, 25y2 = 0, 0156

−1, 9375y1 + 1, 25y2 = −1, 4844

i = 2

0, 75y1 − 1, 9375y2 + 1, 25y3 = 0, 0625x2

0, 75y1 − 1, 9375y2 + 1, 25y3 = 0, 0313

Lilian Berti Problema de Valor de Contorno

# Lilian Berti

# Problema de Valor de Contorno

i = 3

0, 75y2 − 1, 9375y3 + 1, 25y4 = 0, 0625x3

0, 75y2 − 1, 9375y3 = 0, 0469

# Problema de Valor de Contorno

Temos:

| −1, 9375 | 1, 25 | 0 | y1 | −1, 4844 | |
| -------- | -------- | -------- | -- | -------- | ------- |
| 0, 75 | −1, 9375 | 1, 25 | y2 | = | 0, 0313 |
| 0 | 0, 75 | −1, 9375 | y3 | 0, 0469 | |

cuja solução é: y1 = 1, 1075, y2 = 0, 5291, y3 = 0, 1806

Portanto,

y(0, 25) ≈ 1, 1075

y(0, 5) ≈ 0, 5291

y(0, 75) ≈ 0, 1806

Lilian Berti

Exemplo:

y = 0, 01(y − 20)

y(0) = 40

y(10) = 200

Resolva na malha [0, 10] com h = 2.

Pontos da malha: x0 = 0, x1 = 2, x2 = 4, x3 = 6, x4 = 8, x5 = 10

y0 = 40 y5 = 200

Lilian Berti Problema de Valor de Contorno

# Temos:

yi+1 − 2yi + yi−1 = 0, 01(yi − 20)

h2

yi+1 − 2yi + yi−1 = 0, 01yi − 0, 2 (×4)

4

yi+1 − 2yi + yi−1 = 0, 04yi − 0, 8

yi−1 − 2, 04yi + yi+1 = −0, 8

# Lilian Berti

# Problema de Valor de Contorno

# Problema de Valor de Contorno

| i | y0 | y1 | y2 | y3 | y4 | y5 |
| - | ----------------- | ------- | ------------------ | ------- | ------------- | --------- |
| 1 | -2, 04y1 + y2 | = -0, 8 | 40 - 2, 04y1 + y2 | = -0, 8 | -2, 04y1 + y2 | = -40, 8 |
| 2 | y1 - 2, 04y2 + y3 | = -0, 8 | | | | |
| 3 | y2 - 2, 04y3 + y4 | = -0, 8 | | | | |
| 4 | y3 - 2, 04y4 + y5 | = -0, 8 | y3 - 2, 04y4 + 200 | = -0, 8 | y3 - 2, 04y4 | = -200, 8 |

# Obtemos um sistema linear:

−2,04y1 + y2 = −40,8
y1 − 2,04y2 + y3 = −0,8
y2 − 2,04y3 + y4 = −0,8
y3 − 2,04y4 = −200,8

# cuja solução é:

y1 = 65,9698, y2 = 93,7785, y3 = 124,5382, y4 = 159,4795

# Comparando com a solução exata

| x | exata | Dif. Finita |
| -- | -------- | ----------- |
| 0 | 40 | 40 |
| 2 | 65,9518 | 65,9698 |
| 4 | 93,7478 | 93,7785 |
| 6 | 124,5036 | 124,5382 |
| 8 | 159,4534 | 159,4795 |
| 10 | 200 | 200 |

Lilian Berti Problema de Valor de Contorno