import logging

# Configure logging with date/time and output to file and console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")


def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result

def mul(a, b):
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result

def div(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

# Run operations
add(10, 15)
sub(15, 10)
mul(10, 10)
div(20, 0)
