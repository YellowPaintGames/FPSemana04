import json
json_file = input("Type in the json file you want to read: ")
try:
    file = open(json_file, "rt", encoding="utf-8")
    conteudo = file.read()
    
    dados = json.loads(conteudo)

    assert dados["nome"]
    assert dados["idade"]
    assert dados["localização"]

    print(dados)

    file.close()
except FileNotFoundError:
    print("ERRO: Ficheiro Não Encontrado!!!!")
except json.JSONDecodeError:
    if conteudo.strip() == "":
        print("Erro: Ficheiro Vazio!")
    else:
        print("Erro: Ficheiro Não Contém JSON Válido!")
except KeyError:
    print("Erro: Campos Obrigatórios Em Falta!")
finally:
    print("Processo Concluído!")