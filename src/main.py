from fastapi import FastAPI, HTTPException
from api import get_character_info

app = FastAPI()


@app.get('/guerra-nas-estrelas/')
def get_characters_endpoint(ids: str):
    try:
        # Convertendo a string de IDs separados por vírgula para uma lista de inteiros
        ids_list = [int(id) for id in ids.split(',')]

        characters_info = []
        for id in ids_list:
            try:
                character_info = get_character_info(id)
                if character_info:
                    characters_info.append(character_info)
                else:
                    raise HTTPException(status_code=404, detail=f"Personagem com ID {id} não encontrado")
            except Exception:
                raise HTTPException(status_code=500, detail="Ocorreu um erro ao processar a solicitação")

        return characters_info
    except ValueError:
        raise HTTPException(status_code=422, detail="IDs inválidos. Certifique-se de que os IDs sejam inteiros separados por vírgula.")
