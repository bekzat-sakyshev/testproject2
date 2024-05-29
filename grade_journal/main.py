from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return templates.TemplateResponse("index.html", {"request": request, "students": students})

@app.get("/students/create", response_class=HTMLResponse)
def create_student_form(request: Request):
    return templates.TemplateResponse("create_student.html", {"request": request})

@app.post("/students/", response_class=HTMLResponse)
def create_student(request: Request, name: str = Form(...), db: Session = Depends(get_db)):
    student = schemas.StudentCreate(name=name)
    crud.create_student(db=db, student=student)
    students = db.query(models.Student).all()
    return templates.TemplateResponse("index.html", {"request": request, "students": students})

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.create_score(db=db, score=score)

@app.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    db_score = crud.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score






# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List

# import crud, models, schemas
# from database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/students/", response_model=schemas.Student)
# def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
#     return crud.create_student(db=db, student=student)

# @app.get("/students/{student_id}", response_model=schemas.Student)
# def read_student(student_id: int, db: Session = Depends(get_db)):
#     db_student = crud.get_student(db, student_id=student_id)
#     if db_student is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return db_student

# @app.patch("/students/{student_id}", response_model=schemas.Student)
# def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
#     db_student = crud.update_student(db, student_id, student)
#     if db_student is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return db_student

# @app.delete("/students/{student_id}", response_model=schemas.Student)
# def delete_student(student_id: int, db: Session = Depends(get_db)):
#     db_student = crud.delete_student(db, student_id)
#     if db_student is None:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return db_student

# @app.post("/scores/", response_model=schemas.Score)
# def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
#     return crud.create_score(db=db, score=score)

# @app.get("/scores/{score_id}", response_model=schemas.Score)
# def read_score(score_id: int, db: Session = Depends(get_db)):
#     db_score = crud.get_score(db, score_id=score_id)
#     if db_score is None:
#         raise HTTPException(status_code=404, detail="Score not found")
#     return db_score

# @app.patch("/scores/{score_id}", response_model=schemas.Score)
# def update_score(score_id: int, score: schemas.ScoreCreate, db: Session = Depends(get_db)):
#     db_score = crud.update_score(db, score_id, score)
#     if db_score is None:
#         raise HTTPException(status_code=404, detail="Score not found")
#     return db_score

# @app.delete("/scores/{score_id}", response_model=schemas.Score)
# def delete_score(score_id: int, db: Session = Depends(get_db)):
#     db_score = crud.delete_score(db, score_id)
#     if db_score is None:
#         raise HTTPException(status_code=404, detail="Score not found")
#     return db_score
