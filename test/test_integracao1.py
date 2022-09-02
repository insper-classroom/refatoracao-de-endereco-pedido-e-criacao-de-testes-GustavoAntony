import pytest
import numpy as np
from classes.Endereco import Endereco
import http.client as httplib
from requests.exceptions import ConnectionError
import requests
import json


#utilizar seguinte código: pytest -v -m main2
#teste de integração pelo pedido completo: pytest -v -m teste_integracao_pedido
