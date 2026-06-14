
Zeros reais de Funções reais - Método da Secante

# Métodos Numéricos

# Lilian Berti

# Zeros reais de Funções reais - Método da Secante




# Zeros reais de Funções reais - Método da Secante

Uma grande desvantagem do método de Newton é o cálculo f (xk), que para algumas funções pode ser extremamente difícil. Dessa forma, veremos o Método da secante, que utiliza uma aproximação para f (xk).

Lilian Berti





# Método da Secante

f(x)

| x3 | x2 | x1 | x0 |
| -- | -- | -- | -- |

Dada duas aproximações iniciais x0 e x1, a derivada pode ser aproximada por:

f (x1) ≈ f(x¹)−f(x⁰)

x1−x0

f (xk) ≈ f(xᵏ )−f(xᵏ−¹) para k = 1, 2, . . . .

xk −xk−1

Lilian Berti  Zeros reais de Funções reais - Método da Secante




# Zeros reais de Funções reais - Método da Secante

Substituindo a aproximação de f (xk) na fórmula de Newton, temos:

xk+1 = xk -
<frac>- f(xk)</frac>
{f(xk)}

xk+1 = xk -
<frac>- f(xk)(xk - xk-1)</frac>
{f(xk) - f(xk-1)}

xk+1 =
<frac>xkf(xk) - xkf(xk-1) - xkf(xk) + xk-1f(xk)</frac>
{f(xk) - f(xk-1)}

xk+1 =
<frac>xk-1f(xk) - xkf(xk-1)</frac>
{f(xk) - f(xk-1)}

Esta é a fórmula do método da secante, a partir de duas aproximações xk-1 e xk obtemos a aproximação xk+1.





# Exemplo

Determine um zero de f(x) = x3 − 9x + 3 utilizando o método da secante com aproximações iniciais x0 = 0 e x1 = 1 e critério da parada  |xk+1 − xk| ≤ 0, 09.

A fórmula da secante é:

xk+1 = xk − 1 * f(xk) − xk * f(xk−1)

f(xk) − f(xk−1)

Para k = 1

x2 = x0 * f(x1) − x1 * f(x0) = 0 * (−5) − 1 * 3 = 0, 375




Para k = 2

x3 = x1f(x2)−x2f(x1) = 1.(−0,3223)−0,375.(−5) = 0, 3319

f(x2)−f(x1) = −0,3223−(−5)

ER = x3−x2 = 0,3319−0,375 = 0, 1299 > x3 0,3319

Para k = 3

x4 = x2f(x3)−x3f(x2) = 0,375(0,0495)−0,3319.(−0,3223) = 0, 3376

f(x3)−f(x2) = 0,0495−(−0,3223)

ER = x4−x3 = 0,3376−0,3319 = 0, 0169 &#x3C; x4 0,3376

Portanto, x̄ = 0, 3376.

Lilian Berti  Zeros reais de Funções reais - Método da Secante





Ordem de convergência

As condi¸c˜oes de convergência sçao as mesmas do método de Newton, mas a ordem de convergência é superlinear.

(p = 1+√⁵ ≈ 1, 618)

# Lilian Berti

Zeros reais de Funções reais - Método da Secante





# Método da Falsa Posição

Este método pode ser interpretado como uma combinação do método da secante e o método da bissecção.

No método da bissecção alteramos o cálculo de *xk = (a + b) / 2* por:

*xk = (a * f(b) - b * f(a)) / (f(b) - f(a))*

Lilian Berti

Zeros reais de Funções reais - Método da Secante




Encontre um zero de f(x) = x3 − 9x + 3, pelo método da falsa posição utilizando I = (0, 1) e com critério de parada |b − a| &#x3C; ε = 0, 09

# 1ª iteração:

I = (0, 1)

x1 = af(b)−bf(a) = 0(−5)−1.3 = 0, 375

f(b)−f(a) = −5−3

f(0) = 3

f(0, 375) = −0, 3223

f(1) = −5

Novo intervalo I = (0; 0, 375) |b − a| = 0, 375 >

Lilian Berti

Zeros reais de Funções reais - Método da Secante





# 2a iteração: I = (0; 0, 375)

x2 = af(b)−bf(a) = 0(−0,3223)−0,375.3 = 0, 3386

f(b)−f(a) = −0,3223−3

f(0) > 0

f(0, 3386) = −0, 0086

f(0, 375) &#x3C; 0

Novo intervalo I = (0; 0, 3386)     |b − a| = 0, 3386 >

# 3a iteração: I = (0; 0, 3386)

x3 = af(b)−bf(a) = 0(−0,0086)−0,3386.3 = 0, 3376

f(b)−f(a) = −0,0086−3

f(0) > 0

f(0, 3376) = 7, 8.10−5

f(0, 3386) &#x3C; 0

Novo intervalo I = (0, 3376; 0, 3386)

|b − a| = 0, 001 &#x3C;

Portanto, x̄ = x3 = 0, 3376.

Lilian Berti     Zeros reais de Funções reais - Método da Secante



# Comparação entre os métodos

# Garantia de convergência

Método da Bissecção e Falsa Posição convergentes desde que f é contínua em [a, b] e f(a)f(b) &#x3C; 0.

Método de Newton e Secante convergentes se as aproximações iniciais estão “suficientemente” próximas da raiz.

# Rapidez

Garantindo a convergência: 1º Método de Newton, 2º Método da Secante, 3º Método da Falsa Posição e 4º Método da Bissecção.

Lilian Berti  Zeros reais de Funções reais - Método da Secante



# Esforço computacional

# Método da Bissecção e Falsa posição

cálculos mais simples, mas requer um número maior de iterações.

# Método de Newton

requer mais cálculos

# Lilian Berti

# Zeros reais de Funções reais - Método da Secante



Portanto, a escolha do método a ser usado depende da função a ser resolvida, do seu comportamento na vizinhança da raiz, as dificuldades no cálculo de f e o critério de parada.

# Lilian Berti

# Zeros reais de Funções reais - Método da Secante