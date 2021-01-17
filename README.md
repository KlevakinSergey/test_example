Create .env and paste environment variables in .env file with your values
Change direction to the folder with docker-compose.yml file
Run the command: docker-compose up -d --build
Create a superuser account with the command: docker-compose exec app python3 manage.py createsuperuser
Browse to one of the following links: http://0.0.0.0:8000/pages/ or http://0.0.0.0:8000/api/v1/
