import streamlit as st
import time

st.title("atividade_login_senha")

login_salvo ="zezinho69"
senha_salva = "69zezinho"

login = st.text_input("informe seu login: ")
senha = st.text_input("digite sua senha: ", type="password")

if st.button("verificar"):
    if login == login_salvo and senha ==senha_salva:
        st.success("bem vindo!")
    else:
        st.warning("login ou senha invalidas")