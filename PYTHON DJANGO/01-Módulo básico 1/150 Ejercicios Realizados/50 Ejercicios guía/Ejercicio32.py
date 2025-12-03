import re  # Regular expressions para patrones avanzados

def analizar_estructura(texto):
    """Analiza la estructura básica del texto"""
    estadisticas = {
        'caracteres_total': len(texto),
        'caracteres_sin_espacios': len(texto.replace(' ', '')),
        'palabras': len(texto.split()),
        'oraciones': len([s for s in texto.split('.') if s.strip()]),
        'párrafos': len([p for p in texto.split('\n\n') if p.strip()])
    }
    return estadisticas

def encontrar_patrones_email(texto):
    """Encuentra direcciones de email en el texto"""
    patron_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(patron_email, texto)
    return emails

def encontrar_patrones_telefono(texto):
    """Encuentra números de teléfono en diferentes formatos"""
    patrones = [
        r'\b\d{3}-\d{3}-\d{4}\b',       # 123-456-7890
        r'\b\(\d{3}\)\s?\d{3}-\d{4}\b', # (123) 456-7890
        r'\b\d{10}\b'                   # 1234567890
    ]
    telefonos = []
    for patron in patrones:
        telefonos.extend(re.findall(patron, texto))
    return telefonos

def analizar_sentimiento_basico(texto):
    """Análisis básico de sentimiento basado en palabras clave"""
    palabras_positivas = [
        'excelente', 'genial', 'fantástico', 'increíble', 'perfecto',
        'bueno', 'feliz', 'contento', 'alegre', 'maravilloso'
    ]
    palabras_negativas = [
        'terrible', 'malo', 'horrible', 'triste', 'enojado',
        'molesto', 'frustrado', 'decepcionado', 'pesimo'
    ]
    texto_lower = texto.lower()
    puntuacion_positiva = sum(1 for palabra in palabras_positivas if palabra in texto_lower)
    puntuacion_negativa = sum(1 for palabra in palabras_negativas if palabra in texto_lower)
    if puntuacion_positiva > puntuacion_negativa:
        sentimiento = "Positivo"
    elif puntuacion_negativa > puntuacion_positiva:
        sentimiento = "Negativo"
    else:
        sentimiento = "Neutral"
    return {
        'sentimiento': sentimiento,
        'palabras_positivas_encontradas': puntuacion_positiva,
        'palabras_negativas_encontradas': puntuacion_negativa
    }

def encontrar_palabras_repetidas(texto, min_longitud=4):
    """Encuentra palabras que se repiten frecuentemente"""
    # Limpiar y dividir el texto
    palabras = re.findall(r'\b\w+\b', texto.lower())
    palabras_largas = [p for p in palabras if len(p) >= min_longitud]
    # Contar frecuencias
    frecuencias = {}
    for palabra in palabras_largas:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    # Filtrar solo las que aparecen más de una vez
    repetidas = {palabra: freq for palabra, freq in frecuencias.items() if freq > 1}
    return repetidas

def generar_resumen_legible(estadisticas):
    """Convierte estadísticas en texto legible"""
    est = estadisticas
    promedio_palabras_oracion = est['palabras'] / max(est['oraciones'], 1)
    resumen = []
    resumen.append(f"Este texto tiene {est['caracteres_total']} caracteres en total")
    resumen.append(f"Contiene {est['palabras']} palabras distribuidas en {est['oraciones']} oraciones")
    resumen.append(f"El promedio es de {promedio_palabras_oracion:.1f} palabras por oración")
    if est['párrafos'] > 1:
        resumen.append(f"Está organizado en {est['párrafos']} párrafos")
    return resumen

# Función principal de análisis
def analizar_texto_completo(texto):
    """Realiza un análisis completo del texto"""
    print("Análisis completo del texto iniciado.\n")

    estructura = analizar_estructura(texto)
    resumen = generar_resumen_legible(estructura)
    print("ESTRUCTURA DEL TEXTO:")
    for linea in resumen:
        print(linea)
    
    print("\nCORREOS ELECTRÓNICOS ENCONTRADOS:")
    emails = encontrar_patrones_email(texto)
    if emails:
        for email in emails:
            print(f" - {email}")
    else:
        print("No se encontraron correos electrónicos.")
    
    print("\nNÚMEROS DE TELÉFONO ENCONTRADOS:")
    telefonos = encontrar_patrones_telefono(texto)
    if telefonos:
        for tel in telefonos:
            print(f" - {tel}")
    else:
        print("No se encontraron números de teléfono.")
    
    print("\nANÁLISIS DE SENTIMIENTO:")
    sentimiento = analizar_sentimiento_basico(texto)
    print(f"Sentimiento general: {sentimiento['sentimiento']}")
    print(f"Palabras positivas encontradas: {sentimiento['palabras_positivas_encontradas']}")
    print(f"Palabras negativas encontradas: {sentimiento['palabras_negativas_encontradas']}")
    
    print("\nPALABRAS REPETIDAS (mínimo 4 letras):")
    repetidas = encontrar_palabras_repetidas(texto)
    if repetidas:
        for palabra, freq in repetidas.items():
            print(f" - '{palabra}': {freq} veces")
    else:
        print("No se encontraron palabras repetidas.")

# Ejemplo de uso
if __name__ == "__main__":
    texto_prueba = """
    Hola, este es un texto de prueba. Tiene algunos emails como ejemplo@example.com y otro correo prueba@correo.com.
    También incluye teléfonos como 123-456-7890 o (987) 654-3210 y un número sin formato 1234567890.

    El texto tiene varias palabras repetidas, repetidas para probar el análisis. Además es un texto excelente y genial,
    pero también puede tener algo malo o triste.
    """
    analizar_texto_completo(texto_prueba)
