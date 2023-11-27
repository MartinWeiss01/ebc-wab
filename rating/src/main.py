import grpc
import concurrent import futures
import .rating_pb2_grpc as rating_pb2_grpc

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rating_pb2_grpc.add_RatingServicer_to_server(rating_pb2_grpc.RatingServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

if __name__ == "__main__":
    serve()