from decoradores.decorador import meu_decorator


@meu_decorator
def soma(a: int, b: int) -> int:
    return a + b


@meu_decorator
def multiplica(a: int) -> int:
    return a * 2


@meu_decorator
def mensagem(msg: str) -> str:
    return f"{msg.upper()}"


if __name__ == "__main__":
    print(mensagem("ola"))
