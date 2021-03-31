# file is exactly same as the one in aws example code base
# https://github.com/aws/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/container/build_and_push.sh
image=$1

# convert the train and serve python code to executables
chmod +x estimator/train
chmod +x estimator/serve

# Now that we are staring to work with aws, some key things here
# you will need an AWS accoun obviously.
# you will have to download the credential if you haven't already set up
# you will have to install aws command line tool. one option is using pip
# using the tool you can set the credentials up
# information present in the below link
# https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html 


# aws commant to get account information
account=$(aws sts get-caller-identity --query Account --output text)

if [ $? -ne 0 ]
then
    exit 255
fi

# Get the region defined in the current configuration (default to us-west-2 if none defined)
region=$(aws configure get region)
region=${region:-us-west-2}

# creates an ECR usr where teh container will be pushed
fullname="${account}.dkr.ecr.${region}.amazonaws.com/${image}:latest"


# If the repository doesn't exist in ECR, create it.
aws ecr describe-repositories --repository-names "${image}" > /dev/null 2>&1

if [ $? -ne 0 ]
then
    aws ecr create-repository --repository-name "${image}" > /dev/null
fi


# Get the login command from ECR and execute it directly
aws ecr get-login-password --region "${region}" | docker login --username AWS --password-stdin "${account}".dkr.ecr."${region}".amazonaws.com


# Build the docker image locally with the image name and then push it to ECR
# with the full name.

docker build  -t ${image} .
docker tag ${image} ${fullname}

# push container to ecr
docker push ${fullname}