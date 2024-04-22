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
3. Kubernetes using kubectl: Above steps as different deployments and containers.
4. Helm: Same as kubectl but using a single command using helm packaging.


### Prerequisites
- **Docker:** Here are the installation instructions: https://github.com/2kunal6/util/blob/main/installations.txt
- **Minikube:** Here are the installation instructions: https://github.com/2kunal6/util/blob/main/installations.txt


### Run commands
1. src/single_function:
    - Go to the directory: src/single_function
    - python3 -m pipenv shell
    - python3 -m pip install pipenv
    - python3 -m pipenv install
    - python3 single_function_all_ml_steps.py
      - This will parallely start the ML steps as processes.
2. src/docker_compose
    - Go to the directory src/docker_compose
    - docker compose up
      - This command will build and run the individual docker images which correspond to the ML steps.
3. Kubernetes using kubectl:
    - go to the directory src/helm_chart/templates
    - kubectl apply -f load_data_deployment.yaml
    - kubectl apply -f simulate_inference_deployment.yaml
    - kubectl apply -f simulate_inference_service.yaml
    - kubectl apply -f train_model_deployment.yaml
    - The above commands create the Kubernetes resources that hosts the docker containers created above.  For now it is using the docker images from my [docker-hub-account](https://hub.docker.com/repositories/2kunal6), but we can change this to use the docker images from our local machine itself (i.e. minikube's local machine, not our host machine)
4. Helm:
   - go to the directory src/helm_chart
   - helm install
     - This command creates all the resources created by kubectl with this single command.

Common comments for Kubectl and Helm:
- This will expose the Fast API app which you can use through your browser with the url http://<minikube-ip>:8000/docs#/default
      - This minikube ip can be found by running the command 'minikube ip' in your terminal
- Login to minikube using 'minikube ssh' and there we can see the pkl files of the data and model being created.
- kubectl logs <podname> will provide us with the logs, where we can confirm and debug the code execution.


### TODO
- Include Terraform
- Use Kubernetes CronJob instead of sleep
- Expose this over internet
- Apart from the above ones there are many things we can do to make the app more robust like load balancing user queries, communication between containers using a queue, store data and models in cloud, vault etc.
