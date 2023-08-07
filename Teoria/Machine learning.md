## Concept learning

Cosas importantes que necesita un modelo para aprender:
1. los datos y cómo se representan
2. un tipo de función que va a tratar de aprender y que los datos van a tratar de explicar (hipótesis, el conjunto de todas las funciones definidas que me sirven se llama espacio de hipótesis)
3. el tipo de búsqueda que voy a hacer
4. cómo evitar el problema del sobreajuste

*Concept learning*: métodos para inferir funciones booleanas; encontrar soluciones a problemas de qué es lo que define un concepto lógico. 

2. Representación de hipótesis:
- Conjuncion de restricciones sobre los atributos (problema EnjoySport) y FInd-S
- Version Spaces (Consistent hip, positivos Y negativos bien clasificados a la vez) |Consistent(h,D) = forall {x, c(x)} in D
                         h(x) = c(x)|
   and the Candidate-Elimination Algorithm
- Unbiased Learning (con Candidate-Elim): H = Partes(X) con disjunciones y negaciones para garantizar que la resp correcta esté en el espacio (S: {x1+ v x2+ v x3+}  G: {¬(x4- v x5-)})
  Para converger a un único final, cada instancia de X debe ser presentada!
  **Voting no sirve pq va a haber miti positivo miti neg -> no sirve => un modelo que no hace suposiciones (no tiene bias) sobre el concepto target, no tiene base racional para clasificar instancias nuevas. Así que hay que agregar bias/límites para generalizar y no memorizar.** 
-  Ver los demás de otros modelos más adelante

Si puedo explicar un montón de datos, asumo que esto generaliza.

Las búsquedas exhaustivas sobre las distintas posibles instancias no solo llevan un montón de tiempo, sino que también no se generaliza bien (generando sobreajuste) cuando se busca sobre todas las posibles soluciones (como se hace en el List-Then-Eliminate). -> Las soluciones en ML se basan hoy día en hacer **búsquedas ordenadas** (General-to-Specific Ordering hypotheses)

3. Búsqueda de hipotesis
Encontrar la hip especifica maximal (**Find-S algorithm**)
	1. Inicializar h igual a la hipotesis mas especifica del espacio H
	2. Para cada instancia de entramiento positiva *x*
		1. Si la restricción a_i es satisfecha por x, entonces do nothing, else reemplazar a_i en h por la restriccion mas general siguiente que es satisfecha por x
	3. Devolver la hip h
Con este algoritmo todo lo que podemos asegurar es que la hip clsifica como positivos a todos los ejemplos positivos y es lo más especifica posible. Tampoco podemos decir que es la mejor; no hay evidencia de que que sea más especifica sea mejor. Tampoco tenemos nada de evidencia sobre qué pasa con los negativos ya que no se los tuvo en cuenta para encontrar la hip.

**Representación compacta de Version Spaces: Candidate-Elimination Learning Algorithm** (mantener el espacio de soluciones por sus limites en vez de tener todas las soluciones a la vez; no como nros sino como su limite mas gral y su límite más específico)
- General Boundary y Specific Boundary
El algoritmo es muy parecido al Find-S, solo que va removiendo/agregando de G/S segun el ej sea positivo o negativo; si la hipotesis sigue siendo consistente no la toco, sino, si no clasifica bien al ejemplo la modifico para que si lo haga (a la S la generalizo lo menos posible y la G la especifico lo menos posible siempre respetando los ejemplos anteriores).

Si no hay datos incorrectos y si la resp correcta está dentro de nuestro espacio de búsqueda, hay garantías de que el método converja a la hip correcta.

El mejor ejemplo de entrenamiento a pedir es el que más información me da, es decir, el que elimina la mayor cantidad de hipotesis del espacio de hip.

Los conceptos parcialmente aprendidos son útiles para dar una respuesta para aprender. (Respuesta probabilística en Bayes por ej)


1) Espacio de hipótesis y búsqueda: Explique brevemente estos dos conceptos.
	Espacio de hipótesis: conjunto de todas las funciones válidas que puedan explicar los datos y estimar mi problema
	Tipo de búsqueda: manera de encontrar sobre el espacio de hipótesis la (mejor) solución
	
1) Explique la “futilidad del aprendizaje no sesgado” y d´e dos ejemplos de bias sobre los algoritmos vistos

	Si se trata de hacer un aprendizaje no sesgado, para garantizar la presencia de la respuesta correcta, todas las instancias de x deberían ser presentadas. De esta manera, si no se hace ninguna suposición no se puede llegar a una respuesta, ya que en el espacio hay un 50/50 y daría un "empate". Entonces, para generalizar y no memorizar, se deben hacer suposiciones/limites sobre el problema. Si no se hace un bias, el modelo no tiene base racional para estimar sobre instancias nuevas.
	Bias sobre algoritmos vistos:
	- Arboles: árboles cortos y con nodos con mucha ganancia de información cerca de la raíz
	- Redes: generaliza la interpolación suave entre data points

--------------------------------
## Árboles de decisión

- No se usan hoy en día por sí solos pero si como componente de otros métodos
- Se usan porque son métodos entendibles (por los humanos, se entiende fácil la idea del árbol) y no de caja negra

Es un método para aproximación de funciones con valores discretos (clasificación)

Cada nodo testea algún atributo de la instancia

**Representación de datos**: atributos lógicos con número discreto de valores

**Espacio de hipótesis**: cada DT representa una disjunción de conjunciones de restricciones sobre los atributos

- Los datos de train pueden contener errores o faltantes en campos

**Tipo de búsqueda en el espacio de hipótesis**:
Algoritmo:
- si la clase de los ejemplos que hay/quedan es p/todos la misma, devuelvo esa clase.
- si ya recorrí todos los atributos posibles al ir armando el árbol, devuelvo la clase más probable entre los ejemplos
- en otro caso, elijo el atributo que más ganancia de información (posibilidad de dividir lo más posible los ejemplos) me genere (greedy, lo que se busca es minimizar la entropía a la hora de elegir el atributo) y hago una rama por cada valor posible que pueda tomar este atributo (y divido los ejemplos restantes segun el valor que tengan en este atributo)
Notas:
- se usa el espacio de hipotesis completo
- se mantiene una única hipótesis mientras se busca en el espacio de los árboles
- no se hace backtracking durante la búsqueda, siempre pa delante
- se usa todos los ejemplos de entrenamiento disponibles en cada paso de la búsqueda (con toma de decisiones estadísticas)

Bias inductivo en DTL:
- Árboles cortos son preferidos sobre los grandes
- Árboles que colocan atributos con maxima information gain cerca de la raíz son preferentes.
- En C.4.5, además, se pide un mínimo de ganancia para seguir profundizando el árbol. Sino se llega se termina ahí.

ID3 busca de manera incompleta en un espacio completo (generaliza buscando de manera particular, (preference bias), A diferencia de Candidate-Elimination que busca de manera completa en un espacio de hipótesis reducido (language bias))

**Cómo evitar el sobreajuste**
El sobreajuste puede pasar por 
- un ejemplo ruidoso (valor de atributo o clase errónea), esto lleva a que se construyan más ramas en el árbol
- por tema de limitación del tamaño del sampleo, que no refleje la realidad del espacio de estudio

Contramedidas
- Dejar de alargar el árbol antes, "parada temprana", medidas:
	- Usar un set separado de ejemplos: ver si al agregar un nodo en cuestión me da mejor o peor sobre este conjunto
	- Usar test estadístico sobre el nodo que está construyendo para ver la probabilidad que el agregado mejore
- ir hasta el final y volver: post-prune el árbol

Pruning
- Reduced-Error pruning: una vez terminado el árbol, con un conjunto de validación (separado del de training) generado se va cortando ramas para ir mejorando la curva de error, hasta llegar al error óptimo. Si veo que la perfomance vuelve a empeorar, dejo de cortar. Esto con árboles no se hizo mucho porque es muy costoso generar un conjunto de validación.
- Rule Pos-pruning: se transforma al árbol en un conjunto de reglas, y luego se analiza una por una si me la quedo o no. (A diferencia del método anterior que borraba de a nodos enteros, acá se borra una única rama)

Mejoras del algoritmo C4.5 que usamos en la práctica:
- Incorpora atributos continuos: discretiza las variables continuas y las convierte en variables lógicas. T = 40 y T = 46 ==> T < 50
   Ordeno los valores continuos y voy realizando cortes en los puntos medios entre ellos y hago las variables lógicas candidatas T < d/2. Elijo el que me de mayor ganancia de información. Acá si se pueden volver a utilizar nuevamente los atributos más abajo en el árbol.
- Medidas alternativas para seleccionar atributos (para sacar el bias de elegir atributos con más valores posibles en problemas discretos): Gain Ratio
- Manejo de atributos faltantes: asume una respuesta estadística y sigue

1) Describa el espacio de hipótesis y el tipo de búsqueda del algoritmo ID3 (árboles de decisión) en el problema de las espirales anidadas
	El espacio de busqueda consiste en los DT, que representan una disjuncion de conjunciones de restricciones sobre los atributos. El tipo de búsqueda es la búsqueda greedy tratando de obtener la mayor ganancia de informacion en la eleccion del atributo de cada nodo, buscando en el espacio de hipotesis completo de esta forma particular.
2) Explique qu´e hace ´arboles de decisi´on en el caso de variables continuas.
	Las discretiza convirtiendolas en variables lógicas, probando cortes entre puntos medios de los puntos (ordenados previamente) y se fija el corte donde se obtiene mayor ganancia. 
3) Nombre al menos dos criterios con los cuales se detiene el crecimiento de un árbol de decisión durante el entrenamiento, o ajuste, del mismo.
	Durante el entrenamiento: detener el crecimiento antes de tiempo (utilizando fórmulas para analizar la ganancia de agregar un caso más al árbol)
	Post-entrenamiento: pruning (corte de ramas)

--------------------------------

## Evaluación de hipótesis

Dificultades principales cuando hay data limitada disponible: Bias y varianza(error) en el estimado

En general, se puede estimar el erro verdadero a partir de error muestral, sin bias y con una varianza que decrece con el tamaño de la muestra

Los datos para estimar el error deben ser independientes de los que se usaron para aprender, sino se tiene un bias y es sobreoptimista.

Si no tengo muchos datos disponibles (no como los que los sacan de internet):
Muy pocos ejemplos para entrenar => clasificador pobre (hay una relacion directa entre cant de ejemplos train y performance) pero buena medida de error (pero de algo malo)
Pocos ejemplos de test => crece la varianza en la estimacion porque al ser tan chiquito no es representativo de la población real

Resampling: 
- entreno varias veces al modelo con 70/20 y hago un promedio de la varianza. Después entreno el modelo final con todos los datos y hasta podría andar mejor (al entrenar con más datos), así que estimo de más, no de menos.
- Para que los conjuntos de test sean independientes (no haya overlap entre iteraciones), hay que hacer k-fold cross validation (idealmente manteniendo la proporcion original entre las clases en los folds). Mientras menos datos, más chiquito el fold de test (caso extremo: Leave-One-Out)




1) ¿Por que comparar el error de test entre dos algoritmos no alcanza para decir si uno es mejor que el otro?

	Evaluar a partir de una muestra puede llegar a uno a decir que un modelo es mucho mejor que el otro en esa muestra, aunque en realidad el otro modelo en principio estadísticamente sea mejor. 

   ¿Qu´e m´etodos podemos utilizar?
   - Statistical Significance Testing (mostrar que un modelo es consistentemente mejor que el otro): ver cuantas veces la diferencia entre las mediciones de ambos modelos(la media entre todos los ejemplos de testing), cuanto vale esa diferencia en unidades de su varianza. La idea es que de lejos de 0 (que la diferencia sea significativa), esto se hace para poder afirmar con más fuerza que los métodos son distintos. (Test de nula hipótesis: t-test)
	 
2) Discuta el problema que produce usar el error de clasificación “normal” (la proporción de puntos incorrectamente asignados) para evaluar un clasificador en un problema con dos clases muy desbalanceadas.

Si tenemos un problema de clasificación con dos clases muy desbalanceadas, por ej que el 90% de la muestra son positivos, puede pasar que probemos 2 modelos y que uno clasifique bien la totalidad de los positivos pero mal a todos los negativos (esto nos da un 90% de accuracy (10% error)) y otro que clasifique bien solo a una mayoría de los positivos, digamos el 80% pero bien a casi todos los negativos, digamos al 80% de ellos (esto nos da un 80% de accuracy, 20% de error). Esto nos podría llevar a pensar que el 1er modelo es mejor porque tiene menos error, pero esto no necesariamente es así, porque es un modelo que dice siempre que sí, no brinda información sobre los negativos. En vez el 2do modelo quizás sea mejor, ya que por más que tenga un poco menos de accuracy, reconoce (y bastante) a la parte negativa de la población.

Otro escenario es que podemos tener la situación de un clasificador que clasifique muy bien a los positivos y pobremente a los negativos, y viceversa. Si usamos el error normal (1 - accuracy), estos dos modelos tienen el mismo error. Ahora, todo depende del caso de estudio para saber si conviene o no usar la accuracy como medida. Si el problema es clasificar gatos negros de blancos, es lo mismo equivocarse con una u otra clasificación (problema simétrico, ambas clases valen igual). Ahora, si queremos usar el clasificador para detectar casos de alguna enfermedad, sería de mayor interés usar el clasificador que tiene una buena detección de positivos frente al otro que no.

En estos casos es mejor usar otras medidas de error, siempre depende del problema que se esté analizando.

--------------------------------

## ANN

Problemas apropiados para ANNs:
- Regresión y clasificación de multiclase
- Espacios con muchas dimensiones
- Train sets que puedan contener errores (ruido)
- Problemas con largos tiempos de entrenamiento
- Evaluación rápida de la función aprendida
- No es importante entender el mecanismo de decisión de la red, muy "oscuras" (en comparación a los DT)

Perceptrón (clasificación binaria)

**Representación de datos**: valores continuos en un espacio vectorial

**Hipotesis:** formula equivalente a un hiperplano: 
o(x) = sgn(w.x) siendo x y w vectores (w pesos que caracterizan a la neurona, perpendicular a la linea de separación (en 2 dim))


**Espacio de hipótesis:** Todos los hiperplanos

**Tipo de búsqueda:** un plano y un vector w / dejen de un lado del plano lo que vale 1 y del otro -1
Op. 1)
Arranco con un w random y lo voy corrigiendo iterativamente con cada patrón, según una regla (perceptron training rule) y un learning rate predeterminado (chiquito para que no se vaya para cualquier lado). 

*La regla converge a la solucion correcta, si existe la solucion correcta (es decir, si los datos son separables, (ej por una recta en 2 dim)). Si esto no pasa, no se puede asegurar el resultado que va a dar el modelo*

Op.2) Descenso por el gradiente (más automática)
o(x) = w.x (para que sea derivable le saco el sgn)
Arranco con un w random y lo voy corrigiendo, Defino una funcion de error que me diga cuan lejos estoy de que mi w actual haga que los positivos den 1 y los neg -1, y la minimizo usando descenso por el gradiente (moverme learn rate en contra del gradiente para ir del lado que decrece) para llegar a eso.

- Muy lento para converger
- Si la superficie tiene muchas irregularidades, tiende a quedarse atrapado entre mínimos locales en vez de seguir avanzando al mínimo de la función => solución: avanzar de a un patrón en vez de la suma

*En este caso, la regla converge solo asintóticamente hacia el minimo, pero sin importar que los datos sean linealmente separables*

**Poder representacional del perceptron**
- Todas las funciones booleanas primitivas
- No pueden representar al XOR. (No se puede tirar la recta). Pero uno de 2 capas sí (con una capa no linear en las capas ocultas).

**Multilayer networks**
Ahora en vez de usar la función sgn, usamos una función diferenciable (sigmoide).

Las neuronas están completamente conectadas con todas las del nivel superior.

BackPropagation algorithm (pasar info pa delante y errrores pa tras): análogo perceptrón descenso por el gradiente pero un caso por cada capa.
- Implementa una búsqueda de los pesos con una búsqueda de descenso por el gradiente
- Converge a mínimos local.
- Hay muchas soluciones buenas, lo difícil es no quedarse en una solución mala mucho tiempo.
Solución:
- Agregar Momentum al descenso por el gradiente
- Descenso por gradiente stocástico (mismo que para el perceptrón)
	- Batch: computar todos los deltas, actualizar pesos (normalito, se atasca en el min local)
	- Minibatch: agarro un subconjunto de los patrones, hago sus deltas y actualizo los pesos (solucion mejorcita e intermedia)
	- Stochastic: para cada patrón, computo delta y ya actualizo pesos (explora mucho el espacio al no usar el gradiente unificado, sino el de un solo patrón, pero eventualmente llega)
- Entrenar múltiples redes: como los entrenamientos son parcialmente randoms (pesos iniciales, descenso estocástico), podemos entrenar varias redes y nos quedamos con la mejor.

**Poder representativo:** todo. (con dos capas ocultas con sigmoides más una lineal de salida)

**Espacio de hipotesis:** espacio euclideo n-dimensional de los pesos de la red

**Inductive Bias**: nos permite generalizar la interpolación suave entre data points

En las capas ocultas se encodea la información y se descubren nuevas features no explicitas en la representación del input.

Lo que se pueda fittear está relacionado con la cantidad de neuronas de la capa intermedia.

Que la info vaya pa delante y los errores pa tras, promueve un diseño de lo simple a lo complejo, donde en las primeras capas hay cuestiones más primitivas, y las cosas más complejas se logran ver con más capas.

Generalizacion, Sobreajuste y criterio de parada

Inmensa capacidad de aprender => inmensa capacidad de sobreajustar y de aprender ruido

Solución: Para terminar la búsqueda de los pesos, se evalúa la capacidad de generalización con un conjunto que aparto del de entrenamiento (**validación hold-out**). 
¿Por qué no uso el error sobre los datos? Porque quiero generalizar, y el error sobre los datos tiene un bias porque lo uso para ajustar la red; con lo cual no es una medidad correcta de generalización, no puedo mirar el error sobre los mismos datos que estoy ajustando para saber si estoy haciendo sobreajuste o no; se necesita un conjunto independiente. 
Se va guardando la red que tiene menor error a lo largo de muchas epocas, y donde se obtuvo ahi me quedo. (El problema que puede haber es que la curva de validacion tenga forma de W y que el segundo minimo sea el global, y que ahi ya haya sobreajuste en el error de test y hubiese sido mejor quedarse en el 1ero aunque sea mayor)

Otro approach sin usar un conj de validacion es el del weight decay, que consiste en agregar un parámetro de penalización a la función de error que tenga que ver con la complejidad del método que estoy haciendo. (En árboles, cant nodos; en redes, como lo simple es lo inicial, y tiene pesos chiquitos, y lo complejo ya al final con pesos más grandes, esta penalización puede ser una suma de los pesos). De esta manera obtenemos iteraciones más suaves y al mismo tiempo una función de error menos compleja.

1) Al entrenar redes neuronales dividimos típicamente nuestros datos en 3 conjuntos: entrenamiento, validación y test. Explique para qué se usa cada uno.

Entrenamiento: patrones para ir entrenando la red y corrigiendo los pesos de la misma
Validación: conjunto que aparto del conjunto de entrenamiento inicial para controlar el sobreajuste de la red.
Test: conjunto de datos para ajustar la red

2) Explique c´omo se utiliza el Weight Decay en NN.
Para combatir el sobreajuste, el weight decay consiste en agregar un parámetro de penalización a la función de error que tenga que ver con la complejidad del método que estoy haciendo. (En árboles, cant nodos; en redes, como lo simple es lo inicial, y tiene pesos chiquitos, y lo complejo ya al final con pesos más grandes, esta penalización puede ser una suma de los pesos). De esta manera obtenemos iteraciones más suaves y al mismo tiempo una función de error menos compleja.
--------------------------------

## Bayes

Probabilistico: responde con probabilidades
No-proba: aprende reglas y responde una clase
Discriminativo: de aca para allá una clase, de acá para allá la otra
Generativos: trata de crear el modelo de dónde vienen los datos, y dice las probailidades de que un punto caiga en un modelo o en otro


![[classifiers.png]]
Clasificador Bayes
- Se asigna la clase de mayor probabilidad, garantizando el mínimo posible de errores. (MAP)
- Dado un punto,  cuál es la probabilidad de que ese punto haya sido generado por una clase.
- Este modelo generativo se construye dividiendo los datos de las N clases en N generadores, y cada generador construye un modelo de cuál es la probabilidad de haber generado ese punto x, dado que es de la clase.
- Cada generador va a saber generar una clase, va a saber cuáles son las reglas para que un punto haya sido de esta clase cuando se creó o leyó.
- Como MAP es difícil, primero se aplica la regla de Bayes para convertir las probabilidades del Generador en probabilidades a posteriori (prob de la clase dado el ejemplo que estoy leyendo) y ahí aplico MAP.
- El resultado de la inferencia de Bayes depende fuertemente de las probabilidades a priori, las cuales deben estar disponibles para poder aplicar el método y ser buenas. **Tengo que saber cuanta abundancia hay de cada clase.** (esto último aplica a todo MachineLearning)
- Para la clasificación de Bayes, se necesita estimar la probabilidad conjunta P(x1,...,xn | c), la cual es una probabilidad multidimensional en n dimensiones. Esta probabilidad también es muy difícil de conseguir porque aparece el problema de la dimensionalidad (el espacio se vacía en tantas dimensiones) y estimar probabilidades en tantas dimensiones es casi imposible o da muy feo salvo para muy pocas dim. ==> Solución: pasar a Naive Bayes

Naive Bayes
- Asume independencia entre las variables. Es burdo pero funciona bien muchas veces para clasificar. Con esto puedo calcular la prob como la multiplicacion de prob de cada una de las componentes por separado dado c.
- Aplica MAP
- Para sacar el riesgo de una Zero conditional probability, la idea es que esto sea algo muy chiquito en su lugar. Se le suma algo "virtual" para evitar esto pero que siga dando 1 la prob.

Naive Bayes para variables continuas

- La probabilidad condicional es modelada seguido con la distribución normal. Lo único que varía es la media y la varianza en cada variable.
  Se calcula la prob con la distribucion normal y MAP para asignar una etiqueta de clase.
- Otra opcion: discretizar las variables usando histogramas y usar el algoritmo de aprendizaje discreto. 

Problemas numericos: se agregan logaritmos para estabilizar con sumas de ellos en vez de multiplicar varios números con diferente precisión y así perder de manera notable ésta.


1) Describa dos diferencias importantes entre el Aprendizaje Bayesiano y los demás métodos que analizamos en el curso.
	- Bayes es probabilístico a diferencia de los otros métodos vistos: aprende y responde con probabilidades
	- Bayes es generativo a diferencia de los otros métodos vistos (que son discriminativos): trata de crear el modelo de dónde vienen los datos, y dice las probailidades de que un punto caiga en un modelo o en otro
2) ¿Por que no es pr´actico usar el algoritmo est´andar de Bayes?¿Qu´e se le quita para lograr el naive Bayes?¿Soluciona esto el problema?
Para la clasificación de Bayes, se necesita estimar la probabilidad conjunta P(x1,...,xn | c), la cual es una probabilidad multidimensional en n dimensiones. Esta probabilidad también es muy difícil de conseguir porque aparece el problema de la dimensionalidad (el espacio se vacía en tantas dimensiones) y estimar probabilidades en tantas dimensiones es casi imposible o da muy feo salvo para muy pocas dim. ==> Solución: pasar a Naive Bayes. Este asume independencia entre las variables. Es burdo pero funciona bien muchas veces para clasificar. Con esto puedo calcular la prob como la multiplicacion de prob de cada una de las componentes por separado dado c. Según entendí soluciona el problema :/
--------------------------------
## KNN
Lazy learning: guarda la data y pospone las decisiones hasta que una nueva consulta es presentada
Eager learning: generaliza más allá de la training data antes de que una nueva consulta sea presentada

- Instance-Based learning == lazy. A diferencia de los métodos que vimos hasta ahora, no hay espacio de hipotesis ni busqueda dentro de él, sino que aplazo el trabajo de aprender hasta el momento que me preguntan por un caso puntual. La hipotesis está "implicita".
- Son muy fáciles de construir pero cuando hay que dar una respuesta suele llevar un poco más de tiempo.
- Instancias: vector x \in R^n y d() == distancia euclideana (se puede hacer con variables concretas pero es más difícil, asi que por simplicidad nos quedamos en el espacio euclideo)
- Clases discretas
- Tipo de búsqueda para una solicitud de un patrón x:
	- busca los k-vecinos más cercanos a x
	- se hace una votación entre dichos vecinos y se queda con la clase mayoritaria. Si fuese un problema de regresión, podría quedarse con el promedio de los vecinos, por ej.
- Al ser local se puede eliminar mejor el ruido, ya que si hay un positivo en una zona llena de negativos, al promediar pasa a que no afecte tanto.
- "Espacio de hipotesis":  para el caso de un vecino, diagrama poligonos de Voronoi
- "Bias inductivo": asumo que mi espacio de clases/hipotesis es continuo localmente en las clases => Cerca de un punto, la clase tiene que ser la misma que la de ese punto. (esto se mantiene para k vecinos)
- Especialemente sensible al problema de la dimensionalidad o a atributos irrelevantes, ya que todos los atributos son considerados en distancias.
DNN

- Pesa más pesado a los vecinos más cercanos
- k  puede ser igual a «todos»

Regresión pesada localmente
- Pasamos del modelo que funciona para un punto, expandiendolo primero a otro que funcione en una zona, y luego a otro global pero basado en modelos locales que funcionan en pequeñas partes.
- Construye una aproximacion f(x) en la region local alrededor de x (ajuste usualmente lineal o cuadratico a las muestras cerca de x)
- A partir de f(x), se construye una funcion de error y se busca optimizar los coeficientes (como en redes neuronales)
- Para ajustar mejor a los puntos cerca de la zona que nos interesa, se usa la función Kernel K()

Funciones de base radial

- Hibrido entre regresion pesada por distancia y redes neuronales
- La función de kernel ahora es una gaussiana centrada en puntos arbitrarios que voy a ir ajustando con mis datos (a diferencia del modelo anterior que K está centrada en puntos de la muestra)
![[funciones_radiales.png]]

- Se ajustan los centros de las gaussianas y los sigmas para que cubran bien los datos (algoritmo EM)
- Determina los pesos (problema lineal)
- Más simple que el descenso por el gradiente

Extreme Learning Machines
- Muy fácil de usar
- Basado en principios erróneos
- Se toman de manera random los centros y no se los ajusta, solo se ve que caigan dentro de la zona donde están los datos

- Los métodos lazy pueden considerar al patrón x cuando deciden cómo generalizar más allá de la training data (aproximación local)
- Los métodos eager no pueden (ya eligieron su aproximación global a la target function)

1) Vimos en el curso que usando un número mayor de vecinos podemos lograr que el clasificador de k-vecinos funcione bien en problemas ruidosos, como son los datos “diagonal” y “paralelo”. Cuál es el problema que impide que pase lo mismo con el dataset de “espirales con ruido”?
Para el caso de KNN con ruido en espirales, al estar entremezclados los puntos de cada clase (distinto de una clara separación mayoritaria de diagonal y paralelo) genera que los puntos cercanos puedan ser bastante equitativos en cada clase y por ende generar resultados bastante malos
2) Explique en qu´e casos es conveniente usar KNN y en cu´ales DNN.
**KNN (K-Nearest Neighbors):**

- Conveniente para problemas de clasificación o regresión con estructura no lineal.
- Útil cuando el número de atributos es bajo (baja dimensionalidad).
- No asigna pesos a los vecinos cercanos, todos tienen la misma influencia en la predicción.

**Distance-Weighted KNN:**

- Conveniente cuando se desea dar más importancia a los vecinos más cercanos.
- Útil en conjuntos de datos pequeños, ya que puede mejorar la precisión al tener en cuenta la estructura local de los datos.
- Menos sensible a outliers ya que otorga mayor peso a los vecinos cercanos.


--------------------------------------
Deep learning

- Al tener mayor cantidad de datos y capacidad para poder procesarlos, comparados con las redes de antes en estas se procesa mucha más info.
- Se usa una función de error más apropiada, Cross Entropy. En vez de medir que tan lejos está de 1/-1, dice cuál es la probabilidad de que esté bien clasificado el ejemplo.
- Redes convolucionales: *muchas más capas* pero menos pesos, esto la simplifica y hace que generalice mejor. *Siempre de lo simple a lo complejo, cada capa cumple una responsabilidad particular*
- Funciones parcialmente rectas en vez de sigmoideas (más simple y generaliza mejor)
- Dropouts para generalizar mejor: se desconectan neuronas al azar y eso generaliza mejor que que estén totalmente conectadas.
- Modelo que puede usar datos secuenciales (palabras en una oracion) => redes neuronales recurrentes
- Redes neuronales + imagenes = redes neuronales convolucionales

Redes convolucionales
- El algoritmo de entrenamiento es análogo al de ANN (BackPropagation)
- La conectividad no es completa. Cada neurona está conectada solo con *una parte* de sus neuronas predecesoras, y eso tiene que ver con una localidad. Ventajas:
	- Localidad: entender qué hay en una imagen depende del lugar en que se concentra la atención y la relación entre estas partes (partes de la cara de un perro por ej)
	- Reduce el sobreajuste: al tener menos pesos ajustables, se reduce la posibilidad de aprender particularidades.
- Los pesos son compartidos, a diferencia de ANN que eran todos individuales. Se aplica la misma transformación (filtro) de a grupos de neuronas de una capa a otra (el filtro se va desplazando). Ventajas:
	- Invariancia traslacional: la visión responde igual en cualquier lugar, una cara es una cara en cualquier lugar de la imagen.

Cuando no se puede aplicar la transformación porque una zona queda afuera y quiero utilizar dichos bordes ==> Padding
Padding: rellenar los bordes con algo fijo de manera que se pueda convolucionar también el borde exterior de una imagen (normalmente 0)

Stride: mide qué tanta localidad uso, es el número de unidades que el kernel es trasladado por pasada en las filas/columnas.

Una capa convolucional transforma el volumen:
Input 32x32x3 => 5 filtros conv => output: 32x32x5

Pooling: capa para reducir el volumen de la información que pasa de capa en capa (para que no explote); toma una simplificación (usualmente se queda con el valor maximo, MaxPooling) de la zona que ve que es de interés

Al final del modelo, se ponen capas densas que serían las fully connected, son un multilayer perceptron como los que ya vimos

Softmax: una neurona para cada una de las clases

Entrenamiento con backpropagation:
- Derivacion automática (predefinada a la hora de definir el gradiente)
- Acá si o si hay learning rate adaptativos
- Minibatch 
- Unidades Relu para mantener el gradiente (_/ en vez sigmoideas)

Regularización: dos nuevos tipos
- Dropout: se desconectan neuronas al azar y eso generaliza mejor que que estén totalmente conectadas.
- Data augmentation: le realizo operaciones a la data existente (flip, contrast) para aumentar la independencia espacial y contextual; así aprende la característica más importante de la imagen y no alguna particularidad

Transfer learning: reusar la red una vez que es buena haciendo algo. 
- Si tengo que resolver otro problema pero similar al original (de reducción de escala por ej), en vez de ajustar la red al problema, ajusto mi problema a la red (esto por los días/meses que lleva entrenar).
- Si quiero aprender categorías que no están ahí o particularidades finas, se puede adaptar la red al final, es decir; usar las primeras partes de la red (el detector, entrenado con las super bases de datos) y después entrenar la otra parte de la red para adaptarlo a mi problema. 