import streamlit as st

# Título y autor
st.title("Mi primera app")
st.write("Esta app fue elaborada por Albeiro Jose Burbano Tobar")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Saludo personalizado
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
