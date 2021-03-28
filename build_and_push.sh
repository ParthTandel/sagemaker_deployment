image=$1

chmod +x estimator/train
chmod +x estimator/serve

docker build  -t ${image} .
