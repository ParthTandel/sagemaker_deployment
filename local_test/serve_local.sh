
# run train_local before once so that the necesarry files are saved in /opt/model/ model older

# run this from project root directory
# sh local_test/serve_local.sh

image=$1
# get the path from where, you are running the script
# note: run this from the root directory of the project
currentpath="$(pwd)"

# run docker command by mounting local folder to /opt/ml/ folder with post 8080 expose
# as this will be the port we will use to query our server
docker run -v $currentpath/demo_files/:/opt/ml/ -p 8080:8080 --rm ${image} serve