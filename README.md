# SECT Bachelor Project: Honeypot [Work in Progress]

SSH honeypot built with Cowrie with some extension modules:
- Portscan Detection
- Brute Force Detection
- DOS Detection
- Malware Detection [in progress]

## Infrastructure

This project is implemented with infrastructure as code using Packer, so most of the image creation process is automated. The images created are up to date and contain all the packages needed for this project.

## How it works

First, we use **Packer** to create a **__custom image__** for our **honeypot** and **attacker** machine. After the images are created, we run *these images* as **Docker containers**. After the container is runnning we need to set up our honeypot. After everything is set up, we can try to attack our honeypot-container with attacker-container.  

## Installation

## Prerequisite

* [Docker](https://docs.docker.com/get-docker/), [Git](https://github.com/git-guides/install-git), and [Packer](https://developer.hashicorp.com/packer/tutorials/docker-get-started/get-started-install-cli) must be installed before installing this project.

* Please make sure that the **Docker engine** is running.

### Installation's Steps

We need **3 terminals** ( on Windows preferably with **WSL**):

**1st Terminal:** Deployment
- Download or clone the whole repository using
	`git clone https://github.com/dam-du/SECT_Bachelorprojekt.git`
- Change directory to the root of our project
	`cd SECT_Bachelorprojekt/`
- Run `./build.sh` to build our infrastructure.
*Note: *this script creates custom images with packer and runs them in containers**
![Showcase of Honeypot's Deployment](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/clone_and_build.gif)

**2nd Terminal:** Starting cowrie on honeypot's container
- First we need to connect to our honeypot's container as cowrie user using:
`docker exec -it -u cowrie honeypot_container /bin/bash`
- Inside container run `./cowrie.sh`, this script will starts cowrie
- After cowrie is running, enter `exit` and

 **2nd Terminal:** Activating modules on honeypot's container 
- Now we need to connect to honeypot as root user using:
`docker exec -it honeypot_container bin/bash`
- Run `./activate_mods.sh`, it starts all extension modules for the honeypot.
- After activating the modules, the last 10 lines of the log file will be displayed on the terminal. Any malicious activity will be displayed on the logs.
![Showcase of Honeypot's Setup](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/setup_honeypot.gif)


**3rd Terminal:** Attack testcases
- First we need to connect to our attacker's container
`docker exec -it attacker_container /bin/bash`
- There are multiple attack cases, and they can be found inside `/testcase/`
- How to run and showcase about testcase can be found in [Testcase README.md](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/packer/upload/testcase/README.md)
![Showcase of Connecting to Attacker's Container](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/connect_to_attacker.gif)

## Cleanup

Run `./clean.sh` to stop, and remove all containers and images associated with the project.
