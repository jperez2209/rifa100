import streamlit as st
import random
from datetime import datetime
import pytz
from PIL import Image

# Generar lista de números de 3 dígitos desde 000 hasta 999
numeros = [f"{n:02d}" for n in range(100)]

st.set_page_config(
    page_title="Quick Luck",
    page_icon="icon2.ico"
)

img = Image.open("QL2.png")
st.image(img, use_container_width=True)

if st.button("JUGAR"):
    # Seleccionar un número aleatorio
    numero_aleatorio = random.choice(numeros)

    # Definir la zona horaria de Colombia
    zona_horaria_colombia = pytz.timezone("America/Bogota")

    # Obtener la fecha y hora actual en la zona horaria de Colombia con formato de MySQL
    fecha_hora_colombia = datetime.now(zona_horaria_colombia).strftime("%Y-%m-%d %H:%M:%S")

    # Mostrar el resultado
    st.success(f"**El número ganador es:** {numero_aleatorio}")
    st.write(f"**Fecha y hora de selección:** {fecha_hora_colombia}")
