import logging


api_client = logging.getLogger("api_client")
api_client.setLevel(logging.INFO)

file_handler =  logging.FileHandler("py_log1.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")


file_handler.setFormatter(formatter)
api_client.addHandler(file_handler)

api_client.info("test message")