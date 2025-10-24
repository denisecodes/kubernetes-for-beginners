## 🐳 Build and Run the Docker Image Locally

Follow these two simple steps to build and run the `kubeguess` image using your Dockerfile located at `/app/Dockerfile`.

---

### 🧱 Step 1 — Build the Docker image

Use the `-f` flag to specify the Dockerfile location and tag the image as `kubeguess:local`:

```bash
docker build -f /app/Dockerfile -t kubeguess:local .
```

Verify the image was created:

```bash
docker image ls
```

---

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

Example output:

CONTAINER ID   IMAGE              PORTS                    NAMES  
abcd1234       kubeguess:local    0.0.0.0:5000->5000/tcp   kubeguess

---

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
```

---