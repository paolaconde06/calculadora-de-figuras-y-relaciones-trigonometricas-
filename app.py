import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
st.title("Calculadora de figuras y relaciones trigonometricas")
#Parte 1 -Figuras geometricas
st.header("Parte 1-Figuras geometricas")
figura=st.selectbox("Selecciona una figura:",["Circulo","triangulo","Rectangulo","Cuadrado"])
if figura=="Circulo":
  r=st.number_input("Radio(r):",min_value=0.0)
  area=np.pi*r**2
  perimetro=1*np.pi*r
  elif figura=="Triangulo"
  
  
