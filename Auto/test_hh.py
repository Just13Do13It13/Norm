import requests
def test_status():
    resp = requests.get("https://api.hh.ru/vacancies?text=['qa','python']")
    assert resp.status_code == 200, "Статус код некорректный\n{resp.status_code}"
    print("Апи работает!")