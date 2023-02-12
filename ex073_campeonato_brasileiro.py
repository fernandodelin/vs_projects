#Tabela Brasileirão 2023
print('-='*15)
times = ('América Mineiro', 'Athletico Paranaense',
        'Atlético Mineiro', 'Bahia', 'Botafogo',
        'Corinthians', 'Coritiba', 'Cruzeiro',
        'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza',
        'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
        'Red Bull Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print('-='*15)
print(f'Lista de times {times}')
print('-='*15)
print(f'Os 5 primeiros são {times [0:5]}')
print('-='*15)
print(f'Os 4 ultimos são {times [-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O Cruzeiro está na {times.index("Cruzeiro")+1}ª posição.')
print('-='*15)