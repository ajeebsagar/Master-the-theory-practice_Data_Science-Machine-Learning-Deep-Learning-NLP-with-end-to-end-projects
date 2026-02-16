import logging
from venv import logger

## logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app3.log"),
        logging.StreamHandler()
    ]   
)

logger = logging.getLogger("Artimatic App")
def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b}={result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b}={result}")
    return result
def mul(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b}={result}")
    return result
def div(a, b):
    if b == 0:
        logger.error("Division by zero attempted", extra={"a": a, "b": b})
        return None
    result = a / b
    logger.debug(f"Dividing {a} by/ {b}={result}")
    return result

add(10, 5)
sub(10, 5)
mul(10, 5)
div(10, 0)
div(10, 2)
