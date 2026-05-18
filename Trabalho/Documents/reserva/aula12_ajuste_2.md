
# Ajuste de Curvas pelo Método dos Quadrados Mínimos

# Lilian Berti

# Métodos Numéricos

# Ajuste de Curvas pelo Método dos Quadrados Mínimos

# Lilian Berti




# Caso contínuo

Aproximamos f(x) por g(x)

(f ≈ g)

em que g(x) = α1g1(x) + α2g2(x) + · · · + αmgm(x), gi(x) contínuas em [a, b].

|   |   |   |   |   |   |   |   |
| - | - | - | - | - | - | - | - |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |

Minimizamos

F(α1, α2, · · · , αm) = ∫ab [f(x) − g(x)]² dx

Lilian Berti Ajuste de Curvas pelo Método dos Quadrados Mínimos





De modo análogo ao caso discreto, caso m = 2, devemos resolver:

&#x3C; g1, g1 > α1 + &#x3C; g1, g2 > α2 = &#x3C; f, g1 >

&#x3C; g2, g1 > α1 + &#x3C; g2, g2 > α2 = &#x3C; f, g2 >,

em que




# Exemplo

Aproximar f(x) = 4x3 por uma reta no intervalo [0, 1].

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos






# Ajuste de Curvas pelo Método dos Quadrados Mínimos

f(x) ≈ g(x) = α1g1(x) + α2g2(x) em que g1(x) = 1 e g2(x) = x.

|              | 1               |   |        |
| ------------ | --------------- | - | ------ |
| < g1, g1 > = | g1(x)g1(x) dx = |   | dx = 1 |
|              | a               |   | 0      |

|              | 1                 |                        |   |
| ------------ | ----------------- | ---------------------- | - |
| < g1, g2 > = | b g1(x)g2(x) dx = | 1 xdx = 1 = < g2, g1 > |   |
|              | a                 |                        | 0 |

|              | 1                 |            |   |
| ------------ | ----------------- | ---------- | - |
| < g2, g2 > = | b g2(x)g2(x) dx = | 1 x2dx = 1 |   |
|              | a                 |            | 0 |

|             | 1              |           |   |
| ----------- | -------------- | --------- | - |
| < f, g1 > = | f(x)g1(x) dx = | 4x3dx = 1 |   |
|             | a              |           | 0 |

|             | 1                |             |   |
| ----------- | ---------------- | ----------- | - |
| < f, g2 > = | b f(x)g2(x) dx = | 1 4x4dx = 4 |   |
|             | a                |             | 0 |






Substituindo esses valores no sistema

&#x3C; g1, g1 > α1 + &#x3C; g1, g2 > α2 = &#x3C; f, g1 >

&#x3C; g2, g1 > α1 + &#x3C; g2, g2 > α2 = &#x3C; f, g2 >

Temos:

α1 + 1/2 α2 = 1

1/2 α1 + 1/3 α2 = 4/5

cuja solução é: α1 = −4/5 e α2 = 18/5.

Portanto, pelo método dos quadrados mínimos a melhor reta que se aproxima de f(x) = 4x3 no intervalo [0, 1] é:

g(x) = −4/5 + 18/5 x.

Lilian Berti Ajuste de Curvas pelo Método dos Quadrados Mínimos






# Caso não linear

Aproximamos y por uma função g sendo que g não é da forma α1g1(x) + α2g2(x) + · · · + αmgm(x).

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos





Exemplo

# Ajustar os dados por uma função da forma g(x) = aebx.

| x | 0 | 1   | 2   |
| - | - | --- | --- |
| y | 1 | 0,5 | 0,7 |

# Lilian Berti

# Ajuste de Curvas pelo Método dos Quadrados Mínimos






# Linearizando

y ≈ aebx = g(x)

ln y ≈ ln(aebx) = ln a + ln ebx = ln a + bx = G(x)

Considerando α1 = ln a e α2 = b, então:

z = ln y ≈ G(x) = α1 + α2x.

Assim, temos g1(x) = 1 e g2(x) = x. Dessa forma, queremos encontrar a melhor reta que se ajusta a z = ln y.

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos






# Resolvemos:

&#x3C; g

¯ , g

¯ > α + &#x3C; g

¯ , g

¯ > α = &#x3C; z

¯, g

1  1  1  1   2  2  ¯1 >

&#x3C; g

¯ , g

¯ > α + &#x3C; g

¯ , g

¯ > α = &#x3C; z

¯, g

2  1  1  2   2  2  ¯2 > .

em que

g  1 1 1  T

¯1 = ,

g  0 1 2  T

¯2 = e

z  ln 1 ln 0, 5 ln 0, 7  T

¯ = .

Lilian Berti  Ajuste de Curvas pelo M´etodo dos Quadrados M´ınimos





Temos:

3α1 + 3α2 = −1, 0498

3α1 + 5α2 = −1, 4065.

cuja solu¸c˜ao ´e: α1 = −0, 1715 e α2 = −0, 1784.

Como α1 = ln a, segue que, a = eα1 = e−0,1715 = 0, 8424 e α2 = b.

Portanto,

g(x) = 0, 8424e−0,1784x

Lilian Berti  Ajuste de Curvas pelo M´etodo dos Quadrados M´ınimos




Observa¸c˜ao Os parˆametros obtidos n˜ao s˜ao ´otimos dentro do crit´erio de quadrados m´ınimos, pois ajustamos o problema linearizado por quadrados m´ınimos e n˜ao o problema original.

# Lilian Berti

# Ajuste de Curvas pelo M´etodo dos Quadrados M´ınimos






# Ajuste de Curvas pelo Método dos Quadrados Mínimos

Ajustar os dados por uma função do tipo g(x) = α1 / (1 + α2x)

| x | 1   | 3   | 5   |
| - | --- | --- | --- |
| y | 2,9 | 1,2 | 0,7 |






# Linearizando

y ≈ α1 = g(x)

1 + α2x

Seja z = 1, g1(x) = 1 e g2(x) = x. Vamos determinar a melhor reta que se ajusta a z.

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos






Para determinar α1 e α2, resolvemos o sistema linear:

&#x3C; ḡ, ḡ > α + &#x3C; ḡ, ḡ > α = &#x3C; z̄, g1 >

&#x3C; ḡ, ḡ > α + &#x3C; ḡ, ḡ > α = &#x3C; z̄, g2 >.

em que

g1 = 1 1 1 T 1 3 5 T

g2 =  e

z̄ = 0, 3448 0, 883 1, 4286 T.

Lilian Berti

Ajuste de Curvas pelo Método dos Quadrados Mínimos





Temos:

| 3α1 + 9α2  | = | 2, 6067 |
| ---------- | - | ------- |
| 9α1 + 35α2 | = | 9, 9877 |

cuja solução é: α1 = 0, 0559 e α2 = 0, 271

Portanto, y ≈ g(x) = 0, 0559 + 0, 271x

Lilian Berti Ajuste de Curvas pelo Método dos Quadrados Mínimos



# Exemplo

O custo (C) na construção de um aerador em uma estação de tratamento de águas residuais depende do volume (v) do tanque:

C(v) = avb, em que a e b são parâmetros a estimar pelo método dos quadrados mínimos a partir dos dados coletados:

| v (milhares de m3) | 0,4                   | 0,6 | 1   | 1,3 |     |
| ------------------ | --------------------- | --- | --- | --- | --- |
|                    | C (milhares de reais) | 87  | 160 | 190 | 366 |

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos




# Linearizando

C(v) ≈ avb

z = ln C(v) ≈ ln(avb) = ln a + b ln v = α1 + α2 ln v

em que α1 = ln a, α2 = b, g1(v) = 1 e g2(v) = ln v.

Determinando α1 e α2, resolvendo

<ḡ, ḡ=""> α1 + <ḡ, ḡ=""> α2 = <z̄, ḡ1=""></z̄,></ḡ,></ḡ,>
<ḡ, ḡ=""> α1 + <ḡ, ḡ=""> α2 = <z̄, ḡ2="">
</z̄,></ḡ,></ḡ,>
em que

| ḡ1 = | 1        | 1        | 1      | 1       |
| ----- | -------- | -------- | ------ | ------- |
| ḡ2 = | -0, 9163 | -0, 5108 | 0      | 0, 2624 |
| z̄ =  | 4, 4659  | 5, 0752  | 5, 247 | 5, 9026 |

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos






# Temos:

−

| 4α1        | 1, 1647α2   | = | 20, 6907  |
| ---------- | ----------- | - | --------- |
| −1, 1647α1 | + 1, 1694α2 | = | −5, 1357. |

Fazendo L2 ← L2 + 0, 29L1

| 4α1 | − 1, 1647α2 | = | 20, 6907 |
| --- | ----------- | - | -------- |
|     | 0, 8302α2   | = | 0, 8894. |

cuja solu¸c˜ao ´e: α1 = 5, 4846 e α2 = 1, 0713.

Lilian Berti  Ajuste de Curvas pelo M´etodo dos Quadrados M´ınimos






Como α1 = ln a, segue que

a = eα¹ = 240, 9525 e b = α2 = 1, 0713.

Portanto,

C(v) ≈ 240, 9525v1,0713

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos





# Exemplo

Considere a tabela

| x | -8 | -6 | -4 | -2 | 0 | 2 | 4 |
| - | -- | -- | -- | -- | - | - | - |
| y | 30 | 10 | 9  | 6  | 5 | 4 | 4 |

Qual das funções h1(x) = 1 ou h2(x) = α1 + α2x ajusta melhor os dados da tabela?

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos




# Ajuste de Curvas pelo Método dos Quadrados Mínimos

Primeiramente, devemos linearizar as funções h1(x) e h2(x).

y ≈ h1(x) = α1 / (1 + α2x)

Linearizando

1 ≈ α1 + α2x

Considere z1 = 1. Assim:

z1 = 1 ≈ α1 + α2x

y





# Linearizando

y ≈ h2(x) = α1α2

ln y ≈ ln α1 + x ln α2

Considere z2 = ln y, a = ln α1 e b = ln α2. Assim:

z2 = ln y ≈ a + bx

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos




# 4

In(y)

|    | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| -- | - | - | - | - | - | - | - | - |
| -1 |   |   |   |   |   |   |   |   |
| 0  |   |   |   |   |   |   |   |   |
| 1  |   |   |   |   |   |   |   |   |
| 2  |   |   |   |   |   |   |   |   |
| 3  |   |   |   |   |   |   |   |   |

Plotamos os pontos de z1 = 1/y e z2 = ln y. Podemos verificar que os pontos de z1 estão mais alinhados, dessa forma este é uma boa escolha para o ajuste dos dados.

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos






# Exemplo

Aproximar y por uma função do tipo √a + bx.

y ≈ √a + bx

# Linearizando

z = y2 ≈ a + bx

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos







# Exemplo

Aproximar y por uma função do tipo x ln(a + bx)

y ≈ x ln(a + bx)

# Linearizando

y ≈ ln(a + bx)

x

y

z = e x ≈ a + bx

Lilian Berti  Ajuste de Curvas pelo Método dos Quadrados Mínimos

