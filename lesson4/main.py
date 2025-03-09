from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import select
from datetime import date

import database as db

app = FastAPI()


class Lesson(BaseModel):
    title: str
    date: date

    class Config:
        from_attributes = True


class Student(BaseModel):
    id: int
    name: str
    year: int

    class Config:
        from_attributes = True


class Teacher(BaseModel):
    id: int
    name: str
    yoe: int

    class Config:
        from_attributes = True


class TeacherWithLesson(BaseModel):
    teacher: Teacher
    lesson: str

    class Config:
        from_attributes = True


def get_db():
    session = db.session
    try:
        yield session  # Отдаём сессию в эндпоинт
        session.commit()  # Коммитим, если не было ошибок
    except Exception:
        session.rollback()  # Откатываем транзакцию, если была ошибка
        raise
    finally:
        session.close()  # Всегда закрываем сессию


@app.post('/teachers')
def add_teachers(teacher: Teacher, session: db.Session = Depends(get_db)):
    session.add(db.Teacher(**teacher.model_dump()))
    return f"{teacher.name} was added to db"


@app.get('/teachers')
def get_teachers() -> list[Teacher]:
    return [Teacher.model_validate(teacher) for teacher in db.session.execute(select(db.Teacher)).scalars().all()]


@app.post('/students')
def add_teachers(student: Student, session: db.Session = Depends(get_db)):
    session.add(db.Student(**student.model_dump()))
    return f"{student.name} was added to db"


@app.get('/students')
def get_teachers() -> list[Student]:
    return [Student.model_validate(student) for student in db.session.execute(select(db.Student)).scalars().all()]

@app.post('/lessons')
def add_teachers(lesson: Lesson, session: db.Session = Depends(get_db)):
    session.add(db.Lesson(**lesson.model_dump()))
    return f"{lesson.title} was added to db"


@app.get('/lessons')
def get_teachers() -> list[Lesson]:
    return [Lesson.model_validate(lesson) for lesson in db.session.execute(select(db.Lesson)).scalars().all()]


# def nested_dependency(teacher_with_lesson: TeacherWithLesson):
#     lesson = teacher_with_lesson.lesson
#     teacher = teacher_with_lesson.teacher
#     return f"You have joined {lesson}, Your teacher is {teacher.name} with {teacher.yoe} years of experience"
#
#
# def dependency(nested_dep_func: str = Depends(nested_dependency)) -> str:
#     print("Started Handling Nested Dependency Function")
#     return nested_dep_func
#
#
# def car_nested_dependency(car: Car):
#     return f"{car.model} costs {car.price} Nested!"
#
#
# def car_dependency(nested_dep_func: str = Depends(car_nested_dependency)) -> str:
#     return nested_dep_func
#
#
# def car_dependency_not_nested(car: Car):
#     return f"{car.model} costs {car.price}"
#
#
# @app.post('/student')
# def student(dep_func: str = Depends(dependency)):
#     return dep_func
#
#
# @app.post('/car')
# def add_car(dep_func: str = Depends(car_dependency)):
#     return dep_func
