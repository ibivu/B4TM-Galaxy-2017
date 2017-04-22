# Use Docker for Galaxy Assignment

In this document, we will show you how to use the Galaxy docker image on your own computer as the preparation for
the forthcoming Galaxy assignment of B4TM.

This assignment is a group assignment with a maximum of 2 persons in the group. This assignment lasts two weeks
and in the second week, a local docker container is needed to finish the assignment.

Some of you might be confronted with difficulty in using docker image due to the factors like operating systems
and stuff. If so, please let us know. If it is unsolvable, please consider choosing a collaborator who has no such problem to make a group.

## Install the latest version of Docker engine

Docker is evolving quickly, to guarantee the best performance and least errors, we need to use the **latest**
stable version of docker.

### Installation

* [Docker for Mac (Older version might be glitchy)](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)
* [Docker for Windows (Windows 10 Professional or Windows 10 Education)](https://docs.docker.com/docker-for-windows/install/)
* [Docker for Ubuntu](https://docs.docker.com/engine/installation/linux/ubuntu/)
* [Docker for other flavors of Linux](https://docs.docker.com/engine/installation/)

### Windows 10 Education

 If you have a VUnet ID, you can log in to [SURFspot](https://www.surfspot.nl/) to get a free serial key of Windows
 10 Education version, with which you can replace your old serial key in your Windows 10 Home to upgrade it to education version.

## Basics of using Docker

 If you were previously enrolled in the master course ‘Structural Bioinformatics’, you may have been familiar with
 Docker already, in this case, you may skip this section for the next. If you are new to Docker or want to
 review the usage of Docker quickly, you can read this document [here](https://docs.google.com/document/d/1QoL_93B-0VRcJdrxjweUV8JQI0Waehz1rMdiCFeWPeo/edit?usp=sharing).

## Deploy Galaxy Docker Image

### Log in to the docker registry for B4TM

#### What is a docker registry?
Docker registry is probably synonymous with ‘docker repository’ or ‘docker hub’, a place to store and organize
docker images. In most cases, we just pull a docker image from a public registry without being aware of the
docker registry.

#### Why do we use a separate registry?
In Galaxy assignment, a software package called CPLEX is used, which is proprietary, therefore,
it limits the distribution of the software and we have to put it into a private docker registry.

#### How to log in?

Credentials for the private registry:

Item         | Content
:----------: | :----------------------------------:
Registry URL | docker.bioinformatician.science:5678
Username     | b4tm2017
Password     | bioinformatics

Type this command into your terminal `$ docker login docker.bioinformatician.science:5678`, you will be prompted
to type the username and password.

### Create and run a Galaxy instance from the image

`$ docker run -d -p 8888:80 --name b4tm2017 -v /your_directory/:/export/ docker.bioinformatician.science:5678/b4tm/local:0.1`

In this command, we run this docker container in a detached mode (`-d`), mapping the container port 80 to the port 8888 of localhost (`-p`), naming this instance as 'b4tm2017' (`--name`) and mapping a container directory `/export/` to a local directory (`-v`). `/export/` is a special directory in the Galaxy container where all the configured files and tool files are kept. In this assignment, all the modifications and changes take place only in this folder.

Before running this command, please designate a path on your computer to replace `your_directory` in the command.
For linux users, you might use `sudo` if your linux user account is not in the Docker group.

### Test the instance

#### Test it in the Internet browser

Please visit the URL http://127.0.0.1:8888 to test whether Galaxy is accessible on your computer now
(it might take a few minutes after executing the docker command above).

#### Test it in Docker

To log in to the Galaxy instance as a root user, please use the command line `$ docker exec -it b4tm2017 /bin/bash`

Please try the following command inside Galaxy instance to reboot Galaxy without rebooting the container (don’t forget the colon at the end).

```
$ supervisorctl restart galaxy:
```

Or try the following command outside the Galaxy instance to reboot Galaxy without rebooting the container (don’t forget the colon at the end).

```
$ docker exec b4tm2017 supervisorctl restart galaxy:
```

**Please do all the tests. If your group is confronted with difficulties, please let us know.**

### Common Docker commands

#### Show the running containers
```
$ docker ps
```
#### Restart, stop and start the Galaxy container
```
$ docker restart b4tm2017

$ docker stop b4tm2017

$ docker start b4tm2017
```
`b4tm2017` can be replaced your own defined names or container ID, which can be retrieved by `$ docker ps --all`

### How to modify files in `/export/`

There are two ways:

1. The easiest way is to modify files in your own way in the local directory that is mapped to `/export/` in the container.
2. Modify the files in the container directly. You need to log in to the Galaxy container as a root user by `$ docker exec -it b4tm2017 /bin/bash`, and then install an editor in the container, for example, if you want to use 'Emacs', you can `$ apt-get update && apt-get install emacs`.
