# Resolução de sistemas não lineares - Método de Newton

# Lilian Berti

# Métodos Numéricos

Lilian Berti Resolução de sistemas não lineares - Método de Newton

# Resolução de sistemas não lineares

# Exemplos

# a)

x2 - y = 1
2 cos x - y = 0
x2 + x2 = 2

# b)

| x2 - x2 = 1 | | |
| ----------- | - | - |
| 1 | 4 | |

# c)

ln(x2 + x2) - sen(x1x2) = ln 2 + ln π
1 - 2
ex1 x2 + cos(x1x2) = 0

Lilian Berti Resolução de sistemas não lineares - Método de Newton

# Um sistema não linear de n equações e n incógnitas pode ser representado na forma:

f (x1, x2, . . . , xn) = 0

f (x1, x2, . . . , xn) = 0

.

.

.

f (x1, x2, . . . , xn) = 0

em que cada função f : Rn −→ R, i = 1, 2, . . . , n.

# O exemplo item (b), procuramos por x1 e x2 tais que:

f (x1, x2) = x12 + x22 − 2 = 0

f (x1, x2) = x12 − x22 − 1 = 0

4

Lilian Berti Resolução de sistemas não lineares - Método de Newton

Notação: Usaremos a notação vetorial

| x1 | f (x) |
| --- | -------- |
| x2 | f (x) |
| x = | F(x) = 2 |
| . | . |
| . | . |
| xn | f (x) |

Assim, o sistema não linear pode ser representado na forma F(x) = 0. Dessa forma, queremos encontrar x* ∈ R tal que F(x*) = 0.

Lilian Berti

Resolução de sistemas não lineares - Método de Newton

...
1

∇f (x)ᵀ
∂f (x)
∂f (x)
∂f (x)

2
2
2
...
2

J(x) =
.
.
.
.

.
.
.
.
.

.
.
.
.
.

∇f (x)ᵀ
∂f (x)
∂f (x)
∂f (x)

n
n
n
...
n

Lilian Berti Resolução de sistemas não lineares - Método de Newton

# Exemplo:

2x3 − x2 = 1

x1 3 − 2

1x2 x2 = 4

Temos:

f (x1, x2) = 2x3 − x2 − 1

f (x2, x1) = x2x3 − x1 − 4

J(x) =

| 6x1 | −2x2 |
| --- | --------- |
| x3 | 3x1x2 − 1 |
| 2 | |

# Lilian Berti

# Resolução de sistemas não lineares - Método de Newton

# Método de Newton para sistemas não lineares

No caso f(x) = 0 em que f(x) e x são números reais, expandimos f(x) em torno de xk, obtemos:

f(x) ≈ f(xk) + f'(xk)(x − xk).

Então, f(xk+1) = 0, se

f(xk) + f'(xk)(xk+1 − xk) = 0 ou seja,

xk+1 = xk − f(xk)

# Resolução de sistemas não lineares - Método de Newton

De modo similar resolvemos F(x) = 0, utilizando a série de Taylor, expandimos F(x) em torno de x(k):

F(x) ≈ F(x(k)) + F'(x(k))(x − x(k)).

J(x(k))

Então, F(x(k+1)) = 0, se

F(x(k)) + J(x(k))(x(k+1) − x(k)) = 0, ou seja,

J(x(k))(x(k+1) − x(k)) = −F(x(k))

Evitando o cálculo da inversa. Resolvemos:

J(x(k))d = −F(x(k))

em que d = x(k+1) − x(k). Dessa forma, a nova aproximação é dada por:

x(k+1) = x(k) + d

# Critério de parada

F(x(k+1)) ∞ <

ou

x(k+1) − x(k) ∞ <

ou

x(k+1)−x(k) ∞ <

x(k+1) ∞

Lilian Berti Resolução de sistemas não lineares - Método de Newton

# Resolução de sistemas não lineares - Método de Newton

Exemplo: Utilize o método de Newton para resolver o sistema:

2x3 - x2 = 1
x1 - 2
1x2 x2 = 4

com aproximação inicial x(0) = [1, 2; 1, 7]T e erro relativo inferior a = 0, 05.

Lilian Berti

# Resolução de sistemas não lineares - Método de Newton

Temos

F(x) = f(x1, x2) = 2x3 − x2 − 1

J(x) = 6x1 − 2x2

x3 = 3x1x2 − 1

Lilian Berti

# Para k = 0

J(x(0))d = −F(x(0))

| 8, 64 | −3, 4 | d1 | = | − | −0, 434 | = | −0, 434 |
| ------ | ------ | -- | - | ------- | ------- | ------- | ------- |
| 4, 913 | 9, 404 | d2 | | 0, 1956 | | 0, 1956 | |

L2 ← L2 − 0, 5686L1

| 8, 64 | −3, 4 | d1 | = | −0, 434 | | d = 0, 0349 |
| ----- | -------- | -- | - | ------- | - | ----------- |
| 0 | 11, 3372 | d2 | | 0, 4424 | | −0, 039 |

x(1) = x(0) + d = 1, 2 + 0, 0349 = 1, 2349

1, 7 − 0, 039 = 1, 661

ER = x(1)−x(0) ∞ = d ∞ = 0,039 = 0, 0235 >

x(1) ∞ x(1) 1,661

Lilian Berti Resolução de sistemas não lineares - Método de Newton

Para k = 1

| J(x(1))d | = | −F(x(1)) | | | | |
| -------- | ------- | -------- | ------- | -------- | - | -------- |
| 9, 1499 | −3, 322 | d1 | = | −0, 0075 | = | −0, 0075 |
| 4, 5826 | 9, 221 | d2 | −0, 002 | 0, 002 | | |

L2 ← L2 − 0, 5008L1

| 9, 1499 | −3, 322 | d1 | −0, 0075 | d | = | −0, 0006 |
| ------- | -------- | -- | -------- | - | ------- | -------- |
| 0 | 10, 8847 | d2 | 0, 0058 | | 0, 0005 | |

x(2) = x(1) + d = 1, 2349 + (−0, 0006) = 1, 2343

1, 661 + 0, 0005 = 1, 6615

ER = x(2)−x(1) ∞ = d ∞ = 0,0006 = 0, 0003 < x(2) ∞

x(2) = 1,6615

x(2) = 1, 2343

¯x = x = 1, 6615

Lilian Berti Resolução de sistemas não lineares - Método de Newton

# Exemplo:

Duas estações elétricas vão fornecer energia a uma certa região da forma mais economômica poss´ıvel. O custo total das duas estações é dado por:

f(x1, x2) = 0, 1 + 0, 01x1x2 + 0, 15x4 + 0, 01x4 − 0, 25(x1 + x2 − 100)1

em que x1 é a energia fornecida pela primeira estação e x2 é a energia fornecida pela segunda estação.

Determine os valores de x1 e x2 de forma a minimizar o custo total de operações das duas estações. Utilize como aproximação inicial o ponto [2 ; 0, 5]T e critério de parada erro relativo inferior a = 0, 2.

Lilian Berti

# Resolução de sistemas não lineares - Método de Newton