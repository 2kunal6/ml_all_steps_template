### Run command 
- sudo docker build -t foo . && sudo docker run -p 8000:8000 foo
- Run this from the project root location where Dockerfile exists

### Access
- After this is complete, we can access the app via browser using the url outputted.
- For the Fast API homepage: http://0.0.0.0:8000/docs#/default
- For now the External URL won't be available with this config, but that would be available if we run it without Docker.

### TODO
- Expose this over internet

### Prerequisites
- **Docker:** Here are the installation instructions: https://github.com/2kunal6/util/blob/main/installations.txt


kubernetes:
- minikube ip
- more robust: kubernetes cron, kafka, s3 to store data and models, vault
