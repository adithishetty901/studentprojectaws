from flask import Blueprint, render_template, request, redirect
from .database import SessionLocal
from .models import Student

main = Blueprint("main", __name__)

@main.route("/")
def index():
    session = SessionLocal()
    students = session.query(Student).all()
    session.close()
    return render_template("index.html", students=students)

@main.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]

        session = SessionLocal()
        student = Student(name=name, course=course)
        session.add(student)
        session.commit()
        session.close()

        return redirect("/")
    return render_template("add.html")

@main.route("/delete/<int:id>")
def delete(id):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id==id).first()
    session.delete(student)
    session.commit()
    session.close()
    return redirect("/")