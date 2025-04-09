from flask import Blueprint, jsonify
from flask_restful import Api, Resource

student_api = Blueprint('student_api', __name__, url_prefix='/api')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(student_api)

class StudentAPI:
    @staticmethod
    def get_student(name):
        students = {
            "Arshia": {
                "name": "Arshia",
                "age": "16",
                "role": "Scrum",
                "school": "Del Norte High School"
            },
            "Prajna": {
                "name": "Prajna",
                "age": "16",
                "role": "Assistant Scrum",
                "school": "Del Norte"
            },
            "Zoe": {
                "name": "Zoe",
                "age": "16",
                "role": "Devloper",
                "school":"Del Norte"
            },
             "Sanya": {
                "name": "Sanya",
                "age": "16",
                "role": "Devloper",
                "school":"Del Norte"
            },
              "Mirabelle": {
                "name": "Mirabelle",
                "age": "17",
                "role": "Integrator",
                "school":"Del Norte"
            },
               "Claire": {
                "name": "Claire",
                "age": "16",
                "role": "Devloper",
                "school":"Del Norte"
            },
            
        }
        return students.get(name) 

    class _Arshia(Resource):
        def get(self):
            # Use the helper method to get John's details
            arshia_details = StudentAPI.get_student("Arshia")
            return jsonify(arshia_details)

    class _Prajna(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            prajna_details = StudentAPI.get_student("Prajna")
            return jsonify(prajna_details)
    class _Zoe(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            zoe_details = StudentAPI.get_student("Zoe")
            return jsonify(zoe_details)
    class _Sanya(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            sanya_details = StudentAPI.get_student("Sanya")
            return jsonify(sanya_details)
    class _Mirabelle(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            mirabelle_details = StudentAPI.get_student("Mirabelle")
            return jsonify(mirabelle_details)
    class _Claire(Resource):
        def get(self):
            # Use the helper method to get Jeff's details
            claire_details = StudentAPI.get_student("Claire")
            return jsonify(claire_details)
    class _Bulk(Resource):
        def get(self):
            # Use the helper method to get both John's and Jeff's details
            arshia_details = StudentAPI.get_student("Arshia")
            prajna_details = StudentAPI.get_student("Prajna")
            zoe_details = StudentAPI.get_student("Zoe")
            sanya_details = StudentAPI.get_student("Sanya")
            mirabelle_details = StudentAPI.get_student("Mirabelle")
            claire_details = StudentAPI.get_student("Claire")
            return jsonify({"students": [arshia_details, prajna_details, zoe_details, sanya_details, mirabelle_details, claire_details]})

    # Building REST API endpoints
    api.add_resource(_Arshia, '/student/arshia')
    api.add_resource(_Prajna, '/student/prajna')
    api.add_resource(_Zoe, '/student/zoe')
    api.add_resource(_Sanya, '/student/sanya')
    api.add_resource(_Mirabelle, '/student/mirabelle')
    api.add_resource(_Claire, '/student/claire')
    api.add_resource(_Bulk, '/students')

# Instantiate the StudentAPI to register the endpoints
student_api_instance = StudentAPI()