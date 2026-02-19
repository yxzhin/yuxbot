from pydantic import BaseModel


class BaseResponseDTO(BaseModel):
    message: str
    success: bool
