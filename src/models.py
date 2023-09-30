from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    name: str
    description: Optional[str]
    priority: int

    start_cond: str
    end_cond: str
    timeout: Optional[int]

    disabled: bool
    force_termination: bool
    force_run: bool

    status: str
    is_running: bool
    last_run: Optional[datetime]
    last_success: Optional[datetime]
    last_fail: Optional[datetime]
    last_terminate: Optional[datetime]
    last_inaction: Optional[datetime]
    last_crash: Optional[datetime]


class Log(BaseModel):
    timestamp: Optional[datetime] = Field(alias="created")
    task_name: str
    action: str
