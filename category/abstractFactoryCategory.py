from abc import ABC, abstractmethod
from products.interface_product_A import InterfaceProductA
from products.interface_product_B import InterfaceProductB


class AbstractFactoryCategory(ABC):

    @abstractmethod
    def getProductA(self) -> InterfaceProductA:...

    @abstractmethod
    def getProductB(self) -> InterfaceProductB:...
