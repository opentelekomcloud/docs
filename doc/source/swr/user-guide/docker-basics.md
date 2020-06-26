# Docker Basics<a name="swr_01_0006"></a>

Docker is an open-source engine which allows you to create a lightweight, portable, and self-sufficient container for any application. SWR is compatible with Docker, allowing you to use Docker CLI and native APIs to manage your images.

## Installing Docker<a name="section941018533817"></a>

Before installing Docker, get a basic understanding of what Docker is and how it works. For more information, see  [Docker Documentation](https://docs.docker.com).

Docker is compatible with almost all operating systems. Select a Docker version that best suits your needs. If you are not sure which Docker community edition to use, see  [https://docs.docker.com/engine/installation/](https://docs.docker.com/engine/installation/).

>![](/images/icon-note.gif) **NOTE:**   
>-   Before using SWR to store Docker images, ensure that the Docker client used to push images to SWR is updated to 1.11.2 or later.  
>-   If the Docker client is in a private network, bind an elastic IP address \(EIP\) to the Docker client. This EIP will allow the Docker client to download Docker installation packages from the Docker website.  

If you are using a Linux operating system, run the following instructions to quickly install Docker.

```
curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## Building a Docker Image<a name="section135321459915"></a>

This section walks you through the steps of using a  Dockerfile  to build a  Docker image  for a simple web application. Dockerfile is a text file that contains all the instructions a user could call on the command line to build an image. A Docker image is a stack consisting of multiple layers. Each instruction creates a layer.

When using a browser to access a containerized application built from an  nginx image, you will see the default nginx welcome page. In this section, you build a new image based on the  nginx image  to change the welcome message to  **Hello, SWR!**

1.  Log in to the Docker client as the  **root**  user.
2.  Run the following commands to create an empty file named  **Dockerfile**:

    **mkdir mynginx**

    **cd mynginx**

    **touch Dockerfile**

3.  Edit Dockerfile.

    **vim Dockerfile**

    Instructions to be added to the Dockerfile:

    ```
    FROM nginx
    RUN echo '<h1>Hello,SWR!</h1>' > /usr/share/nginx/html/index.html
    ```

    In the preceding instructions:

    -   **FROM**: creates a layer from the base image. A valid Dockerfile must start with a  **FROM**  instruction. In this example, the  **nginx**  image is used as the base image.
    -   **RUN**: executes a command to create a new layer. One of its syntax forms is RUN <command\>. In this example, the  **echo**  command is executed to display  **Hello, SWR!**

    Save the changes and exit.

4.  Run  **docker build  _\[option\]_ _<context path\>_**  to build an image.

    **docker build -t nginx:v3 .**

    -   **-t nginx:v3**: specifies the image name and tag.
    -   **.**: indicates the path where the Dockerfile is located. All contents in this path are packed and sent to the Docker engine to build an image.

5.  Run the following command to list images. From the printout, you can find the newly created  **nginx**  image with a tag of  **v3**.

    **docker images**


## Creating an Image Package<a name="section3433103111126"></a>

This section describes how to compress a  Docker image  into a  .tar  or  .tar.gz  package.

1.  Log in to the Docker client as the  **root**  user.
2.  Run the following command to list images.

    **docker images**

    Check the name and tag of the image to be compressed.

3.  Run the following command to compress the image into a package.

    **docker save  _\[_**_OPTIONS_**_\]_  IMAGE  _\[_**_IMAGE..._**_\]_**

    >![](/images/icon-note.gif) **NOTE:**   
    >**OPTIONS**: can be set to  **--output**  or  **-o**, indicating that the image is exported to a file. \(Optional\)  
    >The file should be in either .tar or .tar.gz.  

    Sample:

    ```
    $ docker save nginx:latest > nginx.tar
    $ ls -sh nginx.tar
    108M nginx.tar
    
    $ docker save php:5-apache > php.tar.gz
    $ ls -sh php.tar.gz
    372M php.tar.gz
    
    $ docker save --output nginx.tar nginx
    $ ls -sh nginx.tar
    108M nginx.tar
    
    $ docker save -o nginx-all.tar nginx
    $ docker save -o nginx-latest.tar nginx:latest
    ```


