from parsing_functions import parse_champions, get_special_champion


links = {
    'popular': 'https://www.leagueofgraphs.com/champions/builds',
    'winrate': 'https://www.leagueofgraphs.com/champions/builds/by-winrate',
    'banrate': 'https://www.leagueofgraphs.com/champions/builds/by-banrate'
}

while True:
    command = input('''Добро пожаловать! Чтобы посмотреть список чемпионов, отсортированных по популярности, введите "popular".
        Чтобы посмотреть информацию по конкретному чемпиону, введите его имя. Чтобы выйти, введите "exit"...\n''')
    if command == 'exit':
        break
    elif command == 'popular':
        print(parse_champions(links['popular']))
    else:
        print(get_special_champion(command))


# работает только для popular

#print(parse_champions(links['winrate']))
get_special_champion('akali')

