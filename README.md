# Todo App

A cloud-native Todo application built with Docker and deployed to AWS ECR. This project demonstrates containerization, cloud deployment, and CI/CD automation.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Docker Build & Deployment](#docker-build--deployment)
- [CI/CD](#cicd)
- [Contributing](#contributing)


## Project Overview

This project is a Todo application consisting of **frontend** and **backend** services. Each service is containerized using Docker and pushed to AWS Elastic Container Registry (ECR). The app is intended for deployment in a cloud-native environment, following best practices for CI/CD and microservices architecture.

## Features

- Add, update, delete, and mark tasks as complete
- RESTful API backend
- Modern frontend UI
- Containerized for easy deployment
- Cloud-ready and CI/CD-friendly

## Tech Stack

- **Frontend:** React / Vue / Angular (based on your actual frontend)
- **Backend:** Node.js / Express
- **Database:** MongoDB / PostgreSQL (as per your backend)
- **Containerization:** Docker
- **Cloud Deployment:** AWS ECR
- **CI/CD:** GitHub Actions (or your pipeline)

## Setup

### Prerequisites

- Node.js >= 16
- Docker >= 20
- AWS CLI configured
- Git

### Clone the repository

```bash
git clone <your-repo-url>
cd todo-app

Install dependencies

Backend:

cd backend
npm install

Frontend:

cd ../frontend
npm install
```
### Docker Build & Deployment

```
Set environment variables

export AWS_REGION=<your-aws-region>
export AWS_ACCOUNT_ID=<your-aws-account-id>
export IMAGE_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/todo-app:latest

Build Docker images

docker build -t $IMAGE_URI ./backend
docker build -t $IMAGE_URI ./frontend

Push to AWS ECR

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
docker push $IMAGE_URI
```
### CI/CD
```
    GitHub Actions automates the Docker build and ECR push process.

    Workflow triggers on every push to main branch.

    Steps:

        Checkout code

        Set up Node.js environment

        Build Docker images

        Authenticate to AWS ECR

        Push Docker images to ECR
```
### Contributing
```
    Fork the repository

    Create a new branch: git checkout -b feature-name

    Make your changes

    Commit your changes: git commit -m "Add some feature"

    Push to the branch: git push origin feature-name

    Open a Pull Request
```