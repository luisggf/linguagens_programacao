import streamlit as st
from util import *
import inspect


response = requests.get(
    'https://pt.wikipedia.org/wiki/Titanic_(filme_de_1997)')

html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')


# inicio da interface
st.title("Informações do Filme")

st.markdown("""
# Como foi feito o exercício da Lista III

Essa aplicação consiste em uma interface via Streamlit que exibe informações sobre o filme Titanic. Abaixo estão os passos realizados para desenvolver essa aplicação:

1. **Instalação das Bibliotecas Necessárias**:
    - Streamlit: Biblioteca para criar interfaces web interativas.
    - Newspaper3k: Biblioteca para extração de dados de artigos.
    - Requests: Biblioteca para fazer requisições HTTP.
    - BeautifulSoup: Biblioteca para parsing de HTML e extração de dados.

2. **Coleta de Dados**:
    - Foi utilizado a URL da página da Wikipédia do filme Titanic.
    - Usamos a biblioteca Newspaper3k para fazer o download e parsing do conteúdo do artigo.
    - Realizamos uma requisição GET para obter o HTML completo da página.

3. **Parsing do HTML**:
    - Foi utilizado BeautifulSoup para fazer o parsing do HTML e extrair as informações necessárias.

4. **Criação da Interface com Streamlit**:
    - Criamos botões para exibir diferentes informações sobre o filme.
    - Foi utilizado a função `inspect.getsource` para exibir o código fonte das funções que extraem os dados.

5. **Funções Utilizadas**:
    - `get_mov_title(source_cod e)`: Obtém o título do filme.
    - `get_genres(soup)`: Obtém os gêneros do filme.
    - `get_cast(soup)`: Obtém o elenco do filme.
    - `get_release_date(soup)`: Obtém a data de lançamento do filme.
    - `get_awards(soup)`: Obtém os prêmios recebidos pelo filme.
    - `get_music(soup)`: Obtém o compositor principal do filme.

6. **Exibição do Código Fonte**:
    - Foi utilizado a biblioteca `inspect` para exibir o código fonte das funções responsáveis por extrair os dados.

Esperamos que este exercício seja útil para entender como criar uma aplicação web interativa usando Streamlit e como extrair e processar dados da web.

## Informações do Filme
""")


def show_function_code(function):
    """Exibe o código fonte da função"""
    code = inspect.getsource(function)
    st.code(code, language='python')


# Adicionando botões e containers para cada seção
if st.button('Exibir Título do Filme'):
    title = get_movie_title(soup)
    st.write(title)
    show_function_code(get_movie_title)

if st.button('Exibir Gêneros'):
    genres = get_genres(soup)
    st.write(", ".join(genres) if genres else "Informação não encontrada")
    show_function_code(get_genres)

if st.button('Exibir Elenco'):
    cast = get_cast(soup)
    st.write(", ".join(cast) if cast else "Informação não encontrada")
    show_function_code(get_cast)

if st.button('Exibir Data de Lançamento'):
    release_dates = get_release_date(soup)
    st.write(", ".join(release_dates)
             if release_dates else "Informação não encontrada")
    show_function_code(get_release_date)

if st.button('Exibir Prêmios'):
    awards = get_awards(soup)
    st.write(", ".join(awards) if awards else "Informação não encontrada")
    show_function_code(get_awards)

if st.button('Exibir Compositor Principal'):
    music = get_music(soup)
    st.write(", ".join(music) if music else "Informação não encontrada")
    show_function_code(get_music)

if st.button('Exibir Primeiro Parágrafo'):
    paragraph = get_nth_paragraph(soup, 1)
    st.write(paragraph if paragraph else "Informação não encontrada")
    show_function_code(get_nth_paragraph)
