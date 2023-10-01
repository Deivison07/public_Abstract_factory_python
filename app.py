from category.categoryProductPremium import CategoryProductPremium
from category.categoryProductSimple import CategoryProductsSimple
from client.client import Cliente

def app():

    cliente1 = Cliente(category=CategoryProductPremium())
    cliente1.info()

    cliente2 = Cliente(category=CategoryProductsSimple())
    cliente2.info()

if __name__ == '__main__':
    app()
