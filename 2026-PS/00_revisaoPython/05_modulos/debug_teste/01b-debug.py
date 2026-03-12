# debug_teste/01b-debug.py

# import Temperatura      # ModuleNotFoundError

from conversores import celsius_para_kelvin # converter_distancia -> ImportError
resultado = celsius_para_kelvin(25)
print(f"25°C em K: {resultado}")

from utils.formatador import formatar_resultado
print(formatar_resultado("teste", 100, "km", 62.1, "mi"))  # TypeError "extra"

from conversores import km_para_milhas
print(f"50 km = {km_para_milhas(50):.2f} mi")

# from debug_teste import algo    ImportError (pacote)
