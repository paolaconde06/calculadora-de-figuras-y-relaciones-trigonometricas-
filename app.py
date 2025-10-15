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
  if figura=="Triangulo":
    b=st.number_input("Base(b):",min_value=0.0)
    h=st.number_input("Altura(h):",min_value=0.0)
    a=st.number_input("Lado (A):",min_value=0.0)
    c=st.number_input("Lado (c):",min_value=0.0)
    area=0.5*b*h
    perimetro=a+b+c
  if figura=="Rectangulo":
    b=st.number_input("Base(b):",min_value=0.0)
    h=st.number:input("Altura(h):",min_value=0.0)
    area=b*h
    perimetro=a+b+c
  if figura=="Cuadrado":
    l=st.number_input("Lado(l):"min_value=0.0)
    
