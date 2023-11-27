import grpc
import concurrent import futures

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:50051")
    server.start()

if __name__ == "__main__":
    serve()