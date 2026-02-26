import streamlit as st
import random
import pandas as pd

st.header('Lanzar una moneda')

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    results = []
    means = []
    
    for i in range(1, number_of_trials + 1):
        flip = random.choice([0, 1])
        results.append(flip)
        means.append(sum(results) / len(results))
    
    st.write(f'Experimento con {number_of_trials} intentos completado.')
    
    df = pd.DataFrame({
        'iteraciones': range(1, number_of_trials + 1),
        'resultado': results,
        'media': means
    })
    
    st.line_chart(df.set_index('iteraciones')['media'])
    st.dataframe(df)