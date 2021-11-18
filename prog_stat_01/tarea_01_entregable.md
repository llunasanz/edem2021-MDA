---
output:
  pdf_document: default
  html_document: default
---
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
Es la variable **cuantitativa** que hace referencia al precio del producto adquirido. Ésta se comprende en un rando de entre 12.01 y 2091.47.

count | mean | std | min | 25% | 50% | 75% | max |
:----:|:------------:|:--------:|:-----:|:------:|:-------:|:-------:|:-------:|
19445 | 1107.337193  | 582.6624 | 12.01 | 575.27 | 1163.89 | 1635.30 | 2091.47 |

A continuación, se muestra la distribución del precio del conjunto de datos. Nótese que distribución normal y que, a su vez, está compuesta por otras distribuciones). En los siguientes gráficos, se observan distintas componentes, basadas en las clases de producto (product_class), que componen la distribución del precio.

Price             |  Price by product class
:-------------------------:|:-------------------------:
![](images/ax_00.svg)  |  ![](images/ax_01.svg)

De la misma manera, se ha extraído las distintas componentes relacionadas con el tamaño del producto (product_size) de los elementos anteriores. También se observa que ninguna componente sigue una distribución normal, además de que no componen 3 grupos distinguidos.

En la siguiente representación de cajas y bigotes, se puede comparar con mayor facilidad los precios de los productos de distintas clases y tamaños.

Price by product class and product size |
:-------------------------:|
![](images/ax_03.svg)|

A simple vista, por ejemplo, se puede averiguar que:
- la totalidad de los productos pequeños y de clase alta son más caros que todos los medianos.
- el rango de precios de los productos grandes y de clase alta es bastante amplio.
- los precios de todos los productos de un mismo tamaño se solapan excepto en los pequeños (pudiendo ser susceptible de formar tres grupos distinguidos).

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
