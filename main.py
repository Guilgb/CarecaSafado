from Sms import Sms
from Email import Email


@staticmethod
def menu():
    print("Digite qual o tipo de mensagem deseja enviar: ")
    print("1- Mensagem Sms \n2- Mensagem email")


menu()


def opcao(opcao=input()):
    match opcao:
        case "1":
            mensagem_sms = Sms(None, None)
            print("Digite a sua mensagem: ")
            mensagem_sms.conteudo = input()
            print("Digite o numero de celular: ")
            mensagem_sms.telefone = input()
            return mensagem_sms

        case "2":

            mensagem_email = Email(None, None)
            print("Digite a sua mensagem: ")
            mensagem_email.conteudo = input()
            print("Digite o endereço de email de destino: ")
            mensagem_email.endereco = input()
            return mensagem_email
        case _:
            return print("Valor invalido!!")


opcao()
print("Commit Save")
