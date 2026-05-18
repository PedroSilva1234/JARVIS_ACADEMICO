
Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky

# Resolu¸c˜ao de sistemas lineares

# C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky

Lilian Berti

M´etodos Num´ericos

Lilian Berti  Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky






# Exemplo:

Sejam

| 1   | 0   | 0 | 3   | 3 | 1    | 1    | 0   | 0 |   |   |
| --- | --- | - | --- | - | ---- | ---- | --- | - | - | - |
| L = | 1/3 | 1 | U = | 0 | −2   | 14/3 | P = | 0 | 0 | 1 |
| 2/3 | 0   | 1 | 0   | 0 | −5/3 | 0    | 1   | 0 |   |   |

os fatores da fatora¸c˜ao LU com pivoteamento parcial da matriz A.

Lilian Berti  Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky






# Resolução de Sistemas Lineares

# a) Resolva o sistema linear Ax = b em que b = [7, 3, 5]ᵀ usando os fatores L, U e P.

# i) Ly = Pb

| 1   | 0 | 0 | y1 | 7 | 7          |
| --- | - | - | -- | - | ---------- |
| 1/3 | 1 | 0 | y2 | 5 | y = 2,6667 |
| 2/3 | 0 | 1 | y3 | 3 | −1,6667    |

# ii) Ux = y

| 3 | 3  | 1    | x1 | 7       | 1     |
| - | -- | ---- | -- | ------- | ----- |
| 0 | −2 | 14/3 | x2 | 2,6667  | x = 1 |
| 0 | 0  | −5/3 | x3 | −1,6667 | 1     |

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky





b) Determine o determinante da matriz A, usados os fatores L, U e P

det(A) = det(PTLU) = det(PT)det(L)det(U) = (−1)pdet(U) em que p é o número de permutações realizadas.

det(A) = (−1)1 · 3 · (−2) · (−5/3) = −10

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky




# c) Determine a matriz A.

Sabemos que:

PA = LU

PTPA = PTLU

A = PTLU

| A | 1 | 0 | 0 |
| - | - | - | - |
| 0 | 0 | 1 |   |
| 0 | 1 | 0 |   |

| A | 3 | 3 | 1    |      |
| - | - | - | ---- | ---- |
|   | 0 |   | −2   | 14/3 |
|   | 0 | 0 | −5/3 |      |

| A | 3 | 3 | 1 |
| - | - | - | - |
| 0 | 0 | 1 |   |
| 0 | 1 | 0 |   |

| A | 2 | 2  | −1 |
| - | - | -- | -- |
|   | 1 | −1 | 5  |
|   |   |    |    |

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky





# Cálculo da matriz inversa

Seja A uma matriz quadrada não singular de ordem 3.

Devemos ter: AA−1 = I3 e A−1A = I3.

Considere: C = A−1. Logo

| a11 | a12 | a13 | c11 | c12 | c13 | 1 0 0 |       |       |
| --- | --- | --- | --- | --- | --- | ----- | ----- | ----- |
| a21 | a22 | a23 | c21 | c22 | c23 |       | 0 1 0 |       |
| a31 | a32 | a33 | c31 | c32 | c33 |       |       | 0 0 1 |

Tomando Xi =

c1i
c2i
c3i

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky




# Resolução de sistemas lineares

Ent˜ao, devemos resolver os seguintes sistemas lineares:

| 1       | 0       | 0       |
| ------- | ------- | ------- |
| 0       | 0       | 1       |
| AX1 = 0 | AX2 = 1 | AX3 = 0 |

Assim, A-1 = C = [X1 X2 X3].

Portanto, devemos resolver três sistemas lineares com a mesma matriz A, sendo alterado somente o vetor de termos independentes.

Entre a eliminação de Gauss e a fatoração LU, o método mais indicado para resolver estes três sistemas é a fatoração LU.

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky





Sejam

| 1   | 0   | 0 | 3   | 3 | 1    | 1    | 0   | 0 |   |   |
| --- | --- | - | --- | - | ---- | ---- | --- | - | - | - |
| L = | 1/3 | 1 | U = | 0 | −2   | 14/3 | P = | 0 | 0 | 1 |
| 2/3 | 0   | 1 | 0   | 0 | −5/3 | 0    | 1   | 0 |   |   |

os fatores da fatora¸c˜ao LU com pivoteamento parcial da matriz A.

Lilian Berti

Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky




# Calcule a matriz inversa da matriz A utilizando os fatores L e U.

A−1 = [X1 X2 X3]

Determinando Xi, i=1,2,3. Resolvendo AXi = ei, (ei coluna i da matriz identidade) usando os fatores L e U.

# Determinando X1

1. Ly = Pe1

| 1   | 0 | 0 | y1 | 1 |
| --- | - | - | -- | - |
| 1/3 | 1 | 0 | y2 | 0 |
| 2/3 | 0 | 1 | y3 | 0 |

y = [1, -0, 3333, -0, 6667]

UX1 = y

| 3 | 3  | 1    | x1 | 1        |
| - | -- | ---- | -- | -------- |
| 0 | −2 | 14/3 | x2 | −0, 3333 |
| 0 | 0  | −5/3 | x3 | −0, 6667 |

X1 = [1, 1, 0, 4]

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky






# Determinando X2

1. Ly = Pe₂

| 1   | 0 | 0 | y1 | 0 | 0 |
| --- | - | - | -- | - | - |
| 1/3 | 1 | 0 | y2 | = | 0 |
| 2/3 | 0 | 1 | y3 | 1 | 1 |
2. UX2 = y

| 3 | 3  | 1    | x1 | 0 | 1, 6  |
| - | -- | ---- | -- | - | ----- |
| 0 | −2 | 14/3 | x2 | = | 0     |
| 0 | 0  | −5/3 | x3 | 1 | −0, 6 |

Lilian Berti  Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky





# Determinando X3

# i)

|     | Ly |   | y1 |   | 0 |
| --- | -- | - | -- | - | - |
| 1/3 | 1  | 0 | y2 | = | 1 |
| 2/3 | 0  | 1 | y3 |   | 0 |

# ii)

|   | UX3 | =    | y  |   |   |           |
| - | --- | ---- | -- | - | - | --------- |
| 3 | 3   | 1    | x1 |   | 0 | 0.5       |
| 0 | −2  | 14/3 | x2 | = | 1 | X3 = −0.5 |
| 0 | 0   | −5/3 | x3 |   | 0 |           |

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky



Portanto,

| −0, 9 | 1, 6  | 0, 5  |
| ----- | ----- | ----- |
| 1, 1  | −1, 4 | −0, 5 |
| 0, 4  | −0, 6 | 0     |

b) Resolva o sistema linear Ax = b em que b = [7, 3, 5]ᵀ usando a matriz inversa A−1.

| −0, 9 | 1, 6  | 0, 5  | 7 | 1 |   |
| ----- | ----- | ----- | - | - | - |
| 1, 1  | −1, 4 | −0, 5 | 3 | = | 1 |
| 0, 4  | −0, 6 | 0     | 5 |   |   |

Lilian Berti  Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky



# Fatora¸c˜ao de Cholesky

# Defini¸c˜ao:

Uma matriz A : n × n ´e sim´etrica se AT = A, ou seja aij = aji, para ∀i,j = 1, 2, . . . n.

# Exemplo:

| 2  | −1 | 0  |
| -- | -- | -- |
| −1 | 2  | −1 |
| 0  | −1 | 2  |

| 50 | 20 | 15 |
| -- | -- | -- |
| 20 | 80 | 0  |
| 15 | 0  | 60 |

Lilian Berti  Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky



# Definição

Uma matriz A : n × n é definida positiva se xTA x > 0 para todo x ∈ R, x ≠ 0.

# Teorema

Uma matriz A : n × n é simétrica e definida positiva se e somente se A pode ser decomposta de forma única no produto GGT, em que G é uma matriz triangular inferior com diagonal positiva.

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky




# Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky

Se A = GGT, na resolu¸c˜ao do sistema linear Ax = b, teremos

GGTx = b.

Para obter a solu¸c˜ao, resolvemos:

1. Gy = b
2. GTx = y.

Lilian Berti





# Cálculo do fator G

Exemplo: Seja A uma matriz simétrica definida positiva.

| a11 | a12 | a13 | a14 |
| --- | --- | --- | --- |
| a21 | a22 | a23 | a24 |
| a31 | a32 | a33 | a34 |
| a41 | a42 | a43 | a44 |

Obtendo G =

| g11 | 0   | 0   | 0   |
| --- | --- | --- | --- |
| g21 | g22 | 0   | 0   |
| g31 | g32 | g33 | 0   |
| g41 | g42 | g43 | g44 |

Devemos ter: A = GGT

Lilian Berti  Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky




# Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky

| a₁₁ | a₁₂ | a₁₃ | a₁₄ |   | g₁₁ |     | 0   | 0   | g₁₁ | g₂₁ | g₃₁ | g₄₁ |
| --- | --- | --- | --- | - | --- | --- | --- | --- | --- | --- | --- | --- |
| a₂₁ | a₂₂ | a₂₃ | a₂₄ | = | g₂₁ | g₂₂ | 0   | 0   | g₂₂ | g₃₂ | g₄₂ |     |
| a₃₁ | a₃₂ | a₃₃ | a₃₄ |   | g₃₁ | g₃₂ | g₃₃ | 0   | 0   | g₃₃ | g₄₃ |     |
| a₄₁ | a₄₂ | a₄₃ | a₄₄ |   | g₄₁ | g₄₂ | g₄₃ | g₄₄ | 0   | 0   | 0   |     |

Temos: √

g² = a₁₁ ⇒ g₁₁ = a₁₁

g₂₁g₁₁ = a₂₁ ⇒ g₂₁ = a²¹

g₃₁g₁₁ = a₃₁ ⇒ g₃₁ = a³¹

g₄₁g₁₁ = a₄₁ ⇒ g₄₁ = a⁴¹

g² + g² = a₂₂ ⇒ g₂₂ = a₂₂ − g²

g₃₁g₂₁ + g₃₂g₂₂ = a₃₂ ⇒ g₃₂ = (a₃₂ − g₃₁g₂₁)/g₂₂

g₄₁g₂₁ + g₄₂g₂₂ = a₄₂ ⇒ g₄₂ = (a₄₂ − g₄₁g₂₁)/g₂₂

g² + g² + g² = a₃₃ ⇒ g₃₃ = a₃₃ − g² − g²

g₄₁g₃₁ + g₄₂g₃₂ + g₄₃g₃₃ = a₄₃ ⇒ g₄₃ = (a₄₃ − g₄₁g₃₁ − g₄₂g₃₂)/g₃₃

g² + g² + g² + g₄₄ = a₄₄ ⇒ g₄₄ = a₄₄ − g² − g² − g²






# Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky

Caso geral, para A : n × n, obtemos G : n × n , por:

gkk = akk - ∑j=1k-1 gkj2
gik = (aik - ∑j=1k-1 gijgkj) / gkk

i = k + 1, . . . , n






# Exemplo: Determine a fatora¸c˜ao de Cholesky da matriz.

| A = | 6  | 15  | 55  |
| --- | -- | --- | --- |
|     | 15 | 55  | 225 |
|     | 55 | 225 | 979 |

Obtendo G de ordem 3.

para k = 1

g₁₁ = √a₁₁ = 6 = 2, 4495

g₂₁ = a²¹ = 15 = 6, 1237

g₁₁ = 2,4495

g₃₁ = a³¹ = 55 = 22, 454

g₁₁ = 2,4495

para k = 2

g₂₂ = a₂₂ − g² = 55 − (6, 1237)² = 4, 1833

g₃₂ = a³²−ᵍ²¹ᵍ³¹ = 225−6,1237(22454) = 20, 917

g₂₂ = 4,1833

para k = 3

g₃₃ = a₃₃ − g² − g² = 979 − (22, 454)² − (20, 917)² = 6, 1101

Lilian Berti Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky






# Lilian Berti

# Resolução de sistemas lineares - Cálculo da matriz inversa e a Fatoração de Cholesky

Portanto,

| 2  | 4495 | 0    | 0   |      |      |
| -- | ---- | ---- | --- | ---- | ---- |
| G  | 6    | 1237 | 4   | 1833 | 0    |
| 22 | 454  | 20   | 917 | 6    | 1101 |





# A fatora¸c˜ao de Cholesky

pode ser usada para verificar se uma matriz ´e sim´etrica e definida positiva; se o m´etodo falhar, a hip´otese ´e falsa.

A fatora¸c˜ao de Cholesky requer a metade do n´umero de opera¸c˜oes efetuadas na fatora¸c˜ao LU.

Lilian Berti  Resolu¸c˜ao de sistemas lineares - C´alculo da matriz inversa e a Fatora¸c˜ao de Cholesky