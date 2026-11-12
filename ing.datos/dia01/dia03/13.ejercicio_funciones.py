ventas_crudas = [
    {
        "id_venta": 1001,
        "cliente": " mArÍa fErNaNdA lÓpEz ",
        "email": "maria.lopez@techcorp.pe",
        "subtotal": 250.0,
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "COMPLETADO",
        "tarjeta": "4557-8890-1234",
    },
    {
        "id_venta": 1002,
        "cliente": "carlos_ruiz",
        "email": "cruiz_sin_arroba.com",
        "subtotal": 120.0,
        "impuesto": 0.0,
        "moneda": "USD",
        "estado": "COMPLETADO",
        "tarjeta": "5120-4432-9981",
    },
    {
        "id_venta": 1003,
        "cliente": None,
        "email": "contacto@startup.io",
        "subtotal": -50.0,  # Error de registro (monto negativo)
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "COMPLETADO",
        "tarjeta": "4111-2222-3333",
    },
    {
        "id_venta": 1004,
        "cliente": " ROBERTO GÓMEZ ",
        "email": "rgomez@gmail.com",
        "subtotal": 500.0,
        "impuesto": 0.18,
        "moneda": "PEN",
        "estado": "CANCELADO",  # Debe filtrarse
        "tarjeta": "4916-0098-7765",
    },
    {
        "id_venta": 1005,
        "cliente": "",
        "email": "ventas@logistica.com",
        "subtotal": 80.0,
        "impuesto": 0.18,
        "moneda": "USD",
        "estado": "COMPLETADO",
        "tarjeta": "5412-7500-8812",
    },
    {
        "id_venta": 1006,
        "cliente": " lucía mendieta",
        "email": "lucia@finanzas.pe",
        "subtotal": 5.0,  # Debajo del monto mínimo
        "impuesto": 0.18,
        "moneda": "EUR",  # Moneda no soportada
        "estado": "COMPLETADO",
        "tarjeta": "4000-1234-5678",
    },
]


"""eliminar los espacio extra y aplica formato titulo"""
def limpiar_nombre(nombre_crudo: str | None):
    if not nombre_crudo or not nombre_crudo.strip():
        return "Nombre no disponible"

    return nombre_crudo.strip().title()


"""Extraer el dominio del correo electrónico"""
def extraer_dominio(correo: str):
    if not correo or "@" not in correo:
        return "Dominio no disponible"
    return correo.strip().split("@")[1].lower()



"""EJERICIO 3 VALIDAR DE  modeda , SOLO SE PERMITE PEN, USD y montos"""
def validar_divisa(moneda: str, monto: float):
    monedas_permitidas = ("PEN", "USD")
    if monto>=0 and moneda.upper() in monedas_permitidas:
        return True
    else:
        return False

    

"""EJERCICIO 4 conversor de divisas con tasas configurable"""
def convertir_a_usd(monto:float, moneda_origen:str, tasa_cambio:float):
    moneda = moneda_origen.upper()
    if moneda == "PEN":
        return round(monto / tasa_cambio, 2)
    if moneda == "USD":
        return round(monto, 2)


"""EJERCICIO 5 orquestador del pipiline """
#filstrar por el estado de negocio 
# limpiar el nombre del cliente
# determinar el dominio
# validar la transaccion
# convertir a USD si es necesario
# CONSTRUIR  un diccionario de salida

def ejecutar_pipiline(datos_crudos: list[dict]):

    registros_limpios = []
    descartados = 0
    monto_total = 0

    # 1. Filtrar por el estado del negocio
    for fila in datos_crudos:

        if fila["estado"] != "COMPLETADO":
            descartados += 1
            continue

        # Crear una copia de la fila original
        fila = fila.copy()

        # 2. Validar la transacción
        if not validar_divisa(fila["moneda"], fila["subtotal"]):
            descartados += 1
            continue

        # 3. Limpiar nombres
        fila["cliente"] = limpiar_nombre(fila["cliente"])

        # 4. Determinar el dominio
        fila["dominio"] = extraer_dominio(fila["email"])

        # 5. Convertir a USD
        fila["subtotal"] = convertir_a_usd(
            fila["subtotal"], fila["moneda"], 3.5
        )

        fila["moneda"] = "USD"

        # 6. Calcular monto total
        monto_total += fila["subtotal"]

        # 7. Agregar fila limpia
        registros_limpios.append(fila)

    return {
        "data_final": registros_limpios,
        "registros_procesados": len(datos_crudos),
        "registros_descartados": descartados,
        "monto_total_usd": round(monto_total, 2)
    }


from pprint import pprint

resultado = ejecutar_pipiline(ventas_crudas)
pprint(resultado)