
# Build by   build_dev_image.sh

docker stop ak_service-dev_1
docker rm ak_service-dev_1
# Run
# docker run -ti -d -p 8000:8000 --name admin -v "$PWD":/app  kammorah/django-dev
docker run -ti --rm -p 5000:5000 --link  ak-redis:ak-redis --name ak_service-dev_1 -e AK_APP_ENV="dev" -v "$PWD":/app -v /ak:/ak  ahmedkammorah/ak_service
 
# docker exec -it tsusers-dev bash

# Run Server
# python manage.py runserver 0.0.0.0:8000


 