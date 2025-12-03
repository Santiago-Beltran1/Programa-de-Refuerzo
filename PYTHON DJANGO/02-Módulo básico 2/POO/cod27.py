import logging
import sys

logger = logging.getLogger('santiago_app')
logger.setLevel(logging.DEBUG)

formatter_full = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_simple = logging.Formatter('%(levelname)s: %(message)s')

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
ch.setFormatter(formatter_simple)

fh = logging.FileHandler('santiago.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter_full)

logger.addHandler(ch)
logger.addHandler(fh)

print("--- Sistema de Logging Santiago ---")

def SantiagoOper(valor):
    logger.debug(f"DEBUG: Iniciando operación con valor: {valor}")
    try:
        resultado = 500 / valor
        logger.info(f"INFO: Operación completada. Resultado: {resultado}")
        if resultado > 100:
            logger.warning(f"WARNING: Resultado {resultado} muy alto.")
    except ZeroDivisionError:
        logger.error("ERROR: División por cero detectada.")
        raise
    except Exception as e:
        logger.critical(f"CRITICAL: Error inesperado: {e}", exc_info=True)
    return True

print("\n--- Ejecutando operaciones Santiago ---")
try:
    SantiagoOper(5)
    SantiagoOper(2)
    SantiagoOper(0)
except ZeroDivisionError:
    print("Capturada división por cero en el flujo principal.")
SantiagoOper(10)

try:
    SantiagoOper([1,2,3])
except Exception:
    print("Capturada excepción inesperada en el flujo principal.")

logger.info("INFO: Fin de la demostración de logging Santiago.")
