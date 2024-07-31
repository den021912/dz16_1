from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def page() -> dict:
    return { '': "Главная страница"}

@app.get('/user/admin')
def admin_page() -> dict:
    return { 'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
def admin_id_page(user_id: str) -> dict:
    return { 'message': f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
def user_page(username: str, age: int) -> dict:
    return {'Информация о пользователе.' 'Имя': username, 'Возраст': age}
