from products.interface_product_B import InterfaceProductB


class ProductBSimple(InterfaceProductB):

    def review(self):
        print('Produto(A) SIMPLES review')
    
    def description(self):
        print('Descrição do produto(B) SIMPLES')
