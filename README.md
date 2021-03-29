# sagemaker_deployment
Simple sagemaker based deployment.


/opt/program/
    train - file used for training
    api - file which contains the flask container(name of the file can be different)
    nginx.cong - nginx server configuration which sagemaker uses
    wsgi.py - load the api application above, required by gunicorn
    serve - file which sagemaker uses to start a production ready flask server using nginx and gunicorn
    other files - eg utils files needed for some processing.

/opt/ml/
    input/ - this is where the input goes to.(Note you dont create it when building the container, 
        Sagemaker will pull input files in this directory which you pass in the fit function. 
        will talk more about this later)
        config/ - can add you model specific configuration here
        data/ - can put your data here
    model/ - save the model specific files fron you training here so that it can be used later
    output/ - any output you want to save
            