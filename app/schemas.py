from pydantic import BaseModel, EmailStr


class PessoaCreate(BaseModel):
    nome: str
    email: EmailStr


class PessoaResponse(BaseModel):
    id: int
    nome: str
    email: str

    model_config = {"from_attributes": True}
