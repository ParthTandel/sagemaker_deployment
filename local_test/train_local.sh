#!/bin/sh

# run this from project root directory
# sh local_test/train_local.sh


image=$1

currentpath="$(pwd)"

mkdir -p $currentpath/demo_files/model/
mkdir -p $currentpath/demo_files/output/

rm -rf $currentpath/demo_files/model/*
rm -rf $currentpath/demo_files/output/*

docker run -v $currentpath/demo_files/:/opt/ml/ --rm ${image} train