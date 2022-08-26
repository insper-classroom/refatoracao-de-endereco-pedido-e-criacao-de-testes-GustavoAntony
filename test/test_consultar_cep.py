import pytest
import numpy as np
from classes.Endereco import Endereco


@pytest.mark.teste_com_internet
@pytest.mark.teste_verificacao
def test_criacao_endereco_sem_cep():
    num = 205

    with pytest.raises(TypeError) as excinfo:
        end = Endereco(num)
    assert 'missing 1 required positional argument: numero' in str(excinfo.value)

@pytest.mark.teste_com_internet
@pytest.mark.teste_verificacao
def test_criacao_endereco_sem_numero():
    pass





@pytest.mark.teste_robustez
@pytest.mark.teste_com_internet
def test_cep_como_int():
    cep = 12232239
    end = Endereco.consultar_cep(cep)
    assert end['logradouro'] == 'Rua José Bonifácio de Oliveira'

@pytest.mark.teste_robustez
@pytest.mark.teste_com_internet
def test_cep_como_string():
    cep = '12232239'
    end = Endereco.consultar_cep(cep)
    assert end['logradouro'] == 'Rua José Bonifácio de Oliveira'

@pytest.mark.teste_robustez
@pytest.mark.teste_com_internet
def test_erro_na_quantidade_digitos_cep():
    cep = 22322398989987
    end = Endereco.consultar_cep(cep)
    assert False == end

@pytest.mark.teste_robustez
@pytest.mark.teste_com_internet
def test_cep_nao_existe():
    cep = 99999999
    end = Endereco.consultar_cep(cep)
    assert False == end

@pytest.mark.teste_robustez
@pytest.mark.teste_sem_internet
def test_sem_internet():
    cep = 12232239
    end = Endereco.consultar_cep(cep)
    assert False == end