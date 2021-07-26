#Exclui algum produto.

from mongoengine.errors import DoesNotExist
from Principal1 import Produto

try:
    produto = Produto.objects(Nome="Tilápia").get()
    produto.delete()
    print("Produto deletado")
except DoesNotExist:
    print("Produto não encontrado")
