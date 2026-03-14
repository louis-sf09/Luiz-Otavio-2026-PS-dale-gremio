# utils/__init__.py
# Expõe a API pública do pacote

from .formatador import linha_separadora, formatar_resultado, cabecalho_secao
from .validador  import validar_numero

__all__ = [
    "linha_separadora", "formatar_resultado", "cabecalho_secao", "validar_numero",
]
