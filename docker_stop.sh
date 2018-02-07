#!/bin/bash
CONTAINERID=$(docker ps --filter "name=pythonapp" -aq)
if [ $CONTAINERID ]
	then
		docker stop $CONTAINERID
		docker rm $CONTAINERID
fi