import streamlit as st
import time

#Configurações da página
st.markdown(
    """
    <style>
    html, body, [class*="View"] {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
    }
    .reportview-container {
        margin: 10px;
        flex: 1;
    }
    .main .block-container {
        width: calc(100% - 15px);  /* Subtrai as margens */
        padding: 0;
        margin: 10px;
    }

    /* Estilos responsivos para diferentes tamanhos de tela */
    @media (max-width: 768px) {
        .reportview-container {
            margin: 10px; /* Menor margem para telas menores */
        }
        .main .block-container {
            width: calc(100% - 50px); /* Ajusta a largura para telas menores */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Definir as credenciais diretamente no código
USERS = {
    "usuario1": "senha1",
    "usuario2": "senha2",
    # Adicione mais usuários conforme necessário
}

# Função para executar o Projeto Canhadas
def projeto():
    import EDD_Compilation
    EDD_Compilation.main()

def login():
    # Adicionando uma imagem
    image_url = "https://raw.githubusercontent.com/SistemaAmbitech/EDD/main/img/Ativo%201.png"
    st.image(image_url, width=450)

    st.title("Login")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Entrar")

    if login_button:
        if username in USERS and USERS[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['show_success'] = True
        else:
            st.error("Usuário ou senha incorretos.")


# Função para mensagem temporária de sucesso para o login
def display_temporary_success_message():
    if st.session_state.get('show_success', False):
        placeholder = st.empty()  # Cria um placeholder para a mensagem
        placeholder.success("Login realizado com sucesso! Seja bem-vindo!")
        time.sleep(3)  # Aguarda 3 segundos
        placeholder.empty()  # Remove a mensagem
        st.session_state['show_success'] = False  # Reseta a flag

def main():

    #hide_menu_style = """
    #        <style>
    #        #MainMenu {visibility: hidden;}
    #            footer {visibility: hidden;}
    #            header {visibility: hidden;}
    #        </style>
    #        """
    #st.markdown(hide_menu_style, unsafe_allow_html=True)

    # Inicializa o estado de autenticação, se não estiver definido
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['show_success'] = False

    if not st.session_state['logged_in']:
        login()
    else:
        # Exibe a mensagem de sucesso se aplicável
        display_temporary_success_message()
        # Chama a função do Projeto Canhadas
        projeto()

if __name__ == "__main__":
    main()
