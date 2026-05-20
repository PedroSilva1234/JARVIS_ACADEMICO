UFMS - Universidade Federal de Mato Grosso do Sul
# Métodos Numéricos

# 6a Lista de Exercícios

# Integração Numérica

# 1.

Seja I = 2 ~~√~~xdx.

1. Calcule o valor aproximado para I pela regra dos trapézios e 1/3 de Simpson, usando quatro e seis divisões de [2,14]. Obtenha um limitante superior para o erro cometido.
2. Quantos divisões, no mínimo, podemos esperar obter erros menores que 10−5 pela regra dos trapézios e 1/3 de Simpson?

# 2.

Calcule o valor aproximado de 0,6 1 1 dx, com três casas decimais de precisão usando regra 1/3 de Simpson.

# 3.

Dada a tabela:

| x    | 0,0 | 0,2    | 0,4    | 0,6    | 0,8    | 1,0    |
| ---- | --- | ------ | ------ | ------ | ------ | ------ |
| f(x) | 1,0 | 1,2408 | 1,5735 | 2,0333 | 2,6965 | 3,7183 |

Sabendo que a regra 1/3 de Simpson é, em geral, mais precisa que a regra dos trapézios, qual seria o modo mais adequado de calcular 1 f(x)dx, usando a tabela acima? Aplique este processo e determine esta integral.

# 4.

Determine a distância percorrida para os seguintes dados:

| t(min) | 1 | 2 | 3,25 | 4,5 | 6   | 7 | 8 | 9 | 9,5 | 10 |
| ------ | - | - | ---- | --- | --- | - | - | - | --- | -- |
| v(m/s) | 5 | 6 | 5,5  | 7   | 8,5 | 8 | 6 | 7 | 7   | 5  |

Use:

1. Regra do trapézio
2. A melhor combinação das regras do trapézio e de Simpson.

# 5.

Uma pessoa desliza, sem atrito, do alto de um escorrega (do ponto A), acoplando-se a um carrinho que se encontra em repouso no ponto B. A partir deste instante, a pessoa e o carrinho movem-se juntos na água até parar.

Sabendo que a velocidade do conjunto pessoa carrinho imediatamente após o acoplamento é 4m/s e que a velocidade, v, em cada instante t na água é dada pela tabela seguinte, calcule (usando todos os pontos) a distância percorrida na água pelo conjunto pessoa-carrinho até parar.

| t | 0,0 | 0,3 | 0,6 | 0,8 | 1,0 | 1,2 | 1,8 | 2,4 | 3,0  | 3,6  | 4,2 |
| - | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
| v | 4,0 | 3,9 | 3,7 | 3,5 | 3,3 | 2,9 | 2,5 | 2,0 | 1,25 | 0,75 | 0,0 |




# 6.

Seja I = x−xdx. Calcule I usando 6 subintervalos, utilizando:

- (a) Regra do Trapézio
- (b) Regra 1/3 de Simpson
- (c) Regra 3/8 de Simpson
- (d) Quadratura Gaussiana em dois pontos.
- (e) Quadratura Gaussiana em três pontos.

# 7.

Um terreno está limitado por uma cerca reta e por um rio. As diferentes distâncias X (em metros) de uma extremidade da cerca ao rio, que é a largura Y do terreno (em metros) foi medida. Os resultados estão na tabela a seguir.

| X | 0 | 20 | 40 | 60 | 80 | 100 | 120 |
| - | - | -- | -- | -- | -- | --- | --- |
| Y | 0 | 22 | 41 | 53 | 38 | 17  | 0   |

Determine a área aproximada do terreno utilizando a Regra 1/3 de Simpson.

# Respostas

1. (a) Regra dos Trapézios: Para n=4 tem-se I ≈ 4,7683868. Para n=6 tem-se I ≈ 4,7077771

Regra 1/3 de Simpson: Para n=4 tem-se I ≈ 4,6763744. Para n=6 tem-se I ≈ 4,6614894
2. (b) Regra dos Trapézios: 1382 ; Regra 1/3 de Simpson: 80.
3. I ≈ 0,4703;
4. I ≈ 1,96446. Utilizando regra dos Trapézios no primeiro intervalo e a regra 1/3 de Simpson nos intervalos restantes.
5. (a) I ≈ 60,375 m.min × 60s = 3622,5

(b) I ≈ 59,9375 m.min × 60s = 3596,25
6. 9,125
7. (a) 0,1405 (b) 0,1320 (c) 0,1322 (d) 0,1194 (e) 0,1317