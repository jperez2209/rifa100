import streamlit as st
import random
from datetime import datetime
from PIL import Image

# Generar lista de números de 3 dígitos desde 000 hasta 999
numeros = [f"{n:02d}" for n in range(100)]

st.set_page_config(
    page_title= "Quick Luck",
    page_icon= "icon2.ico"
)

img = Image.open("QL.png")
st.image(img, use_container_width=True)
#st.title("Bienvenido a Quick Luck")

if st.button("JUGAR"):
    # Seleccionar un elemento aleatorio
    numero_aleatorio = random.choice(numeros)

    # Obtener la fecha actual en formato AAAA/MM/DD
    fecha_actual = datetime.now().strftime("%Y/%m/%d")

    # Mostrar el resultado
    st.success(f"**El número ganador es:** {numero_aleatorio}")
    st.write(f"**Fecha de selección:** {fecha_actual}")