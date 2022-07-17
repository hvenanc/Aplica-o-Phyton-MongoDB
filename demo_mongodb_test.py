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

    
    # Insere vários valores de uma só vez
    # O método insert_one() insere apenas um documento
    collection_name.insert_one(linha)
    #collection_name.insert_many([nlinha,nlinha])
 
    print(dbname.list_collection_names())

    #Checando a existência de uma coleção @Henrique

    # colecao = (input("Busque uma coleção:"))
    # collist = dbname.list_collection_names()
    # if colecao in collist:
    #     print("Coleção encontrada!");
    # else: print("Coleção não encontrada!")

    #imprimindo uma coleção @Henrique

    #x = linha_1

    #print(x)

    #Buscando uma linha de ônibus pelo seu código @Henrique

    print("ENCONTRE UMA LINHA DE ÔNIBUS, INSERINDO SEU CÓDIGO")
    minha_linha = int(input("Insira sua linha:"))
    myquery = {"CÓDIGO":minha_linha}

    mydoc = collection_name.find(myquery)

    for y in mydoc:
     print(y)
