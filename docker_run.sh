#!/bin/bash
CONTAINERID=$(docker ps --filter "name=pythonapp" -aq)
if [ $CONTAINERID ]
	then
		docker stop $CONTAINERID
		docker rm $CONTAINERID
fi
docker run -t -d -p 4000:4000 --name pythonapp pythonapp