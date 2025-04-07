import streamlit as st
import pandas as pd
import plotly.express as px

# Ruta del archivo (cambiá esto por tu ruta local si no estás en ChatGPT)
excel_path = r"C:\Users\fhamedh\Desktop\nacio.xlsx"

# Todas las hojas por nombre real
individual_sheets = [
    'AMBA 2019',
    'AMBA 2022',
    'EMBA 2018 FDS',
    'EMBA JULIO 2018',
    'EMBA FDS 2020',
    'EMBA 3X3 2020',
    'EMBA 3X3 2021',
    'EMBA FDS 2021',
    'EMBA FDS 2022',
    'EMBA 3X3 2022',
]
total_sheet_name = 'TOTAL'

# Cargar las hojas individuales
sheets_dict = pd.read_excel(excel_path, sheet_name=individual_sheets)

# Concatenar todos los DataFrames para crear el TOTAL
df_total = pd.concat(sheets_dict.values(), ignore_index=True)

# Agregar la hoja TOTAL al diccionario
sheets_dict[total_sheet_name] = df_total

# Crear tabs (incluyendo TOTAL al final)
sheet_names = individual_sheets + [total_sheet_name]
tabs = st.tabs(sheet_names)

# Generar los gráficos para cada tab
for i, sheet_name in enumerate(sheet_names):
    with tabs[i]:
        st.title(f"Distribución de Nacionalidades - {sheet_name}")
        df_nacio = sheets_dict[sheet_name]

        if "Nacionalidad" in df_nacio.columns:
            nacionalidades = df_nacio['Nacionalidad'].value_counts()

            fig_pie = px.pie(
                values=nacionalidades.values,
                names=nacionalidades.index,
                title="Distribución de Nacionalidades",
                hole=0.3
            )
            fig_pie.update_traces(
                textinfo='percent+label',
                hovertemplate='%{label}<br>Cantidad: %{value}<br>Porcentaje: %{percent}'
            )
            st.plotly_chart(fig_pie)
        else:
            st.error("La hoja no contiene una columna llamada 'Nacionalidad'.")
