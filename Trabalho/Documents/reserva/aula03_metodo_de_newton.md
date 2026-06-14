
# Zeros reais de Funções reais - Método de Newton

# Lilian Berti

# Métodos Numéricos

# Zeros reais de Funções reais - Método de Newton

# Lilian Berti

# Métodos Numéricos



# Método de Newton (ou Método de Newton-Raphson)

Este método combina duas ideias comuns nas aproximações numéricas: linearização e iteração.

f(x) ↑

f(x0)

Raiz

f(x1)

f(x2)        x0     >

x

Dada uma aproximação inicial x0, temos:

tgα = f(x0) = f'(x0)

x0−x1

x0 − x1 = f(x0) ⇒ x1 = x0 −      f(x0)

f'(x0)             f(x0)

f(x1) = f'(x1) ⇒ x2 = x1 −   f(x1)

x1−x2                        f'(x1)

Lilian Berti      Zeros reais de Funções reais - Método de Newton




# Zeros reais de Funções reais - Método de Newton

De modo geral:

xk+1 = xk − f(xk)

f (xk)

para k = 0, 1, . . . , e f (xk) = 0.

Lilian Berti






# Exemplo:

Encontre um zero de f(x) = x3 − 9x + 3, pelo método de Newton utilizando x0 = 0,5 e com critério de parada xk+1 − xk ≤ 0,09

# Fórmula do Método de Newton:

xk+1 = xk − f(xk) para k = 0, 1, . . . .

Temos: f(x) = x3 − 9x + 3 e f'(x) = 3x2 − 9.

# Iterações:

# Para k = 0

f(x0) = (−1,375)

x1 = x0 − f(0) = 0,5 − (−8,25) = 0,3333

ER = x1 − x0 = 0,3333 − 0,5 = 0,5002 > x1

# Para k = 1

f(x1) = 0,0373

x2 = x1 − f(1) = 0,3333 − (−8,6667) = 0,3376

ER = x2 − x1 = 0,3376 − 0,3333 = 0,0127 &#x3C; x2

Portanto, um zero de f(x) é x̄ = x2 = 0,3376.

Lilian Berti  Zeros reais de Funções reais - Método de Newton





# Teorema de Taylor

Se a função f e suas primeiras n + 1 derivadas forem contínuas em um intervalo contendo a e x, então o valor da função em x é dado por:

f(x) = f(a) + f'(a)(x − a) + f''(a)(x − a)2 + · · · + f(n)(a)(x − a)n + f(n+1)(c)(x − a)n+1




# Pela expansão em Taylor de f(x) em torno de xk

f(x) ≈ f(xk) + f'(xk)(x − xk)

f(xk+1) ≈ f(xk) + f'(xk)(xk+1 − xk)

Na intersecção com o eixo x, f(xk+1) deveria ser zero, ou

f(xk) + f'(xk)(xk+1 − xk) = 0

que pode ser escrita como

xk+1 − xk = − f(xk) / f'(xk)

ou seja

xk+1 = xk − f(xk) / f'(xk)

Lilian Berti

# Zeros reais de Funções reais - Método de Newton





Portanto, o método de Newton consiste em avançar da aproximação xk para a aproximação xk+1, usando a fórmula

xk+1 = xk − f(xk) / f'(xk)

para k = 0, 1, . . . ,

O processo é repetido até que o critério de parada seja satisfeito.

# Lilian Berti

# Zeros reais de Funções reais - Método de Newton




# Algoritmo:

1. Dados x0, f(x), f'(x), e N.
2. Para k = 0, 1, . . . , N faça
3. xk+1 = xk − f(xk)
4. Se xk+1 − xk f(xk) &#x3C; e então
5. - x̄ = xk+1 Pare!

Fim se
6. Se k = N então
7. - ’O método não converge para a solução.’ Pare!

Fim se
8. Fim para

Lilian Berti Zeros reais de Funções reais - Método de Newton





# Convergência do método de Newton

Temos:   ∗             ∗  f(x )

xk+1 − x = xk − x − f ( k )

Logo,         − f(xk)

ek+1 = ek     f (xk).

# Expandindo f(x) em torno de xk

f(x) = f(xk) + f'(xk)(x − xk) + f''(γ) (x − xk)2 para γ ∈ (x, xk)

Dessa forma,

0 = f(x*) = f(xk) + f'(xk)(x* − xk) + f''(γ) (x* − xk)2

f(xk) = f'(xk)(xk − x*) + f''(γ) (xk − x*)2

f(xk) = f'(xk)ek + f''(γ) ek2

então, ek+1 = ek −             (   ) 2  k       ⇒  ek+1 = − f''(γ)ek

f'(xk)                 2f (xk)

Lilian Berti  Zeros reais de Funções reais - Método de Newton



Supondo a convergência, xk e c acabariam aproximados pela raiz x*, então

f (x*) e2

ek+1 = − ------------------

2f (x*)

|ek+1| =  − f (x*) |e2| = C |ek|2

Portanto, M´etodo de Newton tem convergência quadr´atica (p=2). Isto significa que nas proximidades da raiz o n´umero de d´ıgitos corretos dobra a cada itera¸c˜ao.

Lilian Berti  Zeros reais de Fun¸c˜oes reais - M´etodo de Newton




# Exemplo:

Determine a raiz positiva de f(x) = x10 − 1, tomando aproximação inicial x0 = 0, 5.

Temos: f (x) = 10x9

Para k = 0

x1 = x0 − f(x0) = 0, 5 − (−0,999) = 51, 73

f (x0) 0,0195

A aproximação se afastou da solução!

Lilian Berti Zeros reais de Funções reais - Método de Newton





# Zeros reais de Funções reais - Método de Newton

# Observações:

Se x0 não for uma aproximação razoável o que fazer?

Aplicar um método menos restritivo para iniciar.

Derivada quase nula

A reta tangente é praticamente paralela ao eixo horizontal, fazendo que sua intersecção com o eixo acontecerá muito distante. Dessa forma, pode ir para outra raiz ou mesmo divergir.

Lilian Berti




N˜ao existe um crit´erio de convergência geral para o m´etodo de Newton. Sua convergência depende da natureza da fun¸c˜ao e da precis˜ao da aproxima¸c˜ao inicial. ´ E bom ter uma aproxima¸c˜ao inicial “suficientemente” pr´oxima da raiz. E para algumas fun¸c˜oes n˜ao funcionar´a.

# Lilian Berti

# Zeros reais de Fun¸c˜oes reais - M´etodo de Newton





Exemplo:

Uma gamela de comprimento L tem se¸c˜ao transversal semicircular com raio r. Quando a gamela est´a cheia com ´agua at´e uma distancia h do topo, o volume V de ´agua ´e

V = L   0, 5πr2 − r2arcsen  h − h(r2 − h2) 1 .

2

r

Suponha que L = 10, r = 1 p´e e V = 12, 4 p´es3. Determine da profundidade da ´agua na gamela com precis˜ao de 0, 01 p´e.

Lilian Berti  Zeros reais de Fun¸c˜oes reais - M´etodo de Newton




Vimos que ao substituir os dados, temos a equação:

10 0, 5π − arcsen (h) − h(1 − h2) 1 − 12, 4 = 0

2

Seja f(h) = 0, 5π − arcsen (h) − h(1 − h2) 1 − 1, 24.

2

Temos:

−2(1 − h2)

f (h) = √₁ − h2

Vimos que, f admite um zero no intervalo (0,1), tomando x0 = 0.5 como aproximação inicial para o Método de Newton.

Lilian Berti

# Zeros reais de Funções reais - Método de Newton





# Método de Newton usando x0 = 0, 5 e ER &#x3C; 0, 01

# Para k = 0

| f(x)           | (−0,6258)                |
| -------------- | ------------------------ |
| x1 = x0 − f(0) | 0,5 − (−1,7351) = 0,1387 |
| ER             | x1 − x0 = 2,6049 >       |

# Para k = 1

| f(x)           | 0,0543                      |
| -------------- | --------------------------- |
| x2 = x1 − f(1) | 0,1387 − (−1,9807) = 0,1661 |
| ER             | x2 − x1 = 0,1649 >          |

# Para k = 2

| f(x)           | 0,0001                      |
| -------------- | --------------------------- |
| x3 = x2 − f(2) | 0,1661 − (−1,9722) = 0,1662 |
| ER             | x3 − x2 = 0,0006 <          |

x̄ = 0,1662

Portanto, h ≈ 0,1662.

Lilian Berti  Zeros reais de Funções reais - Método de Newton



Exemplo: Seja

C(x) = 10 − 20(e−0,2x − e−0,75x)

a equação que pode ser usada para calcular o nível de concentração de oxigênio C em um rio, em função da distância x, medida a partir do local de descarga de poluentes. Calcule a distância para a qual o nível de oxigênio seja 5. Utilize x0 = 1 e realize três iterações do método de Newton.

Lilian Berti  Zeros reais de Funções reais - Método de Newton