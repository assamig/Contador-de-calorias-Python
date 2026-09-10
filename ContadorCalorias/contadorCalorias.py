import json
import rich
from rich import print
import time
import sys 


arquivo = open("dados_user_calorias.json", "r")
dados = json.load(arquivo)
arquivo.close()






def salvar_dados():
    with open("dados_user_calorias.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def adicionar_usuario(nome, idade, peso, altura, objetivo):




    novo_user = {"user": {
                 "name": nome,
                  "age": idade,
                  "weight": peso,
                  "height": altura,
                  "objective": objetivo,
                  "meals": []
        
    }
}
    dados.append(novo_user)
    

def adicionar_refeicao(nome, nome_refeicao, calorias):
    procurar = procurar_user(nome)
    procurar["user"]["meals"].append({"refeicao":nome_refeicao, "calories": calorias})
    salvar_dados()



def procurar_user(nome):
    for user in dados:
        if nome.lower() == user["user"]["name"].lower():
            return user
            
    else:
        print("[bold red]Usuário não encontrado![bold red]")
   
        
    


def total_calorias(nome):
    soma = 0
    procurar = procurar_user(nome)
    if procurar:
        for refeicao in procurar['user']['meals']:
            soma += refeicao["calories"]

        print(f"[bold green]Total de calorias: {soma}kcals")

    salvar_dados()
    return soma
        

def consultar_user(nome):
    procurar = procurar_user(nome)

    if procurar:
        print("[bold green]-------------------------------------[bold green]")
        print(f"[bold green]Olá {nome}, esses são os seus dados:[bold green]")
        print("[bold green]-------------------------------------[bold green]")
        print(f"[bold green] Nome: {procurar['user']['name']}[bold green]")
        print(f"[bold green] Idade: {procurar['user']['age']}[bold green]")
        print(f"[bold green] Peso: {procurar['user']['weight']}[bold green]")
        print(f"[bold green] Altura: {procurar['user']['height']}[bold green]")
        print(f"[bold green] Objetivo: {procurar['user']['objective']}[bold green]")
        print("[bold green]-------------------------------------[bold green]")
        for refeicao in procurar["user"]["meals"]:
            print(f"[bold green]Refeição: {refeicao["refeicao"]}[bold green]")
            print(f"[bold green]Calorias: {refeicao["calories"]}[bold green]")
        

def cadastro():
    time.sleep(1)
    nome = input("Qual o seu nome?: ").lower().strip()
    idade = int(input("Quantos anos você tem: "))
    peso = float(input("Quanto você pesa?: "))
    altura = float(input("Qual a sua altura: "))
    objetivo = int(input("Qual seu objetivo? Digite sua opção: 1. Emagrecer | 2. Ganhar peso | 3. Manter|: "))
    adicionar_usuario(nome, idade, peso, altura, objetivo)
    salvar_dados()

def reiniciar_dia(nome):
    procurar = procurar_user(nome)
    if procurar:
        dados["user"]["meals"] = []
        salvar_dados()



def decisao_inteligente(nome):
    procurar = procurar_user(nome)
    peso_atual = procurar['user']['weight']
    fator = procurar['user']['objective']
    total = total_calorias(nome)
    deficit = peso_atual * 20
    superavit = peso_atual * 40
    manutencao = peso_atual * 30

    faixa_tolerancia1 = deficit + ((deficit * 20)/100)
    faixa_tolerancia2 = superavit + ((superavit * 20)/100)
    faixa_tolerancia3 = manutencao + ((manutencao * 20)/100)


    if procurar:
        if fator == 1:
            print(f"[bold green]Seu Deficit diário é de {deficit}kcals")
            time.sleep(3)
            if total <= deficit:
                print("[bold green]Você está em Deficit calórico para o seu objetivo de Emagrecimento[bold green]")
            elif total > deficit and total <= faixa_tolerancia1:
                print("[bold green]Suas calorias totais diarias ainda estão numa faixa de tolerãncia[bold green]")
                print("[bold green]Você ainda está em Deficit calórico mesmo assim para o seu objetivo de Emagrecimento[bold green]")
            elif total > faixa_tolerancia1 and total <= manutencao:
                print("[orange1]Você está próximo de sua faixa de Manutenção calórica[orange1]")
            elif total >= manutencao or total < faixa_tolerancia3:
                print("[orange1]Você está na sua faixa de Manutenção calórica[orange1]")
            elif total > faixa_tolerancia3 and total < superavit:
                print("[orange1]Você ficou próximo de seu Superavit calórico[orange1]")
            elif total > superavit:
                print("[orange1]Você ficou em Superavit calórico[orange1]")
            


            
        if fator == 2:
            print(f"[bold green]Seu Superavit diário é de {superavit}kcals")
            if total >= superavit or total >= faixa_tolerancia2:
                print("[bold green]Você está em Superavit calórico para o seu objetivo de Ganho de Massa[bold green]")
            elif total < superavit and total >= manutencao:
                print("[orange1]Você não atingiu seu superavit diário[orange1]")
            elif total > deficit or total < manutencao:
                print("[orange1]Você está perto da sua faixa de Manutenção calórica[orange1]")
            elif total <= deficit:
                print("[orange1]Você está em deficit calórico[orange1]")
                

        if fator == 3:
            print(f"[bold green]Sua Faixa de Manuntenção é de {manutencao}kcals")
            if total == manutencao or total >= faixa_tolerancia3:
                print("[bold green]Você está em Manutenção calórica para o seu objetivo de Manter peso[bold green]")
            elif total < manutencao and total > deficit:
                print("[orange1]Você está próximo da sua Manutenção calórica[orange1]")
            elif total > faixa_tolerancia3 and total < superavit:
                print("[orange1]Você está próximo de seu Superavit calórico[orange1]")
            elif total >= superavit:
                print("[bold orange]Você ficou em Superavit calórico para o seu objetivo de Manutenção de Peso[orange1]")
            elif total <= deficit:
                print("[orange1]Você está em deficit calórico[orange1]")
                



            
def botao_adicionar(nome):
    procurar = procurar_user(nome)
    if procurar:
        print("[bold green]Deseja adicionar uma nova refeição?[bold green]")
        decisao = input("S pra sim | N pra não | F para Sair |: ").upper().strip()
        if decisao == "S":
            print("[bold green]Adicione uma refeição ou digite F para sair[bold green]")
            refeicao = input("Adicionar refeição: ")
            if refeicao.upper() == "F":
                print("Saindo")
                sys.exit()
            else:   
                calorias = int(input("Calorias da refeição: "))
                adicionar_refeicao(nome, refeicao, calorias)
                decisao_inteligente(nome)


        elif decisao == "N":
            print("[bold green]Deseja encerrar o dia?")
            decisao1 = input("S pra sim | N pra não | F para Sair |: ").upper().strip()
            if decisao1 == "S":
                reiniciar_dia(nome)
                print("[bold green]Dia encerrado[bold green]")
                sys.exit()
            elif decisao1 == "N":
                botao_adicionar(nome)
            elif decisao1 == "F":
                print("Saindo...")
                sys.exit()
        elif decisao == "F":
            print("Saindo...")
            sys.exit()
        
        
    
        


            





def menu():
    while True:
        print("[bold green]--------------------------------------[bold green]")
        print("[bold green]Bem vindo ao seu contador de calorias![bold green]")
        entrada = input("Digite o seu nome: ").lower().strip()
        procurar = procurar_user(entrada)
        if procurar:
            print(f"[bold green]Olá {entrada}, bem vindo de volta!")
            while True:
                print("[bold green]1. Adicionar refeição")
                print("[bold green]2. Consultar informações")
                print("[bold green]3. Sair[bold green]")
                decisao_inteligente(entrada)
                decisao = int(input("Digite sua opção: "))
                try:
                    if decisao == 1:
                        time.sleep(2)
                        botao_adicionar(entrada)
                    elif decisao == 2:
                        time.sleep(2)
                        consultar_user(entrada)
                    elif decisao == 3:
                        print("Saindo...")
                        break
                    else:
                        print("[bold red]Digite uma opção válida![bold red]")
                except ValueError:
                    print("[bold red]Digite uma opção válida![bold red]")
            
        else:
            print("[bold green]Faça o seu cadastro![bold green]")
            cadastro()



menu()
              





     
menu()
              





