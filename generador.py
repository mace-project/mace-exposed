import secrets
import string

def generar_string_aleatorio(longitud, caracteres):
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

# 1. AWS Keys
base64_chars = string.ascii_letters + string.digits + "+/"
aws_access_key = "AKIA" + generar_string_aleatorio(16, string.ascii_uppercase + string.digits)
aws_secret_key = generar_string_aleatorio(40, base64_chars)

# 2. Azure Secret
azure_chars = string.ascii_letters + string.digits + "~-."
azure_secret = generar_string_aleatorio(34, azure_chars) + "~" + generar_string_aleatorio(5, string.ascii_letters)

# 3. Formatear como JSON de prueba
mock_secrets_json = f"""{{
  "AWS_ACCESS_KEY_ID": "{aws_access_key}",
  "AWS_SECRET_ACCESS_KEY": "{aws_secret_key}",
  "AZURE_CLIENT_SECRET": "{azure_secret}"
}}"""

print(mock_secrets_json)
# Puedes redirigir esto a un archivo: con 'with open("secrets.json", "w")...'
