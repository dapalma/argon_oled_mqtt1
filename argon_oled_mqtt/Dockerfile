# syntax=docker/dockerfile:1

# 🧱 Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --omit=dev

# Copy source code
COPY . .

# 🧪 Optional: Run tests
# RUN npm test

# 🧼 Clean up unnecessary files
RUN rm -rf tests docs

# 🧊 Stage 2: Production
FROM node:20-alpine
WORKDIR /app

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Copy only necessary files from builder
COPY --from=builder /app .

# Expose port and define startup
EXPOSE 3000
CMD ["node", "index.js"]
