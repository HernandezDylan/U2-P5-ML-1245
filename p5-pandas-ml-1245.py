import numpy as np
import pandas as pd
# Hernandez Dylan Nc 1245
## datos
datos_alumno =[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2],
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
df=pd.DataFrame(datos_alumno,columns=['ci','marcas','paquetes'])
print(df)
#datos a partir de un diccionario
alumno_diccionario={
    "nombre":["Eliseo","Joel","Pedro","Nicole","Dylan","jesse"],
    "califa": ["60","90","100","80","70","50"],
    "edad":["64","15","16","16","18","14"],
}

Estudiantes =pd.DataFrame(alumno_diccionario)
print(Estudiantes)

print("Hernadez Dylan NC=1245")