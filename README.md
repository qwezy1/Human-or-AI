# Ai checker

## Описание
Проект позволяет определить, написана ли новость человеком или искусственным интеллектом. Пользователь вводит текст новости, система анализирует его и возвращает результат с уверенностью

## Технологии
- Backend: Python, Flask, Flask-RESTful
- ML: обученная модель для классификации текста
- Frontend: Vue 3, Vite, CSS
- Docker: контейнеризация backend и frontend

## Структура проекта

├─ backend/<br>
│ ├─ app/<br>
│ │ ├─ main.py # Flask сервер<br>
│ │ ├─ model.py # ML модель и функция predict_class<br>
│ ├─ requirements.txt<br>
│ └─ Dockerfile<br>
├─ frontend/<br>
│ ├─ src/<br>
│ │ ├─ App.vue # Основной Vue компонент<br>
│ ├─ package.json<br>
│ └─ Dockerfile<br>
└─ docker-compose.yml


## Запуск
1. Сборка и запуск всего через Docker Compose::
```bash
docker-compose up --build
```

Использование:

**Откройте [localhost:8080](http://localhost:8080/)**