UFMS - Universidade Federal de Mato Grosso do Sul
# Métodos Numéricos

# 5a Lista de Exercícios

# Interpola¸c˜ao Polinomial

1. Dada a tabela abaixo, calcule e3,1 usando um polinômio de interpola¸c˜ao na forma de Lagrange sobre três pontos. Dê um limitante para o erro cometido.
| x  | 2,4   | 2,6   | 2,8   | 3,0   | 3,2   | 3,4   | 3,6   | 3,8   |
| -- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| ex | 11,02 | 13,46 | 16,44 | 20,08 | 24,53 | 29,96 | 36,59 | 44,70 |
2. Considere a tabela
| x    | 0,0   | 0,5    | 1,0   | 1,5    | 2,0  | 2,5   |
| ---- | ----- | ------ | ----- | ------ | ---- | ----- |
| f(x) | -2,78 | -2,241 | -1,65 | -0,594 | 1,34 | 4,564 |

Usando um polinômio interpolador na Forma de Newton de grau 3 estime o valor de f(1, 23). Dê uma estimativa para o erro cometido.
3. Considere:
| x | 0,0 | 0,2    | 0,4    | 0,6    | 0,8    | 1,0    |
| - | --- | ------ | ------ | ------ | ------ | ------ |
| y | 1,0 | 1,2408 | 1,5735 | 2,0333 | 2,6995 | 3,7183 |

Usando interpola¸c˜ao de grau 3, obtenha x tal que f(x) = 2, 3. Dê uma estimativa para o erro cometido.
4. Supondo que a velocidade do som na água varia com a temperatura de acordo com a tabela abaixo, determinar, utilizando um polinômio interpolador usando três pontos, um valor estimado para a velocidade do som na água em uma temperatura de 1000.
| Temperatura(oC)  | 86,0 | 93,3 | 98,9 | 104,4 | 110,0 |
| ---------------- | ---- | ---- | ---- | ----- | ----- |
| Velocidade (m/s) | 1552 | 1548 | 1544 | 1538  | 1532  |
5. Uma barra de metal encontra-se presa em duas paredes separadas pela distância de 12m. A 5m da parede A (ver figura), um corpo apoiado sobre a barra faz com que este toque no solo. Os pontos de engate nas duas paredes estão a 8m (parede A) e 3m (parede B) do solo, conforme mostra a figura a seguir. Usando interpola¸c˜ao polinomial na forma de Newton, pede-se estimar:
1. a altura, em relação ao solo, de um ponto da barra localizado a 2m da parede A;
2. qual deve ser a altura da barra no ponto localizado a 2m da parede A, para que o trecho compreendido até 5m da mesma seja representado por um polinômio de grau um.

| h |   |
| - | - |
| 0 |   |

SOLO
d = 12 m



# 6.

| w    | 0,1   | 0,2   | 0,4  | 0,6   | 0,8   | 0,9   |
| ---- | ----- | ----- | ---- | ----- | ----- | ----- |
| f(w) | 0,905 | 0,819 | 0,67 | 0,549 | 0,449 | 0,407 |

| x    | 1,0   | 1,2   | 1,4   | 1,7   | 1,8   |
| ---- | ----- | ----- | ----- | ----- | ----- |
| g(x) | 0,210 | 0,320 | 0,480 | 0,560 | 0,780 |

Calcule o valor aproximado de x tal que f(g(x)) = 0, 6, usando polinˆomios interpolantes de grau 2.

# 7.

Com que grau de precis˜ao podemos calcular √115 usando interpola¸c˜ao sobre os pontos x0 = 100, x1 = 121, x2 = 144?

# 8.

A fun¸c˜ao f(x) = 4senx + e−x admite um valor m´aximo no intervalo (0, 2). Usando um processo de interpola¸c˜ao quadr´atica, obtenha uma aproxima¸c˜ao para este valor. Tabele a fun¸c˜ao com espa¸camento h = 0, 5 entre os pontos para construir o polinˆomio.

# Respostas

1. Interpolando em x0 = 2, 8, x1 = 3, 0 e x2 = 3, 2 obtemos f(3, 1) ≈ 22.2038. |E(3, 1)| ≤ 1, 23 × 10−2
2. Usando x0 = 0, 5, x1 = 1, 0, x2 = 1, 5 e x3 = 2, 0 obtemos f(1, 23) ≈ −1, 247. |E(1, 23)| ≈ 0.
3. x ≈ 0, 6880 ; E(2, 3) ≈ 0, 0059.
4.
5. (a) 3,7854 m (b) 4,8m
6. Utilizando interpola¸c˜ao inversa para f(x) sobre os pontos: y0 = 0, 67, y1 = 0, 549 e y2 = 0, 449 obtemos: f(0, 5101) ≈ 0, 6 aplicando o processo de interpola¸c˜ao inversa para g(x) sobre os pontos y0 = 0, 32, y1 = 0, 48 e y2 = 0, 56 obtemos g(1.4972) ≈ 0, 5101. Portanto, x ≈ 1, 4972. f(g(1, 4972)) ≈ f(0, 5101) ≈ 0, 6.
7. |E(115)| ≤ 1, 631 × 10−3
8. 4,222