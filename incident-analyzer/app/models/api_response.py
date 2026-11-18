from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class ApiResponse(Generic[T]):
    success: bool
    message: str
    data: T | None = None
