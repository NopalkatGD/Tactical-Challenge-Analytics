import json
from matplotlib import pyplot

def char_data(ruta, tipo):
    char_type_total =0
    estudiante = []

    pts_vulnerable = []
    pts_resistentes = []
    pts_peligros = []

    list_vuln=[]
    list_res=[]
    list_dan=[]

    with open(ruta) as contenido:
        personajes = json.load(contenido)

        for personaje in personajes:
            name = personaje.get('name')
            char_total = len(personajes)

            vuln_characters = personaje.get("vulnerable").get("Characters")
            for a in vuln_characters:
                list_vuln.append(a)
            res_characters = personaje.get("Resistant").get("Characters")
            for e in res_characters:
                list_res.append(e)
            dan_characters = personaje.get("Dangerous").get("Characters")
            for i in dan_characters:
                list_dan.append(i)

            vuln_char_num = len(vuln_characters)
            res_char_num = len(res_characters)
            dan_char_num = len(dan_characters)
            
            type_char = personaje.get("type")

            if "Pendiente" in vuln_characters or "0" in vuln_characters:
                vuln_char_num = 0

            if "Pendiente" in res_characters or "0" in res_characters:
                res_char_num = 0
            elif "ALL" in res_characters:
                res_char_num = char_total

            if "Pendiente" in dan_characters or "0" in dan_characters:
                dan_char_num = 0

            if tipo in type_char:
                char_type_total +=1

                estudiante.append(name)
                pts_vulnerable.append(vuln_char_num)
                pts_resistentes.append(res_char_num)
                pts_peligros.append(dan_char_num)
    

    return estudiante, pts_vulnerable, pts_resistentes, pts_peligros, list_vuln, list_res, list_dan


if __name__ == '__main__':
    ruta = 'characters.json'
    
    estudiante1, pts_vulnerable1, pts_resistentes1, pts_peligros1, list_vuln1, list_res1, list_dan1 = char_data(ruta, "Special")
    estudiante2, pts_vulnerable2, pts_resistentes2, pts_peligros2, list_vuln2, list_res2, list_dan2 = char_data(ruta, "Stricker")
    
    count_vuln1 = {}
    count_res1 = {}
    count_dan1 = {}
    for personaje in list_vuln1:
        if personaje in count_vuln1:
            count_vuln1[personaje] += 1
        else:
            count_vuln1[personaje] = 1

    for personaje in list_res1:
        if personaje in count_res1:
            count_res1[personaje] += 1
        else:
            count_res1[personaje] = 1
    
    for personaje in list_dan1:
        if personaje in count_dan1:
            count_dan1[personaje] += 1
        else:
            count_dan1[personaje] = 1

    rep_vuln1 = max(count_vuln1, key=count_vuln1.get)
    rep_res1 = max(count_res1, key=count_res1.get)
    rep_dan1 = max(count_dan1, key=count_dan1.get)

    print(rep_dan1)
    width = 0.2
    x1=range(len(estudiante1))
    x2=range(len(estudiante2))

    fig, ax = pyplot.subplots(nrows=2,ncols=1, figsize=(10,4))

    ax[0].bar(x1, height=pts_vulnerable1,color="yellow",width=width, label="cantidad personajes que son vulnerables")
    ax[0].bar([i + width for i in x1], height=pts_resistentes1,color="blue",width=width, label="cantidad de personajes que son resistentes")
    ax[0].bar([i + width * 2 for i in x1],height=pts_peligros1,color="red",width=width, label="cantidad de personajes que pueden derrotar a cada una")
    ax[0].set_title("Estudiantes Specials")
    ax[0].legend()
    ax[0].set_xticks([i + width for i in x1])
    ax[0].set_xticklabels(estudiante1)

    ax[1].bar(x2, height=pts_vulnerable2,color="yellow",width=width, label="cantidad personajes que son vulnerables")
    ax[1].bar([i + width for i in x2],height=pts_resistentes2,color="blue",width=width, label="cantidad de personajes que son resistentes")
    ax[1].bar([i + width * 2 for i in x2],height=pts_peligros2,color="red",width=width, label="cantidad de personajes que pueden derrotar a cada una")
    ax[1].set_title("Estudiantes Strickers")
    ax[1].legend()
    ax[1].set_xticks([i + width for i in x2])
    ax[1].set_xticklabels(estudiante2)
    
    nota = "Estudiante más vulnerable: "+rep_vuln1+"\nEstudiante más vulnerable: más resistente: "+rep_res1+"\nEstudiante más vulnerable: más peligrosa: "+rep_dan1
    nota_x = -0.8
    nota_y = -5.2
    ax[1].text(nota_x,nota_y,nota, fontsize=12,ha="left",va="bottom",color="black")

    fig.tight_layout()

    pyplot.show()

