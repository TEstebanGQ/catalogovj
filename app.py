import utils.screenController as sc
import utils.validateData as vd
import random
import utils.corefiles as cf
from config import DB_FILE
if __name__ == "__main__":
        sc.limpiar_pantalla()
        idVj = random.randint(1023, 9876)
        nomVj = vd.validatetext("Ingrese el nombre del Videojuego: ")
        costVj = vd.validateInt("Costo: ")
        priceVj = vd.validateInt("Precio de venta: ")
        VJ = {
            idVj:{
            "Name":nomVj,
            "Cost":costVj,
            "Price":priceVj

            }
        }
        if not cf.updateJson(VJ,["Adventure"]):
            print("Videojuego agregado exitosamente ✅")
        else:
            print("No se pudo agregar la cerveza ❌ ")