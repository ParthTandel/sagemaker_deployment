
# run train_local before once so that the necesarry files are saved in /opt/model/ model older

# run this from project root directory
# sh local_test/serve_local.sh

image=$1
currentpath="$(pwd)"
docker run -v $currentpath/demo_files/:/opt/ml/ -p 8080:8080 --rm ${image} serve