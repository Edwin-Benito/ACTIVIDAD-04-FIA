Coloreo de un Mapa Municipal con 4 Colores

Este repositorio contiene la implementación del algoritmo de Coloreo de Grafos / Mapas mediante el Teorema de los Cuatro Colores, aplicado a un mapa municipal. El objetivo del proyecto es formalizar el problema de satisfacción de restricciones (CSP) y construir el espacio de búsqueda correspondiente para asignar colores a las regiones colindantes sin que dos regiones adyacentes compartan el mismo color.

Integrantes del Equipo

Edwin Benito Castillo Hernández

José Luis González Rodríguez

Docente: Dr. Jaime Aguilar Ortiz

Asignatura: Fundamentos de Inteligencia Artificial (FIA)

Descripción del Proyecto

El problema consiste en asignar uno de $k=4$ colores disponibles a cada municipio o región de un mapa determinado de manera que no existan dos regiones adyacentes (que compartan frontera) con el mismo color.

Componentes de la Formalización (CSP):

Variables ($V$): Conjunto de municipios o regiones del mapa.

Dominios ($D$): Conjunto de colores disponibles $D = \{\text{Rojo}, \text{Verde}, \text{Azul}, \text{Amarillo}\}$.

Restricciones ($C$): Para cada par de regiones adyacentes $(v_i, v_j)$, el color asignado $c(v_i) \neq c(v_j)$.
