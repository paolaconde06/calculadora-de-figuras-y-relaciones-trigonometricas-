import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt
st.title("Calculadora de figuras y relaciones trigonometricas")
#Parte 1 -Figuras geometricas
st.header("Parte 1-Figuras geometricas")
figura=st.selectbox("Selecciona una figura:",["Circulo","Triangulo","Rectangulo","Cuadrado"])
if figura=="Circulo":
  r=st.number_input("Radio(r):",min_value=0.0)
  area=np.pi*r**2
  perimetro=1*np.pi*r
if figura=="Rectangulo":
  b=st.number_input("Base(b):",min_value=0.0)
  h=st.number_input("Altura(h):",min_value=0.0)
  area=b*h
  perimetro=2*(b+h)
if figura=="Cuadrado":
  l=st.number_input("Lado(l):",min_value=0.0)
  area=l**2
  perimetro=4*l
if figura=="Triangulo":
  b=st.number_input("Base(b):",min_value=0.0)
  h=st.number_input("Altura(h):",min_value=0.0)
  a=st.number_input("Lado(A):",min_value=0.0)
  c=st.number_input("Lado(c):",min_value=0.0)
  area=0.5*b*h
  perimetro=a+b+c
#Mostrar resultados 
if st.button("Calcular"):
  st.success(f"Area={area:.2f}")
  st.success(f"Perimetro={perimetro:.2f}")
  #Visualizacion 
st.header("Parte 2 - Visualizacion")
color=st.color_picker("Selecciona un color para la figura:","#1f77b4")
fig,ax=plt.subplots()
if figura=="Circulo":
  circle=plt.Circulo((0,0),r,color=color,fill=False)
  ax.add_artist(circle)
  ax.set_xlim(-r*1.2,r*1.2)
  ax.set_ylim(-r*1.2,r*1.2)
if figura=="Rectangulo":
  rect=plt.Rectangulo((-b/2,-h/2),b,h,color=color,fill=False)
  ax.add_artist(rect)
  ax.set_xlim(-b,b)
  ax.set_ylim(-h,h)
if figura=="Cuadrado":
  rect = plt.Cuadrado((-l/2, -l/2), l, l, color=color, fill=False)
  ax.add_artist(rect)
  ax.set_xlim(-l, l)
  ax.set_ylim(-l, l)
if figura == "Triángulo":
  puntos = np.array([[0, 0], [b, 0], [b/2, h]])
  tri = plt.Polygon(puntos, color=color, fill=False)
  ax.add_artist(tri)
  ax.set_xlim(-b/2, b*1.2)
  ax.set_ylim(-h*0.5, h*1.2)
ax.set_aspect('equal')
st.pyplot(fig)
# Parte 3 — Relaciones trigonométricas
st.header("Parte 3 — Relaciones trigonométricas")
funcion = st.selectbox("Selecciona una función trigonométrica:", ["sin(x)", "cos(x)", "tan(x)"])
rango = st.slider("Rango (múltiplos de π):", 1, 4, 2)
amplitud = st.slider("Amplitud:", 0.1, 2.0, 1.0)
x = np.linspace(0, rango * np.pi, 300)
if funcion == "sin(x)":
  y = amplitud * np.sin(x)
if funcion == "cos(x)":
  y = amplitud * np.cos(x)
if funcion == "tan(x)":
  y = amplitud * np.tan(x)
  y[np.abs(y) > 10] = np.nan  # evita líneas verticales infinitas
