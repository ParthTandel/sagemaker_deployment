#!/bin/sh

image=$1

mkdir -p /home/parth/sagemaker_deployment/demo_files/model/
mkdir -p /home/parth/sagemaker_deployment/demo_files/output/

rm -rf /home/parth/sagemaker_deployment/demo_files/model/*
rm -rf /home/parth/sagemaker_deployment/demo_files/output/*

docker run -v /home/parth/sagemaker_deployment/demo_files/:/opt/ml/ --rm ${image} train