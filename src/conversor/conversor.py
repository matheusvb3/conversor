def celsius_para_fahrenheit(temp_celsius: float) -> float:
    """
    Converte a temperatura de Celsius para Fahrenheit.

    :param temp_celsius: Temperatura em Celsius.
    :return: Temperatura em Fahrenheit.
    :raise TypeError: Valor de temperatura não é um inteiro ou float.
    """
    if not isinstance(temp_celsius, (float, int)):
        raise TypeError("O valor recebido como parâmetro não é do tipo inteiro ou float.")
    return temp_celsius * 9/5 + 32

def fahrenheit_para_celsius(temp_fahrenheit: float) -> float:
    """
    Converte a temperatura de Fahrenheit para Celsius.

    :param temp_fahrenheit: Temperatura em Fahrenheit.
    :return: Temperatura em Celsius.
    :raise TypeError: Valor de temperatura não é um inteiro ou float.
    """
    if not isinstance(temp_fahrenheit, (float, int)):
        raise TypeError("O valor recebido como parâmetro não é do tipo inteiro ou float.")
    return (temp_fahrenheit - 32) * 5/9
