1) To Run Locally

------------------

cd ai-iris-deployment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

----------------------

2) Dockerize the App

----------------------

docker build -t iris-api:latest .
docker run -d --name iris-api -p 8000:8000 iris-api:latest
# List running containers
docker ps
-------------
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS       PORTS                                    NAMES
315207e768e6   iris-api:latest   "uvicorn app.main:ap…"   17 minutes ago   Up 17 minutes   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   iris-api
---------------
# Stop the container 
docker stop iris-api
# Remove it (optional) (Stopping only ends the container — removing deletes the instance (safe to recreate later).)
docker rm iris-api
-----------------

3) Docker Compose (Simulate Multi-Service Environment)

docker compose up --build

Open your browser and go to:
http://localhost:8000
To open API docs:
http://localhost:8000/docs

ctrl+c -> to stop it

# Then to fully shut down & remove the compose stack:
docker compose down
-----------------
4) Docker Compose to run in background
# To run it in background (-d = detached mode (runs in background))
docker compose up -d

# Check status
docker ps

# To stop it
docker compose down

# (When I run Docker Compose in attached mode, the terminal streams live logs, and Ctrl+C stops the stack. When I run it in detached mode using -d, the app runs in the background like a real service.)

5) Kubernetes 

# to install minikube
brew install minikube
brew install kubectl

# start local cluster
minikube start

# Apply manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# List resources
kubectl get pods
kubectl get svc

# Open service
minikube service iris-api-service


# to scale to 4  
kubectl scale deployment iris-api-deployment --replicas=4

# if any error

kubectl get pods

kubectl get deploy,svc
# if the status is image pull back off - there is error loading image

kubectl get deployment iris-api-deployment -o yaml | grep -A3 "image:"

# Make sure the image exists locally

docker images | grep iris-api

# Load the image into Minikube

minikube image load iris-api:latest

"change yaml file to 
containers:
  - name: iris-api
    image: iris-api:latest (previously it was your-username/iris-api: latest)
    imagePullPolicy: IfNotPresent
    ports:
      - containerPort: 8000"

# Apply it again
kubectl apply -f k8s/deployment.yaml

kubectl rollout status deployment/iris-api-deployment

kubectl get pods

# expose minikube service again 

minikube service iris-api-service

# check 2nd url/docs

# ctrl+c to stop

#optionally stop k8s resource

kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/deployment.yaml

