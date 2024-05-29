from sqlalchemy.orm import Session
import models, schemas

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()

def create_score(db: Session, score: schemas.ScoreCreate):
    db_score = models.Score(student_id=score.student_id, score=score.score)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score