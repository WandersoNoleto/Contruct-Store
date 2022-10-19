from rolepermissions.roles import AbstractUserRole


#Gerente
class Manager(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_prodtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedor': True,
        'excluir_vendedor': True
    }


class Seller(AbstractUserRole):
    avaible_permissions = {
        'realizar_venda': True
    }
