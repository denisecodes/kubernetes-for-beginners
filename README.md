## ☸️ Setting up a Kubernetes Cluster Locally

Before deploying the **KubeGuess** app, you need a local Kubernetes cluster running.  
There are several easy-to-use options available depending on your setup and preference.

### 🧩 Option 1 — Minikube

Minikube is a lightweight Kubernetes implementation that runs locally on your computer.  
It’s great for learning, testing, and running local clusters on macOS, Windows, or Linux.

**Official documentation:**  
👉 [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)

**Basic commands:**

```bash
# Start a new local cluster
minikube start

# Verify it’s running
kubectl get nodes

# Access the dashboard (optional)
minikube dashboard
```

### 🐳 Option 2 — Docker Desktop (with Kubernetes enabled)

Docker Desktop includes an integrated single-node Kubernetes cluster.
It’s ideal if you already use Docker Desktop and want an all-in-one local setup.

Official documentation:
👉 https://docs.docker.com/desktop/kubernetes/

How to enable Kubernetes:
1. Open **Docker Desktop**.  
2. Go to **Settings → Kubernetes**.  
3. Check **“Enable Kubernetes”**.  
4. Wait for it to start — once active, verify with:



```bash
kubectl get nodes
```

### ⚙️ After Setting Up

Once your cluster is up:
	•	Make sure kubectl is configured to point to your local cluster.
	•	You can confirm this by running:

```bash
kubectl config current-context
```

If it shows something like minikube or docker-desktop, you’re good to go!


# 🚀 Setting Up Argo CD Locally to Deploy GitHub Infrastructure Files

You can get **Argo CD** running locally to deploy your **GitHub-hosted infrastructure files** on a local Kubernetes cluster (like **Kind** or **Minikube**) by following these steps.  


## 1️⃣ Prerequisites

- 🧩 Local Kubernetes cluster running (**Kind**, **Minikube**, or **Docker Desktop Kubernetes**)
- ⚙️ `kubectl` installed and configured to point to your cluster: https://kubernetes.io/docs/tasks/tools/
- 🌐 Your **GitHub repository** URL with your infrastructure manifests ready


## 2️⃣ Install Argo CD on Your Cluster

Create a namespace for Argo CD and install the official manifests:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

✅ This installs Argo CD in the argocd namespace.


## 3️⃣ Expose the Argo CD API Server Locally

For local testing, use port-forwarding:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Now open your browser at:

https://localhost:8080

⚠️ You may need to accept a browser warning because Argo CD uses a self-signed certificate.


## 4️⃣ Get the Argo CD Admin Password

By default, the username is admin.
You can get the initial password with either of the following commands:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```


## 5️⃣ Log In to Argo CD

Option 1 — Web UI
1.	Open https://localhost:8080
2.	Username: admin
3.	Password: (from step 4)


6️⃣ Connect Your GitHub Repository

You can connect your repository in two ways:

## Using the Argo CD UI
1.	Go to Settings → Repositories → Connect Repo.
2.	Enter your GitHub repository URL.
3.	If your repo is private, provide a personal access token with repo and read:packages permissions.


## 7️⃣ Create an Argo CD Application

First create the namespace to host the application or you can try getting Argocd to create it for you through their UI in the next step:
```bash
kubectl create namespace kubeguess
```

An Application in Argo CD tells it:
- Which Git repository to track
- Which folder (path) contains the manifests
- hich cluster and namespace to deploy to

## Using the Argo CD UI
1. For Project select default
2. For Cluster select in-cluster
3. For namespace, use kubeguess
4. For repo url, select https://github.com/denisecodes/kubernetes-for-beginners or if you have cloned the repo https://github.com/<your-github-username>/kubernetes-for-beginners
5. For Path select ./infra
6. For Sync options check the following:
- Auto-Create Namespace
- Retry
7. For Sync Policy, check enable auto-sync


### 8️⃣ Verify the Deployment

Check that your Kubernetes resources were created successfully:

kubectl get all -n kubeguess

You should see your Pods, Services, and Deployments running according to your GitHub manifests.

## 🐳 Build and Run the Docker Image Locally

Follow these two simple steps to build and run the `kubeguess` image using your Dockerfile located at `/app/Dockerfile`.


### 🧱 Step 1 — Build the Docker image

Use the `-f` flag to specify the Dockerfile location and tag the image as `kubeguess:local`:

```bash
docker build -f /app/Dockerfile -t kubeguess:local .
```

Verify the image was created:

```bash
docker image ls
```

### 🚀 Step 2 — Run the Container Locally

Run the container in detached mode and map container port 5000 to host port 5000:

```bash
docker run -p 5000:5000 --name kubeguess -d kubeguess:local
```

Access the app in your browser at:

http://localhost:5000

Check the running container:

```bash
docker ps
```

### 🧹  Step 3 — Stop and Clean Up the Container

Stop the running container:

```bash
docker stop kubeguess
```

Remove the container:

```bash
docker rm kubeguess
```

Optional remove the image if you want to rebuild from scratch:

```bash
docker image rm kubeguess:local