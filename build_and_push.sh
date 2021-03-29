image=$1

# convert the train and serve python code to executables
chmod +x estimator/train
chmod +x estimator/serve

# builds a docker container and tags it with the name you pass a input
docker build  -t ${image} .
