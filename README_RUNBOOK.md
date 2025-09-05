Runbook commands

# create venv
python3 -m venv venv
source venv/bin/activate

# install
pip install -r requirements.txt

# run locally
export FLASK_APP=app:create_app
flask run

# docker
docker build -t flask-basics-demo .
docker run -p 8000:8000 flask-basics-demo

# tests
pip install -r tests/requirements.txt
pytest -q
