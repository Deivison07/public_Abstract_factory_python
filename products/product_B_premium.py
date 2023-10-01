from products.interface_product_B import InterfaceProductB


class ProductBPremium(InterfaceProductB):

    def review(self):
        print('Produto(A) premium review')
    
    def description(self):
        print('Descrição do produto(B) premium')
