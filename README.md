# Rick & Morty DevOps Exercise

## Overview
This project is a DevOps home exercise that demonstrates an end-to-end flow:
from data collection using a public API, through containerization, and exposing
the data via a REST API service.

The service fetches characters from the Rick & Morty public API, filters them
according to specific criteria, and exposes the results as JSON over HTTP.

---

## Data Source
Rick & Morty API  
https://rickandmortyapi.com/documentation/#rest

---

## Filtering Logic
Characters are filtered by:
- `species = Human`
- `status = Alive`
- `origin contains "Earth"`

The origin condition is implemented as a substring match because the API uses
values such as `Earth (C-137)`, `Earth (Replacement Dimension)`, etc.

---

## REST API
Note:
When deployed on Kubernetes, the REST API is exposed via an Ingress resource.
Requests are routed based on the hostname defined in the Ingress configuration
(e.g. `rick-morty.local`), which allows clean HTTP access without exposing
NodePorts or direct Pod IPs.


### Healthcheck
**Endpoint**


## Kubernetes Deployment

The application can be deployed to a local Kubernetes cluster
(e.g. minikube or microk8s) using standard Kubernetes manifests.

### Manifests
All Kubernetes manifests are located under the `yamls/` directory:
- `deployment.yaml` – Application deployment
- `service.yaml` – Internal service exposure
- `ingress.yaml` – HTTP routing via Ingress

### Apply Manifests
```bash
kubectl apply -f yamls/
