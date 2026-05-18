Exemplo

Exemplo




# Exemplo:

Uma gamela de comprimento L tem se¸c˜ao transversal semicircular com raio r. Quando a gamela est´a cheia com ´agua at´e uma distancia h do topo, o volume V de ´agua ´e

V = L   0, 5πr2 − r2arcsen  h − h(r2 − h2) 1 .

2

r

Suponha que L = 10, r = 1 p´e e V = 12, 4 p´es3. Determine da profundidade da ´agua na gamela com precis˜ao de 0, 01 p´e.

# Exemplo



Substituindo os dados temos:

12, 4 = 10 0, 5π − arcsen (h) − h(1 − h2)1

10 0, 5π − arcsen (h) − h(1 − h2)1 − 12, 4 = 0

0, 5π − arcsen (h) − h(1 − h2)1 − 1, 24 = 0

Seja f(h) = 0, 5π − arcsen (h) − h(1 − h2)1 − 1, 24.

Localizando o zero de f.

O domínio de f é Df = [−1, 1]. No entanto pelo problema notamos que h ≥ 0 e no máximo o valor do raio (r = 1). Dessa forma, h ∈ [0, 1].

Temos:

f(0) = 0, 3308 e f(1) = −1, 24.

Exemplo




Al´em disso,

f (h) =        − √ 1         −  1 − h2 − h(1 − h2)−1/2 (−2h)

=  − √ 1   2     −  1 − h2 + √ h2  2

−1 + h2                     2

=  √1 − h2 −       1 − h

=  −1 + h2 − (1 − h2)

1 − h2

−2 + 2h2                −2(1 − h2)

=  √1 − h2       =   √₁ − h₂  &#x3C; 0,         h ∈ (0, 1).

Como f(0) · f(1) &#x3C; 0, f ´e cont´ınua e f (h) &#x3C; 0 em (0,1), ent˜ao

existe um ´unico zero de f(h) em (0,1).

# Exemplo






Pelo método da Bissecção o número de iterações para obter a solução será:

k > log(b − a) − log  .

log 2

Para I = (0, 1) e ε = 0, 01, temos:

k > log(1 − 0) − log 0, 01

log 2

k > 6, 64

ou seja, serão necessárias 7 iterações.

Tomando x ← h. Aplicando o método da Bissecção.

Exemplo





# Iterações

# 1ª iteração:

I = (0, 1)

| f(0)                | > 0              |     |               |
| ------------------- | ---------------- | --- | ------------- |
| x₁ = a+b = 1 = 0, 5 | f(0,5) = -0,6258 | < 0 | I = (0; 0, 5) |
| f(1)                | < 0              |     |               |

# 2ª iteração:

I = (0; 0, 5)

|            | f(0)              | > 0 |                |
| ---------- | ----------------- | --- | -------------- |
| x₂ = 0, 25 | f(0,25) = -0,1639 | < 0 | I = (0; 0, 25) |
|            | f(0,5)            | < 0 |                |

# 3ª iteração:

I = (0; 0, 25)

|             | f(0)              | > 0 |                     |
| ----------- | ----------------- | --- | ------------------- |
| x₃ = 0, 125 | f(0,125) = 0,0814 | > 0 | I = (0, 125; 0, 25) |
|             | f(0,25)           | < 0 |                     |

# 4ª iteração:

I = (0, 125; 0, 25)

|              | f(0,125)           | > 0 |                       |
| ------------ | ------------------ | --- | --------------------- |
| x₄ = 0, 1875 | f(0,1875) = -0,042 | < 0 | I = (0, 125; 0, 1875) |
|              | f(0,25)            | < 0 |                       |

# Exemplo




# 5ª iteração: I = (0, 125; 0, 1875)

| f(0,125)     | >                  | 0 |   |                        |
| ------------ | ------------------ | - | - | ---------------------- |
| x₅ = 0, 1563 | f(0,1563) = 0,0195 | > | 0 | I = (0, 1563; 0, 1875) |
| f(0,1875)    | <                  | 0 |   |                        |

# 6ª iteração: I = (0, 1563; 0, 1875)

| f(0,1563)    | >                   | 0 |   |                        |
| ------------ | ------------------- | - | - | ---------------------- |
| x₆ = 0, 1719 | f(0,1719) = -0,0113 | < | 0 | I = (0, 1563; 0, 1719) |
| f(0,1875)    | <                   | 0 |   |                        |

# 7ª iteração: I = (0, 1563; 0, 1719)

| f(0,1563)    | >                 | 0 |   |                        |
| ------------ | ----------------- | - | - | ---------------------- |
| x₇ = 0, 1641 | f(0,1641) = 0,004 | > | 0 | I = (0, 1641; 0, 1719) |
| f(0,1719)    | <                 | 0 |   |                        |

|b − a| = |0, 1719 − 0, 1641| = 0, 0078 &#x3C; 0, 01

Logo,

x̄ = (0,1641 + 0,1719) / 2 = 0, 168

Exemplo





Portanto, h ≈ 0, 168.

Dessa forma, a profundidade da água é de aproximadamente r − h = 1 − 0, 168 = 0, 832.

# Exemplo