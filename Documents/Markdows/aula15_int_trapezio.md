# Integração Numérica

# Lilian Berti

# Métodos Numéricos

# Lilian Berti

# Integração Numérica

# Integração Numérica

Se uma função f(x) é contínua em um intervalo [a, b] e sua primitiva F(x) é conhecida então:

b

f(x)dx = F(b) − F(a) em que F (x) = f(x).

a

No entanto, pode ser complicado obter F(x) ou mesmo não é conhecida a expressão da função f(x).

Lilian Berti Integração Numérica

# Exemplos

# (a)

Na tabela, temos a leitura de velocidades instantânea de um veículo ao percorrer uma pista.

| t(min) | 0 | 10 | 20 | 30 | 40 | 50 | 60 |
| ------- | -- | -- | -- | -- | -- | -- | -- |
| V(km/h) | 23 | 28 | 40 | 47 | 60 | 60 | 50 |

Qual a distância s percorrida?

s =
∫01 v(t) dt

# (b)

∫14 ln(x3 + √ex + 1) dx

# (c)

∫01 e-x2 dx

Lilian Berti Integração Numérica

# Integração Numérica

Sabemos que a integral definida (de Riemann) de uma função contínua f em [a, b] é

b
I = ∫ f(x)dx = lim Σ f(xk)∆x
a n→∞ k=1

em que ∆x = b−a e xk são pontos amostrais do intervalo [a, b].

Na integração numérica, aproximamos I por uma soma finita, na qual f é amostrada em alguns pontos.

Lilian Berti

# Integração Numérica

Na fórmula de integração de numérica de n + 1 pontos, temos

I =
n
∑
k=1
Akf(xk) + R

em que x0, x1, · · · , xn ∈ [a, b] são os pontos para a integração, A0, A1, · · · , An são os pesos, R é o resto.

Dessa forma, na integração numérica definimos:

I =
b
∫
a
f(x)dx ≈
n
∑
k=1
Akf(xk)

Nosso objetivo será escolher os pontos xk nos quais f é amostrada e também determinar os pesos Ak.

Lilian Berti

Fórmulas de Newton-Cotes

substitui a função a ser integrada ou aproxima os dados por um polinômio de grau n, que interpola f em pontos igualmente espaçados no intervalo de integração [a, b].

Os pontos de integração são definidos por: xi+1 = xi + h, i = 0, 1, · · · , n − 1 em que x0 = a, xn = b e h = b−a (n: número de subintervalos).

As fórmulas são do tipo:

| b | f(x) dx | ≈ | pn(x) dx | | |
| - | ------- | -- | -------- | ----------------------------------------------- | ------------------------------------------------ |
| | xn | xn | | \[f(x₀)L₀(x) + f(x₁)L₁(x) + · · · + f(xₙ)Lₙ(x)] | dx |
| a | xn | xn | ≈ | f(x0) | L0(x) dx + f(x1) L1(x) dx + · · · f(xn) Ln(x) dx |
| | xn | xn | | x0 | |
| | | | ≈ | f(xi)Ai | |
| | i=0 | | | | |

em que Ai = xn Li(x) dx.

Lilian Berti

Integração Numérica

# Regra do Trapézio

Caso n = 1 (f(x) ≈ p1(x)): Interpolando f(x) em x0 e x1 (x1 = x0 + h). Temos:

∫ab f(x) dx ≈ f(x0)A0 + f(x1)A1

em que

A0 = ∫x0x1 L0(x) dx = ∫x0x1 x − x1 dx

= − 1 ∫x0x1 x1 (x − x1) dx = − 1/h ∫x0x1 x0 − x1 dx

= − 1/h [x1 (x0 − x1)] = − 1/h [x0 − x1]

= − 1 [−(x1 − x0)2] = 1/2h2 = h

Lilian Berti Integração Numérica

De maneira análoga, é possível verificar que:

A1 = ∫x0x1 L1(x) dx = h.

Portanto,

∫ab f(x) dx ≈ f(x0) h + f(x1) h

# Erro

O erro do polinômio de interpolação é dado por:

E(x) = f(x) − pn(x) = (x − x0)(x − x1) · · · (x − xn) fn+1(ξ) em

# Integração Numérica

f(x) dx = [p₁(x) + E(x)] dx = p1(x) dx + E(x) dx

Logo, o erro da integração é dado por:

ET = b E(x) dx = b(x − x0)(x − x1) f (ξ) dx

a a 2

Pelo teorema do Valor médio para integrais, existe γ ∈ [a, b], tal que:

ET = f (γ) b(x − x0)(x − x1) dx = − 1 f (γ) (b − a)³

2 a 2 6

= − 1 f (γ)h³

12

Logo,

|ET| ≤ h³ max |f (x)|.

12 x∈[a,b]

Lilian Berti

# Exemplo:

Calcule I =      4 √x dx utilizando a regra do trapézio.

1

Temos h = b − a = 4 − 1 = 3 e f(x) = √x. Tomando x0 = 1 e x2 = 4, então:

I ≈ h [f(x0) + f(x1)] = 3 [√1 + √4] = 4, 5

2

Erro:          h3          33          1

|ET| ≤          max |f (x)| = max          − ~~√~~          ≈ 0, 5625

# Regra do Trapézio Repetida

Considerando n subintervalos em [a, b].

| b | x1 | x2 | xn |
| --------- | ---------- | ---------- | ---------------- |
| f(x) dx ≈ | p1(x) dx + | p1(x) dx + | · · · + p1(x) dx |
| a | x0 | x1 | xn−1 |

≈ h [f(x0) + f(x1)] + h [f(x1) + f(x2)] + · · · + h [f(xn−1) + f(xn)]

2

≈ h f(x0) + f(xn) + 2 ∑i=1n−1 f(xi) = ITR

2

Erro

ETR = − n h³ f(γi) em que γi ∈ [xi−1, xi]

i=1 12

= −n h³ f(γi)

12

|ETR| ≤ n h³ max |f (x)| com h = b − a

12 x∈[a,b]

≤ (b − a) h² max |f (x)|

12 x∈[a,b]

Lilian Berti Integração Numérica

# Exemplo:

Calcule I = 4 √x dx utilizando a regra do trapézio com:

(a) 2 repetições, ou seja, 2 subintervalos em [1,4].

Temos:

b − a = 4 − 1

n = 2, h = n = 2 = 1, 5

| x | 1 | 2,5 | 4 |
| ---- | - | ----- | - |
| f(x) | 1 | √₂, 5 | 2 |

I ≈ h [f(1) + f(4) + 2f(2, 5)] = 4, 6217.

Lilian Berti Integração Numérica

(b) 4 repetições, ou seja, 4 subintervalos em [1,4].

Temos:

b − a      4 − 1

n = 4 e h = n      =      4      = 0, 75

| x | 1 | 1,75 | 2,5 | 3,25 | 4 |
| ---- | - | ------ | ----- | ------ | - |
| f(x) | 1 | √₁, 75 | √₂, 5 | √₃, 25 | 2 |

I ≈ h [f(1) + f(4) + 2(f(1, 75) + f(2, 5) + f(3, 25))] = 4, 6550.

|ETR| ≤ (b − a) h² max |f (x)| = (4 − 1)0, 75² · 1 = 0, 0352

12 x∈[a,b]

12

Lilian Berti Integração Numérica

# Exemplo

Na tabela, temos a leitura de velocidades instantânea de um veículo ao percorrer uma pista.

| t(min) | 0 | 10 | 20 | 30 | 40 | 50 | 60 |
| ------- | -- | -- | -- | -- | -- | -- | -- |
| V(km/h) | 23 | 28 | 40 | 47 | 60 | 60 | 50 |

Qual a distância s percorrida? Deixando as grandezas na mesma unidade.

| t(h) | 0 | 1/6 | 2/6 | 3/6 | 4/6 | 5/6 | 1 |
| ------- | -- | --- | --- | --- | --- | --- | -- |
| V(km/h) | 23 | 28 | 40 | 47 | 60 | 60 | 50 |

s = 1 v(t)dt ≈ 1/6 [23 + 50 + 2(28 + 40 + 47 + 60 + 60)] ≈ 45, 25km

Lilian Berti Integração Numérica

Exemplo: Uma linha reta foi traçada de modo a tangenciar as margens de um rio nos pontos A e B. Para medir a área do trecho entre o rio e a reta AB foram traçadas perpendiculares em relação a reta com um intervalo de 0,05m. Qual é esta área?

| p | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| - | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| c | 3,28 | 4,02 | 4,64 | 5,26 | 4,98 | 3,62 | 3,82 | 4,68 | 5,26 | 5,82 | 3,24 |

em que p é a perpendicular e c é o comprimento em metros

Lilian Berti Integração Numérica

Resposta:

0,5

área = I = f(x)dx ≈ IT

IT = 0,05 [3, 28+2(4, 02+4, 64+5, 26+4, 98+3, 62+3, 82+4, 68+5, 26+5, 82)+3, 24] =

2

2, 268

Lilian Berti Integração Numérica