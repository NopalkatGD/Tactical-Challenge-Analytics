# Tactical Challenge Analytics

Últimamente se ha vuelto casi un meme que para explicar un videojuego es necesario abrir un archivo de Excel con muchos parámetros con el objetivo de sacar mayor provecho a unidades o artículos.

En esta ocasión quise hacer análisis estadístico al videojuego Blue Archive; mas específicamente su modo de juego Tactical Challenge.

Los jugadores de Blue Archive sabemos que este modo de juego puede llegar a ser injusto ya sea por el factor suerte o por no invertir demasiado tiempo y dinero en el juego, en especial llegando a cierto nivel en este modo de juego.

Con la finalidad de practicar mi habilidades en programación y ayudar a mis amigos y a mi, decidí realizar un programa en Python para hacer el análisis estadístico utilizando la librerías de json y matplotlib.

Los parámetros a analizar en fueron tomados a partir de mi experiencia y el historial de victorias y derrotas dentro del juego guardándolos dentro de un archivo json que funciona como base de datos donde se encuentran los personajes más usados en el modo de juego Tactical Challenge.

La base de datos se interpreta de la siguiente manera:

``` json
[
    {
        "name":"", //Nombre del Personaje
        "type":"Stricker", //la funcion del personaje en el campo de batalla (Stricker | Special)
        "vulnerable":{ //Aqui se nombran a quellos personajes que son vulnerables cante el personaje que se nombra en "name":"(personaje)"
            "Characters":["p1","p2","p3"]
        },
        "Resistant":{ //Aquí se nombran aquellos personajes que pueden resistir todos o la mayoria de los ataques del perosnaje que se nombra en "name":"(personaje)"
            "Characters":["p1","p2","p3"]
        },
        "Dangerous":{ //aqui se nombran a todos lo personajes que son potencialmente peligroso o pueden derrotar al personaje nombrado en "name":"(personaje)"
            "Characters":["p1","p2","p3"]
        }
    }
]
```

> Dejaré una platilla de la base de datos que usé si es que deseas hacer tu propio análisis.

La siguiente grafica muestra las unidades más utilizadas vistas en el historial de batallas tanto de defensa como en ataque.
![grafica](https://github.com/NopalkatGD/Tactical-Challenge-Analytics/blob/main/ANEXOS/Pasted%20image%2020231116184721.png?raw=true)

- En color Amarillo se muestra la cantidad de personajes que cada unidad puede derrotar, siendo Shun la que más personajes puede derrotar.
- En color Azul son aquellos personajes que resisten los ataques de cada unidad, en la grafica se muestra que Yuuka es la unidad menos peligrosa, esto debido a su gameplay que se sentra en absorber todos los ataques.
- Y en Rojo se muestra la cantidad de personajes pueden derrotar a esa unidad teniendo Hoshino (Swimsuit - Traje de baño) como la más vulnerable debido a sus estadísticas y que toma una posición al frente de la batalla

> En la nota de abajo se muestra otros valores tomados a partir de cuantas veces se repite la unidad dentro de cada parámetro considerado, es debido a que se menciona a Mariana y no a Yuuka como las más resistente

![pociciones](https://github.com/NopalkatGD/Tactical-Challenge-Analytics/blob/main/ANEXOS/Pasted%20image%2020231116190313.png?raw=true)

En lo personal este análisis me ha servido demasiado para estar en una posición alta dentro de este modo de juego, sin embargo la base de datos seguirá actualizándose para llenar los espació de personajes que no tengo o no he podido usar lo suficiente para entender sus mecánicas.

El proyecto seguirá en desarrollo implementando nuevas funciones como nombrar que personajes son más aptos para combatir y ante que equipo personalizado
