import pytest
from create_dir_ya_disk import create_dir

def test_create_dir():   
    assert create_dir('new_dir_test') == 201 , "Папка не создаётся,возможно она уже есть" 
        
def test_create_dir_3XX():   
    assert 400 > create_dir('new_dir_test') >= 300 , "Не перенаправление"   

def test_create_dir_4XX():   
    assert 500 > create_dir('new_dir_test') >= 400 , "Не ошибка клиента"
    
def test_create_dir_5XX():   
    assert  create_dir('new_dir_test') >= 500 , "Не ошибка сервера"

if __name__ == '__main__':
    
        test_create_dir()
 
    
    