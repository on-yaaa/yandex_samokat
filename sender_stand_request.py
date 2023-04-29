import configuration
import requests
import data

# запрос на создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, headers=data.headers, json=order_body)

# возвращение трека заказа
def get_order_track():
    response = post_new_order(data.order_body)
    return response.json().get('track')

# получение заказа по треку заказа
def get_order_on_track(track):
    headers_dict = data.headers.copy()
    return requests.post(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER, json={"track": track}, headers=headers_dict)

def test_create_and_get_order():
    track_number = get_order_track()
    retrieve_order_url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER.replace('{track_number}', str(track_number))

    response = requests.get(retrieve_order_url)

    assert response.status_code == 200