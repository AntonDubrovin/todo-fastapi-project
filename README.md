Разработка и деплой FastAPI-сервисов с использованием Docker

TODO-сервис: Реализует CRUD-операции для списка задач с
хранением данных в SQLite

TODO-сервис:
- Эндпоинты:
  - POST /items: Создание задачи (title, description?, completed=false).
  - GET /items: Получение списка всех задач.
  - GET /items/{item_id}: Получение задачи по ID.
  - PUT /items/{item_id}: Обновление задачи по ID.
  - DELETE /items/{item_id}: Удаление задачи.
- Все операции должны работать с базой SQLite.
- Перед запуском должен автоматически создается таблица, если она не
существует.


Docker HUB: https://hub.docker.com/repository/docker/antondubrovin/todo_service/general


- docker build -t antondubrovin/todo_service:latest . 
- docker login
- docker push antondubrovin/todo_service:latest
- docker ps -a
- docker run -d -p 8000:80 antondubrovin/todo_service:latest

http://localhost:8000/docs
![image](https://github.com/user-attachments/assets/35cd3c55-2b61-48c1-9bc7-b4e3d959b30d)

