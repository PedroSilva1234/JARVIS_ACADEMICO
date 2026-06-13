# Estudo do erro na interpolação polinomial

# Lilian Berti

# Métodos Numéricos

# Estudo do erro na interpolação polinomial

# Lilian Berti

# Lembrando da Série de Taylor em torno de x0

f(x) = f(x0) + f'(x0)(x − x0) +
f''(x0) (x − x0)2 +
\(\frac{f^{(n)}(x0)(x − x0)n}{n!}\) +
\(\frac{f^{(n+1)}(c)(x − x0)n+1}{(n + 1)!}\)

# O polinômio interpolador na forma de Newton:

pn(x) = f(x0) + (x − x0)f[x0, x1] +
(x − x0)(x − x1)f[x0, x1, x2] +
\(\cdots\) + (x − x0)(x − x1) · · · (x − xn−1)f[x0, x1, x2, . . . , xn]

é parecido com a estrutura da expansão em série de Taylor no sentido de que os termos adicionados sequencialmente para capturar o comportamento de ordem superior da função subjacente. Esses termos são diferenças divididas finitas e, portanto, representam aproximações de derivadas de ordem superior.

Lilian Berti Estudo do erro na interpolação polinomial

# Estudo do erro na interpolação polinomial

Como no caso da série de Taylor, pode ser obtida uma formulação para o erro do trucamento. Na série de Taylor o erro é:

E = fn+1(ξ)(xi+1 − xi)n+1 em que ξ ∈ (xi, xi+1).

(n + 1)!

# Teorema

Sejam x0 < x1 < x2 < · · · < xn (n+1) pontos distintos e f(x) com derivadas até a ordem (n+1) para todo x pertencente ao intervalo [x0, xn]. Seja pn(x) o polinômio interpolador de f(x) nos pontos x0, x1, · · · , xn. Então qualquer x em [x0, xn] o erro é dado por:

E(x) = f(x) − pn(x) = (x − x0)(x − x1) · · · (x − xn) fn+1(ξ) / (n + 1)!

em que ξ ∈ (x0, xn).

Observação: A importância do teorema é mais teórica do que prática, visto que não conseguimos o ponto ξ de modo que seja válida a igualdade.

Lilian Berti Estudo do erro na interpolação polinomial

# Limitante para o erro

Sob as hipóteses do teorema acima, temos:

|(x − x )(x − x ) · · · (x − x )|

|E(x)| = |f(x) − p(x)| ≤ 0 (n 11)! n max |f(ⁿ+1)(x)|

+ x∈[x0,xn]

Lilian Berti Estudo do erro na interpolação polinomial

# Exemplo

Considere a tabela:

| x | 0,5 | 0,9 | 1,1 | 1,6 | 2,0 |
| ---- | ------ | ------ | ------ | ------ | ------ |
| f(x) | 0,1276 | 0,4316 | 0,6636 | 1,5308 | 2,5839 |

em que f(x) = cos (x) + x2 − 1. Calcule o limitante superior para o erro quando avaliamos f(1, 4) usando um polinômio de interpolação de grau 2.

Lilian Berti Estudo do erro na interpolação polinomial

# Temos:

|(x − x0)(x − x1)(x − x2)|

E(x) ≤ (2 + 1)! max |f (x)|

x∈[x0,x2]

f(x) = cos x + x2 − 1

f (x) = −sen x + 2x

f (x) = − cos x + 2

f (x) = sen x

Como queremos estimar f(1, 4) usando o polinômio de grau 2, tomando os três pontos consecutivos na vizinhança de 1,4:

x0 = 0, 9, x1 = 1, 1 e x2 = 1, 6.

Então: |f ( )| |f ( π )| π

max x = 2 = sen 2 = 1.

x∈[x0,x2]

Logo,

|E(1, 4)| ≤ |(1, 4 − 0, 9)(1, 4 − 1, 1)(1, 4 − 1, 6)| ≈ 0, 005.

6

Lilian Berti Estudo do erro na interpolação polinomial

# Agora, vamos utilizar o polinômio interpolador na forma de Newton.

# Tabela das diferenças divididas.

| x | ordem 0 | ordem 1 | ordem 2 | |
| --- | ------- | ------- | ------- | ------ |
| 0,9 | 0,4316 | | 1,16 | |
| 1,1 | 0,6636 | 0,8206 | | 1,7344 |
| 1,6 | 1,5308 | | | |

p2(x) = f[x0] + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2]

p2(x) = 0, 4316 + (x − 0, 9)1, 16 + (x − 0, 9)(x − 1, 1)0, 8206

p2(1, 4) = 1, 1347

Dessa forma:

|E(1, 4)| = |f(1, 4) − p(1, 4)| = |1, 13 − 1, 1347| = 0, 0047.

Lilian Berti Estudo do erro na interpolação polinomial

Agora, tomando x0 = 1, 1, x1 = 1, 6 e x2 = 2, 0

|E(1, 4)| ≤ |(1, 4 − 1, 1)(1, 4 − 1, 6)(1, 4 − 2)| · |f ( π )| ≈ 0, 006

Lilian Berti Estudo do erro na interpolação polinomial

# Observação

Pelo teorema:

E(x) = f(x) − pn (x) = (x − x0)(x − x1) · · · (x − xn ) fn+1(ξ) / (n + 1)!

Se a função f(x) é dada na forma de tabela, o valor E(x) não pode ser calculado, pois não é possível calcular fn+1(x).

Usando as diferenças divididas finitas para aproximar a (n + 1) derivada, temos:

E(x) = (x − x0)(x − x1) · · · (x − xn )f[x0, x1, x2, · · · , xn , x]

Lilian Berti Estudo do erro na interpolação polinomial

# Estimativa para o erro

Se a função f(x) é dada na forma de tabela, o valor E(x) não pode ser estimado, pois não é possível calcular fn+1(x) ou mesmo f[x0, x1, · · · , xn, x]. Entretanto, se estiver disponível um ponto adicional f(xn+1) podemos estimar o erro por:

E(x) ≈ (x − x0)(x − x1) · · · (x − xn) · f[x0, x1, · · · , xn, xn+1]

Obs: Escolhemos como ponto adicional xn+1 como o mais próximo do valor x a ser estimado.

Lilian Berti Estudo do erro na interpolação polinomial

# Exemplo Anterior

Considere a tabela:

| x | 0,5 | 0,9 | 1,1 | 1,6 | 2,0 |
| ---- | ------ | ------ | ------ | ------ | ------ |
| f(x) | 0,1276 | 0,4316 | 0,6636 | 1,5308 | 2,5839 |

em que f(x) = cos (x) + x2 − 1. Calcule uma estimativa para o erro quando avaliamos f(1, 4) usando um polinômio de interpolação de grau 2.

Lilian Berti Estudo do erro na interpolação polinomial

Tabela das Diferenças Divididas

| x | ordem 0 | ordem 1 | ordem 2 | ordem 3 | |
| --- | ------- | ------- | ------- | ------- | ------ |
| 0,9 | 0,4316 | | 1,16 | | |
| 1,1 | 0,6636 | 0,8206 | | 1,7344 | 0,1615 |
| 1,6 | 1,5308 | 0,9982 | | 2,6328 | |
| 2,0 | 2,5839 | | | | |

Interpolamos em x0 = 0, 9, x1 = 1, 1 e x2 = 1, 6, para estimar o valor de f(1, 4), obtemos:

p2(1, 4) = 1, 1347

|E(1, 4)| = |f(1, 4) − p(1, 4)| = |1, 13 − 1, 1347| = 0, 0047.

Pela fórmula da estimativa do erro, escolhendo x3 = 2 como ponto adicional, visto que está mais próximo de x = 1, 4, temos:

|E(x)| ≈ |(x − x0)(x − x1)(x − x2)| · f[x0, x1, x2, 2]

|E(1, 4)| ≈ |(1, 4 − 0, 9)(1, 4 − 1, 1)(1, 4 − 1, 6)| · 0, 1615 ≈ 0, 0048

Lilian Berti Estudo do erro na interpolação polinomial

# Exemplo:

Considere a tabela:

| x | 0,2 | 0,34 | 0,4 | 0,52 | 0,6 | 0,72 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| f(x) | 0,16 | 0,22 | 0,27 | 0,29 | 0,32 | 0,37 |

a) Obter f(0, 5) usando um polinômio de interpolação de grau 2.

b) Dê uma estimativa para o erro.

Lilian Berti Estudo do erro na interpolação polinomial

Interpolando em x0 = 0,4, x1 = 0,52, x2 = 0,6. E o ponto adicional x3 = 0,34 para a estimativa do erro.

# Tabela das Diferenças Divididas

| x | ordem 0 | ordem 1 | ordem 2 | ordem 3 | |
| ---- | ------- | ------- | ------- | ------- | ------- |
| 0,34 | 0,22 | | 0,8333 | | |
| 0,4 | 0,27 | -3,7033 | | 0,1667 | 18,2494 |
| 0,52 | 0,29 | 1,0415 | | 0,375 | |
| 0,6 | 0,32 | | | | |

# a)

p2(x) = f[x0] + (x − x0)f[x0, x1] + (x − x0)(x − x1)f[x0, x1, x2]

p2(x) = 0,27 + (x − 0,4)0,1667 + (x − 0,4)(x − 0,52)1,0415

p2(0,5) = 0,2846 ≈ f(0,5)

# b)

|E(x)| ≈ |(x − x0)(x − x1)(x − x2)| · |f[x0, x1, x2, 0,34]|

|E(0,5)| ≈ |(0,5 − 0,4)(0,5 − 0,52)(0,5 − 0,6)||18,2494| = 0,0036

Lilian Berti Estudo do erro na interpolação polinomial

# Escolha do Grau do Polinômio Interpolador

O polinômio de grau n aproximará bem a função se as diferenças divididas de ordem n são praticamente constantes ou se as diferenças divididas de ordem n + 1 são próximas de zero.

# Lilian Berti

Estudo do erro na interpolação polinomial

# Exemplo

Considere a função f(x) = √x cuja tabela das diferenças divididas é:

| x | ordem 0 | ordem 1 | ordem 2 |
| ---- | ------- | ------- | ------- |
| 1 | 1 | | 0,5 |
| 1,01 | 1,005 | 0 | 0,5 |
| 1,02 | 1,01 | -0,5 | 0,49 |
| 1,03 | 1,0149 | 0 | 0,49 |
| 1,04 | 1,0198 | 0 | 0,49 |
| 1,05 | 1,0247 | | |

Dessa forma, dizemos que um polinômio de grau 1 fornece uma boa aproximação para f(x) = √x em [1; 1, 05].

Lilian Berti Estudo do erro na interpolação polinomial

# Interpolação Inversa

Dada a tabela:

| x | 0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 |
| ---- | - | ------ | ------ | ------ | ------ | ------ |
| f(x) | 1 | 1,1052 | 1,2214 | 1,3499 | 1,4918 | 1,6487 |

Obter x tal que y = f(x) = 1,3165 usando uma interpolação quadrática. Dê uma estimativa para o erro.

# Lilian Berti

# Estudo do erro na interpolação polinomial

# Fazendo a interpolação quadrática com y0 = 1, 2214, y1 = 1, 3499 e y2 = 1, 4918.

# Tabela das diferenças divididas:

| y | ordem 0 | ordem 1 | ordem 2 | ordem 3 |
| ------ | ------- | ------- | ------- | ------- |
| 1,1052 | 0,1 | | | |
| | | 0,8606 | | |
| 1,2214 | 0,2 | -0,3367 | | |
| | | 0,7782 | 0,1679 | |
| 1,3499 | 0,3 | -0,2718 | | |
| | | 0,7047 | | |
| 1,4918 | 0,4 | | | |

p(y) = g(y0) + (y − y0)g[y0, y1] + (y − y0)(y − y1)g[y0, y1, y2]

p(y) = 0, 2 + (y − 1, 2214)0, 7782 + (y − 1, 2214)(y − 1, 3499)(−0, 2718)

p(1, 3165) = 0, 2749 ≈ x

Lilian Berti Estudo do erro na interpolação polinomial

# Lilian Berti

# Estudo do erro na interpolação polinomial

|E(y)| ≈ |(y − y₀)(y − y₁)(y − y₂)|g[y₀, y₁, y₂, 1, 1052]

|E(1, 3165)| ≈ |(1, 3165 − 1, 2214)(1, 3165 − 1, 3499)(1, 3165 − 1, 4918)| · 0, 1679

≈ 0, 0001