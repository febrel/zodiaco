from flask import Flask, render_template, request, flash
import time;

app = Flask(__name__)

app.secret_key = "manbearpig_MUDMAN888"

# Imprimiendo la fecha y hora de hoy
hoy = time.localtime()


# Variables globales de la fecha actual
yearMax =  hoy[0]
months=  hoy[1]
day = hoy.tm_mday


# Funciones de Flask (Rutas)
def retornaZodiaco(dia, mes):
    
    if (dia>=21 and mes== 'Mar') or (dia<=20 and mes== 'Abr'):
        resultado = 'Aries'
    elif (dia>=24 and mes== 'Sep') or (dia<=23 and mes== 'Oct'):
        resultado = 'Libra'
    elif (dia>=21 and mes== 'Abr') or (dia<=21 and mes== 'May'):
        resultado = 'Tauro'
    elif (dia>=24 and mes== 'Oct') or (dia<=22 and mes== 'Nov'):
        resultado = 'Escorpio'
    elif (dia>=22 and mes== 'May') or (dia<=21 and mes== 'Jun'):
        resultado = 'G\u00E9minis'
    elif (dia>=23 and mes== 'Nov') or (dia<=21 and mes== 'Dic'):
        resultado = 'Sagitario'
    elif (dia>=21 and mes== 'Jun') or (dia<=23 and mes== 'Jul'):
        resultado = 'C\u00E1ncer'
    elif (dia>=22 and mes== 'Dic') or (dia<=20 and mes== 'Ene'):
        resultado = 'Capricornio'
    elif (dia>=24 and mes== 'Jul') or (dia<=23 and mes== 'Ago'):
        resultado = 'Leo'
    elif (dia>=21 and mes== 'Ene') or (dia<=19 and mes== 'Feb'):
        resultado = 'Acuario'
    elif (dia>=24 and mes== 'Ago') or (dia<=23 and mes== 'Sep'):
        resultado = 'Virgo'
    elif (dia>=20 and mes== 'Feb') or (dia<=20 and mes== 'Mar'):
        resultado = 'Piscis'
    
    return resultado

def retornaDescripcion(zodiaco):

    resultado_valor = ''

    descripcion = {
            'Aries': 'Signo de fuego y el primero de la rueda zodiacal. ¡Inician el año astral! Los Aries llevan la palabra iniciativa escrita en la frente. Ya sea en temas profesionales, como en relaciones sentimentales, familiares o amistosas. No obstante, este liderazgo, seguridad y personalidad tan directa puede hacer que la gente se llegue a asustar. O que incluso les cueste seguirles el ritmo. Una manera rápida y práctica de saber que estás junto a uno de ellos: no pueden estar más de cinco minutos metidos en la cama una vez se despiertan.',
            'Tauro': 'Los Tauro, signos de tierra, tienen un don natural para conquistar, gracias a su sensualidad innata. Pero aquí no terminan sus virtudes: son los signos perfectos para hacer que mantengamos los pies en el suelo, ya que son bastante pragmáticos y con las ideas bien claras. Son los que más estabilidad pueden aportar, porque rara vez cambiarán de opinión. Aunque quizá deberían dejar de pensar tanto en las objetos materiales y centrarse en los pequeños placeres y detalles de la vida.',
            'Géminis': 'Muy sociables y demasiado curiosos, aspecto negativo cuando se trata de establecer una relación ya que les cuesta mucho comprometerse. En un signo de aire y en su cabeza conviven dos gemelos literalmente hablando si te basas en su símbolo que les ha ce cambiar de opinión constantemente. Además, pecar un poco de falsos y fantasmas. Los mejores políticos, oradores y comerciales, eso sí. Los Géminis serán las almas de la conversación, aunque evitarán a toda costa hablar de sus verdaderos sentimientos, para proteger su corazoncito.',
            'Cáncer': 'Se llevan el premio a los más sensibles del horóscopo. La palabra drama les pertenece y son capaces de generarlo en su cabeza con un motivo los más mínimo sensible. Esto ocurre porque son muy sensibles y tienden a ser inseguros con ellos mismos. Confían demasiado en los demás, eso sí. Quizá por eso son los mejores en empatizar y escuchar los problemas ajenos. En el extremo contrario, cuando se sienten amenazados o vulnerables, los Cáncer, de naturaleza agua, se esconden bajo su caparazón y sacan lo peor de ellos: un carácter terrible y muy desagradable.',
            'Leo': 'Estar bajo el signo de fuego del león significa tener luz propia, una extrema lealtad hacia los demás y una maravillosa facilidad para hacer sentir bien a las personas de su alrededor. Parece todo maravilloso, ¿verdad? Pero no es oro todo lo que reluce porque, al estar regidos por el Sol, los Leo son muy egocéntricos. Muchísimo. Aspecto que les hace ser muy egoístas y poco empáticos en muchísimas ocasiones. De la misma manera, ojito con llevarles la contraria. Tienen un humor de perros cuando las cosas no salen como quieren.',
            'Virgo': 'El fin vital de cualquier Virgo, signo de tierra, es encontrar la perfección y la pureza en absolutamente todo lo que tiene alrededor. Para ello, son muy ordenados, rozando incluso el convertirse en maniáticos. Su parte positiva reside en la servicialidad y generosidad que siempre demuestran a los demás. Aunque deben aceptarse tal y como son, y trabajar en dejar de analizar todo lo que ocurre constantemente para criticarlo después. Los reyes del ‘overthinking’, sí son.',
            'Libra': 'No hay nada que le guste menos a un Libra que el desequilibrio, ya sea emocional o en las relaciones. La razón reside en que dudan de todo, constantemente, como buen signo de aire que es. No de sí mismo, sino más bien de las decisiones que toman. ¿Le quiero o no le quiero? ¡Así todo el rato! Por eso, muchas veces evitan cualquier tipo de compromiso aunque, una vez que se tiran a la piscina, lo dan todo. Y es que, son el signo más romántico del zodiaco. ‘‘Al about love’’. Lo que les lleva a creerse los protas de sus propios drama en cualquier situación.',
            'Escorpio': 'Escorpio tiene una parte muy buena y otra muy mala. Por un lado, son sensibles, muy comprensivos, luchan constantemente por lo que piensan que es justo. Pero hasta llegar ahí, nos encontramos con un ardiente caparazón, que utilizan a modo de escudo. Quizá más veces de las que deberían, ya que tienen muchísimo carácter, pero en el fondo son unos bollitos de canela que tienen pánico a que les hagan daño ‘AKA’ un signo de agua.',
            'Sagitario': 'Todos los actos de un Sagitario, signo de fuego, tienen como finalidad convertir las experiencias en aprendizaje. No obstante, esta inquietud y exceso confianza en los demás pueden jugarles malísimas pasadas. Como, por ejemplo, llegar a obsesionarse demasiado con algo. No hablamos de cabezonería, sino de repetir una idea en la cabeza en repetidas ocasiones y tener todo bajo control. Esto ocurre en todos los ámbitos de sus vidas: desde el amor, pasando por el trabajo, hasta en un viaje que realicen o una cena que preparen.',
            'Capricornio': 'Son tan ambiciosos y tienen tanta disciplina, que es muy fácil que acaben perdiendo la perspectiva. ¡Por mucho elemento de tierra que sean! Son muy cabezones, queriendo llevar siempre la razón y no aceptando más opiniones. Esto, si no lo controlan, pueden volverse en su contra, convirtiéndoles en personas algo controladoras e intensas. Como parte positiva (que también tienen mucho), siempre saben lo que quieren y anteponen su familia y bienestar a todo lo demás. Además, su paciencia es ilimitada.',
            'Acuario': 'Lo más destacable de su personalidad es que nunca, nunca, nunca se dan por vencidos a la hora de luchar por su libertad. Son almas libres (ejem, signo de aire) y los responsables de iniciar los grandes cambios en el mundo. ¡Estamos en plena época acuariana de cambio! Ahora bien, esta manera de fluir y querer ser rebelde les lleva a descuidar en muchísimas ocasiones a quienes de verdad les quieren y apoyan. En otras palabras: son los típicos de los que puedes estar sin saber nada durante meses. Y ten claro que te dejarán con los dos ticks azules en cualquier momento.',
            'Piscis': 'Los Piscis son conocidos por dos características muy marcadas: su gusto por el drama y la imaginación. En la primera son unos cracks, de verdad. No llegan al nivel de los Cáncer, pero sí son capaces de montarse su propia peli y vivir en ella tan a gusto, aún sabiendo que está muy alejada de la realidad. No obstante, esto está muy relacionada con que siempre están en las nubes, pensando en sus cosas y soñando. Llevan dentro una gran espiritualidad. También son empatía y compasivos, aunque puede ponérseles en contra, ya que muchas veces tardan en ver la toxicidad existente de algunas relaciones.'
        }
    

    for clave, valor in descripcion.items():
        if (clave == zodiaco):
            resultado_valor = valor

    return resultado_valor


def retornaMesEntero(mes):

    resultado_clave = 0

    resultado_meses = {
        1:"Ene", 
        2: "Feb", 
        3: "Mar", 
        4: "Abr", 
        5: "May", 
        6: "Jun", 
        7: "Jul", 
        8: "Ago", 
        9: "Sep", 
        10: "Oct", 
        11: "Nov", 
        12: "Dic"
    }

    for clave, valor in resultado_meses.items():
        if (valor == mes):
            resultado_clave = clave

    return resultado_clave

def retornaEdad(year_html, month_html, day_html):

    # Variables que retornan el resultado
    yearsOutput = 0;
    monthsOutput = 0;
    daysOutput = 0;

    # Si year es menor al actual y mes es menor al mes actual y dias menos que el actual
    if ((year_html < yearMax) and (month_html < months) and (day_html < day)):
        yearsOutput = yearMax - year_html;
        monthsOutput = months - month_html;
        daysOutput = day - day_html;
    # Si year es menor al actual y mes es menor al mes actual y dias igual que el actual
    elif ((year_html < yearMax) and (month_html < months) and (day_html == day)):
        yearsOutput = yearMax - year_html;
        monthsOutput = months - month_html;
        daysOutput = 0;

    # Si year es menor al actual y mes es menor al mes actual y dias mayor que el actual
    elif ((year_html < yearMax) and (month_html < months) and (day_html > day)):
        yearsOutput = yearMax - year_html;
        monthsOutput = (months - month_html) - 1;
        daysOutput = diasMeses[months] - (day_html - day);

    # Si year es menor al actual y mes es menor al mes actual y dias mayor que el actual
    elif ((year_html < yearMax) and (month_html == months) and (day_html == day)):
        yearsOutput = yearMax - year_html;
        monthsOutput = 0;
        daysOutput = 0;

    # Si year es menor al actual y mes es igual al mes actual y dias menor al actual
    elif ((year_html < yearMax) and (month_html == months) and (day_html < day)):
        yearsOutput = (yearMax - year_html);
        monthsOutput = 0;
        daysOutput = day - day_html;

    # Si year es menor al actual y mes es igual al mes actual y dias mayor al actual
    elif ((year_html < yearMax) and (month_html == months) and (day_html > day)):
        yearsOutput = (yearMax - year_html) - 1;
        monthsOutput = 12 - 1;
        console.log(diasMeses[months]);
        daysOutput = diasMeses[months] - (day_html - day);

    # Si year es menor al actual y mes es mayor al mes actual y dias menor al actual
    elif ((year_html < yearMax) and (month_html > months) and (day_html < day)):
        yearsOutput = (yearMax - year_html) - 1;
        monthsOutput = (12 - (month_html - months));
        daysOutput = day - day_html;

    # Si year es igual al actual y mes es mayor al actual y dia es igual al actual
    elif ((year_html < yearMax) and (month_html > months) and (day_html == day)):
        yearsOutput = (yearMax - year_html) - 1;
        monthsOutput = (12 - (month_html - months));
        daysOutput = 0;

    # Si year es igual al actual y mes es mayor al actual y dia es mayor al actual
    elif ((year_html < yearMax) and (month_html > months) and (day_html > day)):
        yearsOutput = (yearMax - year_html) - 1;
        monthsOutput = (12 - (month_html - months) - 1);
        daysOutput = diasMeses[months] - (day_html - day);
    
    # Si year es mayor o igual al actual y mes es menor al actual 
    elif ((year_html >= yearMax) and (month_html < months) and (day_html < day)):
        yearsOutput = 0;
        monthsOutput = months - month_html;
        daysOutput = day - day_html;

    # Si year es mayor o igual al actual y mes es menor al actual  y dia es igual al actual
    elif ((year_html >= yearMax) and (month_html < months) and (day_html == day)):
        yearsOutput = 0;
        monthsOutput = months - month_html;
        daysOutput = 0;

    # Si year es mayor o igual al actual y mes es menor al actual  y dia es mayor al actual
    elif ((year_html >= yearMax) and (month_html < months) and (day_html > day)):
        yearsOutput = 0;
        monthsOutput = (months - month_html) - 1;
        daysOutput = diasMeses[months] - (day_html - day);

    # Si year es igual al actual y dia es igual al actual
    elif ((year_html >= yearMax) and (month_html == months) and (day_html == day)):
        yearsOutput = 0;
        monthsOutput = 0;
        daysOutput = 0;
    # Si year es igual al actual y dia es igual al actual
    elif ((year_html >= yearMax) and (month_html == months) and (day_html < day)):
        yearsOutput = 0;
        monthsOutput = 0;
        daysOutput = day - day_html;

    else:
        print("Ninguno")
    
    
    return yearsOutput, monthsOutput, daysOutput
    

@app.route('/', methods=["GET","POST"])
def index():

    if request.method =='POST':
        year_html = request.form['yearInput']
        month_html = request.form['monthInput']
        day_html = request.form['dayInput']

        error = None

        # Condicional para controlar que se llenen los apartados
        if (not month_html or not day_html or  not year_html):
            error = 'Faltan datos requeridos!'
        else:
            resultado_zodiaco = retornaZodiaco(int(day_html), month_html)
            resultado_descrip = retornaDescripcion(resultado_zodiaco)

            mes_trasformado = retornaMesEntero(month_html)

            resultado_anios, resultado_meses, resultado_dias= retornaEdad(int(year_html), mes_trasformado, int(day_html))


            resultado = [
                {
                'zodiaco': resultado_zodiaco,
                'descripcion': resultado_descrip,
                'year': resultado_anios,
                'month': resultado_meses,
                'day': resultado_dias
                }
            ]


            return render_template("resultado.html", resultado = resultado)
        
        flash(error)
    return render_template("index.html")


@app.route('/zodiaco')
def zodiaco():
    
    return render_template("resultado.html")