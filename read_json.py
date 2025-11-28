import json
import os.path
path="data.json"
if os.path.exists(path)==False:
    print("ERRO: Ficheiro não existe")
elif ".json" not in path:
    print("ERRO: Ficheiro não é JSON")
else:
    file = open(path, "rt",encoding='utf-8')
    json_data = file.read()
    if json_data=='' or json_data=='{}':
        print("ERRO: O ficheiro está vazio")
    else:
        data = json.loads(json_data)
        if "idade" not in data or "nome" not in data or "localização" not in data:
            print("ERRO: Campos obrigatórios em falta")
        else:
            print(data)
            file.close()