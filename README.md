# flask-demo (Azure Repos + Azure Pipelines)

This repo shows a minimal Flask app with unit tests and an Azure Pipelines YAML that:
1) runs pytest
2) builds a Docker image
3) pushes to Docker Hub

## Quick start (locally)

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
uvicorn app:app --host 0.0.0.0 --port 5000  # or: flask run --app app
```

## Docker (local)

```bash
docker build -t yourname/flask-demo:local .
docker run -p 5000:5000 yourname/flask-demo:local
curl http://localhost:5000/health
```

## Azure Pipelines (CI)

1. Create a new Azure DevOps project → Repos → **flask-demo** repository.
2. Upload this repo content (push via git).
3. In **Project Settings → Service connections → New → Docker Registry**, create a connection to Docker Hub (e.g., name: `dockerhub-sc`).
   - Registry type: Docker Hub
   - Authentication: Username/Password or Access Token
4. In the pipeline variables (optional) set `dockerHubRepo` to `DOCKER_HUB_USERNAME/flask-demo`.
5. Create a pipeline from existing YAML → `azure-pipelines.yml`.
6. Run the pipeline; it will:
   - install deps and run `pytest`
   - build and push the image to Docker Hub with tags `latest` and the commit SHA.

## Image

`docker pull DOCKER_HUB_USERNAME/flask-demo:latest`

