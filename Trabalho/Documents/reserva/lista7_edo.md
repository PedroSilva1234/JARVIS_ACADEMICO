UFMS - Universidade Federal de Mato Grosso do Sul
# Métodos Numéricos

# 7a Lista de Exercícios

# Equação Diferencial Ordinária

1. Dado o PVI:

y = 4 − 2x

y(0) = 2.

1. Encontre uma aproximação para y(0, 5) usando o método de Euler Aperfeiçoado com h = 0, 25.
2. Compare seus resultados com a solução exata: y(x) = −x² + 4x + 2.
2. Considere o PVI:

y = yx² − y

y(0) = 1.

Encontre a solução aproximada para o PVI com h = 0, 5 e considerando x ∈ [0; 1] utilizando:
1. Método de Euler;
2. Método de Euler Aperfeiçoado;
3. Método de Taylor de segunda ordem;
4. Sabendo que a solução analítica do problema é y = e(−ˣ⁺ x³ ). Analise o erro absoluto dos valores obtidos no item (a), (b) e (c).
3. Use o método de Euler para resolver o sistema de equações diferenciais:

y = −2y + 5e−x

z = − yz²

para x ∈ [0; 0, 2] usando um tamanho de passo 0,1 com y(0) = 2 e z(0) = 4.
4. Considere o problema:

y" = −7y,

y(0) = 2, 0 ≤ x ≤ 0, 5,

y'(0) = 0

1. Reescreva este problema como um sistema de equações de 1ª ordem.
2. Resolva o sistema do item (a) usando o método de Euler com h = 0, 25.
5. O PVC:

y" = 4(y − x),

y(0) = 0, 0 ≤ x ≤ 1,

y(1) = 2

tem a solução y(x) = e²(e⁴ − 1)−1(e²x − e−²x) + x. Use o Método das Diferenças Finitas para aproximar a solução e compare os resultados com a solução real usando h = 0, 25.
6. O PVC:

y" = 2y − y + xex − x,

y(0) = 0, 0 ≤ x ≤ 2,

y(2) = −4

tem a solução y(x) = 1/6 x³ex − 5/3 xex + 2ex − x − 2. Use o Método das Diferenças Finitas para aproximar a solução e compare os resultados com a solução real usando h = 0, 5.






# Respostas

# 1.

(a) y(0, 5) ≈ 3, 75

(b)

| i | xi   | yi     | y(xi)  | erro |
| - | ---- | ------ | ------ | ---- |
| 0 | 0    | 2      | 2      | 0    |
| 1 | 0,25 | 2,9375 | 2,9375 | 0    |
| 2 | 0,5  | 3,75   | 3,75   | 0    |

|   |     | Euler  | Euler Aperf. | Taylor | Exata  |
| - | --- | ------ | ------------ | ------ | ------ |
| i | xi  | yi     | yi           | yi     | y(xi)  |
| 2 | 0   | 1      | 1            | 1      | 1      |
| 1 | 0,5 | 0,5    | 0,6563       | 0,625  | 0,6323 |
| 2 | 1   | 0,3125 | 0,5332       | 0,5127 | 0,5134 |

# 3.

| xi  | yi     | zi     |
| --- | ------ | ------ |
| 0,1 | 2,1    | 2,4    |
| 0,2 | 2,1324 | 1,7952 |

# 4.

(b)

| xi   | yi    | zi = y (xi) |
| ---- | ----- | ----------- |
| 0,25 | 2     | -3,5        |
| 0,5  | 1,125 | -7          |

# 5.

y(0, 25) ≈ 0, 3951; y(0, 5) ≈ 0, 8265; y(0, 75) ≈ 1, 3395

# 6.

y(0, 5) ≈ −0, 5082; y(1) ≈ −1, 6166; y(1, 5) ≈ −3, 2745

