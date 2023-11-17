import json

def char_data(ruta):
    vuln_char_lst = []
    contador = []
    with open(ruta) as contenido:
        personajes = json.load(contenido)
        for personaje in personajes:
            nombre_lst = personaje.get("name")
            vuln_characters = personaje.get("Dangerous").get("Characters")
            for i in vuln_characters:
                vuln_char_lst.append(i)
    return vuln_char_lst

if __name__ == '__main__':
    ruta = 'characters.json'
    vuln_char_lst = char_data(ruta)

    personaje_contador = {}
    for personaje in vuln_char_lst:
        if personaje in personaje_contador:
            personaje_contador[personaje] += 1
        else:
            personaje_contador[personaje] = 1
    
    repetida = max(personaje_contador, key=personaje_contador.get)

    print(repetida)