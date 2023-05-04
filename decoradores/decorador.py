import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        retorno = func(*args, **kwargs)
        print(
            f" a funcao {func.__name__} foi executada em {time.time() - inicio}")
        return retorno
    return wrapper


def excecao(func):
    def exception(*args, **kwargs):
        try:
            resposta = func(*args, **kwargs)
            return resposta
        except Exception as error:
            print(error)
    return exception
