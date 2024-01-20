# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Manually install 'express'
RUN npm install express

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 3000 to the outside world
EXPOSE 3000

# Define the command to run your app
CMD ["node", "./app.js"]

