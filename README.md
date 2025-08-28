# Python face-finder

**Create/Start python venv**
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate

**Run local dev server**
`fastapi dev src/main.py --host 0.0.0.0 --port 8000`

**Run deployment server**
`fastapi run src/main.py`

**Build docker**
`docker build . -t face-finder`

**Run docker**
`docker run -p 8000:8000 face-finder`
