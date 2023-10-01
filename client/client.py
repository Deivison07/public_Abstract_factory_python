from category.abstractFactoryCategory import AbstractFactoryCategory

class Cliente(): 
    def __init__(self, category:AbstractFactoryCategory) -> None:
        self.categoriaProduto: AbstractFactoryCategory = category

    def info(self):
        self.categoriaProduto.getProductA().description()
        self.categoriaProduto.getProductB().review()

