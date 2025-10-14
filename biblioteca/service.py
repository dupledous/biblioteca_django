import requests
def  get_libro(query,max_results = 10):
    try:
        url ='https://www.googleapis.com/books/v1/volumes?q={query}&axResults={max_results}'
        respuesta = requests.get(url)
        data = respuesta.json()
        libros = []
        if 'items' in data:
            for item in data['items']:
                info = item.get('volumeInfo',{})
                libros.append({
                    'titulo':info.get("title",'sin titulo'),
                    'autor':",".join(info.get('authors',["Desconocido"])),
                    'imagen':info.get("imageLinks",{}.get('thumbnail')),
                    'descripcion':info.get("descripcion",'sin descripcion'),
                    'link':info.get("infoLink",'#')
                })
                return libros
    except requests.exceptions.RequestException as e:
        return f"error:{e}"