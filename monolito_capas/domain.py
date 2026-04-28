# Capa de Dominio: Define la lógica pura y las reglas de negocio
class CaesarCipher:
    @staticmethod
    def transform(text: str, shift: int) -> str:
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result
