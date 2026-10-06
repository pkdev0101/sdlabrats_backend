from flask import Blueprint, jsonify

programs_api = Blueprint(
    "programs_api",
    __name__,
    url_prefix="/api/programs"
)

@programs_api.route("/", methods=["GET"])
def get_programs():
    programs = [
        {
            "id": 1,
            "name": "After School Program",
            "grades": "K-8",
            "description": "Hands-on science activities for students."
        },
        {
            "id": 2,
            "name": "Summer Camps",
            "grades": "K-8",
            "description": "Science-focused summer camp programs."
        }
    ]

    return jsonify(programs)