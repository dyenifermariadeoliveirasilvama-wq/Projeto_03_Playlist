import streamlit as st

# Dados de exemplo
generos = ["Pop", "Trap", "MPB", "Sertanejo"]

# Dicionário relacionando gêneros aos seus livros
musicas_por_genero = {
    "Pop": ["Michael Jackson", "Bruno Mars", "Harry Styles"],
    "Trap": ["Veigh", "Brandão", "Alee"],
    "MPB": ["Jorge Vercilo","Djavan", "Tim maia"],
    "Sertanejo": ["Matheus e Kauan", "Marilia mendoça", "Simone e Simaria"]
}

# Selectbox para escolher o gênero
st.sidebar.image("logo.png")
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    musica_selecionado = st.sidebar.selectbox(
    "Selecione o livro:", 
    musicas_por_genero[genero_selecionado])
    
# Mostrar apenas a música selecionada
if genero_selecionado and musica_selecionado:
   st.write(f" ** musica selecionado :** {musica_selecionado}")
   st.write(f" ** Gênero :** {genero_selecionado}")
   st.image(f"{musica_selecionado}.png")