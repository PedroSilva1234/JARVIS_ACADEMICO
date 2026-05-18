Zeros reais de Funções reais - Método da Bissecção

# Métodos Numéricos

# Zeros reais de Funções reais - Método da Bissecção

Lilian Berti

# Zeros reais de funções reais

# Definição:

Um número real γ é zero de função f(x) ou uma raiz da equação f(x) = 0 se f(γ) = 0.

# Exemplos

a) f(x) = 2x − 1

f(x) = 0 ⇔ x = 1

b) f(x) = ax² + bx + c, para a, b, c ∈ R, a ≠ 0

f(x) = 0 ⇔ x = −b ± √b² − 4ac

c) f(x) = x³ + x² − 10x + 8

x =? tal que f(x) = 0

d) f(x) = eˣ + x² − 2

x =? tal que f(x) = 0

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# Zeros reais de Funções reais - Método da Bissecção

Veremos métodos numéricos que encontram uma solução aproximada para estas raízes.

O cálculo de uma raiz pode ser dividido em duas etapas:

# Etapa 1: Isolamento da raiz

Encontra um intervalo (a, b) que contenha uma raiz de f(x) = 0.

# Etapa 2: Refinamento da raiz

A partir de um valor inicial x0 ∈ (a, b) gera uma sequência {x0, x1, . . . , xk, . . . } que convirga para uma raiz de f(x) = 0.

Lilian Berti

# Etapa 1: Isolamento da raiz

# Método Gráfico

# Exemplos:

a) f(x) = x + ln(x − 1)

f(x) = 0 ⇔ x + ln(x − 1) = 0 ⇔ ln(x − 1) = −x

| 25 | 05 | 38 | 23 | -38 |
| -- | -- | -- | -- | --- |

O intervalo (1, 2) contém uma raiz.

Lilian Berti

Zeros reais de Funções reais - Método da Bissecção

b) f(x) = ex² + x² − 2

f(x) = 0 ⇔ ex = −x2 + 2

Possui uma raiz em (−√2, 0) e uma raiz em (√2, 0).

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# Método Analítico

# Teorema de Bolzano

Se f : [a, b] → R é uma função contínua tal que f(a)f(b) < 0 então existe x∗ ∈ (a, b) tal que f(x∗) = 0.

# Exemplo:

Mostre que existe pelo menos uma solução da equação ex + x² − 2 = 0 em (√2, 0).

Seja f(x) = ex + x² − 2. Temos:

f(0) = −1 e f(√2) = 4, 1133.

Como f(0) · f(√2) < 0 e f é contínua em (√2, 0) pelo Teorema de Bolzano existe pelo menos um zero de f em (√2, 0).

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# Exemplo:

Determine os intervalos que contenha as raízes de x3 − 9x + 3 = 0

Analisando os valores da função em (−4, 3).

| x | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
| ---- | --- | -- | -- | -- | - | -- | -- | - |
| f(x) | -25 | 3 | 13 | 11 | 3 | -5 | -7 | 3 |

Temos uma raiz em cada um dos seguintes intervalos (−4, −3), (0, 1) e (2, 3).

Lilian Berti

Zeros reais de Funções reais - Método da Bissecção

# Proposição:

Se f : [a, b] → R é uma função diferenciável, f(a)f(b) < 0 e f'(x) > 0 (ou f'(x) < 0) para todo x ∈ (a, b), então existe um único x∗ tal que f(x∗) = 0.

# Exemplo:

f(x) = ex + x2 − 2

Temos: Df = R

f'(x) = ex + 2x > 0, ∀x ∈ (0, √2).

Como f(0) · f(√2) < 0 e f é contínua e f'(x) > 0 para todo x em (0, √2), segue que existe um único zero de f em (0, √2).

Lilian Berti

Zeros reais de Funções reais - Método da Bissecção

# Exemplo: Localize os zeros de f(x) = √x − 5e−x

Temos: Df = R+

| x | 0 | 1 | 2 |
| ---- | -- | ------- | ------ |
| f(x) | -5 | -0,8394 | 0,7375 |

Como f(1) · f(2) < 0, f' é contínua e f = 1 + 5e−x > 0, para todo x ∈ D, então f é estritamente crescente. Dessa forma, admite um único zero que pertence ao intervalo (1, 2).

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# Etapa 2: Refinamento da raiz

Uma sequência x0, x1, . . . , xk é gerada a partir do intervalo (a,b) obtido na Etapa 1.

# Critério de parada:

interrompe a sequência gerada pelo método. Avalia se xk está suficientemente próximo da raiz.

x̄ = xk é raiz aproximada com precisão se pelo menos um dos critérios:

- |xk − xk−1| ≤
- |xk − xk−1| ≤ |xk|
- |f(xk)| ≤

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# Método da Bissecção

Seja f(x) uma função contínua em (a, b) com f(a)f(b) < 0. Suponha que exista uma única raiz de f(x) = 0 em (a, b). O método consiste em reduzir a amplitude do intervalo que contém a raiz até atingir a precisão requerida |b − a| < ε. É utilizado a divisão sucessiva do intervalo ao meio.

Lilian Berti

Zeros reais de Funções reais - Método da Bissecção

Exemplo Seja f(x) = x3 − 9x + 3. Determine um zero de f sabendo que ele está contido no intervalo I = (0, 1). Utilize o método da bisseção com precisão = 0, 09.

# 1a iteração:

I = (0, 1)

x1 = a+b = 1 = 0, 5

2

f(0) = 3

f(0,5) = -1,375

f(1) = -5

Novo intervalo I = (0; 0, 5)

|b − a| = 0, 5 >

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# 2a iteração: I = (0; 0, 5)

x2 = a + b = 0,5 = 0, 25

| f(0) | > | 0 |
| ------- | - | ------ |
| f(0,25) | = | 0,7656 |
| f(0,5) | < | 0 |

Novo intervalo I = (0, 25; 0, 5)

|b − a| = 0, 25 >

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# 3a iteração: I = (0, 25; 0, 5)

x3 = a + b = 0, 375

| f(0,25) | > | 0 |
| -------- | - | ------- |
| f(0,375) | = | -0,3223 |
| f(0,5) | < | 0 |

Novo intervalo I = (0, 25; 0, 375)

|b − a| = 0, 125 >

Lilian Berti

Zeros reais de Funções reais - Método da Bissecção

# 4a iteração: I = (0, 25; 0, 375)

x4 = a + b = 0, 3125

| f(0,25) | > | 0 |
| --------- | - | ----- |
| f(0,3125) | = | 0,218 |
| f(0,375) | < | 0 |

Novo intervalo I = (0, 3125; 0, 375)

|b − a| = 0, 0625 &#x3C;

Portanto, x̄ = 0,3125 + 0,375

# Algoritmo: Método da Bissecção

Dados: f(x), a, b, N (número máximo de iterações)

1. Para i = 1, 2, . . . , N
2. x = (a + b)/2
3. Se f(a)f(x) &#x3C; 0 então
4. b = x
5. Caso contrário
6. a = x
7. Se |b − a| ≤
8. solução: x = (a + b)/2 Pare!

Lilian Berti

Zeros reais de Funções reais - Método da Bissecção

# Considerações sobre a convergência do método da Bissecção

Se f(x) é contínua no intervalo (a,b) e f(a)f(b) &#x3C; 0 o método da Bissecção gera uma sequência que converge para a raiz da equação f(x) = 0.

# Número de iterações

bk−ak = bk−1 − ak−1 = bk−2 − ak−2 = · · · = b0 − a0 = b − a

Devemos ter: |bk − ak| &#x3C; . Logo:

| 2 | 22 | 2k | | | | |
| --------- | --------------------- | ----------- |---|---|---|---|
| \|b − a\| | 2k | > \|b − a\| |
| | 2k | > \|b − a\| | | |
| k | > log \|b − a\| − log | | | |
| log 2 | | | | | | |

Lilian Berti Zeros reais de Funções reais - Método da Bissecção

# Ordem de convergência

Seja o erro da iteração k definido por ek = xk − x∗. Um crtitério para avaliar a convergência do método é:

lim k→+∞ |ek+1| = C ≥ 0

|ek|p

em que p ≥ 1 é a ordem de convergência do método gerador da sequência, C é a constante assintótica.

Assim, nas proximidades de x∗, temos:

|ek+1| ≈ C|ek|p.

Quanto maior o valor de p mais rápida a sequência convergirá para a raiz.

Lilian Berti

Zeros reais de Funções reais - método da Bissecção

Exemplo:

C=0,5 e e3 = 0, 012

para p = 1

e4 ≈ 0, 5(0, 012)1 = 0, 006

para p = 2

e4 ≈ 0, 5(0, 012)2 = 0, 000072

Lilian Berti

Zeros reais de Funções reais - Método da Bissecção

# Zeros reais de Funções reais - Método da Bissecção

No método da Bissecção, temos:

ek = bk − ak

ek+1 ≈ 1/2 ek

Assim, p = 1, o método converge linearmente.

Lilian Berti

# Considerações sobre o método da bissecção:

Uma dificuldade para aplicação do método é a sua inicialização;

As iterações envolvem cálculo simples, mas a sua convergência é lenta;

Caso o intervalo inicial b − a >> e for muito pequeno, o número de iterações pode ser grande.

Lilian Berti Zeros reais de Funções reais - Método da Bissecção