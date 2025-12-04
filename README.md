# Ai checker

## Описание
Проект позволяет определить, написан текст человеком или искусственным интеллектом. Пользователь вводит текст, предложение и система анализирует его и возвращает результат с уверенностью

## Что нужно для запуска
Нужен docker, открытые порты **3000** **5000** **5173**

## Технологии
- Backend: Python, Flask, Flask-RESTful
- ML: обученная модель для классификации текста
- Frontend: Vue 3, Vite, CSS
- Docker: контейнеризация backend и frontend

## Структура проекта

│ ├─ app/<br>
│ │ ├─ main.py # flask сервер<br>
│ │ ├─ model.py # ML модель и функции<br>
│ ├─ requirements.txt<br>
│ └─ Dockerfile<br>
├─ frontend/<br>
│ ├─ src/<br>
│ │ ├─ App.vue # основной Vue компонент<br>
│ ├─ package.json<br>
│ └─ Dockerfile<br>
├─ gateway/<br>
|   ├─gateway.py # единный вход в приложение <br>
|   ├─dockerfile <br>
|
└─ docker-compose.yml


## Запуск
1. Сборка и запуск всего через Docker Compose::
```bash
docker-compose up --build
```

Использование:

**Откройте [localhost:5173](http://localhost:5173/)**
