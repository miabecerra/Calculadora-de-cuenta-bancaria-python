import time

# =========================================
# CONSTANTES
# =========================================

PIN_CORRECTO = "1234"
INTENTOS_MAXIMOS = 3
SALDO_INICIAL = 50000

OPCION_DEPOSITAR = 1
OPCION_EXTRAER = 2
OPCION_SALIR = 3

INTENTOS_CONEXION = 3
PAUSA_CONEXION = 1

# =========================================
# FUNCIONES
# =========================================

def simular_conexion():
    """Muestra los intentos de conexión al servidor."""
    for i in range(INTENTOS_CONEXION):
        print(f"Conectando al servidor... intento {i+1}")
        time.sleep(PAUSA_CONEXION)

def validar_acceso(pin_correcto):
    """Pide el PIN y devuelve True si es correcto dentro de los intentos permitidos."""
    intentos = INTENTOS_MAXIMOS
    while True:
        pin_usuario = input("Ingrese su PIN: ")
        if pin_usuario == pin_correcto: return True
        else:
            intentos -= 1
            if intentos <= 0: return False
            else: print(f"PIN incorrecto, quedan {intentos} intentos.")

def mostrar_menu():
    """Muestra el menú y devuelve una opción válida."""
    while True:
        print("1. Depositar\n2. Extraer\n3. Salir")
        opcion_usuario = int(input("Ingrese una opcion: "))

        if opcion_usuario in range(1,4): return opcion_usuario
        else: print("Opcion invalida, intente de nuevo")

def pedir_monto():
    """Pide un monto mayor a cero y lo devuelve."""
    monto_usuario = int(input("Ingrese un monto: "))
    if monto_usuario > 0: return monto_usuario

def depositar(saldo, monto):
    """Devuelve el saldo luego de depositar."""
    return saldo + monto

def extraer(saldo, monto):
    """Intenta extraer dinero. Si no alcanza, mantiene el saldo."""
    if monto < saldo: saldo -= monto
    else: print("Fondos insuficientes")
    return saldo

# =========================================
# PROGRAMA PRINCIPAL
# =========================================

def main():
    """Ejecuta el cajero automático."""
    simular_conexion()

    if not validar_acceso(PIN_CORRECTO):
        print("Acceso denegado.")
        return

    saldo = SALDO_INICIAL
    print("Acceso concedido.")
    print("Saldo actual:", saldo)

    while True:
        opcion = mostrar_menu()
        
        if opcion == OPCION_DEPOSITAR:
            monto = pedir_monto()
            saldo = depositar(saldo, monto)
            print("Depósito realizado.")
            print("Saldo actual:", saldo)
        elif opcion == OPCION_EXTRAER:
            monto = pedir_monto()
            saldo = extraer(saldo, monto)
            print("Saldo actual:", saldo)
        else:
            print("Gracias por usar el cajero.")
            break

main()