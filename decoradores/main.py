from time import sleep

from decorador import my_decorator


@my_decorator
def funcao_1(mensagem: str) -> None:
    sleep(5)
    print(mensagem)


def main(func, *args, **kwargs):
    func(*args, **kwargs)


if __name__ == "__main__":
    main(funcao_1, "Ola Seja bem-vindo!")
