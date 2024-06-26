FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the filesystem read-only
RUN apt-get update && apt-get install -y --no-install-recommends libcap2-bin && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Add a non-root user
RUN useradd -m discordbot

# Change ownership of the app directory
RUN chown -R discordbot:discordbot /app

# Switch to the non-root user
USER discordbot

# Make port 80 available to the world outside this container
#EXPOSE 80

# Run bot.py when the container launches
CMD ["python", "bot.py"]