# Use the official Redis image as a base
FROM redis:latest

# Set the working directory to /data
WORKDIR /data

# Expose the Redis port
EXPOSE 6379

# Set the default command to run when the container starts
CMD ["redis-server"]