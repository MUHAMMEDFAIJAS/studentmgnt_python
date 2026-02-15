from flask import Flask, request, jsonify
from models import (
    create_table,
    add_student,
    get_students,
    get_student,
    update_student,
    delete_student
)

app = Flask(__name__)

create_table()


@app.route("/")
def home():
    return jsonify({"message": "Student Management API Running"})


@app.route("/students", methods=["POST"])
def create():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    name = data.get("name")
    mark = data.get("mark")

    if not name or mark is None:
        return jsonify({"error": "Name and mark required"}), 400

    add_student(name, mark)
    return jsonify({"message": "Student created"}), 201


# READ ALL
@app.route("/students", methods=["GET"])
def read_all():
    students = get_students()
    return jsonify([
        {"id": s[0], "name": s[1], "mark": s[2]}
        for s in students
    ])


# READ ONE
@app.route("/students/<int:student_id>", methods=["GET"])
def read_one(student_id):
    student = get_student(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({
        "id": student[0],
        "name": student[1],
        "mark": student[2]
    })


# UPDATE
@app.route("/students/<int:student_id>", methods=["PUT"])
def update(student_id):
    data = request.get_json()

    if not data or "name" not in data or "mark" not in data:
        return jsonify({"error": "Name and mark required"}), 400

    update_student(student_id, data["name"], data["mark"])
    return jsonify({"message": "Student updated"})


# DELETE
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete(student_id):
    delete_student(student_id)
    return jsonify({"message": "Student deleted"})


if __name__ == "__main__":
    app.run(debug=True)
