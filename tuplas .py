# Solicita ao usuário que insira coordenadas geográficas (latitude e longitude) separadas por vírgula
entrada = input("Digite a latitude e longitude separadas por vírgula: ")
coordenadas = tuple(map(float, entrada.split(",")))

# Desempacota a tupla e exibe as coordenadas
latitude, longitude = coordenadas
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
