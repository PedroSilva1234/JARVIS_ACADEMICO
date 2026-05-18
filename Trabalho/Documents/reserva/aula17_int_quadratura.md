
Integra¸c˜ao Num´erica - Quadratura Gaussiana

# M´etodos Num´ericos

# Lilian Berti

# Integra¸c˜ao Num´erica - Quadratura Gaussiana



# Definição:

O grau de precisão de uma fórmula de integração é o maior inteiro positivo η de modo que a fórmula é exata para a integração de xk, para k = 0, 1, 2, · · · , η.

O grau de precisão das fórmulas de Newton - Cotes são baseadas em um polinômio de grau n é η = n se η é ímpar e η = n + 1 se n é par.

# Regra do Trapézio:

η = 1

# Regra 1/3 e 3/8 de Simpson:

η = 3

Lilian Berti Integração Numérica - Quadratura Gaussiana



# Exemplo: Calcule (x³ + x) dx

# (a) Usando a Regra 1/3 de Simpson (n=2)

h = b−a = 3−0 = 1,5

| n    |    |       | 2  |
| ---- | -- | ----- | -- |
| x    | x0 | x1    | x2 |
|      | 0  | 1,5   | 3  |
| f(x) | 0  | 4,875 | 30 |

I ≈ h [f(x0) + 4f(x1) + f(x2)] = 24, 75

# (b) Usando a Regra 3/8 de Simpson (n=3)

h = b−a = 3−0 = 1

| n    | 3 |    |    |    |    |
| ---- | - | -- | -- | -- | -- |
|      | x | x0 | x1 | x2 | x3 |
|      | 0 | 1  | 2  | 3  |    |
| f(x) | 0 | 2  | 10 | 30 |    |

I ≈ 3h [f(x0) + 3f(x1) + 3f(x2) + f(x3)] = 24, 75

Lilian Berti Integra¸c˜ao Num´erica - Quadratura Gaussiana



# c) Solução analítica

3(x3 + x) dx =




# Integra¸c˜ao Num´erica - Quadratura Gaussiana

Vimos que a integra¸c˜ao num´erica tem como forma geral:

b
I =  f(x) dx ≈ A0f(x0) + A1f(x1) + · · · + An f(xn ) = IA
a

As f´ormulas de Newton-Cotes escolhe Ak tomando pontos igualmente espa¸cados a = x0 &#x3C; x1 &#x3C; · · · &#x3C; xn = b.





# Quadratura Gaussiana

Escolhe Ak e xk para que IA seja exata para polinômios de grau até 2n + 1.

1. Para simplicidade o intervalo de integração é alterado de [a,b] para [-1,1] obtido pela mudança de variável x para t.
x = 1 (b − a)t + 1 (b + a) =⇒ dx = 1 (b − a)dt.

Logo,

I =  b f(x) dx =  1 f  1 (b − a)t + 1 (b + a)     1 (b − a) dt =  1 F(t)dt ≈

a            −1   2    2                     2               −1

F(t)

n

AiF(ti).

i=0

Lilian Berti  Integração Numérica - Quadratura Gaussiana




# 2) Fixa um n´umero n (inteiro) tal que se f(x) for um polinˆomio de grau at´e 2n + 1 a solu¸c˜ao exata.

Caso n = 1

| b   | 1         |          |                    |
| --- | --------- | -------- | ------------------ |
| I = | f(x) dx = | F(t)dt = | A₀F(t₀) + A₁F(t₁). |
| a   | −1        |          |                    |

Determinamos A₀, A₁, t₀ e t₁, de modo que seja exata para polinˆomios de grau at´e 3.

Devemos ter:

|   | 1  |   | 1dt = A₀ + A₁ |
| - | -- | - | ------------- |
|   | −1 |   |               |

|   | 1  |   | tdt = A₀t₀ + A₁t₁ |
| - | -- | - | ----------------- |
|   | −1 |   |                   |

|   | 1  |   | t²dt = A₀t² + A₁t² |
| - | -- | - | ------------------ |
|   | 0  |   | 1                  |
|   | −1 |   |                    |

|   | 1  |   | t³dt = A₀t³ + A₁t³ |
| - | -- | - | ------------------ |
|   | 0  |   | 1                  |
|   | −1 |   |                    |

Lilian Berti Integra¸c˜ao Num´erica - Quadratura Gaussiana






# Integração Numérica - Quadratura Gaussiana

obtemos o sistema não linear:

| A₀ + A₁     | = 2   |
| ----------- | ----- |
| A₀t₀ + A₁t₁ | = 0   |
| A₀t² + A₁t² | = 2/3 |
| 0           | 1     |
| A₀t³ + A₁t³ | = 0   |
| 0           | 1     |

cuja solução é: A₀ = A₁ = 1, t₀ = −√3 e t₁ = √₃.






Portanto,

I ≈ F  − √3  + F  √₃ ,

3          3

sendo que para polinˆomios at´e grau 3, a solu¸c˜ao ´e exata.

Caso n = 2, as opera¸c˜oes s˜ao realizadas de modo an´alogo, obtendo a f´ormula:

I =  1 F(t) dt ≈ 5 F  − 3    + 8 F (0) + 5 F     3  .

−1    9            5    9  9                5

Lilian Berti  Integra¸c˜ao Num´erica - Quadratura Gaussiana






# Fatores de peso e Argumento da função na Fórmula da Quadratura para diversos pontos

| Pontos | Fatores de peso | Argumento da função |
| ------ | --------------- | ------------------- |
| 2      | A0 = 1          | t0 = −0, 577350269  |
|        | A1 = 1          | t1 = 0, 577350269   |
| 3      | A0 = 0, 5555556 | t0 = −0, 774596669  |
|        | A1 = 0, 8888889 | t1 = 0              |
|        | A2 = 0, 5555556 | t2 = 0, 774596669   |
| 4      | A0 = 0, 3478548 | t0 = −0, 861136312  |
|        | A1 = 0, 6521452 | t1 = −0, 339981044  |
|        | A2 = 0, 6521452 | t2 = 0, 339981044   |
|        | A3 = 0, 3478548 | t3 = 0, 861136312   |
| 5      | A0 = 0, 2369269 | t0 = −0, 906179846  |
|        | A1 = 0, 4786287 | t1 = −0, 538469310  |
|        | A2 = 0, 5688889 | t2 = 0              |
|        | A3 = 0, 4786287 | t3 = 0, 538469310   |
|        | A4 = 0, 2369269 | t4 = 0, 906179846   |
| 6      | A0 = 0, 1713245 | t0 = −0, 932469514  |
|        | A1 = 0, 3607616 | t1 = −0, 661209386  |
|        | A2 = 0, 4679139 | t2 = −0, 238619186  |
|        | A3 = 0, 4679139 | t3 = 0, 238619186   |
|        | A4 = 0, 3607616 | t4 = 0, 661209386   |
|        | A5 = 0, 1713245 | t5 = 0, 932469514   |

Lilian Berti Integração Numérica - Quadratura Gaussiana






# Exemplo:

Seja I =     1,5

x = (b − a)t + (b + a) = 0, 5t + 2, 5 = 0, 25t + 1, 25 ⇒ dx = 0, 25dt

Logo,

I =         2

= (0, 25t + 1, 25)² ln (0, 25t + 1, 25) 0, 25dt

=         −1

= F(t)dt

≈ F−1 − √3 + F √₃ = 0, 1923

Lilian Berti Integra¸c˜ao Num´erica - Quadratura Gaussiana






# Exemplo:

Seja I = ∫04 e3x sen(2x)dx. Calcule I utilizando a quadratura gaussiana com dois pontos.

Temos:

x = (b − a)t + (b + a) = (π/4)t + (π/4) = πt + π ⇒ dx = π dt

Logo,

I = ∫-11 e3(πt+π) sen(2πt + π) π dt

≈ F-1 − √3 + F√₃ = 0, 2106 + 2, 3808 = 2, 5914

Lilian Berti Integração Numérica - Quadratura Gaussiana






# Exemplo:

Seja I =  1∫0 e−x² dx. Calcule I utilizando:

# (a) quadratura gaussiana com dois pontos

Temos:

x = (b − a)t + (b + a) = t + 1 ⇒ dx = 1 dt

Logo,

I = 1∫0 e−x dx = −1∫2 e−t + 1 2 dt

= 1∫1 F(t) dt

≈ F−1(−√3) + F(√₃) = 0, 7466

Lilian Berti  Integração Numérica - Quadratura Gaussiana





# (b) quadratura gaussiana com três pontos

I =  1 e−x² dx ≈ 5 F−3 + 8 F0 + 5 F3 = 0, 7468

Pelo software I=0,746824, pela regra 1/3 de simpson I ≈ 0, 7452

Lilian Berti  Integração Numérica - Quadratura Gaussiana




# Exemplo:

A quantidade de massa que pode ser transportada por um tubo durante um período de tempo pode ser calculada por:

M = ∫t1t2 Q(t)c(t) dt

em que M é massa (mg), t1 é o instante inicial (min), t2 é o instante final (min), Q(t) é a vazão (m3/min) e c(t) é a concentração (mg/m3). As seguintes representações funcionais definem a variação temporal da vazão e da concentração:

Q(t) = 9 + 5 cos2(0, 4t)

c(t) = 5e-0,5t + 2e0,15t

Determine a massa transportada entre t1 = 2 e t2 = 8 min utilizando a Quadratura Gaussiana em dois e três pontos.

Lilian Berti

Integração Numérica - Quadratura Gaussiana






# Temos:

M = 8(9 + 5 cos2(0, 4t))(5e−0,5t + 2e0,15t) dt

t = (b − a)u + (b + a) = 6u + 10 = 3u + 5 ⇒ dt = 3du

Logo:

M = 1 (9 + 5 cos2(0, 4(3u + 5)))(5e−0,5(3u+5) + 2e0,15(3u+5))3du

= F(u)du

Usando a Quadratura Gaussiana em dois pontos:

M ≈ F−√3 + F√₃ = 340, 67

Usando a Quadratura Gaussiana em três pontos:

M ≈ 5 F−3 + 8 F(0) + 5 F3 = 335, 66

Lilian Berti Integração Numérica - Quadratura Gaussiana






Exemplo: O valor médio de uma corrente elétrica oscilante em um período pode ser zero. Por exemplo, suponha que a corrente seja descrita por uma única função senoidal: *i(t) = sen(2πt/T), em que T* é o período. O valor médio dessa função pode ser determinado pela seguinte equação:

*i = (1/T) ∫0T sen(2πt/T) dt = (1/T) [-cos(2π) + cos(0)]*

i = 0

Apesar de o resultado médio ser zero, tal corrente é capaz de realizar trabalho e produzir calor. Portanto, os engenheiros eletricistas, em geral, caracterizam corrente por:

*IRMS = (1/T) ∫0T i²(t) dt*

em que *i(t) é a corrente instantânea. Calcule a corrente eficaz ou RMS da onda com a forma dada abaixo para T = 1 s*.

Para *0 ≤ t ≤ T/2, i(t) = 10e-t/Tsen(2πt)*

Para *T/2 &#x3C; t ≤ T, i(t) = 0.*

Lilian Berti

Integração Numérica - Quadratura Gaussiana






# A determinação da corrente eficaz envolve o cálculo da integral

I = 1/2(10e−tsen(2πt))2 dt

Resolvendo pela Quadratura Gaussiana, fazendo a mudança de variável.

t = (b − a)u + (b + a) = 0, 5u + 0, 5 = 0, 25u + 0, 25 ⇒ dt = 0, 25du

Logo:

I = 1 2 (10e−(0,25u + 0,25)sen(2π(0,25u + 0,25)))2 0,25du

Usando a Quadratura Gaussiana em dois pontos:

I ≈ F−√3 + F√3 = 11,9978

Usando a Quadratura Gaussiana em três pontos:

I ≈ 5 F−3 + 8 F(0) + 5 F3 = 15,6576

Lilian Berti Integração Numérica - Quadratura Gaussiana





# Usando a Quadratura Gaussiana com diversos pontos.

| Pontos | Estimativa I |
| ------ | ------------ |
| 2      | 11,99782     |
| 3      | 15,65755     |
| 4      | 15,40580     |
| 5      | 15,41263     |
| 6      | 15,41261     |

Lilian Berti  Integra¸c˜ao Num´erica - Quadratura Gaussiana



# Usando as Regras do Trapézio e Regra 1/3 de Simpson para determinar I.

| Regra                | subintervalos | Estimativa I |
| -------------------- | ------------- | ------------ |
| Regra do Trapézio    | 2             | 15,16327     |
|                      | 4             | 15,40143     |
|                      | 8             | 15,41196     |
|                      | 16            | 15,41257     |
|                      | 32            | 15,41261     |
|                      | 64            | 15,41261     |
|                      | 128           | 15,41261     |
| Regra 1/3 de Simpson | 2             | 20,21769     |
|                      | 4             | 15,48082     |
|                      | 8             | 15,41547     |
|                      | 16            | 15,41277     |
|                      | 32            | 15,41261     |

Lilian Berti Integração Numérica - Quadratura Gaussiana



# Comparando:

| **Fórmulas de Newton-Cotes**            | **Quadratura Gaussiana**                    |
| --------------------------------------- | ------------------------------------------- |
| pontos igualmente espaçados em \[a, b]; | pontos não igualmente espaçados em \[a, b]; |
| exatas para polinômios até grau n;      | exatas para polinômios até grau 2n + 1;     |
| aplicável a dados tabelados.            | aplicável quando f é disponível.            |

Lilian Berti

Integração Numérica - Quadratura Gaussiana