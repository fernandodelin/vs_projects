#colocando cores no terminal
#sempre ira começar com \033[estilo da fonte; texto; background m
'''estilo

0 sem formatação
1 negrito
4 sublinhado
7 negativo(cores invertidas)

texto

30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 roxo
36 azul claro
37 cinza

Background

40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 roxo
46 azul claro
47 cinza
'''
print('\33[7;30;41mHello motherfucker!\033[m')

