# utils/validador.py

def validar_numero(valor_str, minimo=None, maximo=None):
    """Testa se a entrada do usuário é float e se está dentro dos limites estabelacidos"""
    msg_erro = f"  Valor inválido! Digite um numero válido!"
    
    try:
        # Caso seja float
        valor_float = float(valor_str)

        # Testa se o valor está dentro dos limites
        if minimo != None and valor_float < minimo:
            return False, 0, msg_erro
        if maximo != None and valor_float > maximo:
            return False, 0, msg_erro

        return True, valor_float, ""
    
    except ValueError:
        # Caso não seja float
        pass

    return False, 0, msg_erro

if __name__ == "__main__":
    print("  Testando validador.py...")
    print("  Validar '21', minimo 19, maximo 22")
    print(f"  Resultado validação: {validar_numero("21", 19, 22)} Esperado: (True, 21.0)")
    print("  OK!")
