import streamlit as st
import pandas as pd

st.title("🎯 Loto 6/49 - Frecvență Numere")

uploaded_file = st.file_uploader("Încarcă fișierul Excel cu extrageri", type=["xlsx"])
if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
        df = df.dropna(subset=['Data'])

        draw_cols = ['Nr.1','Nr.2','Nr.3','Nr.4','Nr.5','Nr.6']
        numbers = pd.Series(df[draw_cols].values.ravel())
        freq = numbers.value_counts().sort_values(ascending=False)

        st.subheader("🔢 Top 10 Numere Frecvente")
        st.dataframe(freq.head(10).reset_index().rename(columns={'index': 'Număr', 0: 'Frecvență'}))

    except Exception as e:
        st.error(f"Eroare la procesare: {e}")
