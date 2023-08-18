destinos = ["Destino A", "Destino B", "Destino_C"]
def mostrar_menu():
    print("Seleccione su destino:")
    for i, destino in enumerate(destinos):
        print(f"{i + 1}. {destino}")
    seleccion = int(input()) - 1
    return seleccion
def obtener_datos():
    tarjeta_credito = input("Introduzca su tarjeta de crédito: ")
    identificacion_personal = input("Introduzca su número de identificación personal: ")
    return tarjeta_credito, identificacion_personal
def expedir_boleto(destino):
    print(f"¡Boleto de tren a {destinos[destino]} expedido y cargado a su cuenta!")
def main():
    print("Bienvenido al sistema de expedición de boletos de tren automático.")
    input("Presione Enter para iniciar")
    destino_seleccionado = mostrar_menu()
    if destino_seleccionado >= 0 and destino_seleccionado < len(destinos):
        print(f"Ha seleccionado {destinos[destino_seleccionado]}.")
        tarjeta, identificacion = obtener_datos() 
        expedir_boleto(destino_seleccionado)
    else:
        print("Selección de destino inválida.")
main()