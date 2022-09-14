import requests

#создаем папку на Yandex Диске 
def create_dir(dir_new):
    with open('tokens_id.txt','r') as document:
        str_token_VK = document.readline()
        str_user_ID_VK = document.readline()
        str_token_ya = document.readline()
        token_ya = str_token_ya.replace('\n','')
    Url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {"Authorization": token_ya}
    params = {"path":dir_new,"overwrite":"true"}
    res1 = requests.put(Url,headers = headers,params=params)
    res_st = res1.status_code
    return res_st

if __name__ == '__main__':
          
    str_dir = 'dir_for_photos'
    print(create_dir(str_dir))