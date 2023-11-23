import pandas as pd
import streamlit as st #pip install streamlit
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.write("""
# Tutorial Streamlit para PF Codo a Codo
Pueden encontrar el repo en el siguiente enlace https://github.com/HX-FNegrete/streamlit-mlops
Para hacer el deply directo desde Streamlit, leer la documentación oficial aquí: https://streamlit.io/cloud
Para hacer el deploy de Streamlit con Render, se puede seguir este tutorial: https://github.com/HX-FNegrete/render-fastapi-tutorial
""")

df = pd.read_csv('DataAnalyst.csv')
#print(df)

st.write("""
## Top 5 ciudades con más anuncios laborales:
""")
value_counts = df.Location.value_counts()
top_5 = value_counts.nlargest(5) #usamos solo el top 5 para gráficar
# Cramos gráfico
st.bar_chart(top_5)


#Creación de nueva columna
df["States"] = df["Location"].str.split(", ").str[-1]


st.write("""
## Gráfico barras de los estados de USA con más anuncios laborales:
""")
plt.figure(figsize=(12, 10))
sns.countplot(data=df, x=df['States'])
st.pyplot(plt)


st.write("""
### Primer insight encontrado: 
Acá ya nos encontramos con un primer insight: En el primer gráfico, obtuvimos que el valor que más se repetía era el de la Ciudad de Nueva York. En el segundo gráfico (primera columna color rosa), se puede observar como esto es cierto. El problema es que el Estado de California figura con más entradas. Esto significa que, si bien NYC aparece más veces, en el agregado, hay más ciudades de California con anuncios de empleo.   

¿Se podría decir que hay más chances de conseguir un trabajo en California que en Nueva York?
Nos restan más análisis para poder determinar esto. 
""")

st.write("""
## Ejemplo gráfico interactivo con plotly:
""")
# Ejemplo de segundo gráfico con plotly y hacer algo más interactivo:
# Creamos el plot
fig = px.bar(df, x="States")

# Add hover text
fig.update_traces(hoverinfo="all")

# Render the plot in Streamlit
st.plotly_chart(fig)

