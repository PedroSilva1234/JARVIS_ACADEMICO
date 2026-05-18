UFMS - Universidade Federal de Mato Grosso do Sul
# Métodos Numéricos

# 3a Lista de Exercícios

# Sistemas não-lineares

# 1.

Considere o sistema não-linear:

x12 + x22 - 1 = 0

x1 + x2 = 0

1. Localize graficamente as soluções do sistema não linear.
2. Obtenha uma solução através do Método de Newton escolhendo como chute inicial [1, -1]T e com erro relativo inferior a 0,09.
3. Obtenha uma solução através do Método de Newton Modificado utilizando a mesma aproximação inicial e critério de parada do item anterior.

# 2.

Realize duas iterações do método de Newton na resolução do sistema não linear abaixo:

x12 + x22 = 2

ex1 - x2 = 2

x(0) = [1.5, 2.0]T

# 3.

Considere o sistema não linear abaixo:

ex1 - 1 = 0

ex2 - 1 = 0

A solução deste sistema é: x* = [0, 0]T.

1. Verifique que a matriz Jacobiana é não singular (matriz invertível) em x*.
2. Realize uma iteração do Método de Newton aplicado a este sistema, usando x(0) = [-10, -10]T. Analise o resultado obtido e justifique o que acontece. Sugestão: analise a matriz Jacobiana. (Utilize 6 casas decimais).

# 4.

Se aplicarmos o método de Newton para sistemas não lineares, para resolver um sistema linear, Ax = b, A : n × n, x, b ∈ Rn, quantas iterações o método irá realizar? Justifique.

# 5.

Seja f(x1, x2) = 5x2 - 5x1x2 + 2, 5x2 - x1 - 1, 5x2. Calcule os valores de x1 e x2 que minimizam f(x1, x2), utilizando o método iterativo de Newton. Para aproximação inicial use [1, 1]T e critério de parada F(xk) ∞ &#x3C; 10-6 ou no máximo duas iterações. Comente os resultados.

# 6.

A concentração de um poluente num lago depende do tempo t e é dado por:

C(t) = 70eβt + 20eωt.

Sabendo que: C(1) = 27,5702 e C(2) = 17,6567. Utilize o método de Newton para determinar β e ω. Considere para aproximação inicial o ponto β, ω = [-1, 9, -0, 15]T, realize uma iteração e apresente o erro relativo.





# 7.

Para combater um vírus que infectou um grupo de indivíduos vai ser administrado um composto químico sintetizado com base em duas substâncias elementares x1 e x2. Sabe-se que se forem administrados a α miligramas de composto a cada indivíduo, a concentração (mg/litro) de cada uma das substâncias elementares na circulação sanguínea é dada implicitamente (para α ∈ [0, 5]) pelo sistema de equações:

16x1 − cos(α(x2 − 2x1)) = 0

16x2 + 0,75sen(α(−x2 − 3x1)) = 0

Para α = 1, determine x1 e x2 usando um método iterativo mais adequado. Use a aproximação inicial x(0) = [0, 1 0, 01]T e termine o processo iterativo considerando o erro absoluto menor que ε = 0, 05.

# 8.

Dado o sistema não linear:

3x1 − cos(x2x3) = 1

4x2 − 625x2 + 2x2 = 1

e−x1x2 + 20x3 = − 10π−3

Determine o sistema linear (J(xk)d = −F(xk)) que deve ser resolvido em cada iteração do Método de Newton para encontrar a solução deste sistema.

# Respostas

1. (b) x = x(2) = [0, 7083 0, 7084]T (c) x = x(2) = [0, 7188 0, 7187]T
2. x = x(2) = [0, 8901 1, 1456]T
3. (a) verifique que o determinante da matriz é diferente de zero.

(b) x(1) = [22211, 2222 22211, 2222]T. A próxima aproximação estará distante da solução exata, isto ocorre devido que a matriz jacobiana no ponto inicial é praticamente singular.
4.
5. x = x(1) = [0, 5 0, 8]T
6. β ≈ −1, 9987 e ω ≈ −0, 9987. ER = 0, 0494
7. x1 ≈ 0, 0623 e x2 ≈ 0, 0092 (1 iteração) EA = 0, 0377

3x1 − cos(x2x3) − 1

3x3sen(x2x3) x2sen(x2x3)

F(x) = 4x2 − 625x2 + 2x2 − 1

J(x) = 8x1 − 1250x2 + 2 0

e−x1x2 + 20x3 + 10π−3

−x2e−x1x2 −x1e−x1x2 20