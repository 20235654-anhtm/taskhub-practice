# TaskHub - Task Management System API

Dự án TaskHub phục vụ thực hành FastAPI Layered Architecture.

## Session 1: Core Setup & Architecture
- Khung dự án chuẩn Layered Architecture (`core`, `schemas`, `services`, `api`).
- Khởi tạo `FastAPI` instance với `lifespan` event và `APIRouter`.
- Pydantic v2 validation cho `Task`.
- CRUD endpoints cơ bản cho `Task` (in-memory mock storage).

## Cách chạy dự án
1. Kích hoạt môi trường ảo:
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
2. Cài đặt các gói phụ thuộc:
   ```bash
   pip install -r requirements.txt
   ```
3. Chạy server phát triển:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Truy cập giao diện API Documentation (Swagger UI):
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
