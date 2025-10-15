import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
st.title("Calculadora de figuras y relaciones trigonometricas")
if seccion==("Parte1:Figuras geometricas"):
  st.header("Parte 1-Figuras geometricas")
  figura=st.selectbox("Seleciona una figura ",["Circulo","Triangulo","Rectangulo","Cuadrado]
  st.session_state.figura_seleccionada=figura
  parametros={}
  if figura=="Circulo":
    r=st.number 
