from pymongo import MongoClient


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Conecta o Banco a URL do atlas
    CONNECTION_STRING = "mongodb+srv://Henrique:94003046@cluster0.mvw12.mongodb.net/?retryWrites=true&w=majority"

    # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cria o banco de dados
    return client['Onibus']

    # Isso é adicionado para que muitos arquivos possam reutilizar a função get_database()


if __name__ == "__main__":
    dbname = get_database()

    #Criando uma coleção

    #def cadastrarLinha():

    collection_name = dbname["Linhas"]

    print("Digite os dados da sua linha:")
    print("\n")
    codigo=int(input("CÓDIGO: "))
    nome=(input("NOME: "))
    tarifa=float(input("TARIFA: "))
    frota=int(input("FROTA: "))
    integração=(input("INTEGRAÇÃO:"))
    arCondicionado=(input("AR-CONDICIONADO: "))
    print("\n")
    print("LINHA CADASTRADA COM SUCESSO!")

    #Inserindo Itens

    linha = {
        "CÓDIGO": codigo,
        "LINHA": nome,
        "TARIFA": tarifa,
        "FROTA": frota,
        "INTEGRAÇÃO": integração,
        "AR-CONDICIONADO": arCondicionado
    }

    collection_name.insert_one(linha)
    # O método insert_one() insere apenas um documento
    
    #Buscando uma linha de ônibus pelo seu código @Henrique

    #def buscarLinha():

    print("ENCONTRE UMA LINHA DE ÔNIBUS, INSERINDO SEU CÓDIGO\n")
    minha_linha = int(input("INSIRA O CÓDIGO DA LINHA:\n"))
    myquery = {"CÓDIGO":minha_linha}

    mydoc = collection_name.find(myquery)

    for y in mydoc:
     print(y,"\n")
     

    #Excluindo linha do Banco @Henrique

    print("EXCLUA UMA LINHA DE ÔNIBUS, INSERINDO SEU CÓDIGO")
    minha_linha = int(input("INSIRA O CÓDIGO DA LINHA QUE DESEJA EXCLUIR:"))
    myquery = {"CÓDIGO":minha_linha}
    collection_name.delete_one(myquery)
    print("LINHA EXCLUIDA COM SUCESSO!")
    print("LINHA EXCLUIDA: ",minha_linha)

    #Menu (Testando um menu, usando o básico de funções) @Henrique
    # print("\n")
    # print("---------------MENU-----------------")
    # menudeopções = ["Cadastrar nova Linha", "Consultar Linhas",
    #                 "Excluir Linha",]
    # for numero, opção in enumerate(menudeopções):
    #     print(numero+1, "-", opção)
    # print("------------------------------------")

    # opção=int(input("Digite sua escolha: \n"))
    # if opção==1:
    #     cadastrarLinha()
    # elif opção==2:
    #     buscarLinha()
    # elif opção==3:
    #     excluirLinha()

