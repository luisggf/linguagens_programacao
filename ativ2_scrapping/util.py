import re
from bs4 import BeautifulSoup
import requests


def get_nth_paragraph(soup, n):
    """
    Retorna o texto do n-ésimo parágrafo <p> da página.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup da página.
        n (int): Índice do parágrafo desejado (1 para o primeiro parágrafo).

    Returns:
        str: Texto do n-ésimo parágrafo ou None se não houver parágrafos suficientes.
    """
    paragraphs = soup.find_all('p')
    if len(paragraphs) >= n:
        return paragraphs[n-1].get_text()
    else:
        return None


def get_movie_title(soup):
    """
    Retorna o conteúdo do elemento <h1> com id="firstHeading".

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup da página.

    Returns:
        str: Título do filme ou mensagem de erro se não for encontrado.
    """
    title_element = soup.find('h1', id='firstHeading')
    if title_element:
        return title_element.get_text()
    else:
        return "Failed to find the title of the movie."


def get_genres(soup):
    """
    Retorna a lista de gêneros do filme.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup da página.

    Returns:
        list: Lista de gêneros ou lista vazia se não forem encontrados.
    """
    all_tds = soup.find_all('td', attrs={
                            "style": "vertical-align: top; text-align: left; font-weight:bold; text-align:left"})
    for td in all_tds:
        if "Gênero" in td.get_text(strip=True):
            genres_td = td.find_next_sibling('td')
            if genres_td:
                genres_list = genres_td.find_all('a')
                genres = [a.get_text(strip=True) for a in genres_list]
                return genres
    return []


def get_cast(soup):
    """
    Retorna a lista de membros do elenco do filme.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup da página.

    Returns:
        list: Lista de membros do elenco ou lista vazia se não forem encontrados.
    """
    all_tds = soup.find_all('td', attrs={
                            "style": "vertical-align: top; text-align: left; font-weight:bold; text-align:left"})
    for td in all_tds:
        if "Elenco" in td.get_text(strip=True):
            cast_td = td.find_next_sibling('td')
            if cast_td:
                cast_list = cast_td.find_all('a')
                cast = [a.get_text(strip=True) for a in cast_list]
                return cast
    return []


def get_music(soup):
    """
    Retorna a lista de compositores principais do filme.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup da página.

    Returns:
        list: Lista de compositores principais ou lista vazia se não forem encontrados.
    """
    all_tds = soup.find_all('td', attrs={
                            "style": "vertical-align: top; text-align: left; font-weight:bold; text-align:left"})
    for td in all_tds:
        if "Música" in td.get_text(strip=True):
            music_td = td.find_next_sibling('td')
            if music_td:
                music_list = music_td.find_all('a')
                musics = [a.get_text(strip=True) for a in music_list]
                return musics
    return []


def get_awards(soup):
    """
    Retorna a lista de prêmios do filme.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup da página.

    Returns:
        list: Lista de prêmios ou lista vazia se não forem encontrados.
    """
    awards = []
    potential_award_elements = soup.find_all(['p', 'ul', 'li'])
    for element in potential_award_elements:
        if "premio" in element.get_text(strip=True).lower() or "award" in element.get_text(strip=True).lower():
            award_links = element.find_all('a')
            for link in award_links:
                award_text = link.get_text(strip=True)
                if award_text:
                    awards.append(award_text)
    return awards


def get_release_date(soup):
    """
    Retorna a lista de datas de lançamento do filme.

    Args:
        soup (BeautifulSoup): Objeto BeautifulSoup da página.

    Returns:
        list: Lista de datas de lançamento ou lista vazia se não forem encontradas.
    """
    all_tds = soup.find_all('td', attrs={
                            "style": "vertical-align: top; text-align: left; text-align:left"})
    for td in all_tds:
        div = td.find('div', attrs={'style': 'margin-left: 0em;'})
        if div:
            release_list = div.find_all('li')
            release_dates = [li.get_text(strip=True) for li in release_list]
            return release_dates
    return []
