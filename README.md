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

### Healthcheck
**Endpoint**
