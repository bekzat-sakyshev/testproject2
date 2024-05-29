from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
        from_attributes = True

class ScoreBase(BaseModel):
    student_id: int
    score: int

class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    id: int
    class Config:
        from_attributes = True