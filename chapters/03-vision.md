# Chapter 3: El Despertar de la Vision Artificial

## *El Sueno que Cambio Todo (2013-2022)*

> *"El sueno se habia hecho realidad: las maquinas habian aprendido a 'ver', y yo habia aprendido a ensenarles."*

---

## 3.1 Kur

En la oscura noche diviso una estrella que me llama la atencion por sus movimientos. Luego ella se empieza a hacer mas grande, me da miedo, la veo cada vez mas cerca hasta que la tengo sobre mi cabeza. No puedo creer lo que estoy viendo: es como de tres puntas con la forma de Kur, el dragon sumerio que hasta ese sueno desconocia.

La misma gira y gira sobre mi cabeza. Tengo miedo pero me animo, levanto mis manos y empiezo a hablar en lenguas extranas con ella. Una luz potente increible baja y me llena de una paz que pocas veces senti.

Me despierto del sueno y estoy lleno de esa energia. A los dias comienzo a experimentar con cosas nuevas: robots, drones, impresoras 3D. Esto es por principios del 2013.

**El despertar:** Ese sueno marco el inicio de mi fascinacion por la tecnologia que podia "ver" y "entender". Sin saberlo, habia comenzado mi camino hacia la inteligencia artificial.

---

## 3.2 El Descubrimiento de TensorFlow (2015)

Luego en el 2015 descubro TensorFlow. En ese momento lo corro en una Raspberry Pi y entreno mi primer modelo pequeno ahi para probarlo. Estaba fascinado. La IA llegaba a mi vida para cambiarlo todo.

Entonces comienza mi periodo de experimentacion con IA. Hasta que pude tener mi GPU paso mucho tiempo, algunos anos, pero nunca deje de entrenar pequenos modelos y construir datasets.

**Los primeros experimentos:** Lo primero fue entrenar los modelos que venian de base con TensorFlow, tanto de objetos como plantas o animales. A veces estaba hasta 4 dias entrenando un modelo por los recursos limitados de las Raspberry Pi version 2 y mi laptop.

**El primer proyecto real:** Un detector de plagas en hojas verdes. Ya por esos anos comenzaron a circular algunos datasets, asi que la cosa comenzaba a ponerse interesante. Tambien pude trasladar luego ese detector de plagas a una app para celular.

**Los primeros desafios:**
- La Raspberry Pi se sobrecalentaba constantemente
- Cada entrenamiento tomaba dias completos para resultados mediocres
- No entendia conceptos como overfitting o data augmentation
- Pero la fascinacion era mas fuerte que la frustracion

---

## 3.3 Los Primeros Proyectos Reales

En este periodo de experimentacion intensa, construi y entrene diversos modelos que marcaron hitos importantes en mi viaje con la inteligencia artificial.

### Deteccion de Plagas en Plantas

Desarrolle sistemas de vision artificial para detectar plagas en plantas, un paso inicial en la aplicacion de la IA a problemas reales y especificos.

Mi primer proyecto serio fue desarrollar un sistema para detectar diferentes tipos de plagas y enfermedades en hojas de plantas con precision suficiente para ser util en agricultura real.

El proceso de construccion del dataset fue artesanal: fotografie miles de hojas infectadas y sanas. Luego pase noches enteras anotando manualmente cada imagen. Desarrolle mis propias herramientas de anotacion para convertir las marcas XML en formatos utilizables por TensorFlow.

```python
# xml_a_csv.py - Mi herramienta de anotacion casera
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                    int(root.find('size')[0].text),
                    int(root.find('size')[1].text),
                    member[0].text,  # Tipo de plaga
                    int(member[4][0].text),  # xmin
                    int(member[4][1].text),  # ymin
                    int(member[4][2].text),  # xmax
                    int(member[4][3].text))  # ymax
            xml_list.append(value)

    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df
```

### Deteccion de Objetos con Drones (YOLO)

Uno de mis proyectos mas ambiciosos fue desarrollar un sistema para detectar objetos desde imagenes capturadas con drones. El objetivo especifico era identificar piletas desde el aire, lo cual tenia aplicaciones practicas para mapeo urbano y servicios municipales.

Para este proyecto utilice YOLO (You Only Look Once), que en ese momento era una arquitectura revolucionaria para deteccion de objetos en tiempo real. El desafio principal era construir un dataset de calidad con imagenes aereas.

El proceso de anotacion:
- Capture cientos de imagenes con drones a diferentes alturas
- Desarrolle herramientas personalizadas para anotar objetos en imagenes aereas
- Cada pileta tenia que ser marcada manualmente con bounding boxes precisos
- El dataset final incluia diferentes tipos de piletas: rectangulares, circulares, irregulares

Los resultados fueron prometedores: el modelo logro una precision del 85% en la deteccion de piletas, incluso en condiciones de iluminacion variable y con obstaculos parciales como arboles o estructuras.

### Vehiculo Autonomo en Miniatura

Uno de mis proyectos mas desafiantes fue construir un pequeno vehiculo autonomo que funcionaba con una Raspberry Pi y la camara de Raspberry Pi, controlado desde una PC con Ubuntu y una GPU.

El sistema funcionaba de la siguiente manera:

- La Raspberry Pi capturaba video en tiempo real desde la camara
- Las imagenes se transmitian via WiFi a la PC con GPU
- La PC procesaba las imagenes con un modelo de deteccion de objetos
- Las decisiones de navegacion se enviaban de vuelta a la Raspberry Pi
- Los motores del vehiculo respondian a los comandos de direccion

Los desafios tecnicos fueron enormes:

- Latencia en la comunicacion WiFi entre dispositivos
- Procesamiento en tiempo real con hardware limitado
- Deteccion de obstaculos y planificacion de rutas basica
- Calibracion de motores y sensores

El modelo de vision artificial tenia que detectar:
- Obstaculos estaticos (paredes, muebles)
- Obstaculos dinamicos (personas, mascotas)
- Rutas navegables (espacios libres)
- Objetivos especificos (objetos a alcanzar)

Aunque primitivo comparado con los vehiculos autonomos actuales, este proyecto me enseno los fundamentos de la integracion entre vision artificial, toma de decisiones y control robotico.

### Interprete de CAPTCHAs

Otro proyecto fascinante fue entrenar un modelo para interpretar CAPTCHAs con IA. Este proyecto me enseno mucho sobre el procesamiento de texto en imagenes y los desafios unicos que presenta la deteccion de caracteres distorsionados.

**El desafio de los CAPTCHAs:**
- Texto distorsionado intencionalmente para confundir a las maquinas
- Fondos con ruido visual y lineas que interfieren
- Diferentes fuentes y tamanos de texto
- Rotaciones y deformaciones aleatorias

**Mi enfoque fue crear un pipeline que:**
1. Preprocesaba la imagen para reducir el ruido
2. Segmentaba caracteres individuales
3. Clasificaba cada caracter usando una red neuronal convolucional
4. Combinaba los resultados para formar la palabra completa

### Deteccion de Enfermedades en Pandemia

En la pandemia, experimente con modelos para detectar enfermedades. Claramente sabiamos que se venia algo increible, la IA estaba en manos de mucha gente creativa, era solo cuestion de tiempo antes de que llegara la revolucion que vivimos hoy.

Trabaje en modelos para:
- Deteccion de patrones en radiografias de torax
- Analisis de sintomas a partir de imagenes medicas
- Clasificacion de lesiones cutaneas

---

## 3.4 Reflexiones: Del Sueno a la Realidad

Mirando hacia atras, ese sueno de 2013 con el dragon sumerio Kur fue profetico. Sin saberlo, habia comenzado un viaje que me llevaria desde la experimentacion amateur hasta proyectos que realmente impactaban en el mundo real.

Cada proyecto me enseno algo fundamental:

- El detector de plagas me enseno la importancia de la calidad de los datos
- El proyecto con drones me mostro los desafios de la vision artificial en condiciones reales
- El vehiculo autonomo me introdujo a la integracion de sistemas complejos
- Los CAPTCHAs me ensenaron sobre el procesamiento de texto en imagenes
- Los modelos medicos me mostraron la responsabilidad etica de la IA

La evolucion del hardware tambien fue crucial. Desde aquella primera Raspberry Pi sobrecalentada hasta conseguir mi primera GPU, cada mejora tecnologica abria nuevas posibilidades.

Pero lo mas importante fue entender que la IA no es solo sobre algoritmos perfectos, sino sobre resolver problemas reales para personas reales. Cada linea de codigo que escribi entre 2013 y 2022 me acerco mas a esa comprension.

El sueno se habia hecho realidad: las maquinas habian aprendido a "ver", y yo habia aprendido a ensenarles.

---

*Next: [Chapter 4 — The Architecture of Thought](04-architecture.md)*
