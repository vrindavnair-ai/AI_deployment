--> 1) To Run Locally

------------------

1) cd ai-iris-deployment
2) python -m venv .venv
3) source .venv/bin/activate  # On Windows: .venv\Scripts\activate
4) pip install -r app/requirements.txt
5) uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

----------------------

--> 2) Dockerize the App

----------------------

1) docker build -t iris-api:latest .
2) docker run -d --name iris-api -p 8000:8000 iris-api:latest
# List running containers
3) docker ps
-------------
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS       PORTS                                    NAMES
315207e768e6   iris-api:latest   "uvicorn app.main:ap…"   17 minutes ago   Up 17 minutes   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   iris-api
---------------
# Stop the container 
4) docker stop iris-api
# Remove it (optional) (Stopping only ends the container — removing deletes the instance (safe to recreate later).)
5) docker rm iris-api
-----------------

--> 3) Docker Compose (Simulate Multi-Service Environment)

1) docker compose up --build

Open your browser and go to:
http://localhost:8000
To open API docs:
http://localhost:8000/docs

ctrl+c -> to stop it

# Then to fully shut down & remove the compose stack:
2) docker compose down

-----------------

--> 4) Docker Compose to run in background
# To run it in background (-d = detached mode (runs in background))
1) docker compose up -d

# Check status
2) docker ps

# To stop it
3) docker compose down

# (When I run Docker Compose in attached mode, the terminal streams live logs, and Ctrl+C stops the stack. When I run it in detached mode using -d, the app runs in the background like a real service.)

--> 5) Kubernetes 

# to install minikube
1) brew install minikube
2) brew install kubectl

# start local cluster
3) minikube start

# Apply manifests
4) kubectl apply -f k8s/deployment.yaml
5) kubectl apply -f k8s/service.yaml

# List resources
6) kubectl get pods
7) kubectl get svc

# Open service
8) minikube service iris-api-service


# to scale to 4  
9) kubectl scale deployment iris-api-deployment --replicas=4

# if any error

10) kubectl get pods

11) kubectl get deploy,svc
# if the status is image pull back off - there is error loading image

12) kubectl get deployment iris-api-deployment -o yaml | grep -A3 "image:"

# Make sure the image exists locally

13) docker images | grep iris-api

# Load the image into Minikube

14) minikube image load iris-api:latest

"change yaml file to 
containers:
  - name: iris-api
    image: iris-api:latest (previously it was your-username/iris-api: latest)
    imagePullPolicy: IfNotPresent
    ports:
      - containerPort: 8000"

# Apply it again
15) kubectl apply -f k8s/deployment.yaml

16) kubectl rollout status deployment/iris-api-deployment

17) kubectl get pods

# expose minikube service again 

18) minikube service iris-api-service

# check 2nd url/docs

# ctrl+c to stop

#optionally stop k8s resource

19) kubectl delete -f k8s/service.yaml
20) kubectl delete -f k8s/deployment.yaml


-- > 6) # to add to github

1) create a git repository without readme
2) touch .gitignore
3) # Python venv
.venv/
venv/

# Mac files
.DS_Store

# Python cache
__pycache__/
*.pyc

# Docker
*.log

# Kubernetes log outputs
*.txt
#this ensures unnecessary files don't get commited

4) git add .

5) git commit -m "Initial commit - AI Iris Deployment project"

6) git remote add origin https://github.com/vrindavnair-ai/AI_deployment.git

7) git branch -M main

8) git push -u origin main

9) # to see if anything updated after pushing
git status 

9) # I modified readme
git add README.md

10) # Commit it
git commit -m "Update README content"

11) git push

