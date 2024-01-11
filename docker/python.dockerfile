FROM python:3.11

WORKDIR /exercises

# Copy the requirements file into the container at /exercises
COPY docker/requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Keep the container running
CMD ["tail", "-f", "/dev/null"]