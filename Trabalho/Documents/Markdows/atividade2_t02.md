Métodos Numéricos - Turma 02 - 2024/2
# Atividade 2

Trabalhe 4 dígitos decimais. Justifique as suas respostas.

# 1.

A população (p) de uma pequena comunidade na periferia de uma cidade cresce rapidamente durante um período de 20 anos:

| t | 0 | 5 | 10 | 15 | 20 |
| - | --- | --- | --- | --- | ---- |
| p | 100 | 200 | 450 | 950 | 2000 |

Como um engenheiro trabalhando para um companhia de serviços públicos, prever qual será a população daqui a 5 anos para antecipar a demanda por energia elétrica. Use um modelo exponencial para fazer essa previsão. (p ≈ aebx)

# 2.

Você mediu a queda de tensão V através de um resistor para diversos valores diferentes da corrente i. Os resultados são:

| i | 0,25 | 0,75 | 1,25 | 1,5 | 2,0 |
| - | ----- | ---- | ---- | ---- | --- |
| V | -0,45 | -0,6 | 0,7 | 1,88 | 6,0 |

Use na forma de Newton a interpolação polinomial de grau 1, 2 e 3 para determinar uma estimativa da queda de tensão para i = 1, 15. Dê uma estimativa para o erro para cada valor encontrado. Comente seus resultados.

# 3.

A lei de Faraday caracteriza a queda de tensão através de um indutor como

VL = L di/dt

em que VL é a queda de tensão (V), L é a indutância (em henrys; 1H = 1V · s/A), i é a corrente (A) e t é o tempo (s).

Com base na lei de Faraday, use os dados da tensão para obter uma estimativa da indutância, L, em henrys se uma corrente de 2A passar por um período de 400 milissegundos.

| t, ms | 0 | 10 | 20 | 40 | 60 | 80 | 120 | 180 | 280 | 400 |
| -------- | - | -- | -- | -- | -- | -- | --- | --- | --- | --- |
| V, volts | 0 | 18 | 29 | 44 | 49 | 46 | 35 | 26 | 15 | 7 |

Pela lei de Faraday, temos L = ∫(0 to t) V dt / i.

# 4.

Para um circuito RL simples, a lei da tensão de Kirchhoff exige que (se a lei de Ohm for válida)

L di/dt + Ri = 0,

em que i é a corrente, L é a indutância e R é a resistência. Se L = 1, R = 1, 5 e i(0) = 0, 5, encontre a solução aproximada i(0, 2) usando h = 0, 1 utilizando:

(a) Método de Euler;

(b) Método de Euler Aperfeiçoado;

(c) Sabendo que a solução analítica do problema é y = 0, 5e^(-2t). Analise o erro absoluto dos valores obtidos no item (a) e (b).

# 5.

Uma haste aquecida com uma fonte de calor uniforme pode ser modelada pela equação de Poisson:

d²T/dx² = -f(x).

Dada uma fonte de calor f(x) = 0, 12x³ − 2, 4x² + 12x e as condições de contorno T(0) = 40 e T(10) = 200, determine a distribuição de temperatura com o método de diferenças finitas com h = ∆x = 2.