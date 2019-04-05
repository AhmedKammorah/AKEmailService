#!/usr/bin/env bash

export PYTHONPATH=$PYTHONPATH:$(pwd)/MainService
export AKSERVICE=$(pwd)/MainService
echo 'Path has been set'
python -c 'import sys; print(sys.path)'
echo '--------------------------------'
echo 'Buzz main path for key AKSERVICE'
echo $AKSERVICE
