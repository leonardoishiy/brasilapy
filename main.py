from brasilapy.client import BrasilAPI

client = BrasilAPI()

estado = client.get_corretoras(cnpj = "02332886000104")

print(estado)