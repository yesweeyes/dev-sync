# Use Node.js with expo-cli
FROM node:18

# Install Expo CLI globally
RUN npm install -g expo-cli

# Set working directory
WORKDIR /code

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the project
COPY . .

# Expose Expo ports (19000: Metro, 19001: WebSocket, 19002: DevTools)
EXPOSE 19000 19001 19002

# Start Expo
CMD ["npx", "expo", "start", "--web"]
