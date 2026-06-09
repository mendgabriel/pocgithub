from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Pessoa
from app.schemas import PessoaCreate, PessoaResponse

app = FastAPI(
    title="API de Cadastro de Pessoas",
    description="API simples para cadastrar e listar pessoas.",
    version="1.0.0",
)


@app.on_event("startup")
def criar_tabelas():
    Base.metadata.create_all(bind=engine)


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def pagina_inicial():
    return FileResponse("static/index.html")


@app.post("/pessoas", response_model=PessoaResponse, status_code=201)
def criar_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    existente = db.query(Pessoa).filter(Pessoa.email == pessoa.email).first()
    if existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

    nova_pessoa = Pessoa(nome=pessoa.nome, email=pessoa.email)
    db.add(nova_pessoa)
    db.commit()
    db.refresh(nova_pessoa)
    return nova_pessoa


@app.get("/pessoas", response_model=list[PessoaResponse])
def listar_pessoas(db: Session = Depends(get_db)):
    return db.query(Pessoa).order_by(Pessoa.id).all()
