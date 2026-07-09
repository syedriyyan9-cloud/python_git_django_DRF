import logging

# Configure root logger: level=DEBUG means all messages DEBUG and above are captured
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),          # Prints to console
        logging.FileHandler('app.log')    # Writes to a file
    ]
)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    if b == 0:
        logging.error("Attempted division by zero!")
        return None
    return a / b

logging.info("Program started")
result = divide(10, 0)
logging.info(f"Result: {result}")
logging.warning("This is a warning message")

'''
The basicConfig sets a debug level and a detailed format that includes 
timestamps. We have two handlers: one shows logs on the console, another 
writes them to app.log. The divide function logs a debug message for 
tracing, and an error if division by zero occurs. Since our level is DEBUG, 
all messages appear. If we changed it to INFO, the debug line would be 
hidden. This setup gives you a permanent record (app.log) while still 
seeing output in real-time, which is far more robust than scattered print 
statements for any serious project.
'''