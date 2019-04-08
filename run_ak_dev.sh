
# Build by   build_dev_image.sh

docker stop ak_service-dev_1
docker rm ak_service-dev_1
# Run
docker run -ti --rm -p 5001:5000 --link  ak-redis:ak-redis --name ak_service-dev_1 -e AK_APP_ENV="dev" -v "$PWD":/app -v /ak:/ak  ahmedkammorah/ak_email_service
