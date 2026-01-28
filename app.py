import streamlit as st


st.title("Calculadora de Propinas")


st.sidebar.header("Datos")

total_cuenta = st.sidebar.number_input("Monto total ($)", min_value=0.0, value=100.0)
porcentaje = st.sidebar.number_input("Porcentaje de propina", min_value=0, max_value=100, value=15)

if st.sidebar.button("Calcular"):
 
    propina = total_cuenta * (porcentaje / 100)
    
    st.metric(label="Propina sugerida", value=f"${propina:.2f}")
    st.write(f"Total a pagar: ${total_cuenta + propina:.2f}")

