### Introduction
ML applications are comprised of the following fundamental steps that work in symphony to provide inferences:
1. Load data periodically
2. Train Model periodically
3. Serve inferences

These are just the fundamental steps and these could be further subdivided into many steps like data wrangling, feature extraction, parameter fine-tuning etc.  There could be additional steps as well like storing and analyzing user feedback, analyzing inference quality, result post-processing to filter out harmful content, etc.

Furthermore, the training step is not required for unsupervised apps and that can be replaced by a fine-tuning step which provides the best results.  Ex. Finding the best k in KNN or K-means clustering.


### Deployment
Kubernetes is one of the deployment options which runs the above steps as different deployments or containers, but there's a learning curve to that.

In this project, I tried to show a template implementation in the following increasing levels of difficulty, and with that increasing levels of quality and robustness of the app:
1. Processes: A single python function with the above steps working in parallel as processes.
2. Docker Compose: Above steps as different docker containers.
3. Kubernetes kubectl: Above steps as different deployments and containers.
4. Helm: Same as kubectl (i.e. different deployments and containers) but using a single command using helm packaging.


### Prerequisites
- **Docker:** Here are the installation instructions: https://github.com/2kunal6/util/blob/main/installations.txt
- **Minikube:** Here are the installation instructions: https://github.com/2kunal6/util/blob/main/installations.txt


### Run commands
1. src/single_function:
    - 
- sudo docker build -t foo . && sudo docker run -p 8000:8000 foo
- Run this from the project root location where Dockerfile exists

### TODO
- Expose this over internet



kubernetes:
- minikube ip
- more robust: kubernetes cron, kafka, s3 to store data and models, vault
- minikube ssh -> and check if the pkl files are created
- Fast API homepage: http://0.0.0.0:8000/docs#/default
- kubectl logs <podname>
- docker images created from 'docker compose up'
