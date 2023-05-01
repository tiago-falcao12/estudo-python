import time

# função que recebe outra função


def meu_decorator(func):
    def wrapper(*args):
        inicio = time.time()
        retorno = func(*args)
        print(f"terminou a execução em {time.time() - inicio}")
        return retorno
    return wrapper
