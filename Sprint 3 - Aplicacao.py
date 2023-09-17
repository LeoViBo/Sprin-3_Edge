import pandas as pd
import time as tm

'''FUNÇÕES GERAIS'''

def _escolhaOpcao(texto, opcoes):
    print(pd.DataFrame({texto: opcoes}))
    opcao = input("Escolha a opção digitando o número correspondente:\n")
    while not opcao.isnumeric():
        opcao = input("Digite Apenas o número.\nEscolha a opção digitando o número correspondente:\n")
    opcao = int(opcao)
    while not opcao in range(len(opcoes)):
        opcao = input("Digite uma opção válida.\nEscolha a opção digitando o número correspondente:\n")
        while not opcao.isnumeric():
            opcao = input("Digite Apenas o número.\nEscolha a opção digitando o número correspondente:\n")
        opcao = int(opcao)
    return opcao

def _verificarIsNum(texto):
    num = input(texto)
    while not num.isnumeric():
        print("Digite apenas números.")
        num = input(texto)
    num = int(num)
    return num

def _textoComDelay(segundos, texto):
    print(texto)
    tm.sleep(segundos)
    print("")
    return

def _printarValvulas(usuario):
    if not listaLogins[usuario]['valvula']['nome']:
        print('Você não tem nenhuma valvula adicionada.\n')
    else:
        print(pd.DataFrame(listaLogins[usuario]['valvula']))
    return

def _alterarValorValvula (key,  usuario,  numValvula,  time, novoValor):
    antigoValor = listaLogins[usuario]['valvula'][key][numValvula]
    listaLogins[usuario]['valvula'][key][numValvula] = novoValor
    _textoComDelay(time, f"{key} da válvula {listaLogins[usuario]['valvula']['nome'][numValvula]} alterado de {antigoValor} para {novoValor}.")
    return

def _alterarValorValvulaBaseadoEmLista (key, usuario, numValvula, time, lista):
    antigoValor = listaLogins[usuario]['valvula'][key][numValvula]
    novoValor = _escolhaOpcao(f"Qual será a nova {key}: ", lista)
    for j in range(len(lista)):
        if j == novoValor:
            listaLogins[usuario]['valvula'][key][numValvula] = lista[j]
            _textoComDelay(time, f"{key} da válvula {listaLogins[usuario]['valvula']['nome'][numValvula]} alterado de {antigoValor} para {lista[j]}.")
            return

'''FUNÇÕES ESPECIFICAS'''

def _adicionarValvula(usuario):
    nomeValvula = input("Digite o nome da válvula: ")
    localValvula = _escolhaOpcao("Aonde essa valvula será colocada:", listaLocalValvula)
    categoriaValvula = _escolhaOpcao("Qual a categoria do estabelecimento em que será instalado?", listaCategorias)
    listaLogins[usuario]['valvula']['nome'].append(nomeValvula)
    listaLogins[usuario]['valvula']['local'].append(listaLocalValvula[localValvula])
    listaLogins[usuario]['valvula']['estado'].append(True)
    listaLogins[usuario]['valvula']['fluxo'].append(0)
    listaLogins[usuario]['valvula']['categoria'].append(listaCategorias[categoriaValvula])
    print(f"Válvula {nomeValvula} adicionada.")
    return

def _excluirValvula(usuario, numValvula):
    _textoComDelay(2, f"Valvula {listaLogins[usuario]['valvula']['nome'][numValvula]} excluida")
    for key in listaLogins[usuario]['valvula'].keys():
        listaLogins[usuario]['valvula'][key].pop(numValvula)
    return

def _editarValvula(usuario):
    if not listaLogins[usuario]['valvula']['nome']:
        print('Você não tem nenhuma valvula adicionada.\n')
    else:
        editarValvula = _escolhaOpcao("Qual válvula deseja editar?", listaLogins[usuario]['valvula']['nome'])
        while True:
            opcaoEditarValvula = _escolhaOpcao(f"O que deseja editar da valvula {listaLogins[usuario]['valvula']['nome'][editarValvula]}?", listaEditarValvula)
            if opcaoEditarValvula == 0: #Trocar nome da válvula
                novoNome = input("Digite o novo nome da válvula:\n")
                _alterarValorValvula('nome', usuario, editarValvula, 2, novoNome)
            elif opcaoEditarValvula == 1: #Mudar localização da válvula
                _alterarValorValvulaBaseadoEmLista('local', usuario, editarValvula, 2, listaLocalValvula)
            elif opcaoEditarValvula == 2: #Inverter estado da valvula
                novoEstado = not listaLogins[usuario]['valvula']['estado'][editarValvula]
                _alterarValorValvula('estado', usuario, editarValvula, 2, novoEstado)
            elif opcaoEditarValvula == 3: #Editar fluxo de Água
                novoFluxo = _verificarIsNum("Para qual valor (em ml) deseja alterar: ")
                _alterarValorValvula('fluxo', usuario, editarValvula, 2, novoFluxo)
            elif opcaoEditarValvula == 4: #Mudar categoria da válvula
                _alterarValorValvulaBaseadoEmLista('categoria', usuario, editarValvula, 2, listaCategorias)
            elif opcaoEditarValvula == 5: #Excluir a Valvula
                _excluirValvula(usuario, editarValvula)
            else:
                break
    return

def _calculoContaAgua(usuario):
    #Quantidade de agua gasta.
    #Index 0 = Residencial Social, index 1 = Residencial, index 2 = Comercial, index 3 = Industrial, index 4 = Publica, index 5 = Publica Municipal
    listaFluxoTotal = [0, 0, 0, 0, 0, 0]
    #Index 1 = 0 a 10m³, index 2 = 11 a 20m³, index 3 = 21 a 30m³, index 4 = 31 a 50m³, index 5 = +50m³
    listaTaxaTotal = [[13.41, 1.58, 2.40, 2.40, 2.88], [33.52, 3.94, 6.01, 6.01, 7.20], [67.39, 6.68, 10.86, 10.86, 12.74], [67.39, 6.68, 10.86, 10.86, 12.74], [50.52, 5.02, 8.17, 8.17, 9.55], [33.69, 3.35, 5.43, 5.43, 6.37]]

    if listaLogins[usuario]['valvula']['nome']:
        for j in range(len(listaLogins[usuario]['valvula']['nome'])):
            for k in range(len(listaCategorias)):
                if listaLogins[usuario]['valvula']['categoria'][j] == listaCategorias[k]:
                    listaFluxoTotal[k] += listaLogins[usuario]['valvula']['fluxo'][j]
        fluxoTotal = sum(listaFluxoTotal)
        if fluxoTotal > 0:
            for j in range(len(listaCategorias)):
                if listaFluxoTotal[j] > 0:
                    listaFluxoTotal[j] = listaFluxoTotal[j]*(1/1000000)
                    if listaFluxoTotal[j] <= 10:
                        valorConta = listaTaxaTotal[j][0]
                    elif listaFluxoTotal[j] >= 11 and listaFluxoTotal[j] <= 20:
                        valorConta = listaTaxaTotal[j][0] + (listaFluxoTotal[j] - 10) * listaTaxaTotal[j][1]
                    elif listaFluxoTotal[j] >= 21 and listaFluxoTotal[j] <= 30:
                        valorConta = listaTaxaTotal[j][0] + (listaFluxoTotal[j] - 10) * listaTaxaTotal[j][2]
                    elif listaFluxoTotal[j] >= 31 and listaFluxoTotal[j] <= 50:
                        valorConta = listaTaxaTotal[j][0] + (listaFluxoTotal[j] - 10) * listaTaxaTotal[j][3]
                    elif listaFluxoTotal[j] > 50:
                        valorConta = listaTaxaTotal[j][0] + (listaFluxoTotal[j] - 10) * listaTaxaTotal[j][4]
                    valorEsgoto = valorConta * 80 / 100
                    valorFinal = valorConta + valorEsgoto
                    print(f"O Valor estipulado da sua conta de água de categoria {listaCategorias[j]} é de R${valorFinal:.2f}, com um total de {listaFluxoTotal[j]}m³.")
        else:
            print("Suas valvulas não captaram nenhuma água.")
    else:
        print('Você não tem válvulas adicionadas.')
    return


listaLogins = [{
    'nome': 'Leonardo',
    'senha': 'Senha1234',
    'valvula': {
        'nome': ['Valvula1', 'Roberto', 'Valvula 3', 'v4'],
        'local': ['Cozinha', 'Banheiro', 'Lavanderia', 'Banheiro'],
        'estado': [True, True, True, False],
        'fluxo': [1000000, 2000000, 500000, 800000], #calculado em ml
        'categoria': ['Residêncial', 'Residêncial', 'Residêncial', 'Residêncial']
    }
}]

listaMenu = ['Adicionar nova válvula', 'Editar válvula existente', 'Ver válvulas', 'Calcular conta de água', 'Sair']
listaLocalValvula = ['Banheiro', 'Cozinha', 'Lavanderia', 'Jaridim', 'Outro']
listaEditarValvula = ['Mudar nome', 'Mudar local', 'Abrir/Fechar válvula', 'Alterar fluxo de água', 'Mudar Categoria', 'Excluir', 'Voltar ao menu']
listaCategorias = ['Residêncial Social', 'Residêncial', 'Comercial', 'Industrial', 'Pública', 'Pública municipal']

_textoComDelay(2, "Bem vindo ao WaterWatch!")
while True:
    menuLogin = _escolhaOpcao("O que deseja fazer?", ['Fazer Login', 'Criar conta', 'Sair'])
    if menuLogin == 0: #Fazer Login
        loginNome = input("Digite o nome de seu login: ")
        for i in range(len(listaLogins)):
            if loginNome == listaLogins[i]['nome']:
                loginSenha = input("Digite a senha do seu login: ")
                if loginSenha == listaLogins[i]['senha']:
                    _textoComDelay(1, f"\nBem-vindo ao Water Watch {loginNome}!")
                    while True: #App Iniciado
                        opcaoEscolhida = _escolhaOpcao("O Que deseja fazer?", listaMenu)
                        if opcaoEscolhida == 0: #Adicionar Valvula
                            _adicionarValvula(i)
                            _textoComDelay(2, "Voltando para o menu...")
                        elif opcaoEscolhida == 1: #Editar Valvulas
                            _editarValvula(i)
                            _textoComDelay(2, "Voltando para o menu...")
                        elif opcaoEscolhida == 2: #Mostrar lista de valvulas e seus detalhes
                            _printarValvulas(i)
                            _textoComDelay(3, "Voltando para o menu...")
                        elif opcaoEscolhida == 3: #Estipular conta de água
                            _calculoContaAgua(i)
                            _textoComDelay(3, "Voltando para o menu...")
                        elif opcaoEscolhida == 4: #Sair
                            _textoComDelay(3, "Saindo da conta...")
                            break
                else:
                    _textoComDelay(1, "Senha inválida")
            elif i == len(listaLogins):
                _textoComDelay(1, "Login inválido")
    elif menuLogin == 1: #Criar conta
        novoNome = input("Digite seu nome. Ele será usado para fazer seu login:")
        novaSenha = input("Digite a senha que será usada para seu login: ")
        listaLogins.append({
            'nome': novoNome,
            'senha': novaSenha,
            'valvula': {
                'nome': [],
                'local': [],
                'estado': [],
                'fluxo': [],
                'categoria': []
            }
        })
        _textoComDelay(3,f"Conta {novoNome} registrada! Faça o login para continuar.")
    elif menuLogin == 2: #Sair
        print("Agradeçemos e volte sempre!")
        break
