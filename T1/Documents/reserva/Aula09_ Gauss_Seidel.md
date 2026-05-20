
# Resolução de sistemas lineares - Métodos iterativos

# Lilian Berti

# Métodos Numéricos

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos



# Método de Gauss- Seidel

Considere o sistema linear

| a11x1 | + | a12x2 | + | a13x3 | = | b1 |
| ----- | - | ----- | - | ----- | - | -- |
| a21x1 | + | a22x2 | + | a23x3 | = | b2 |
| a31x1 | + | a32x2 | + | a33x3 | = | b3 |

Seja A = L + D + U em que

| 0   | 0   | 0 | a11 | 0 | 0   | 0 | a12 | a13 |   |     |
| --- | --- | - | --- | - | --- | - | --- | --- | - | --- |
| a21 | 0   | 0 | D = | 0 | a22 | 0 | U = | 0   | 0 | a23 |
| a31 | a32 | 0 | 0   | 0 | a33 | 0 | 0   | 0   |   |     |

Supondo aii = 0

Ax = b

(L + D + U)x = b

(L + D)x = -Ux + b

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos



Caso (L + D)-1 existir, então o processo iterativo é dado por:

x(k+1) = −(L + D)-1U x(k) + (L + D)-1b

| B | c |
| - | - |

Evitar o cálculo da inversa (L + D)-1

(L + D)x(ᵏ+1) = −Ux(k) + b

Dx(k+1) = −Lx(k+1) − Ux(k) + b

x(k+1) = −D-1(Lx(k+1) − Ux(k) + b)

ou seja, o esquema iterativo é dado por:

x(k+1) = 1 (b1 − a1,2x(ᵏ) − a1,3x(ᵏ))

1             a11    2    3

x(k+1) = 1 (b2 − a2,1x(ᵏ+1) − a2,3x(ᵏ))

2             a22    1    3

x(k+1) = 1 (b3 − a3,1x(ᵏ+1) − a3,2x(ᵏ+1))

3             a33    1    2

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos




# Resolução de sistemas lineares - Métodos iterativos

O vetor x(k+1) é obtido a partir dos elementos mais recentes, tanto do próprio x(k+1) quanto de x(k).

# Forma geral:

| bi       | -    | i-1    | aijx(k+1) | - | n                   | aijx(k) |
| -------- | ---- | ------ | --------- | - | ------------------- | ------- |
| j        |      |        |           |   |                     |         |
| x(k+1) = | j=1, | j=i+1, |           |   | i = 1, 2, . . . , n |         |
| i        |      | aii    |           |   |                     |         |





# Exemplo: Resolva o sistema linear pelo método de Gauss - Seidel

utilizando como aproximação inicial o vetor [0, 0, 0]T e critério de parada erro relativo inferior a 0,05.

5x1 + x2 + x3 = 5
3x1 + 4x2 + x3 = 6
3x1 + 3x2 + 6x3 = 0

# Esquema iterativo:

| x(k+1) = 1 (5 − x(k) − x(k))    | 1 | 5 | 2 | 3 |
| ------------------------------- | - | - | - | - |
| x(k+1) = 1 (6 − 3x(k+1) − x(k)) | 2 | 4 | 1 | 3 |
| x(k+1) = 1 (−3x(k+1) − 3x(k+1)) | 3 | 6 | 1 | 2 |

Lilian Berti Resolução de sistemas lineares - Métodos iterativos





# Para k = 0

| x(1) | = | 1(5 − x(0) − x(0))  | = | 1(5 − 0 − 0)        | = | 1       |
| ---- | - | ------------------- | - | ------------------- | - | ------- |
| 1    | 5 | 2                   | 3 | 5                   |   |         |
| x(1) | = | 1(6 − 3x(1) − x(0)) | = | 1(6 − 3(1) − 0)     | = | 0, 75   |
| 2    | 4 | 1                   | 3 | 4                   |   |         |
| x(1) | = | 1(−3x(1) − 3x(1))   | = | 1(−3(1) − 3(0, 75)) | = | −0, 875 |
| 3    | 6 | 1                   | 2 | 6                   |   |         |

x(1) = [1 ; 0, 75 ; −0, 875]T

ER = x(1)−x(0) ∞ = max{1;0,75;0,875} = 1 > 0, 05

x(1) ∞ = max{1;0,75;0,875}

Lilian Berti  Resolu¸c˜ao de sistemas lineares - M´etodos iterativos






# Para k = 1

x(2) = 1(5 − x(1) − x(1)) = 1(5 − 0, 75 − (−0, 875)) = 1, 025

| 1 | 5 | 2 | 3 | 5 |
| - | - | - | - | - |

x(2) = 1(6 − 3x(2) − x(1)) = 1(6 − 3(1, 025) − (−0, 875)) = 0, 95

| 2 | 4 | 1 | 3 | 4 |
| - | - | - | - | - |

x(2) = 1(−3x(2) − 3x(2)) = 1(−3(1, 025) − 3(0, 95)) = −0, 9875

| 3 | 6 | 1 | 2 | 6 |
| - | - | - | - | - |

x(2) = [1, 025 ; 0, 95 ; −0, 9875]T

ER = x(2)−x(1) ∞ = max{0,025;0,2;0,1125} = 0,2 = 0, 1951 >

x(2) ∞ max{1,025 ; 0,95 ; 0,9875} 1,025

0, 05

Lilian Berti Resolu¸c˜ao de sistemas lineares - M´etodos iterativos





# Resolução de sistemas lineares - Métodos iterativos

Para k = 2

| x(3) | = | 1(5 − x(2) − x(2)) | = | 1(5 − 1, 025 − (−0, 9875)) | = | 1, 0075 |
| ---- | - | ------------------ | - | -------------------------- | - | ------- |
| 1    | 5 | 2                  | 3 | 5                          |   |         |

| x(3) | = | 1(6 − 3x(3) − x(2)) | = | 1(6 − 3(1, 0075) − (−0, 9875)) | = | 0, 9913 |
| ---- | - | ------------------- | - | ------------------------------ | - | ------- |
| 2    | 4 | 1                   | 3 | 4                              |   |         |

| x(3) | = | 1(−3x(3) − 3x(3)) | = | 1(−3(1, 0075) − 3(0, 9913)) | = | −0, 9994 |
| ---- | - | ----------------- | - | --------------------------- | - | -------- |
| 3    | 6 | 1                 | 2 | 6                           |   |          |

x(3) = [1, 0075 ; 0, 9913 ; −0, 9994]T

ER = x(3)−x(2) ∞ = max{0,0175;0,0413;0,0119} = 0,0413 = 0, 041 &#x3C;

x(3) ∞ max{1,0075 ; 0,9913 ; 0,9994} 1,0075

0, 05

Portanto, x (3) [1 − 9994]ᵀ

¯ = x = , 0075 ; 0, 9913 ; 0, .

Lilian Berti




# Critério para Convergência:

- Critério das linhas (visto aula passada)
- Critério de Sassenfeld

Sejam

β₁ = (a₁₂ + a₁₃ + · · · + a₁ₙ)/a₁₁

βi = (ai₁β₁ + ai₂β₂ + · · · + aii−₁βi−₁ + aii₊₁ + aii₊₂ + · · · + ain)/aii

Se

β = max {βi} &#x3C; 1,

1≤i≤n

então o método de Gauss-Seidel gera uma sequência convergente, independente da aproximação inicial x(0). Além disso, quando menor o valor β, mais rápida a convergência.

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos






# Exemplo:

Verifique se a matriz do exemplo anterior satisfaz o critério das linhas e o critério de Sassenfeld

| 5   | 1 | 1 |   |
| --- | - | - | - |
| A = | 3 | 4 | 1 |
|     | 3 | 3 | 6 |

# Verificando o Critério das linhas

Temos:

α1 = 5 + 1 = 2 = 0, 4

5

α2 = 3 + 1 = 1

4

α3 = 3 + 3 = 1

6

Como α = max{α1, α2, α3} = 1, segue que o critério das linhas não é satisfeito, não podemos garantir a convergência.

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos






# Verificando o Critério de Sassenfeld

Temos:

| β1 = | 5   | 1 | 1 |   |
| ---- | --- | - | - | - |
|      | A = | 3 | 4 | 1 |
|      |     | 3 | 3 | 6 |

β1 = 1 + 1 = 2 = 0, 4

β2 = 3β¹ + 1 = 0, 55

β3 = 3β¹ + 3β² = 0, 47

Como β = max{β1, β2, β3} = 0, 55 &#x3C; 1, segue que o critério de Sassenfeld é satisfeito, garantindo a convergência.

Lilian Berti Resolução de sistemas lineares - Métodos iterativos






# Exemplo: Considere Ax = b em que:

| 20 | 2  | 3  | −1 | 150 |
| -- | -- | -- | -- | --- |
| 2  | 8  | −1 | 1  | 4   |
| 1  | −1 | −5 | 2  | −11 |
| 5  | 2  | −3 | 10 | 48  |

Verifique se o critério de Sassenfeld é satisfeito.

Temos:

β1 = 2 + 3 + −1 = 0, 3

β2 = 2β1 + −1 + 1 = 0, 325

β3 = 1β1 + −1β2 + 2 = 0, 525

β4 = 5β1 + 2β2 + −3β3 = 0, 3725

Como β = max{β1, β2, β3} = 0, 55 &#x3C; 1, segue que o critério de Sassenfeld é satisfeito.

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos





# Lilian Berti

# Resolução de sistemas lineares - Métodos iterativos



# Interpretação Geométrica (caso 2x2)

Seja:

| x1 | + | x2  | = | 3  | x(0) = | 0 | x\* = | 1,5 |
| -- | - | --- | - | -- | ------ | - | ----- | --- |
| x1 | − | 3x2 | = | −3 |        | 0 |       | 1,5 |

Resolvendo o sistema linear pelo método de Gauss-Jacobi.

x(k+1) = 3 − x(k)

x1 = 3 + x1k

x(k+1) = 3 + x1k

x2 = 3

| x(1) | =    | 3        |          |          |               |   |        |
| ---- | ---- | -------- | -------- | -------- | ------------- | - | ------ |
|      | x(2) | =        | 2        |          |               |   |        |
|      |      |          | x(3)     | =        | 1             |   |        |
|      |      |          |          |          | x(4)          | = | 1,3333 |
|      |      | x(1) = 3 | x(2) = 2 | x(3) = 1 | x(4) = 1,3333 |   |        |

Lilian Berti

Resolução de sistemas lineares - Métodos iterativos



# Resolvendo o sistema linear pelo método de Gauss-Seidel.

x(k+1) = 3 − x(k)

1



# Resolução de sistemas lineares - Métodos iterativos

Observação: Neste exemplo:

| x1 | + | x2  | = | 3  |
| -- | - | --- | - | -- |
| x1 | − | 3x2 | = | −3 |

O critério das linhas e o critério de Sassenfeld não são satisfeitos.

Isto mostra que estes critérios são apenas uma condição suficiente.

E o critério de Sassenfeld também não é satisfeito.

Lilian Berti




# Resolução de sistemas lineares - Métodos iterativos

Caso fosse permutado as equações teríamos:

| x1 | − | 3x2 | = | −3 |
| -- | - | --- | - | -- |
| x1 | + | x2  | = | 3  |

Ambos os critérios de convergência não seriam satisfeitos.

Resolvendo pelo método de Gauss-Jacobi:

| x(k+1) | = | −3 + 3x(k) | 1 | 2 |
| ------ | - | ---------- | - | - |
| x(k+1) | = | 3 − x(k)   | 2 | 1 |

| x(0) | = | 0 | x(2) | = | −3 | x(3) | = | 6 |
| ---- | - | - | ---- | - | -- | ---- | - | - |
|      |   | 0 |      | 3 |    | 6    |   |   |

Teremos divergência.

Lilian Berti





# Resolvendo pelo método de Gauss-Seidel:

x(k+1) = −3 + 3x(k)

1

x(k+1) = 3 − x(k+1)

2

| x(0) | x(2) | x(3) |
| ---- | ---- | ---- |
| 0    | −3   | 15   |
|      | 6    | −12  |

Teremos divergência.

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos



Exemplo: Uma transportadora tem três caminhões (C1, C2, C3) estão equipados para levar três tipos diferentes de máquinas (A, B, C) de acordo com a tabela.

|    | MA | MB | MC |
| -- | -- | -- | -- |
| C1 | 1  | 0  | 2  |
| C2 | 1  | 1  | 1  |
| C3 | 1  | 2  | 1  |

O caminhão 1 pode levar a máquina A, nenhuma máquina B e duas máquinas C. Supondo que cada caminhão vai com a carga máxima, quantos caminhões de cada tipo devemos enviar para transportar exatamente 12 máquinas A, 10 máquinas B e 16 máquinas C?

Temos:

x1 + x2 + x3 = 12

x2 + 2x3 = 10

2x1 + x2 + x3 = 16

em que: xi : quantidade de caminhão i = 1, 2, 3

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos



# Gauss-Seidel

a) É possível garantir a convergência do método de na resolução deste problema?

O critério das linhas não é satisfeito, pois α1 = 1, α2 = 2 e α3 = 3. Logo, α > 1. O critério de Sassenfeld também não é satisfeito.

b) É possível permutar linhas e garantir a convergência?

Não é possível.

c) Podemos resolver por um método direto?

Sim, podemos utilizar a eliminação de Gauss.

Lilian Berti Resolução de sistemas lineares - Métodos iterativos



# Comparando os métodos.

# Métodos Diretos

- Determinam a solução em número finito de passos se a matriz é não singular;
- Solução exata a menos de erros de arredondamento;
- Não preservam a estrutura da matriz.

# Métodos Iterativos

- Não é garantido encontrar a solução (pode ou não convergir);
- Constrói uma sequência de aproximações;
- Preservam a estrutura da matriz.

Lilian Berti  Resolução de sistemas lineares - Métodos iterativos