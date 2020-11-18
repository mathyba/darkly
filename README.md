# Darkly

A web security project for 42 school, as an introduction to the [OWASP project](https://owasp.org/www-project-top-ten/) and most common web vulnerabilities.

## Installation

### Set up the Darkly VM

This Virtual Machine image is provided by 42.

Create a linux virtual machine with the iso with the virtualization software of your choice, such as Oracle VM VirtualBox.

The VM will load and display an IP address that you will need to fill in the docker-compose.yml in order to use the scripts provided for some exploits.
Then you can head to your browser as the VM instructs.

### Set up the Darkly study project

Clone the project directory

```
git clone https://github.com/mathyba/darkly.git
```

Full set-up is provided with Docker and Docker-Compose
If you don't have these installed, check out the official [Docker](https://docs.docker.com/get-docker/) doc and follow the guidelines for your distribution.

## Usage

### Running the main "darkly" container

Following commands should be run at the root level of the project directory:

Build a docker image named "darkly":

```
docker build . -t darkly
```

Run darkly project container in interactive mode:

```
docker run -ti darkly
```

From there, you will have access to all the dependencies and scripts necessary to solve the challenge.

### Running the mitmproxy container

A proxy is useful throughout the project.

Launch the container:
```
docker run --rm -it -p 8080:8080 -p 127.0.0.1:8081:8081 -v (pwd)/Ressources/.mitmproxy:/home/mitmproxy/.mitmproxy mitmproxy/mitmproxy:latest mitmweb --web-host 0.0.0.0
```
In your browser network settings, add an HTTP proxy server on host 127.0.0.1 and port 8080.

Point your browser to `http://mitm.it` - if your proxy set-up is working, you should have access to various certificates.

Point to `http://0.0.0.0:8081` to access the mitmproxy GUI.

