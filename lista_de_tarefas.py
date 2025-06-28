import os
import copy
import json

get = 'lista.json'

def carregar_tarefas():
    with open(get, 'r', encoding='utf8') as arquivo:
        return json.load(arquivo)

tarefas = carregar_tarefas()
    

def listar_tarefas():
    for tarefa in tarefas:
        print(tarefa, sep='\n')

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def limpar():
    os.system('cls')

def desfazer():
    try: tarefas.pop()
    except IndexError:
        print("Nenhuma tarefa para desfazer.")

def refazer():
    try: tarefas.append(lista_reserva[-1]), lista_reserva.pop()
    except IndexError:
        print("Nenhuma tarefa para refazer.")

comandos = ['listar', 'desfazer', 'refazer', 'limpar', 'sair']

lista_reserva = []
resposta = ""

while True:
    print("Comandos: listar, desfazer, refazer, limpar, sair")
    resposta = input("Digite uma tarefa ou um comando: ").strip().lower()
    if resposta == "listar":
        listar_tarefas()
    elif resposta == "desfazer":
        lista_reserva.append(tarefas[-1])
        desfazer()
    elif resposta == "limpar":
        limpar()    
    elif resposta not in comandos:
        adicionar_tarefa(resposta)
    elif resposta == "refazer":
        refazer()
    
    elif resposta == "sair":
        with open(get, 'w', encoding='utf8') as arquivo:
            json.dump(tarefas, arquivo, indent=4)
        break

    print()