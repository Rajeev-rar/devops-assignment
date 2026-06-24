# DevOps Assignment - FastAPI Application Deployment

## Project Overview

This project demonstrates a complete DevOps workflow for deploying a FastAPI application using Docker, Docker Compose, Nginx, PostgreSQL, Redis, AWS EC2, and GitHub Actions CI/CD.

The objective of this project is to build a production-ready deployment pipeline that automates application deployment from GitHub to AWS EC2 whenever changes are pushed to the main branch.

---

# Live Application

**Application URL**

http://18.208.214.244

**Health Check Endpoint**

http://18.208.214.244/health

---

# GitHub Repository

Repository URL:

https://github.com/Rajeev-rar/devops-assignment

---
# System Architecture

### User Layer

- Users access the application through a web browser.
- Requests are sent to the AWS EC2 Public IP.

### Reverse Proxy Layer

- Nginx receives incoming requests.
- Nginx forwards requests to the FastAPI container.

### Application Layer

- FastAPI handles API requests.
- Provides application endpoints.
- Health monitoring endpoint available.

### Data Layer

- PostgreSQL container for persistent storage.
- Redis container for caching and session storage.

### Infrastructure Layer

- AWS EC2 hosts all containers.
- Docker Compose manages multi-container deployment.

### CI/CD Layer

- GitHub Actions automatically deploys changes to EC2.
- Deployment starts whenever code is pushed to the main branch.

---

# Tech Stack

## Backend

- FastAPI
- Python 3

## Containerization

- Docker
- Docker Compose

## Web Server

- Nginx

## Database

- PostgreSQL 15

## Cache

- Redis 7

## Cloud Platform

- AWS EC2

## Version Control

- Git
- GitHub

## CI/CD

- GitHub Actions

---

# Project Structure

```text
devops-assignment/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── default.conf
│
├── docker-compose.yml
├── .env
├── README.md
│
└── docs/
```

---

# Docker Setup

## Build Containers

```bash
docker compose build
```

## Start Containers

```bash
docker compose up -d
```

## Stop Containers

```bash
docker compose down
```

## Check Running Containers

```bash
docker ps
```

---

# Docker Services

## FastAPI Application

Runs on:

```text
Port 8000
```

---

## PostgreSQL

Database container.

```text
Port 5432
```

Uses Docker volume for persistence.

---

## Redis

Caching container.

```text
Port 6379
```

Uses Docker volume for persistence.

---

## Nginx

Reverse proxy service.

```text
Port 80
```

Routes requests to FastAPI.

---

# Deployment Steps

## Step 1

Launch AWS EC2 Ubuntu Instance.

---

## Step 2

Configure Security Group.

Allow:

```text
22  SSH
80  HTTP
8000 Application
```

---

## Step 3

Install Git.

```bash
sudo apt update
sudo apt install git -y
```

---

## Step 4

Install Docker.

```bash
sudo apt install docker.io -y
```

---

## Step 5

Install Docker Compose.

```bash
sudo apt install docker-compose-v2 -y
```

---

## Step 6

Clone Repository.

```bash
git clone https://github.com/Rajeev-rar/devops-assignment.git
```

---

## Step 7

Move to Project Directory.

```bash
cd devops-assignment
```

---

## Step 8

Start Containers.

```bash
sudo docker compose up -d --build
```

---

## Step 9

Verify Deployment.

```bash
sudo docker ps
```

---

# GitHub Actions CI/CD Workflow

## Objective

Automatically deploy application to AWS EC2 whenever code is pushed to the main branch.

---

## Workflow Trigger

```yaml
on:
  push:
    branches:
      - main
```

---

## GitHub Secrets Used

### EC2_HOST

AWS EC2 Public IP

### EC2_USERNAME

```text
ubuntu
```

### EC2_SSH_KEY

Private SSH key used for deployment.

---

## Deployment Process

### Developer Pushes Code

```bash
git add .
git commit -m "update"
git push origin main
```

↓

### GitHub Actions Starts

↓

### Connects to EC2 Using SSH

↓

### Pulls Latest Code

```bash
git pull origin main
```

↓

### Rebuilds Containers

```bash
sudo docker compose down
sudo docker compose up -d --build
```

↓

### Deployment Complete

---

# CI/CD Workflow File

Location:

```text
.github/workflows/deploy.yml
```

Purpose:

- Build application
- Connect to EC2
- Deploy latest code
- Restart containers

---

# Health Check Endpoint

Endpoint:

```text
/health
```

URL:

```text
http://18.208.214.244/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

# Security Measures

The following security measures have been implemented:

### AWS Security Groups

Only required ports are exposed.

### SSH Key Authentication

Password login is avoided.

### GitHub Secrets

Sensitive credentials stored securely.

### Environment Variables

Secrets separated from application code.

---

# Monitoring Strategy

Current Monitoring Approach:

### Docker Logs

```bash
sudo docker logs container_name
```

### Health Endpoint

```text
/health
```

Used for application availability checks.

### GitHub Actions

Deployment status monitored through workflow runs.

Benefits:

- Lightweight monitoring
- Quick troubleshooting
- Easy deployment tracking

---

# Backup Strategy

Current Backup Approach:

### PostgreSQL Docker Volume Backup

Database data is stored inside persistent Docker volumes.

Example:

```bash
docker volume ls
```

Volume data remains available even if containers are recreated.

### Source Code Backup

GitHub repository serves as source code backup.

Benefits:

- Persistent database storage
- Recovery from container failures
- Version-controlled source code

---

# Validation Checklist

## Application

- [x] FastAPI Running

## Containerization

- [x] Docker Implemented
- [x] Docker Compose Implemented

## Reverse Proxy

- [x] Nginx Configured

## Database

- [x] PostgreSQL Running

## Cache

- [x] Redis Running

## Cloud

- [x] AWS EC2 Deployment Completed

## CI/CD

- [x] GitHub Actions Configured
- [x] Auto Deploy to EC2 Configured

---

# Troubleshooting

## Docker Permission Error

Solution:

```bash
sudo usermod -aG docker ubuntu
```

---

## Check Running Containers

```bash
sudo docker ps
```

---

## Check Application Logs

```bash
sudo docker logs devops-assignment-app-1
```

---

## Restart Services

```bash
sudo docker compose down
sudo docker compose up -d --build
```

---

# Learning Outcomes

Through this project, the following skills were gained:

- Linux Administration
- Docker Containerization
- Docker Compose
- Nginx Reverse Proxy
- AWS EC2 Deployment
- Git and GitHub
- GitHub Actions CI/CD
- PostgreSQL Administration
- Redis Basics
- Infrastructure Automation

---

# Future Improvements

- Domain Name Configuration
- HTTPS using SSL Certificates
- Prometheus Monitoring
- Grafana Dashboards
- Automated Database Backups
- Kubernetes Deployment
- Terraform Infrastructure Provisioning

---

# Author

**Rajeev**

DevOps & Cloud Enthusiast

GitHub:
https://github.com/Rajeev-rar