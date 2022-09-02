import pytest
import numpy as np
from classes.Endereco import Endereco
import http.client as httplib
from requests.exceptions import ConnectionError
import requests
import json

def test_criacao_pessoa_fisica():
    nome = 'Carlos'
    pass