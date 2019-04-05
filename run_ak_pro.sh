
# stop and remove tscore containers 
docker stop ak_service_1
docker rm ak_service_1

# Run tsusers Container
docker run -ti -d -p 5005:5005  --name ak_service_1 -e AK_APP_ENV="pro" -v "$PWD":/app -v /ak:/ak ahmedkammorah/ak_service