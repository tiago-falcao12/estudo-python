from decorador import my_decorator


@my_decorator
def soma(a: int, b: int) -> int:
    return a + b


@my_decorator
def multiplica(a: int) -> int:
    return a * 2


@my_decorator
def mensagem(msg: str) -> str:
    return f"{msg.upper()}"


if __name__ == "__main__":
    print(mensagem("ola"))
