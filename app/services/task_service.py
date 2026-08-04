from datetime import datetime
from typing import List
from fastapi import HTTPException, status
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate, TaskStatus, TaskPriority

class TaskService:
    def __init__(self):
        # Bộ nhớ tạm lưu trữ danh sách tasks trong RAM cho Session 1
        self._tasks: List[TaskResponse] = [
            TaskResponse(
                id=1,
                title="Cài đặt dự án TaskHub",
                description="Khởi tạo skeleton app và cấu trúc thư mục Layered Architecture",
                status=TaskStatus.DONE,
                priority=TaskPriority.HIGH,
                created_at=datetime.now()
            )
        ]
        self._counter = 1

    def get_all_tasks(self) -> List[TaskResponse]:
        return self._tasks

    def get_task_by_id(self, task_id: int) -> TaskResponse:
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task với ID {task_id} không tồn tại!"
        )

    def create_task(self, task_in: TaskCreate) -> TaskResponse:
        self._counter += 1
        new_task = TaskResponse(
            id=self._counter,
            title=task_in.title,
            description=task_in.description,
            status=task_in.status,
            priority=task_in.priority,
            created_at=datetime.now()
        )
        self._tasks.append(new_task)
        return new_task

    def update_task(self, task_id: int, task_in: TaskUpdate) -> TaskResponse:
        task = self.get_task_by_id(task_id)
        update_data = task_in.model_dump(exclude_unset=True)
        
        updated_task = task.model_copy(update=update_data)
        
        for index, item in enumerate(self._tasks):
            if item.id == task_id:
                self._tasks[index] = updated_task
                break
                
        return updated_task

    def delete_task(self, task_id: int) -> dict:
        task = self.get_task_by_id(task_id)
        self._tasks.remove(task)
        return {"message": f"Đã xóa thành công Task ID {task_id}"}

task_service_instance = TaskService()

def get_task_service() -> TaskService:
    return task_service_instance
