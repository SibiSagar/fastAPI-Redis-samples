To build the Docker image, save this file as `Dockerfile` in the root of your project directory, then run the following command:

```shell
docker build -t my-redis-image .
```

To run the container, use the following command:

```shell
docker run -d --name my-redis-container -p 6379:6379 my-redis-image
```
