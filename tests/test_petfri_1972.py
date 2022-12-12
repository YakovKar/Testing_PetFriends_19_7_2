from api import PetFriends
from settings import valid_email,valid_password
import os

pf = PetFriends()

def test_add_new_pet_simple(name='Хофма', animal_type='Кошка', age='27'):
    """Проверяем можно ли добавить животного без изображения через запрос POST /api/create_pet_simple"""

    #Запрашиваем ключ api и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    #Добавляем питомца без изображения
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    #Сверяем полученный результат с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_photo_pet(pet_photo='images/hofma_nya.jpg'):
    """Проверяем возможность добавить фотографию"""

    #Получаем ключ и запрашиваем список питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    #Получаем полный путь к изображениюпитомцаи сохраняем его в переменную pet_photo
    #pet_photo = os.path.join(os.path.dirname(__file__), pet_photo) #С помощью dirname определяем директорию из которой запущен тест

    #Если список не пустой то пробуем обновить его фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_new_photo_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200

    #Если список питомцев пустой то, вызываем ошибку
    else:
        # Если список питомцев пустой то, вызываем ошибку
         raise Exception('There is no my pets')

def test_get_api_key_non_valid_data(email="non-existent@gmail.com", password="15432"):
    """Проверяем что запрос api ключа возвращает статус 403, т.к. это незарегистрированный пользователь"""

    #Запрашиваем ключ api и сохраняем его в переменную auth_key
    status, result = pf.get_api_key("non-existent@gmail.com", "15432")


    #Сверяем полученный результат с ожидаемым результатом
    assert status == 403
    return "Пользователь не зарегестрирован"

def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этот ключ
    запрашиваем список моих питомцев 'my_pets' """

    _,auth_key = pf.get_api_key(valid_email, valid_password)
    status,result =pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_simple_without_data(name='', animal_type='', age=''):
    """Проверяем что можно добавить питомца без фото с пустыми полями данных"""

      # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_simple_with_long_data(name='repeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatnamerepeatname',
                                           animal_type='onetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetypeonetype',
                                           age='2143254435435098493453430485093485843958340583845083405983408508340583984509834058883405834583405834058348503480583405830485093485098340580934805834853485034850934850934850983408583408534085038405834058304583459034754357634752365467234567235745237645234069798'):
    """Проверяем можно ли добавить питомца, если ввести длинные параметры"""

      # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_simple_with_chinese_data(name='安吉丽娜*光', animal_type='某种中国动物', age='四十三'):
    """Проверяем можно ли добавить животное, если ввести параметры на китайском"""

      # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_get_my_pets_with_valid_key(filter='my_pits'):
    """ Проверяем, что тест выдаст ошибку, если ошибиться в параметре фильтр"""

    _,auth_key = pf.get_api_key(valid_email, valid_password)
    status,result =pf.get_list_of_pets(auth_key, filter)
    #Ошибка сигнализирующая, что сервер не может обработать отправленный запрос
    assert status == 500
    print("There is no such filter")

def test_add_new_pet_with_valid_data(name='Павел', animal_type='Жираф',
                                     age='15', pet_photo='images/zho_rafik.jpg'):
    """Проверяем можно ли добавить питомца, если указан неверный адрес фото"""
    try:
        #Получаем полный путь к изображению питомца и сохраняем его в переменную pet_photo
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

        #Запрашиваем ключ api и сохраняем его в переменную auth_key
        _, auth_key = pf.get_api_key(valid_email, valid_password)

        #Добавляем питомца
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    except FileNotFoundError:
        print('Photo not found')

def test_add_new_pet_simple(name='Хофма', animal_type='Кошка', age='27', colour='white'):
    """Проверяем можно ли добавить животного с непредусмотреннным параметром
    :param colour:
    """

    #Запрашиваем ключ api и сохраняем его в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    #Добавляем питомца без изображения
    status, result = pf.add_new_pet_simple(auth_key, name, animal_type, age)

    #Сверяем полученный результат с ожидаемым результатом
    assert status == 200
    assert result['name'] == name








