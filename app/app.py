from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Mock cluster state
pods = []
nodes = ["node-1", "node-2", "node-3"]
statuses = ["Running", "Pending", "Crashed (oops!)"]

@app.route("/")
def index():
    return render_template("index.html", pods=pods)

@app.route("/deploy", methods=["POST"])
def deploy_pod():
    pod_name = f"pod-{len(pods)+1}"
    pod = {
        "name": pod_name,
        "node": random.choice(nodes),
        "status": random.choice(statuses)
    }
    pods.append(pod)
    return redirect(url_for("index"))

@app.route("/delete/<pod_name>")
def delete_pod(pod_name):
    global pods
    pods = [p for p in pods if p["name"] != pod_name]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)