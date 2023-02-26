# SECT Bachelor Project: Honeypot [Work in Progress]

SSH honeypot built with Cowrie with some extension modules:
- Portscan Detection
- Brute Force Detection
- DOS Detection
- Malware Detection [WIP]

## Infrastructure

This project is implemented with infrastructure as code using packer, so most of the image's creation is automated. The images created are up to date and contain all the packages needed for this project. After the images are created, it will be then used by packer to be run as containers. The system in this project contain of a honeypot container, attacker container, and a simple nginx container.

## How it works

First, we use **Packer** to create a **__custom image__** for our **honeypot** and **attacker** machine. After the images are created, we run *these images* as **Docker containers**. After the container is runnning we need to set up our honeypot. After everything is set up, we can try to attack our honeypot-container with attacker-container.  

## Installation

### Prerequisite

* [Docker](https://docs.docker.com/get-docker/), [Git](https://github.com/git-guides/install-git), and [Packer](https://developer.hashicorp.com/packer/tutorials/docker-get-started/get-started-install-cli) must be installed before installing this project.

* Please make sure that the **Docker engine** is running.

### Installation's Steps

We need **3 terminals** ( on Windows preferably with **WSL**):

**1st Terminal:** Deployment
- Download or clone the whole repository using
	`git clone https://github.com/dam-du/SECT_Bachelorprojekt.git`
- Change directory to the root of our project
	`cd SECT_Bachelorprojekt/`
- Run `./build.sh` to build our infrastructure with packer and create the containers.
![Showcase of Honeypot's Deployment](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/clone_and_build.gif)

**2nd Terminal:** Starting cowrie on honeypot's container
- First we need to connect to our honeypot's container as cowrie user using:
`docker exec -it -u cowrie honeypot_container /bin/bash`
- Inside container run `./cowrie.sh`, this script will starts cowrie
- After cowrie is running, enter `exit` and

 **2nd Terminal:** Activating modules on honeypot's container 
- Now we need to connect to honeypot as root user using:
`docker exec -it honeypot_container bin/bash`
- Now before we activate our modules, there are 2 different versions prepared: the normal and extended one. 
	- Run `./activate_mods.sh`, it starts all extension modules for the honeypot (normal).
	- Or run `./xactivate_mods.sh`, it starts all extension modules and push all network traffics to the log.
- After activating the modules, the last 10 lines of the log file will be displayed on the terminal. Any malicious activity will be displayed on the logs.

![Showcase of Honeypot's Setup](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/setup_honeypot.gif)

- Here is the showcase for the extended one.
![Showcase of Extended Honeypot's Setup](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/showcase_extended_distributed_anomaly_detector.gif)

**3rd Terminal:** Attack testcases
- First we need to connect to our attacker's container
`docker exec -it attacker_container /bin/bash`
- There are multiple attack cases, and they can be found inside `/testcase/`
- How to run and showcase about testcase can be found in [Testcase README.md](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/packer/upload/testcase/README.md)

![Showcase of Connecting to Attacker's Container](https://github.com/dam-du/SECT_Bachelorprojekt/blob/main/graphics/connect_to_attacker.gif)

## Cleanup

Run `./clean.sh` to stop, and remove all containers and images associated with the project.
