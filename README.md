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
