class Task:
    def __init__(self, id , titulo, descricao, completa=False) -> None:
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.completa = completa
    
    def para_dicionario(self):
        return{
            "id" : self.id,
            "titulo" : self.titulo,
            "descrição" : self.descricao,
            "completa" : self.completa
        }
    