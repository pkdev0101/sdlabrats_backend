from flask import Blueprint, jsonify

from model.labrats_programs import LABRATS_PROGRAMS

programs_api = Blueprint(
    "programs_api",
    __name__,
    url_prefix="/api/programs"
)

@programs_api.route("/", methods=["GET"])
def get_programs():
    """San Diego LabRats program catalog; inquiry validation uses the same slugs."""
    return jsonify(LABRATS_PROGRAMS)
