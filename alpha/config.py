import os
ENV = bool(os.environ.get("ENV", False))

if ENV:

    class Config(object):

      API_ID = int(os.environ.get("API_ID", 0))

    API_HASH = os.environ.get("API_HASH")

    STRING_SESSION = os.environ.get("STRING_SESSIOn")
