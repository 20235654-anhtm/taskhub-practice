from typing import List
from fastapi import APIRouter, Depends, status
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService, get_task_service

router = APIRouter()

@router.get("", response_model=List[TaskResponse], summary="Lấy danh sách tất cả Task")
def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_all_tasks()

@router.get("/{task_id}", response_model=TaskResponse, summary="Lấy chi tiết 1 Task")
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.get_task_by_id(task_id)

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED, summary="Tạo mới 1 Task")
def create_task(task_in: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task_in)

@router.patch("/{task_id}", response_model=TaskResponse, summary="Cập nhật thông tin Task")
def update_task(task_id: int, task_in: TaskUpdate, service: TaskService = Depends(get_task_service)):
    return service.update_task(task_id, task_in)

@router.delete("/{task_id}", summary="Xóa 1 Task")
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    return service.delete_task(task_id)
