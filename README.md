# Task API(FastAPI + Async SQLAlchemy)

## Описание
Это REST API для управлением списком задач. Хотя в рамках тестового задания допускалось храниение данных в памяти, 
было принято решение реализовать полноценную backend-архитектуру с использованием базы данных и асинхронного ORM, чтобы продемонстрировать production-ready подход.

---

## Технологии

- FastAPI
- SQLAlchemy 2.0
- SQLite
- Pydantic v2
- Python 3.12

---

## Архитектурное решение 

Проект построен как production-style backend:

### Слои приложения

- router - HTTP слой 
- services - бизнес-логика
- schemas - валидация
- models - модели
- db - конфигурация базы данных и сессий

---

## Запуск
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```