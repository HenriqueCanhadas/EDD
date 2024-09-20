import streamlit as st
import streamlit_authenticator as stauth
import yaml
import requests
import time

# Configurações da página
st.set_page_config(layout="wide")
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
        <div style="text-align: Left">
            <span style="font-size: 50px; font-weight: bold;">SERVMAR</span>
        </div>
        """,
        unsafe_allow_html=True
)

# Função para autenticar o usuário
def authenticate():
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = None

    config_url = 'https://raw.githubusercontent.com/TecnologiaServmar/ProjetoCanhadas/main/config.yaml'
    try:
        response = requests.get(config_url)
        if response.status_code == 200:
            config = yaml.load(response.content, Loader=yaml.SafeLoader)
        else:
            st.error("Falha ao carregar o arquivo de configuração.")
            return
    except Exception as e:
        st.error(f"Erro ao buscar o arquivo de configuração: {e}")
        return

    # Pede as credenciais do usuário
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if username and password:
        # Busca as credenciais no arquivo de configuração
        if username in config['credentials']['usernames']:
            user_credentials = config['credentials']['usernames'][username]
            if password == user_credentials['password']:  # Compara diretamente a senha sem hash
                st.session_state["authentication_status"] = True
                st.session_state["username"] = username
            else:
                st.session_state["authentication_status"] = False
        else:
            st.session_state["authentication_status"] = False
    else:
        st.session_state["authentication_status"] = None

# Função para exibir a mensagem de sucesso temporária
def display_temporary_success_message():
    success_placeholder = st.empty()
    success_placeholder.success("Login Feito, Seja Bem Vindo!")
    time.sleep(3)
    success_placeholder.empty()

# Função principal
def main():
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    # Verifica o estado de autenticação
    if "authentication_status" not in st.session_state:
        st.session_state["authentication_status"] = None

    if st.session_state.get("authentication_status") is None or st.session_state.get("authentication_status") is False:
        authenticate()

    # Verifica se o login foi bem-sucedido
    if st.session_state.get("authentication_status"):
        # Verifica se a mensagem de sucesso já foi exibida
        if not st.session_state.get("success_message_displayed", False):
            display_temporary_success_message()
            st.session_state["success_message_displayed"] = True
        st.write(f"Bem-vindo, {st.session_state.get('username')}!")
        # Chamaria aqui a função do Projeto Canhadas
        # projeto()
    elif st.session_state.get("authentication_status") is False:
        st.error("Usuário e/ou Senha Incorretos")

if __name__ == "__main__":
    main()
