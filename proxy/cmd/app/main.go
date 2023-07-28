package main

import (
	"context"
	"fmt"
	"io/fs"
	"io/ioutil"
	"mime"
	"net/http"
	"os"
	"strings"

	pb "github.com/endpoints/examples/bookstore/api/proto"
	"github.com/endpoints/examples/bookstore/third_party"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"
	"google.golang.org/grpc/grpclog"
)

// getOpenAPIHandler serves an OpenAPI UI.
// Adapted from https://github.com/philips/grpc-gateway-example/blob/a269bcb5931ca92be0ceae6130ac27ae89582ecc/cmd/serve.go#L63
func getOpenAPIHandler() http.Handler {
	mime.AddExtensionType(".svg", "image/svg+xml")
	// Use subdirectory in embedded files
	subFS, err := fs.Sub(third_party.OpenAPI, "OpenAPI")
	if err != nil {
		panic("couldn't create sub filesystem: " + err.Error())
	}
	return http.FileServer(http.FS(subFS))
}

func main() {
	// Adds gRPC internal logs. This is quite verbose, so adjust as desired!
	log := grpclog.NewLoggerV2(os.Stdout, ioutil.Discard, ioutil.Discard)
	grpclog.SetLoggerV2(log)

	// creating mux for gRPC gateway. This will multiplex or route request different gRPC service
	mux := runtime.NewServeMux()
	// setting up a dail up for gRPC service by specifying endpoint/target url
	err := pb.RegisterBookstoreHandlerFromEndpoint(context.Background(), mux, "localhost:8000", []grpc.DialOption{grpc.WithInsecure()})
	if err != nil {
		log.Fatal(err)
	}

	oa := getOpenAPIHandler()

	// Creating a normal HTTP server
	gatewayAddr := "localhost:8081"
	server := &http.Server{
		Addr: gatewayAddr,
		Handler: http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			if strings.HasPrefix(r.URL.Path, "/api") {
				mux.ServeHTTP(w, r)
				return
			}
			oa.ServeHTTP(w, r)
		}),
	}

	log.Info("Serving gRPC-Gateway and OpenAPI Documentation on http://", gatewayAddr)
	log.Fatalln(fmt.Errorf("serving gRPC-Gateway server: %w", server.ListenAndServe()))
}
