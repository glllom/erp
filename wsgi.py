from app import process_app, db
from flask_migrate import Migrate


if __name__ == '__main__':
    process_app.run(debug=True, port=5050)