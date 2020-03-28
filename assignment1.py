from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

STUDENTS = {
  '1': {'student_id': 100688204, 'first_name': 'shubham', 'last_name': 'dikshit', 'DOB': '26/08/1992', 'Amount_Due': 0},
  '2': {'student_id': 100688205, 'first_name': 'himanshu', 'last_name': 'dhiman', 'DOB': '16/05/1995', 'Amount_Due': 0},
  '3': {'student_id': 100688203, 'first_name': 'ankit', 'last_name': 'patel', 'DOB': '13/05/1993', 'Amount_Due': 0},
  '4': {'student_id': 100688206, 'first_name': 'harin', 'last_name': 'shah', 'DOB': '13/07/1989', 'Amount_Due': 0},
}
parser = reqparse.RequestParser()

class StudentsList(Resource):
    def get(self):
        return STUDENTS
    def post(self):
        parser.add_argument("student_id")
        parser.add_argument("first_name")
        parser.add_argument("last_name")
        parser.add_argument("DOB")
        parser.add_argument("Amount_Due")
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id
        STUDENTS[student_id] = {
         "student_id": args["student_id"],
         "first_name": args["first_name"],
         "last_name": args["last_name"],
         "DOB": args["DOB"],
         "Amount_Due": args["Amount_Due"],
        }
        return STUDENTS[student_id], 201



class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id]
    def put(self, student_id):
        parser.add_argument("student_id")
        parser.add_argument("first_name")
        parser.add_argument("last_name")
        parser.add_argument("DOB")
        parser.add_argument("Amount_Due")
        args = parser.parse_args()
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["student_id"] = args["student_id"] if args["student_id"] is not None else student["student_id"]
            student["first_name"] = args["first_name"] if args["first_name"] is not None else student["first_name"]
            student["last_name"] = args["last_name"] if args["last_name"] is not None else student["last_name"]
            student["DOB"] = args["DOB"] if args["DOB"] is not None else student["DOB"]
            student["Amount_Due"] = args["Amount_Due"] if args["Amount_Due"] is not None else student["Amount_Due"]
            return student, 200
    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
        return '', 204

api.add_resource(Student, '/students/<student_id>')
api.add_resource(StudentsList, '/students/')
if __name__ == "__main__":
  app.run(debug=False)