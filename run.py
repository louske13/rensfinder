from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()  # ✅ Crée les tables s'il n'y en a pas

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
