from requests_html import HTMLSession

MAX_TIME = 80

def parse_champions(src_url):
    session = HTMLSession()

    # URL веб-сайта
    url = src_url

    # Отправка запроса и получение содержимого страницы
    response = session.get(url, timeout=MAX_TIME)

    # Парсинг HTML-содержимого и выполнение JavaScript
    response.html.render(timeout=MAX_TIME)
    dom_tree = response.html
    print(dom_tree.html)
    table = response.html.find('table', first=True)

    # Проверка, найдена ли таблица
    if table:
        # Извлекаем содержимое ячеек таблицы
        rows = table.find('tr')
        text = ''
        for row in rows:
            cells = row.find('td')
            for cell in cells:
                if cell.text is not None and cell.text.strip() != '' and (cell.text[0].isdigit() or cell.text[0].isalpha()):
                    text += cell.text + '\t'
            text += '\n'
        return text
    else:
        return "Таблица не найдена на странице."


def get_special_champion(name):
    session = HTMLSession()
    url = f'https://www.leagueofgraphs.com/champions/builds/{name}'
    response = session.get(url, timeout=MAX_TIME)
    info = []
    if response.html.find('#graphDD1', first=True) is None:
        return 'Чемпиона с таким именем не найдено'
    for i in range(3):
        info.append(response.html.find(f'#graphDD{i+1}', first=True).text)
    return f'''Информация о {name}:
    Популярность: {info[0]}
    Винрейт: {info[1]}
    Банрейт: {info[2]}'''


