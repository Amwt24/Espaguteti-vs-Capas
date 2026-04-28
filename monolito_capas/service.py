# Capa de Servicio: Orquestación de la lógica de negocio
from domain import CaesarCipher

class CipherService:
    def encrypt(self, text: str, shift: int) -> str:
        return CaesarCipher.transform(text, shift)

    def decrypt(self, text: str, shift: int) -> str:
        return CaesarCipher.transform(text, -shift)
