from pymongo import MongoClient


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Conecta o Banco a URL do atlas
    CONNECTION_STRING = "mongodb+srv://Henrique:94003046@cluster0.mvw12.mongodb.net/?retryWrites=true&w=majority"

    # Crie uma conexão usando MongoClient. Você pode importar MongoClient ou usar pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cria o banco de dados
    return client['Loja']

    # Isso é adicionado para que muitos arquivos possam reutilizar a função get_database()


if __name__ == "__main__":
    dbname = get_database()

    # Criando uma coleção

    collection_name = dbname["Itens"]

    # Inserindo Itens

    item_1 = {
        "id": "IT1",
        "ean": "7892840211240",
        "prooduto": "SALGADINHO DORITOS QUEIJO NACHO 56G",
        "medida": "un",
        "preco": 8.59,
        "estoque": 48
    }

    item_2 = {
        "id": "IT2",
        "ean": "7896045504541",
        "prooduto": "CERVEJA AMSTEL 600ML",
        "medida": "un",
        "preco": 8.89,
        "estoque": 60
    }

    # Insere vários valores de uma só vez
    # O método insert_one() insere apenas um documento
    collection_name.insert_many([item_1, item_2])
