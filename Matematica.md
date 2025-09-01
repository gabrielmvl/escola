# Matematica - capitulo 6
# Poligonos e simetria: a base da progamação visual

## Poligonos

- **Linhas fechadas** formadas apenas por **segmentos de reta** que **não se cruzam** a não ser em suas **extremidades**.

### Poligonos regulares

- Poligonos regulares são aqueles que são convexos, possuem todos os lados congruentes e seus angulos internos são congruentes, ou seja, seus lados e angulos têm a mesma medida.

![regular](https://www.universoformulas.com/imagenes/matematicas/geometria/poligono-regular.jpg)

#### Poligono convexo

- é quando os angulos internos medem menos que 180ª graus.

![convexos.png](https://i.postimg.cc/hvGLSKZb/convexos.png)

### Poligonos irregulares

- Todos os polígonos que não são regulares.

![irregular](https://www.universoformulas.com/imagenes/matematicas/geometria/poligono-irregular.jpg)

### Classificação de poligonos

| Nº de lados | Nome             | Diagonais | Soma dos ângulos internos |
|-------------|------------------|-----------|---------------------------|
| 3           | Triângulo        | 0         | 180°                      |
| 4           | Quadrado         | 2         | 360°                      |
| 5           | Pentágono        | 5         | 540°                      |
| 6           | Hexágono         | 9         | 720°                      |
| 7           | Heptágono        | 14        | 900°                      |
| 8           | Octógono         | 20        | 1080°                     |
| 9           | Eneágono         | 27        | 1260°                     |
| 10          | Decágono         | 35        | 1440°                     |
| 11          | Unndecágono      | 44        | 1620°                     |
| 12          | Dodecágono       | 54        | 1800°                     |
| 15          | Pentadecágono    | 90        | 2340°                     |
| 20          | Icoságono        | 170       | 3240°                     |

### Cálculo de diagonais 

- $D =$ **Num_Diagonais**
- $n =$ **Num_Lados**

$D = \frac{n \times (n - 3)}{2}$

- [Calculadora](./Matematica.py)

### Cálculo da soma de ângulos internos

- $Si =$ **Soma dos ângulos internos**
- $n =$ **Num_Lados**

$Si = (n - 2) \times 180^\circ$

- [Calculadora](./Matematica.py)