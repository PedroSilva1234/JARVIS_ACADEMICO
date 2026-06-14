# Aritmética de ponto flutuante

# Lilian Berti

# Métodos Numéricos

# Lilian Berti

# Aritmética de ponto flutuante

# Aritmética de ponto flutuante

Exemplo: Calcule a área de uma circunferência em que o raio é 100m.

A = πr2 = 3, 14 · 1002 = 31.400m2

(ou A = 3, 1416 · 1002 = 31.416m2

ou A = 31.415, 9265m2)

Como justificar as diferenças entre os resultados? É possível obter o valor exato desta área?

Lilian Berti Aritmética de ponto flutuante

# Aritmética de ponto flutuante

Um número real tem a seguinte forma geral de representação:

±0, d1d2 · · · dt × βE

em que: di são os dígitos da parte fracionária, 0 ≤ di ≤ β − 1, i = 1, · · · , t, β é o valor da base, t é os dígitos da mantissa e E é o expoente inteiro (l ≤ E ≤ u). Se d1 = 0 diz-se que o número está normalizado.

Notação: F(β, t, l, u)

# Exemplos

1) Representação de π = 3, 141592653 · · ·

a) F(10, 3, −2, 2)

π = 0, 314 × 101

Lilian Berti Aritmética de ponto flutuante

# 2) Considere o sistema F(10, 3, −4, 4)

| x | Representação |
| ---------- | ------------------------------ |
| -279 | −0, 279 × 103 |
| 1,25 | 0, 125 × 101 |
| 0,0123 | 0, 123 × 10−1 |
| -0,0000052 | −0, 52 × 10−6 (erro underflow) |
| 123456 | 0, 123 × 106 (erro overflow) |

Lilian Berti Aritmética de ponto flutuante

3) Qual o maior e o menor valor em módulo representado no sistema F(10, 3, −4, 4) ?

menor: m = 0, 100 × 10−4 = 10−5 = 0, 00001

Maior: M = 0, 999 × 104 = 9990

Lilian Berti Aritmética de ponto flutuante

Considere x = 0, d1d2d3 . . . dt dt+1 . . .

# Aproximação com t dígitos por arredondamento:

Se dt+1 < 5 ⇒ x = 0, d1d2d3 . . . dt

Se dt+1 ≥ 5 ⇒ x = 0, d1d2d3 . . . (dt + 1)

# Exemplo:

Seja F(10, 3, −4, 4)

| √ | Arredondamento |
| ----- | ----------------- |
| 2 | 1, 41421356 . . . |
| e | 2, 71828182 . . . |
| 100,5 | 0, 101 × 103 |

Lilian Berti Aritmética de ponto flutuante

# Operações em aritmética de ponto flutuante com três dígitos significativos e arrendondamento

1. (11,4 + 3,18) + 5,05 = 14,6 + 5,05 = 19,7
2. 11,4 + (3,18 + 5,05) = 11,4 + 8,23 = 19,6
3. 3,18 × 11,4 = 36,3 = 7,19

5,05
4. 3,¹⁸ × 11,4 = 0,63 × 11,4 = 7,18

5,05
5. 3,18 × (5,05 + 11,4) = 3,18 × 16,5 = 52,5
6. 3,18 × 5,05 + 3,18 × 11,4 = 16,1 + 36,3 = 52,4

OBS: As operações aritméticas são associativas e distributivas

Lilian Berti Aritmética de ponto flutuante

# Erros:

Sejam x um número exato e x̄ uma aproximação para x.

# Erro absoluto:

E(¯) = |x̄ - x|

# Erro relativo:

E(¯) = |x̄ - x| / |x|, x ≠ 0

Lilian Berti Aritmética de ponto flutuante

Exemplos:

1. x = 1 e x̄ = 1, 373

E (x̄)     | − |

A x     = 1     1, 373 = 0, 373

E (x̄)     |1 − 1, 373|

R x = 1     = 0, 373
2. x = 3876 e x̄ = 3876, 373

E (x̄)     | − |

A x = 3876     3876, 373 = 0, 373

E (x̄)     |3876 − 3876, 373|

R x = |3876|     = 0, 000096

Lilian Berti Aritmética de ponto flutuante

# Exemplo:

Considere o sistema de ponto flutuante com cinco dígitos significativos. Seja x = 49213 + 31,728 − 49244. Temos:

# Valor Exato:

x = 0,728

# Valor aproximado:

| x | − | − |
| ------------------ | ----- | ------- |
| ¯ = 49213 + 31,728 | 49244 | = 49245 |
| 49244 | = 1 | |

E (¯) Rx = 0,728 − 1 = 0,37363

Note que, o erro relativo na adição inicial é:

ER = 49244,728 − 49245 = 5,5243 × 10−6

49244,728

Os dígitos perdidos na adição passa a ser importante na subtração.

Lilian Berti Aritmética de ponto flutuante