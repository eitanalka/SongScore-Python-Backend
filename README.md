# SongScore-Python-Backend

## Prerequisites
Install Docker:
  - Mac: https://docs.docker.com/docker-for-mac/install/
  - Windows: https://docs.docker.com/docker-for-windows/install/

## Getting Started
1. Clone this repo
2. Download classify lyrics model from drive and put it in the server folder
3. run `docker-compose up`
4. Make a post request to `localhost:5000/classify-lyrics` with a json object that includes a `lyrics` field