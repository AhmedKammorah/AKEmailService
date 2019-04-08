# @Author: Ahmed kammorah
# @Date:   2019-04-06 01:13:33
# @Last Modified by:   Ahmed kammorah
# @Last Modified time: 2019-04-08 00:17:52
docker stop ak-redis
docker rm -f ak-redis
docker run --name ak-redis -d redis