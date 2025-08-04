from flask import Blueprint, render_template

documentation_bp = Blueprint('documentation', __name__)

@documentation_bp.route("/documentation")
def documentation():
    return render_template("doc.html")