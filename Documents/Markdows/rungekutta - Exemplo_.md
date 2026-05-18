# Exemplo - Método de Runge Kutta

# Lilian Berti

# Métodos Numéricos

# Lilian Berti

# Exemplo - Método de Runge Kutta

# Método de Runge Kutta

não é necessário o cálculo de derivadas múltiplas avaliações de f

Lilian Berti

# Exemplo - Método de Runge Kutta

# Runge Kutta de 1a ordem

Método de Euler

yi+1 = yi + hf(xi, yi)

para i = 0, 1, · · · , N − 1.

# Runge Kutta de 2a ordem

Método de Euler Modificado (Método do ponto médio)

yˆi+₁ = yi + h f( xi, yi )

yi+1 = yi + hf(xi + h, yˆi+₁)

Lilian Berti

Exemplo - Método de Runge Kutta

# Método de Euler Aperfeiçoado

yi+1 = yi + h f( xi, yi )

yi+1 = yi + h [f(xi, yi) + f(xi+1, yi+1)]

# Lilian Berti

# Exemplo - Método de Runge Kutta

# Runge Kutta de 4aordem (clássico)

yi+1 = yi + h (K1 + 2k2 + 2k3 + k4)

6

em que

k1 = f(xi, yi)

k2 = f(xi + h , yi + h k1)

2

k3 = f(xi + h , yi + h k2)

2

k4 = f(xi + h, yi + hk3)

Lilian Berti

# Exemplo - Método de Runge Kutta

# Exemplo: Suponha que a densidade populacional p de lagartas

seja descrita pelo PVI

dp = rp 1 − k − p² 2
dt p 1 + p
p(0) = p₀

em que p₀ é a população inicial (no instante t = 0), r está relacionado à taxa de reprodução da lagarta e k à quantidade de folhas disponíveis na planta. O termo p² 2 descreve a predação da lagarta (por pássaros, por exemplo).

Considerando r = 3, k = 1 e p₀ = 0, 1, qual será a população de lagartas no instante t = 10?

Lilian Berti

# Exemplo - Método de Runge Kutta

# Temos:

dp = 3p(1 − p) − p2 2

dt

p(0) = 0, 1

Utilizar um método numérico para estimar p para 0 ≤ t ≤ 10.

# Lilian Berti

# Exemplo - Método de Runge Kutta

# Usando o método de Euler com valores diferentes de h:

| 1.0 | n |
| --- | ---- |
| 0.8 | |
| 0.6 | |
| y | |
| 0.4 | 0.25 |
| 0.2 | 0.5 |
| 0.0 | |

| | 0 | 2 | 4 | 6 | 8 | 10 |
| - | - | - | - | - | - | -- |
| | | X | | | | |

# Lilian Berti

# Exemplo - Método de Runge Kutta

# Aproximações para p(10):

| h | 2 | 1 | 0,5 | 0,25 |
| ----- | ---------- | ------- | ------- | ------- |
| y(10) | 1,07 × 105 | 0,91505 | 0,83597 | 0,83597 |

# Observações:

Para valores de h ≥ 1 o método é instável. Resultados semelhantes foram obtidos considerando h = 0, 5 e h = 0, 25.

Lilian Berti Exemplo - Método de Runge Kutta

# Usando o método de Euler Aperfeiçoado com valores diferentes de h:

| | 1.0 | 0.8 | 0.6 | 0.4 | 0.25 | 0.2 | 0.5 | 1.0 | 2.0 | 0.0 |
| - | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| x | 0 | 2 | 4 | 6 | 8 | 10 | | | | |

# Lilian Berti

# Exemplo - Método de Runge Kutta

# Aproximações para p(10):

| h | 2 | 1 | 0,5 | 0,25 |
| ----- | ----------- | ------- | ------- | ------- |
| y(10) | −1,8 × 1016 | 0,44578 | 0,83597 | 0,83597 |

# Observações:

Para valores de h ≥ 1 o método é instável. Resultados semelhantes foram obtidos considerando h = 0,5 e h = 0,25. Assim, acreditamos que com h = 0,5 é suficiente para ter uma boa aproximação. Necessitando assim de apenas 20 iterações.

Lilian Berti

Exemplo - Método de Runge Kutta

# Usando o método Runge Kutta de 4ª ordem, com valores diferentes de h:

| 1.0 | 0.8 | 0.6 | y | 0.4 | | |
| --- | ---- | --- | --- | --- | - | -- |
| | 0.25 | | 0.5 | | | |
| | 1.0 | | 2.0 | | | |
| 0.0 | 0 | 2 | 4 | 6 | 8 | 10 |

Lilian Berti

Exemplo - Método de Runge Kutta

# Aproximações para p(10):

| h | 2 | 1 | 0,5 | 0,25 |
| ----- | ------------- | ------- | ------- | ------- |
| y(10) | −8,35 × 10284 | 0,82311 | 0,83597 | 0,83597 |

# Observações:

Para valores de h ≥ 1, temos um erro bem significativo. Resultados semelhantes foram obtidos considerando h = 0, 5 e h = 0, 25.

# Lilian Berti

# Exemplo - Método de Runge Kutta

Exemplo: A reação qu´ımica na qual duas moléculas de dicromato de potássio sólido (K2Cr2O7), duas moléculas de água (H2O) e três átomos de enxofre sólido (S) são combinados para produzir três moléculas de dióxido de enxofre (SO2), quatro moléculas de hidróxido de potássio sólido (KOH) e duas moléculas de óxido crômico sólido (Cr2O3) pode ser representada simbolicamente pela equação estequiométrica:

2K2Cr2O7 + 2H2O + 3S → 4KOH + 2Cr2O3 + 3SO2

Se n1 moléculas de K2Cr2O7, n2 moléculas de H2O e n3 moléculas de S estão originalmente dispon´ıveis, a seguinte equação diferencial descreve a quantidade x(t) de KOH depois de um tempo t:

dx = k n1 − x2 n2 − x2 n3 − 3x3

dt

em que k é a constante de velocidade da reação. Se k = 6, 22 × 10−19, n1 = n2 = 2 × 103 e n3 = 3 × 103, use o método de Runge- Kutta de quarta ordem para determinar quantas unidades de hidróxido de potássio terão sido formado após 0,2 s.

Lilian Berti

Exemplo - Método de Runge Kutta

# Exemplo - Método de Runge Kutta

Temos:

| dx | = | 6, 22×10−19 | 2 × 103 − x2 | 2 × 103 − x2 | 3 × 103 − 3x3 | |
| -- | - | ----------- | ------------ | ------------ | ------------- | - |
| dt | | 2 | | 2 | | 4 |

x(0) = 0

Lilian Berti

# Exemplo - Método de Runge Kutta

Usando o método de Runge Kutta de quarta - ordem com h = 0, 01, obtemos x(0, 2) ≈ 2099 unidades.

| | 0 | 0.025 | 0.100 | 0.200 |
| - | ---- | ----- | ----- | ----- |
| y | 2500 | 2000 | 1500 | 1000 |
| | 500 | 0 | | |

# Exemplo

Um circuito elétrico consiste em um capacitor, de capacitância constante C = 1,1 farads, em série com um resistor de resistência constante R0 = 2,1 ohms. Uma tensão ε(t) = 110 é aplicada a partir do instante t = 0. Quando o resistor esquenta, a resistência se torna uma função da corrente i,

R(t) = R0 + ki, em que k = 0,9,

e a equação diferencial para i(t) se torna

1 + 2k i di + 1C i = 1C dε .

R0 dt R0 R0 dt

Encontre i(2), supondo i(0) = 0.

Lilian Berti

Exemplo - Método de Runge Kutta

Temos:

1 + 2 · 0, 9 i di + 1 i = 1 · 110 cos t

2, 1 dt 2, 1 · 1, 1 2, 1 · 1, 1

Logo,

(1 + 0, 8571i) di + 0, 4329i = 47, 6190 cos t

dt

(1 + 0, 8571i) di = 47, 6190 cos t − 0, 4329i

dt

di = 47, 6190 cos t − 0, 4329i

dt 1 + 0, 8571i

Lilian Berti Exemplo - Método de Runge Kutta

# Exemplo - Método de Runge Kutta

Usando o método de Runge Kutta de quarta - ordem com h = 0, 1, obtemos i(2) ≈ 8, 2572.

| Rk4 | | | | | | | | |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| | 8 | 6 | y | | | | | |
| 4 | 2 | 0 | | | | | | |
| 0.00 | 0.25 | 0.50 | 0.75 | 1.00 | 1.25 | 1.50 | 1.75 | 2.00 |

x