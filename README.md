<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=azure,py,flask,ai,html,css,redis,vscode" />
  </a>
</p>

<h1 align="center">Building Containerized Applications with Azure Container Apps and OpenAI API</h1>


## Introduction

Today's focus is on Azure Container Apps and the OpenAI API, illustrating how to build containerized applications and APIs without the need for Docker. This guide is designed for developers looking to leverage the latest in container technology and AI integrations.

### The Evolution of Technology and Containers

The landscape of technology is rapidly evolving, introducing amazing features and applications almost daily. Containers have become the new standard for building and deploying applications due to their flexibility, control, security, and a variety of hosting options. Typically, Docker is used to create Dockerfiles, configure images, and manage the deployment of these containers to platforms like Kubernetes or Container Registries. However, Azure Container Apps now allows us to bypass Docker, enabling the building and pushing of containers directly to Azure Container Registry and subsequently to Azure Container Apps' managed environment. This simplifies the app deployment lifecycle significantly.

## Architecture of Our Workshop

Our workshop showcases an architecture involving:

- A **Python Flask Web App** as the frontend.
- A **Python-based container image** as the backend API endpoint.

The frontend allows users to select a city from a drop-down menu and receive information and photos of that city. The backend service fetches photographs stored in a Storage Account and uses the OpenAI Chat Completions API to retrieve general information about the selected city. This setup can be extended into a full-fledged tourist or travel web application, complete with security, scalability, redundancy, and flexibility.

## Building the Application

We'll use Azure CLI for a straightforward approach to building our resources:

1. **Create a Storage Account**: Begin by setting up a Storage Account and adding a container with photos of various cities (e.g., Athens.jpg, Berlin.jpg, Rome.jpg).
2. **Follow the Blog for Detailed Instructions**: For step-by-step guidance, visit [Azure Container Apps, APIs, Redis Cache, and Microservices with OpenAI Chat Completions](https://www.cloudblogger.eu/2023/12/30/azure-container-apps-apis-redis-cache-and-microservices-with-openai-chat-completions/).

This approach offers an integrated solution for enterprise-scale applications, ready for production with features like Azure Redis Cache for enhanced performance.

## Contribute

We encourage contributions! If you have ideas on how to improve this application or want to report a bug, please feel free to open an issue or submit a pull request.
