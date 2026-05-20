# Resolução de sistemas lineares - Fatoração LU

# Lilian Berti

# Métodos Numéricos

# Resolução de sistemas lineares - Fatoração LU

# Lilian Berti

Fatoração LU

Suponha que seja possível fatorar a matriz A como A = LU em que L é uma matriz triangular inferior com diagonal unitária (lii = 1, ∀i), U é uma matriz triangular superior.

Podemos reescrever o sistema linear Ax = b, como:

LUx = b.

Para obter a solução, resolvemos:

1. Ly = b
2. Ux = y

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Cálculo dos fatores L e U utilizando a Eliminação de Gauss

# Exemplo:

| a11 | a12 | a13 | x1 | b1 | |
| --- | --- | --- | -- | -- | -- |
| a21 | a22 | a23 | x2 | = | b2 |
| a31 | a32 | a33 | x3 | b3 | |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

Temos:
a11 a12 a13
A(0) = A = a21 a22 a23
a31 a32 a33

Etapa 1

pivô: a11 = 0

m21 = a21/a11 L2 ← L2 − m21L1

m31 = a31/a11 L3 ← L3 − m31L1

1 0 0 a₁₁ a₁₂ a₁₃ a₁₁ a₁₂ a₁₃
M(0)A(0) = −m₂₁ 1 0 a₂₁ a₂₂ a₂₃ = 0 a₂₂ a₂₃ = A(1)
−m₃₁ 0 1 a₃₁ a₃₂ a₃₃ 0 a₃₂ a₃₃

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Etapa 2

pivô: a22 = 0

m32 = a32/a22 L3 ← L3 − m32L2

| 1 | 0 | 0 | a11 | a12 | a13 |
| - | ---- | - | --- | --- | --- |
| 0 | 1 | 0 | 0 | a22 | a23 |
| 0 | −m32 | 1 | 0 | a32 | a33 |

M(1)A(1) = = 0 = 0 = A(2)

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Resolução de sistemas lineares - Fatoração LU

M(1)A(1) = A(2)

M(1)M(0)A(0) = A(2)

A = [M(1)M(0)]−1A(2)

A = [M(0)]−1[M(1)]−1A(2)

A =

# Teorema

Dada uma matriz A : n × n, seja Ak a matriz constituída das k primeiras linhas e colunas da matriz A. Suponha que det(Ak) = 0 para k = 1, 2, . . . , (n − 1). Então, existe uma única matriz triangular inferior L com diagonal unitária e uma única matriz triangular superior U tais que A = LU.

Lilian Berti

Resolução de sistemas lineares - Fatoração LU

Exemplo: Considere o sistema linear

| 2 | 3 | 1 | x1 | 9 | |
| - | -- | -- | -- | -- | - |
| 1 | 1 | 1 | x2 | = | 4 |
| 1 | −1 | −1 | x3 | −2 | |

a) Verifique que a A admite fatoração LU.

det(A1) = |a11| = |2| = 2

det(A2) = 2 3 = −1

1 1

Como det(A1) = 0 e det(A2) = 0, a matriz A admite uma única fatoração LU.

Lilian Berti Resoluçõ de sistemas lineares - Fatoração LU

# b) Resolva o sistema linear utilizando a fatoração LU.

| 2 | 3 | 1 |
| - | -- | -- |
| 1 | 1 | 1 |
| 1 | −1 | −1 |

Etapa 1:

pivô: 2

m21 = 0, 5     L2 ← L2 − 0, 5L1

m31 = 0, 5     L3 ← L3 − 0, 5L1

| 2 | 3 | 1 |
| --- | ---- | ---- |
| 0,5 | −0,5 | 0,5 |
| 0,5 | −2,5 | −1,5 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Etapa 2:

pivô: -0,5

m32 = 5 L3 ← L3 − 5L2

| 2 | 3 | 1 | |
| ------ | ---- | ----- | ---- |
| A(2) = | 0, 5 | −0, 5 | 0, 5 |
| | 0, 5 | 5 | −4 |

Logo,

| 1 | 0 | 0 | |
| --- | ---- | - | - |
| L = | 0, 5 | 1 | 0 |
| | 0, 5 | 5 | 1 |

e U =

| 0 | −0, 5 | 0, 5 | |
| - | ----- | ---- | -- |
| | 0 | 0 | −4 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Resolvendo:

# i) Ly = b

| y1 | = | 9 | 9 |
| ----------------- | - | -- | --------- |
| 0, 5y1 + y2 | = | 4 | y = −0, 5 |
| 0, 5y1 + 5y2 + y3 | = | −2 | −4 |

# ii) Ux = b

| 2x1 + 3x2 + x3 | | | = | 9 | 1 |
| -------------- | ----------------- | ----- | - | ----- | ----- |
| | − 0, 5x2 + 0, 5x3 | | = | −0, 5 | x = 2 |
| | | − 4x3 | = | −4 | 1 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

c) Calcule o determinante da matriz A.

Como A = LU, segue que:

det(A) = det(L)det(U) = det(U) = 2 · (0, 5) · (−4) = 4

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Diferença entre eliminação de Gauss e fatoração LU

ausência do vetor b na fase de eliminação;

resolver Ly = b funciona como uma mémoria dos cálculos a ser efetuados em b.

Isto facilita quando é necessário resolver vários sistemas lineares com a mesma matriz de coeficientes, pois a fatoração é feita uma única vez.

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# O que poderia dar errado nos cálculos da fatoração LU?

Exemplo:

| A = | 10−20 1 |
| --- | ------- |
| | 1 1 |

m21 = 1 = 1020

10−20

a22 = 1 − 1020 = −1020

| LU = | 1 0 | 10−20 1 |
| ---- | ------ | --------- |
| | 1020 1 | 0 −1020 1 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

O exemplo mostra que o mesmo quando a matriz tem fatoração LU, a qualidade numérica pode ser desastrosa. Perceba que um erro muito pequeno na troca de (1 − 1020) por (−1020) o produto LU já ficou bem diferente.

Apesar do pivô não ser nulo, ele é muito pequeno, isto implicou no multiplicador grande. Logo, surgiu a perda de d´ıgitos.

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Fatoração LU com pivoteamento parcial

# Matriz de permutação P:

Uma matriz quadrada de ordem n que pode ser obtida da matriz identidade de ordem n, permutando-se as linhas e colunas.

# Exemplo:

| 0 | 1 | 0 |
| - | - | - |
| 0 | 0 | 1 |
| 1 | 0 | 0 |

P =

| 3 | 1 | 4 |
| - | - | - |
| 1 | 5 | 9 |
| 2 | 6 | 5 |

A =

| 1 | 5 | 9 |
| - | - | - |
| 2 | 6 | 5 |
| 3 | 1 | 4 |

PA =

| 1 | 5 | 9 |
| - | - | - |
| 2 | 6 | 5 |
| 3 | 1 | 4 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Observação:

| 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | | | | | |
| --- | - | - | - | - | - | - | - | - | - | - | - | - | - |
| PPT | = | 0 | 0 | 1 | 1 | 0 | 0 | = | 0 | 1 | 0 | = | I |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | | | | | |

| 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | | | | | |
| --- | - | - | - | - | - | - | - | - | - | - | - | - | - |
| PTP | = | 1 | 0 | 0 | 0 | 0 | 1 | = | 0 | 1 | 0 | = | I |
| 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | | | | | |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Resolução de sistemas lineares - Fatoração LU

Seja PA = LU, então o sistema linear Ax = b é equivalente a:

PAx = Pb
LUx = Pb

Resolvemos:

1. Ly = Pb
2. Ux = y

Lilian Berti

# Exemplo: Resolva Ax = b em que

| 2 | −1 | 6 | 7 |
| -- | -- | -- | -- |
| 8 | 4 | −1 | 11 |
| −2 | 5 | 1 | |

Note que: det(A1) = 2 = 0 e det(A2) = 16 = 0 assim a matriz A admite fatoração LU.

# Etapa 1

pivô: 8 ⇒ L1 ↔ L2

| 0 | 1 | 0 |
| - | - | - |
| 1 | 0 | 0 |
| 0 | 0 | 1 |

P =

| 8 | 4 | −1 |
| -- | -- | -- |
| 2 | −1 | 6 |
| −2 | 5 | 1 |

m21 = 0, 25 m31 = −0, 25

| 8 | 4 | −1 |
| ------ | -- | ----- |
| 0, 25 | −2 | 6, 25 |
| −0, 25 | 6 | 0, 75 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Etapa 2

pivô: 6 ⇒ L2 ↔ L3

| | 0 | 1 | 0 | 8 | 4 | −1 | |
| - | - | - | - | ------ | ------ | -- | ----- |
| | 0 | 0 | 1 | A(1) = | −0, 25 | 6 | 0, 75 |
| | 1 | 0 | 0 | | 0, 25 | −2 | 6, 25 |

m32 = −0, 3333

| 8 | 4 | −1 | |
| ------ | ------ | -------- | ----- |
| A(2) = | −0, 25 | 6 | 0, 75 |
| | 0, 25 | −0, 3333 | 6, 5 |

Então:

| | 0 | 1 | 0 | | 1 | 0 | 0 |
| - | - | - | - | --- | ------ | -------- | - |
| | 0 | 0 | 1 | L = | −0, 25 | 1 | |
| | 1 | 0 | 0 | | 0, 25 | −0, 3333 | 1 |

| 8 | 4 | −1 | |
| --- | - | -- | ----- |
| U = | 0 | 6 | 0, 75 |
| | 0 | 0 | 6, 5 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU

# Resolvendo PAx = Pb = 4

# i) Ly = Pb

| | y1 | y2 | y3 |
| ------------------------ | --- | --------- | -- |
| −0, 25y1 + y2 | = 4 | y = 6, 75 | |
| 0, 25y1 − 0, 3333y2 + y3 | = 7 | 6, 5 | |

# ii) Ux = y

| | x1 | x2 | x3 |
| -------------- | ------- | ----- | -- |
| 8x1 + 4x2 − x3 | = 11 | | 1 |
| 6x2 + 0, 75x3 | = 6, 75 | x = 1 | |
| 6, 5x3 | = 6, 5 | | 1 |

Lilian Berti Resolução de sistemas lineares - Fatoração LU