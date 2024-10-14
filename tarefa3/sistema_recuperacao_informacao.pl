% ---------------------------------------------
% Base de Dados de Documentos
% ---------------------------------------------

documento(
    id1,
    "Explorando Inteligência Artificial",
    "Ana Silva",
    2021,
    ["Inteligência Artificial", "Machine Learning", "Redes Neurais"],
    "Este artigo explora os conceitos básicos de Inteligência Artificial e suas aplicações em Machine Learning e Redes Neurais."
).

documento(
    id2,
    "Introdução ao Processamento de Linguagem Natural",
    "Carlos Sousa",
    2020,
    ["Processamento de Linguagem Natural", "Linguística", "Inteligência Artificial"],
    "Um estudo introdutório sobre Processamento de Linguagem Natural e sua relação com a linguística e a Inteligência Artificial."
).

documento(
    id3,
    "Avanços em Computação Quântica",
    "Maria Oliveira",
    2022,
    ["Computação Quântica", "Tecnologia", "Física"],
    "Este artigo analisa os avanços recentes na Computação Quântica e suas implicações tecnológicas."
).

documento(
    id4,
    "Técnicas de Data Mining",
    "João Pedro",
    2019,
    ["Data Mining", "Big Data", "Estatística"],
    "Discussão sobre técnicas avançadas de Data Mining aplicadas a grandes volumes de dados (Big Data)."
).

% ---------------------------------------------
% Mecanismos de Recuperação
% ---------------------------------------------

% Consulta por título
consulta_por_titulo(Titulo, Id, Autor, Data, PalavrasChave, Resumo) :-
    documento(Id, Titulo, Autor, Data, PalavrasChave, Resumo).

% Consulta por autor
consulta_por_autor(Autor, Id, Titulo, Data, PalavrasChave, Resumo) :-
    documento(Id, Titulo, Autor, Data, PalavrasChave, Resumo).

% Consulta por palavras-chave
consulta_por_palavra_chave(PalavraChave, Id, Titulo, Autor, Data, Resumo) :-
    documento(Id, Titulo, Autor, Data, PalavrasChave, Resumo),
    member(PalavraChave, PalavrasChave).

% Consulta por combinação de autor e data
consulta_por_autor_data(Autor, Ano, Id, Titulo, PalavrasChave, Resumo) :-
    documento(Id, Titulo, Autor, Data, PalavrasChave, Resumo),
    Data >= Ano.

% ---------------------------------------------
% Operadores Lógicos
% ---------------------------------------------

% Consulta combinada usando AND
consulta_and(Autor, PalavraChave, Id, Titulo, Data, Resumo) :-
    consulta_por_autor(Autor, Id, Titulo, Data, PalavrasChave, Resumo),
    member(PalavraChave, PalavrasChave).

% Consulta combinada usando OR
consulta_or(Autor, PalavraChave, Id, Titulo, Data, Resumo) :-
    consulta_por_autor(Autor, Id, Titulo, Data, PalavrasChave, Resumo);
    consulta_por_palavra_chave(PalavraChave, Id, Titulo, Autor, Data, Resumo).

% Consulta usando NOT
consulta_not(Autor, PalavraChave, Id, Titulo, Data, Resumo) :-
    consulta_por_autor(Autor, Id, Titulo, Data, PalavrasChave, Resumo),
    \+ member(PalavraChave, PalavrasChave).

% ---------------------------------------------
% Mecanismo de Ranqueamento
% ---------------------------------------------

% Rankear por data mais recente
rankear_por_data(ListaDocumentos, ListaOrdenada) :-
    sort(4, @>=, ListaDocumentos, ListaOrdenada).

% ---------------------------------------------
% Interface de Linha de Comando para o Usuário
% ---------------------------------------------

interface_usuario :-
    writeln('Bem-vindo ao Sistema de Recuperação de Informação.'),
    writeln('Escolha uma opção de consulta:'),
    writeln('1. Consultar por Título'),
    writeln('2. Consultar por Autor'),
    writeln('3. Consultar por Palavra-chave'),
    writeln('4. Consultar por Autor e Data'),
    writeln('5. Sair'),
    read(Opcao),
    executar_consulta(Opcao),
    (Opcao \= 5 -> interface_usuario ; true).

executar_consulta(1) :-
    writeln('Digite o título:'),
    read(Titulo),
    findall((Id, Autor, Data, PalavrasChave, Resumo), consulta_por_titulo(Titulo, Id, Autor, Data, PalavrasChave, Resumo), Resultados),
    writeln('Resultados da consulta:'),
    writeln(Resultados).

executar_consulta(2) :-
    writeln('Digite o autor:'),
    read(Autor),
    findall((Id, Titulo, Data, PalavrasChave, Resumo), consulta_por_autor(Autor, Id, Titulo, Data, PalavrasChave, Resumo), Resultados),
    writeln('Resultados da consulta:'),
    writeln(Resultados).

executar_consulta(3) :-
    writeln('Digite a palavra-chave:'),
    read(PalavraChave),
    findall((Id, Titulo, Autor, Data, Resumo), consulta_por_palavra_chave(PalavraChave, Id, Titulo, Autor, Data, Resumo), Resultados),
    writeln('Resultados da consulta:'),
    writeln(Resultados).

executar_consulta(4) :-
    writeln('Digite o autor:'),
    read(Autor),
    writeln('Digite o ano:'),
    read(Ano),
    findall((Id, Titulo, PalavrasChave, Resumo), consulta_por_autor_data(Autor, Ano, Id, Titulo, PalavrasChave, Resumo), Resultados),
    writeln('Resultados da consulta:'),
    writeln(Resultados).

executar_consulta(5) :-
    writeln('Saindo do sistema. Obrigado!').

% ---------------------------------------------
% Casos de Teste
% ---------------------------------------------

testes :-
    writeln('Teste 1: Consulta por Autor "Ana Silva"'),
    findall((Id, Titulo, Data, PalavrasChave, Resumo), consulta_por_autor("Ana Silva", Id, Titulo, Data, PalavrasChave, Resumo), Resultados1),
    writeln(Resultados1),

    writeln('Teste 2: Consulta por Palavra-chave "Inteligência Artificial"'),
    findall((Id, Titulo, Autor, Data, Resumo), consulta_por_palavra_chave("Inteligência Artificial", Id, Titulo, Autor, Data, Resumo), Resultados2),
    writeln(Resultados2).

% Para executar o sistema, chame 'interface_usuario.' na linha de comando.
% Para executar os testes, chame 'testes.' na linha de comando.
