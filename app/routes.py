from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
import subprocess

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@main.route("/run-script", methods=["POST"])
@login_required
def run_script():
    script = request.form.get("script")
    keywords = request.form.get("keywords", "")
    feeds = request.form.get("feeds", "")
    recipients = request.form.get("recipients", "")

    # Enregistre temporairement les données utilisateur (à remplacer plus tard par une DB)
    with open("user_input.txt", "w", encoding="utf-8") as f:
        f.write("Mots-clés:\n" + keywords + "\n\n")
        f.write("Flux RSS:\n" + feeds + "\n\n")
        f.write("Destinataires:\n" + recipients + "\n")

    # Appel du script selon le choix
    if script == "sonar":
        subprocess.Popen(["python", "app/logic/sonar.py"])
    elif script == "satellite":
        subprocess.Popen(["python", "app/logic/satellite.py"])
    else:
        flash("Script inconnu", "error")

    flash(f"Script {script} lancé avec succès !", "success")
    return redirect("/dashboard")
