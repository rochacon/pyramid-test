default: deps test

deps:
	@pip install -r requirements.txt

test:
	@py.test -s tests/

get-gunicorn:
	@pip install -U gunicorn

run: get-gunicorn
	@gunicorn -b 127.0.0.1:8000 app:application

