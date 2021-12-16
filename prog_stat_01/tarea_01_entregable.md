# Tarea 1

<div style="text-align: right"> Lluna Sanz Montrull </div>
<div style="text-align: right"> Master en Data Analytics para la Empresa </div>
<div style="text-align: right"> EDEM - 2021 </div>

## Datos utilizados

Se ha hecho uso del conjunto de datos [Customer_transaction_dataset](https://www.kaggle.com/archit9406/customer-transaction-dataset), concretamente, de la hoja "Transactions".
- Se ha creado la columna prod_per_customer que representa la cantidad de productos adquiridos, en total, por un cliente determinado.
- Se han rellenado los valores perdidos numéricos mediante interpolación y se han eliminado los valores NaN categóricos (para dichos valores, se podría considerar recoger los datos perdidos, sustituirlos por el valor más común de la columna o deducir su posible valor mediante un clasificador).
- Se ha comprobado que *transaction_id* tiene la misma cantidad de elementos únicos que la longitud de su columna, desvelando que los clientes han comprado un único producto por pedido.

### Tabla y tipos de datos

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>transaction_id</th>
      <th>product_id</th>
      <th>customer_id</th>
      <th>transaction_date</th>
      <th>online_order</th>
      <th>order_status</th>
      <th>brand</th>
      <th>product_line</th>
      <th>product_class</th>
      <th>product_size</th>
      <th>list_price</th>
      <th>standard_cost</th>
      <th>product_first_sold_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>2950</td>
      <td>2017-02-25</td>
      <td>0.0</td>
      <td>Approved</td>
      <td>Solex</td>
      <td>Standard</td>
      <td>medium</td>
      <td>medium</td>
      <td>71.49</td>
      <td>53.62</td>
      <td>41245.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>3120</td>
      <td>2017-05-21</td>
      <td>1.0</td>
      <td>Approved</td>
      <td>Trek Bicycles</td>
      <td>Standard</td>
      <td>medium</td>
      <td>large</td>
      <td>2091.47</td>
      <td>388.92</td>
      <td>41701.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>37</td>
      <td>402</td>
      <td>2017-10-16</td>
      <td>0.0</td>
      <td>Approved</td>
      <td>OHM Cycles</td>
      <td>Standard</td>
      <td>low</td>
      <td>medium</td>
      <td>1793.43</td>
      <td>248.82</td>
      <td>36361.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>88</td>
      <td>3135</td>
      <td>2017-08-31</td>
      <td>0.0</td>
      <td>Approved</td>
      <td>Norco Bicycles</td>
      <td>Standard</td>
      <td>medium</td>
      <td>medium</td>
      <td>1198.46</td>
      <td>381.10</td>
      <td>36145.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>78</td>
      <td>787</td>
      <td>2017-10-01</td>
      <td>1.0</td>
      <td>Approved</td>
      <td>Giant Bicycles</td>
      <td>Standard</td>
      <td>medium</td>
      <td>large</td>
      <td>1765.30</td>
      <td>709.48</td>
      <td>42226.0</td>
    </tr>
  </tbody>
</table>
<p>19445 rows × 13 columns</p>
</div>


## Estudio de variables

### list_price
Es la variable **cuantitativa** que hace referencia al precio del producto adquirido. Ésta se comprende en un rango de entre 12.01 y 2091.47.

count | mean | std | min | 25% | 50% | 75% | max |
:----:|:------------:|:--------:|:-----:|:------:|:-------:|:-------:|:-------:|
19445 | 1107.337193  | 582.6624 | 12.01 | 575.27 | 1163.89 | 1635.30 | 2091.47 |

#### Precio por clase de producto

A continuación, se muestra la distribución del precio del conjunto de datos. Nótese que la distribución del precio tiene tres máximos. En los siguientes gráficos, se observan distintas componentes, basadas en las clases de producto (product_class), que componen la distribución del precio.

Price             |  Price by product class
:-------------------------:|:-------------------------:
![](images/ax_00.svg)  |  ![](images/ax_01.svg)

De la misma manera, se ha extraído las distintas componentes relacionadas con el tamaño del producto (product_size) de los elementos anteriores. También se observa que ninguna componente sigue una distribución normal, además de que no componen 3 grupos distinguidos.

Realizando un test de las medias de precio de producto por clase, se obtiene el siguiente resultado:
- Estadístico: 180.00865523079634
- p-valor: 3.4533480856070333e-78

![](images/ax_06.svg)

#### Precio por clase de producto y tamaño

##### Productos de la misma clase con distinto tamaño

- **Clase baja**
- Estadístico: 5.718485684777187
- p-valor: 1.1841388434092325e-08


- **Clase mediana**
- Estadístico: 1605.0992524574058
- p-valor: 0.0


- **Clase alta**
- Estadístico: 434.1296627906751
- p-valor: 5.528692640792395e-166


##### p-valor de productos del mismo tamaño con distinta clase

- **Pequeños**
- Estadístico: 369.6347230319062
- p-valor: 4.800140843515247e-143


- **Medianos**
- Estadístico: 26.046975445006176
- p-valor: 5.14000726165566e-12


- **Grandes**
- Estadístico: 29.068346771113216
- p-valor: 2.566556221510514e-168

##### p-valor combinatorio

Aplicando el t-test para todos los pares de subsets (exceptuando los que son iguales y el subconjunto inexistente de productos grandes de clase baja), se obtiene la siguiente tabla:

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Class 1</th>
      <th>Size 1</th>
      <th>Class 2</th>
      <th>Size 2</th>
      <th>Statistic</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>32</th>
      <td>low</td>
      <td>small</td>
      <td>high</td>
      <td>medium</td>
      <td>-0.439619</td>
      <td>0.660</td>
    </tr>
    <tr>
      <th>39</th>
      <td>high</td>
      <td>medium</td>
      <td>low</td>
      <td>small</td>
      <td>0.439619</td>
      <td>0.660</td>
    </tr>
    <tr>
      <th>26</th>
      <td>low</td>
      <td>medium</td>
      <td>high</td>
      <td>large</td>
      <td>1.367159</td>
      <td>0.172</td>
    </tr>
    <tr>
      <th>45</th>
      <td>high</td>
      <td>large</td>
      <td>low</td>
      <td>medium</td>
      <td>-1.367159</td>
      <td>0.172</td>
    </tr>
    <tr>
      <th>28</th>
      <td>low</td>
      <td>small</td>
      <td>medium</td>
      <td>medium</td>
      <td>2.236733</td>
      <td>0.025</td>
    </tr>
    <tr>
      <th>3</th>
      <td>medium</td>
      <td>medium</td>
      <td>low</td>
      <td>small</td>
      <td>-2.236733</td>
      <td>0.025</td>
    </tr>
    <tr>
      <th>42</th>
      <td>high</td>
      <td>large</td>
      <td>medium</td>
      <td>medium</td>
      <td>-3.754626</td>
      <td>1.747e-04</td>
    </tr>
    <tr>
      <th>5</th>
      <td>medium</td>
      <td>medium</td>
      <td>high</td>
      <td>large</td>
      <td>3.754626</td>
      <td>1.747e-04</td>
    </tr>
    <tr>
      <th>33</th>
      <td>low</td>
      <td>small</td>
      <td>high</td>
      <td>large</td>
      <td>4.175018</td>
      <td>3.182e-05</td>
    </tr>
    <tr>
      <th>46</th>
      <td>high</td>
      <td>large</td>
      <td>low</td>
      <td>small</td>
      <td>-4.175018</td>
      <td>3.182e-05</td>
    </tr>
    <tr>
      <th>4</th>
      <td>medium</td>
      <td>medium</td>
      <td>high</td>
      <td>medium</td>
      <td>-4.247274</td>
      <td>2.182e-05</td>
    </tr>
    <tr>
      <th>35</th>
      <td>high</td>
      <td>medium</td>
      <td>medium</td>
      <td>medium</td>
      <td>4.247274</td>
      <td>2.182e-05</td>
    </tr>
    <tr>
      <th>2</th>
      <td>medium</td>
      <td>medium</td>
      <td>low</td>
      <td>medium</td>
      <td>4.682813</td>
      <td>2.864e-06</td>
    </tr>
    <tr>
      <th>21</th>
      <td>low</td>
      <td>medium</td>
      <td>medium</td>
      <td>medium</td>
      <td>-4.682813</td>
      <td>2.864e-06</td>
    </tr>
    <tr>
      <th>31</th>
      <td>low</td>
      <td>small</td>
      <td>low</td>
      <td>medium</td>
      <td>5.718486</td>
      <td>1.184e-08</td>
    </tr>
    <tr>
      <th>24</th>
      <td>low</td>
      <td>medium</td>
      <td>low</td>
      <td>small</td>
      <td>-5.718486</td>
      <td>1.184e-08</td>
    </tr>
    <tr>
      <th>47</th>
      <td>high</td>
      <td>large</td>
      <td>high</td>
      <td>medium</td>
      <td>-5.722584</td>
      <td>1.170e-08</td>
    </tr>
    <tr>
      <th>40</th>
      <td>high</td>
      <td>medium</td>
      <td>high</td>
      <td>large</td>
      <td>5.722584</td>
      <td>1.170e-08</td>
    </tr>
    <tr>
      <th>38</th>
      <td>high</td>
      <td>medium</td>
      <td>low</td>
      <td>medium</td>
      <td>8.288674</td>
      <td>1.523e-16</td>
    </tr>
    <tr>
      <th>25</th>
      <td>low</td>
      <td>medium</td>
      <td>high</td>
      <td>medium</td>
      <td>-8.288674</td>
      <td>1.523e-16</td>
    </tr>
    <tr>
      <th>50</th>
      <td>high</td>
      <td>small</td>
      <td>medium</td>
      <td>large</td>
      <td>9.701996</td>
      <td>5.395e-22</td>
    </tr>
    <tr>
      <th>13</th>
      <td>medium</td>
      <td>large</td>
      <td>high</td>
      <td>small</td>
      <td>-9.701996</td>
      <td>5.395e-22</td>
    </tr>
    <tr>
      <th>30</th>
      <td>low</td>
      <td>small</td>
      <td>medium</td>
      <td>small</td>
      <td>-11.657978</td>
      <td>1.365e-30</td>
    </tr>
    <tr>
      <th>17</th>
      <td>medium</td>
      <td>small</td>
      <td>low</td>
      <td>small</td>
      <td>11.657978</td>
      <td>1.365e-30</td>
    </tr>
    <tr>
      <th>19</th>
      <td>medium</td>
      <td>small</td>
      <td>high</td>
      <td>large</td>
      <td>14.172834</td>
      <td>9.400e-44</td>
    </tr>
    <tr>
      <th>44</th>
      <td>high</td>
      <td>large</td>
      <td>medium</td>
      <td>small</td>
      <td>-14.172834</td>
      <td>9.400e-44</td>
    </tr>
    <tr>
      <th>18</th>
      <td>medium</td>
      <td>small</td>
      <td>high</td>
      <td>medium</td>
      <td>15.204312</td>
      <td>1.079e-50</td>
    </tr>
    <tr>
      <th>37</th>
      <td>high</td>
      <td>medium</td>
      <td>medium</td>
      <td>small</td>
      <td>-15.204312</td>
      <td>1.079e-50</td>
    </tr>
    <tr>
      <th>20</th>
      <td>medium</td>
      <td>small</td>
      <td>high</td>
      <td>small</td>
      <td>-20.437005</td>
      <td>1.041e-84</td>
    </tr>
    <tr>
      <th>51</th>
      <td>high</td>
      <td>small</td>
      <td>medium</td>
      <td>small</td>
      <td>20.437005</td>
      <td>1.041e-84</td>
    </tr>
    <tr>
      <th>15</th>
      <td>medium</td>
      <td>small</td>
      <td>medium</td>
      <td>large</td>
      <td>-20.589639</td>
      <td>1.666e-90</td>
    </tr>
    <tr>
      <th>8</th>
      <td>medium</td>
      <td>large</td>
      <td>medium</td>
      <td>small</td>
      <td>20.589639</td>
      <td>1.666e-90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>medium</td>
      <td>medium</td>
      <td>medium</td>
      <td>small</td>
      <td>-20.954369</td>
      <td>1.689e-95</td>
    </tr>
    <tr>
      <th>14</th>
      <td>medium</td>
      <td>small</td>
      <td>medium</td>
      <td>medium</td>
      <td>20.954369</td>
      <td>1.689e-95</td>
    </tr>
    <tr>
      <th>48</th>
      <td>high</td>
      <td>large</td>
      <td>high</td>
      <td>small</td>
      <td>-24.076130</td>
      <td>4.801e-100</td>
    </tr>
    <tr>
      <th>55</th>
      <td>high</td>
      <td>small</td>
      <td>high</td>
      <td>large</td>
      <td>24.076130</td>
      <td>4.801e-100</td>
    </tr>
    <tr>
      <th>23</th>
      <td>low</td>
      <td>medium</td>
      <td>medium</td>
      <td>small</td>
      <td>-24.109789</td>
      <td>7.811e-120</td>
    </tr>
    <tr>
      <th>16</th>
      <td>medium</td>
      <td>small</td>
      <td>low</td>
      <td>medium</td>
      <td>24.109789</td>
      <td>7.811e-120</td>
    </tr>
    <tr>
      <th>29</th>
      <td>low</td>
      <td>small</td>
      <td>medium</td>
      <td>large</td>
      <td>-28.283912</td>
      <td>1.013e-160</td>
    </tr>
    <tr>
      <th>10</th>
      <td>medium</td>
      <td>large</td>
      <td>low</td>
      <td>small</td>
      <td>28.283912</td>
      <td>1.013e-160</td>
    </tr>
    <tr>
      <th>43</th>
      <td>high</td>
      <td>large</td>
      <td>medium</td>
      <td>large</td>
      <td>-29.068347</td>
      <td>2.567e-168</td>
    </tr>
    <tr>
      <th>12</th>
      <td>medium</td>
      <td>large</td>
      <td>high</td>
      <td>large</td>
      <td>29.068347</td>
      <td>2.567e-168</td>
    </tr>
    <tr>
      <th>34</th>
      <td>low</td>
      <td>small</td>
      <td>high</td>
      <td>small</td>
      <td>-33.806683</td>
      <td>3.268e-171</td>
    </tr>
    <tr>
      <th>53</th>
      <td>high</td>
      <td>small</td>
      <td>low</td>
      <td>small</td>
      <td>33.806683</td>
      <td>3.268e-171</td>
    </tr>
    <tr>
      <th>41</th>
      <td>high</td>
      <td>medium</td>
      <td>high</td>
      <td>small</td>
      <td>-31.532222</td>
      <td>1.111e-182</td>
    </tr>
    <tr>
      <th>54</th>
      <td>high</td>
      <td>small</td>
      <td>high</td>
      <td>medium</td>
      <td>31.532222</td>
      <td>1.111e-182</td>
    </tr>
    <tr>
      <th>6</th>
      <td>medium</td>
      <td>medium</td>
      <td>high</td>
      <td>small</td>
      <td>-29.513785</td>
      <td>9.499e-183</td>
    </tr>
    <tr>
      <th>49</th>
      <td>high</td>
      <td>small</td>
      <td>medium</td>
      <td>medium</td>
      <td>29.513785</td>
      <td>9.499e-183</td>
    </tr>
    <tr>
      <th>27</th>
      <td>low</td>
      <td>medium</td>
      <td>high</td>
      <td>small</td>
      <td>-40.209588</td>
      <td>1.368e-274</td>
    </tr>
    <tr>
      <th>52</th>
      <td>high</td>
      <td>small</td>
      <td>low</td>
      <td>medium</td>
      <td>40.209588</td>
      <td>1.368e-274</td>
    </tr>
    <tr>
      <th>36</th>
      <td>high</td>
      <td>medium</td>
      <td>medium</td>
      <td>large</td>
      <td>-40.371289</td>
      <td>0.000e+00</td>
    </tr>
    <tr>
      <th>11</th>
      <td>medium</td>
      <td>large</td>
      <td>high</td>
      <td>medium</td>
      <td>40.371289</td>
      <td>0.000e+00</td>
    </tr>
    <tr>
      <th>7</th>
      <td>medium</td>
      <td>large</td>
      <td>medium</td>
      <td>medium</td>
      <td>55.497811</td>
      <td>0.000e+00</td>
    </tr>
    <tr>
      <th>9</th>
      <td>medium</td>
      <td>large</td>
      <td>low</td>
      <td>medium</td>
      <td>52.286502</td>
      <td>0.000e+00</td>
    </tr>
    <tr>
      <th>22</th>
      <td>low</td>
      <td>medium</td>
      <td>medium</td>
      <td>large</td>
      <td>-52.286502</td>
      <td>0.000e+00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>medium</td>
      <td>medium</td>
      <td>medium</td>
      <td>large</td>
      <td>-55.497811</td>
      <td>0.000e+00</td>
    </tr>
  </tbody>
</table>
</div>

Como se observa, para las cuatro primeras comparaciones, no existe evidencia suficiente como para afirmar que sus medias son iguales con un intervalo de confianza 95%.

En las siguientes representaciones, se puede comparar con mayor facilidad los precios de los productos de distintas clases y tamaños.

Price by product class and product size |
:-------------------------:|
![](images/ax_07.svg)|



A simple vista, por ejemplo, se puede averiguar que:
- la totalidad de los productos pequeños y de clase alta son más caros que todos los medianos.
- el rango de precios de los productos grandes y de clase alta es bastante amplio.
- los precios de todos los productos de un mismo tamaño se solapan excepto en los pequeños (pudiendo ser susceptible de formar tres grupos distinguidos).


### list_price y standard_cost

Dado un producto, se estudiará la existencia de relación entre el precio y el coste del producto.

Standard cost and list price |
:-------------------------:|
![](images/ax_12.svg)|

En el análisis, se observa que existe una correlación, positiva y moderada, muy significativa.

Cabe destacar que la nube de puntos podría no seguir una distribución aleatoria. De hecho, se observa que el ratio entre precio y coste no suele bajar de cierto valor, algo que hace pensar que se haya fijado un margen de beneficio mínimo por cada producto. Para observalo mejor, se puede representar gráficamente el valor actual con el predicho por la regresión lineal.

Actual vs predicted plot |
:-------------------------:|
![](images/ax_13.svg)|

En la gráfica anterior, no se observa una nube de puntos uniforme. Por tanto, con toda esta información, sí se podría llegar a afirmar que la fijación de precios, con relación al coste, no se deba al azar.

#### Por tamaño de producto

Desglosando el primer plot de este apartado por tamaño de producto, se obtiene lo siguiente:

Standard cost and list price by product size |
:-------------------------:|
![](images/ax_14.svg)|

- Los costes y los precios de los productos <ins>pequeños</ins> siguen una correlación perfecta y positiva.
- Los costes y los precios de los productos <ins>medianos</ins> siguen una correlación moderada y positiva.
- Los costes y los precios de los productos <ins>grandes</ins> siguen una correlación débil y positiva.

Remarcar que, como se puede contemplar en la figura anterior y como se comentó anteriormente acerca de los márgenes de beneficio, los productos de tamaño pequeño, en términos generales, son los que tienen el márgen de beneficio más pequeño de todos los productos.

También se puede observar la representación entre valores actuales y predichos por tamaño de producto.

Actual vs predicted plot by size |
:-------------------------:|
![](images/ax_15.svg)|


### brand
Es la variable **cualitativa** referida a las marcas de los productos.

De acuerdo con la tabla, se pueden extraer la siguiente información que, por ejemplo, puede ayudar en la gestión de stock (tanto en tiendas como en almacenes) como en la estrategia de digitalización de la compañía:
- Solex es la marca más vendida.
- La mitad de los pedidos se realizan online.
- Los pedidos cancelados totales son inferiores al 1% del total de pedidos, con una media de precio por artículo de 1138.15.
  - Se puede afirmar que es semejante a la media de pedidos totales tras un t-test de ambas.

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>frecuencia</th>
      <th>frecuencia_relativa</th>
      <th>pedidos_online</th>
      <th>%_online</th>
      <th>pedidos_aprob</th>
      <th>pedidos_cancel</th>
      <th>%_cancelados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Solex</th>
      <td>4169</td>
      <td>0.214400</td>
      <td>2047</td>
      <td>49.100504</td>
      <td>4128</td>
      <td>41</td>
      <td>0.983449</td>
    </tr>
    <tr>
      <th>WeareA2B</th>
      <td>3245</td>
      <td>0.166881</td>
      <td>1460</td>
      <td>44.992296</td>
      <td>2906</td>
      <td>25</td>
      <td>0.770416</td>
    </tr>
    <tr>
      <th>Giant Bicycles</th>
      <td>3244</td>
      <td>0.166830</td>
      <td>1560</td>
      <td>48.088779</td>
      <td>2967</td>
      <td>26</td>
      <td>0.801480</td>
    </tr>
    <tr>
      <th>OHM Cycles</th>
      <td>2993</td>
      <td>0.153921</td>
      <td>1417</td>
      <td>47.343802</td>
      <td>2840</td>
      <td>23</td>
      <td>0.768460</td>
    </tr>
    <tr>
      <th>Trek Bicycles</th>
      <td>2931</td>
      <td>0.150733</td>
      <td>1640</td>
      <td>55.953599</td>
      <td>3217</td>
      <td>27</td>
      <td>0.921187</td>
    </tr>
    <tr>
      <th>Norco Bicycles</th>
      <td>2863</td>
      <td>0.147236</td>
      <td>1615</td>
      <td>56.409361</td>
      <td>3215</td>
      <td>30</td>
      <td>1.047852</td>
    </tr>
    <tr>
      <th>Total</th>
      <td>19445</td>
      <td>1.000000</td>
      <td>9739</td>
      <td>50.084855</td>
      <td>19273</td>
      <td>172</td>
      <td>0.884546</td>
    </tr>
  </tbody>
</table>
</div>

<img src="images/ax_05.svg" alt="drawing" width="800"/>

#### Análisis de la influencia de la marca en el precio de las compras
En este caso, se categoriza la variable "list_price" a tres categorías, dependiendo de si los productos adquiridos son baratos, de precio medio o caros.

Para ello, se han tomado el primer y tercer cuartil como valores determinantes de la categoría, dando lugar a la siguiente tabla cruzada con valores porcentuales:


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>brand</th>
      <th>Giant Bicycles</th>
      <th>Norco Bicycles</th>
      <th>OHM Cycles</th>
      <th>Solex</th>
      <th>Trek Bicycles</th>
      <th>WeareA2B</th>
      <th>All</th>
    </tr>
    <tr>
      <th>list_price_cat</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cheap</th>
      <td>11.652281</td>
      <td>28.606357</td>
      <td>30.003341</td>
      <td>31.086592</td>
      <td>38.314568</td>
      <td>11.340524</td>
      <td>25.106711</td>
    </tr>
    <tr>
      <th>Average</th>
      <td>59.309494</td>
      <td>65.106532</td>
      <td>43.935850</td>
      <td>46.581914</td>
      <td>26.441488</td>
      <td>57.442219</td>
      <td>49.802006</td>
    </tr>
    <tr>
      <th>Expensive</th>
      <td>29.038224</td>
      <td>6.287111</td>
      <td>26.060809</td>
      <td>22.331494</td>
      <td>35.243944</td>
      <td>31.217257</td>
      <td>25.091283</td>
    </tr>
  </tbody>
</table>
</div>


Aplicando el chi-cuadrado:

- Chi: 1972.8325162484111
- p-value: 0.0

Con un p-valor de 0, se puede afirmar que existe una relación, en las ventas, entre la marca y el precio de los productos.

Bar graph            |  Stacked graph
:-------------------------:|:-------------------------:
![](images/ax_08.svg)  |  ![](images/ax_11.svg)

Area chart            |  Heat map
:-------------------------:|:-------------------------:
![](images/ax_09.svg)  |  ![](images/ax_10.svg)
