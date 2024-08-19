def celsius_para_fahrenheit(temp_celsius: float) -> float:
    """
    Converte a temperatura de Celsius para Fahrenheit.

    :param celsius: Temperatura em Celsius.
    :return: Temperatura em Fahrenheit.
    """
    return temp_celsius * 9/5 + 32

def fahrenheit_para_celsius(temp_fahrenheit: float) -> float:
    """
    Converte a temperatura de Fahrenheit para Celsius.

    :param fahrenheit: Temperatura em Fahrenheit.
    :return: Temperatura em Celsius.
    """
    return (temp_fahrenheit - 32) * 5/9
