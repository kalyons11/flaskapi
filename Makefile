default: install test

install:
	pip install -r requirements.txt
	pip install . --upgrade

deploy:
	pip install pipreqs
	pipreqs . --force

test:
	docker ps
	docker build . -f Dockerfile.test -t flaskapi-test
	docker run -p 5000:5000 --rm -it flaskapi-test 

start:
	docker build . -t flaskapi
	docker run -p 5000:5000 --rm -it flaskapi 
