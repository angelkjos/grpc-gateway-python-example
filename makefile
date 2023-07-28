# Directory containing your .proto files
PROTO_DIR := .
PROTO_DIR_THIRD_PARTY := ./third_party

# Directory to output your Python files to
OUTPUT_DIR_PY := ./server
OUTPUT_DIR_GO := ./proxy/api/proto
OUTPUT_DIR_OPENAPI := ./proxy/third_party/OpenAPI/bookstore/v1

# Default target for the make command
all: generate-python generate-grpc-gateway

# Command to generate Python files from all Proto files
generate-python:
	@python3 -m grpc_tools.protoc \
		--python_out=$(OUTPUT_DIR_PY) \
		--pyi_out=$(OUTPUT_DIR_PY) \
		--grpc_python_out=$(OUTPUT_DIR_PY) \
		--proto_path=$(PROTO_DIR) \
		--proto_path=$(PROTO_DIR_THIRD_PARTY) \
		$(PROTO_DIR)/*.proto

generate-grpc-gateway:
	@protoc \
   		--go_out=$(OUTPUT_DIR_GO) --go_opt paths=source_relative \
   		--go-grpc_out=$(OUTPUT_DIR_GO) --go-grpc_opt paths=source_relative \
		--grpc-gateway_out=$(OUTPUT_DIR_GO) --grpc-gateway_opt paths=source_relative \
		--openapiv2_out=logtostderr=true:$(OUTPUT_DIR_OPENAPI) \
		--proto_path=$(PROTO_DIR) \
		--proto_path=$(PROTO_DIR_THIRD_PARTY) \
   		$(PROTO_DIR)/*.proto
