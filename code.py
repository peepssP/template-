import random

class SistemaAleatorio:
    def __init__(self):
        pass
    
    def gerar_numero_aleatorio(self, inicio, fim):
        """Gera um número aleatório entre inicio e fim, inclusive."""
        return random.randint(inicio, fim)
    
    def selecionar_item_aleatorio(self, lista):
        """Seleciona um item aleatório de uma lista fornecida."""
        if not lista:
            raise ValueError("A lista fornecida está vazia.")
        return random.choice(lista)
    
    def embaralhar_lista(self, lista):
        """Embaralha a ordem dos itens na lista fornecida."""
        random.shuffle(lista)
        return lista
    
    def gerar_aleatorio_com_peso(self, lista, pesos):
        """Gera um item aleatório de uma lista com pesos fornecidos."""
        if len(lista) != len(pesos):
            raise ValueError("A lista e os pesos devem ter o mesmo tamanho.")
        return random.choices(lista, weights=pesos, k=1)[0]

# Exemplo de uso do sistema aleatório
if __name__ == "__main__":
    sistema = SistemaAleatorio()
    
    # Gerar um número aleatório entre 1 e 100
    numero_aleatorio = sistema.gerar_numero_aleatorio(1, 100)
    print(f"Número aleatório: {numero_aleatorio}")
    
    # Selecionar um item aleatório de uma lista
    itens = ["maçã", "banana", "laranja", "uva"]
    item_aleatorio = sistema.selecionar_item_aleatorio(itens)
    print(f"Item aleatório: {item_aleatorio}")
    
    # Embaralhar uma lista
    lista_embaralhada = sistema.embaralhar_lista(itens)
    print(f"Lista embaralhada: {lista_embaralhada}")
    
    # Gerar um item aleatório de uma lista com pesos
    pesos = [0.1, 0.3, 0.4, 0.2]  # A soma dos pesos não precisa ser 1
    item_aleatorio_peso = sistema.gerar_aleatorio_com_peso(itens, pesos)
    print(f"Item aleatório com peso: {item_aleatorio_peso}")
