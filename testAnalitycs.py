import json

def char_data(ruta, tipo):
    char_type_total =0
    all_char_test_res= []
    total_char_test = []
    with open(ruta) as contenido:
        personajes = json.load(contenido)

        for personaje in personajes:
            name = personaje.get('name')
            char_total = len(personajes)
            total_char_test.append("name")

            vuln_characters = personaje.get("vulnerable").get("Characters")
            res_characters = personaje.get("Resistant").get("Characters")
            
            for all_test in res_characters:
                all_char_test_res.append(all_test)

            dan_characters = personaje.get("Dangerous").get("Characters")

            vuln_char_num = len(vuln_characters)
            res_char_num = len(res_characters)
            dan_char_num = len(dan_characters)
            
            type_char = personaje.get("type")

            if "Pendiente" in vuln_characters or "0" in vuln_characters:
                vuln_char_num = 0

            if "Pendiente" in res_characters or "0" in res_characters:
                res_char_num = 0
                res_characters = "Ninguna"
            elif "ALL" in res_characters:
                res_char_num = char_total
                res_characters = "ALL"

            if "Pendiente" in dan_characters or "0" in dan_characters:
                dan_char_num = 0
            
            if tipo in type_char:
                char_type_total +=1
                print(name)
                print(f"Personajes que son vulnerables: {vuln_characters}")
                print(f"Personajes que le resisten: {res_characters}")
                print(f"Personajes que pueden derrotarla: {dan_characters}")
                print(f"vulnerables: {vuln_char_num} | Resistentes: {res_char_num} | Peligros: {dan_char_num}")
                print()
    
    cantidad = 1
    num_array = []
    for i in total_char_test:
        contador = 0
        numbre_test_1 = i
        for j in all_char_test_res:
            numbre_test_2 = j

            if numbre_test_1 == numbre_test_2:
                cantidad +=1
                contador = cantidad
        num_array.append(contador)
    print(num_array)

if __name__ == '__main__':
    ruta = 'characters.json'
    char_data(ruta, "Stricker")
    print("########################################################################\n")
    char_data(ruta, "Special")
