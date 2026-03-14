# conversores/massa.py

def kg_para_libras(kg):
    """Converte quilogramas para libras"""
    return kg * 2.20462

def kg_para_gramas(kg):
    """Converte quilogramas para gramas"""
    return kg * 1000

if __name__ == "__main__":
    print("Testando massa.py...")
    print(f"10kg = {kg_para_libras(10)}lbs  (esperado: 22.0462)")
    print(f"22kg = {kg_para_gramas(22)}g      (esperado: 22000)")
    print("OK!")
