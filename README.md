# Sample project to showcase Python gRPC <-> HTTP REST transcoding with grpc-gateway

This project implements a simple Python gRPC server for a bookstore. On top of that we have a proxy running which can transcode and expose all services defined in the `.proto` file as REST endpoints.

All REST endpoint details (path, parameters, descriptions etc.) are defined within the `.proto` file using common google API annotations.

# Project Structure
## proxy
This is a Go http proxy which can transcode HTTP/HTTPS REST into gRPC calls for you. It uses [grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) behind the scenes.

The Go server also serves a Swagger API Web UI where your endpoints are documented. Access it via `localhost:8081`.

You will need to have Go installed on your system via the official website.

### How to run the proxy:
`go run cmd/app/main.go`

Once running, you will be able to access your gRPC api with the proxy using simple HTT requests.
For example: `curl localhost:8081/api/v1/shelves`

## server
This is the actual `python` server implementation of the gRPC server.
First install all dependencies with: `pip3 install -r requirements.txt`

### How to run the server:
`python3 bookstore_server.py`

### How to run a simple python grpc client:
There is also a simple python grpc client in order to test your implementation. 
Run it with: `python3 bookstore_client.py` and you'll get a grpc response back.

## third_party
Contains a few third party proto files which are used as imports to define the API endpoint details. You can just copy these over, or alternatively checkout the `googleapis` repo in its entirety as a submodule. 
Copying these over like this just keeps it simple and small. We only need these few files.

## Proto files generation
The proto files are already generated and added to this repo for convenience. If you make changes to them you'll have to regenerate them.
Generating the proto files is done in the `Makefile`:
Just run: `make` from the root of the repo. (Keep in mind that you might need to install some dependencies like `protoc` and maybe some others).


