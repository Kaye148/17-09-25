import streamlit as st

st.title("Laço de Repetição")

st.write("Escreva um algoritmo que solicite duas notas para um aluno.Caso seja menor que 10, moestre a pergunta novamente.")

nota1 = st.number_input("digite a primeira nota: ", min_value=0, max_value=10)
nota2 = st.number_input("digite a segunda nota: ", min_value=0, max_value=10)

media = (nota1 + nota2) /2

if st.button("calcular a média"):
    st.info(f"média:{media}")