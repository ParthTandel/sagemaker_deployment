#!/bin/sh

# run this from project root directory
# sh local_test/train_local.sh


image=$1

# get the path from where, you are running the script
# note: run this from the root directory of the project
currentpath="$(pwd)"

# create model and output folder if not already present
mkdir -p $currentpath/demo_files/model/
mkdir -p $currentpath/demo_files/output/

# clean up model and output folders if things are already present in them
rm -rf $currentpath/demo_files/model/*
rm -rf $currentpath/demo_files/output/*

# run docker command by mounting local folder to /opt/ml/ folder
docker run -v $currentpath/demo_files/:/opt/ml/ --rm ${image} train