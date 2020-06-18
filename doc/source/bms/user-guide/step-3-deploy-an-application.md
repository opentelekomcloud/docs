# Step 3: Deploy an Application<a name="EN-US_TOPIC_0083745261"></a>

This section describes how to deploy an application on a BMS.

## Install and Start Nginx<a name="section1766432205115"></a>

1.  Run the  **yum install nginx**  command to install Nginx and enter  **y**  as prompted.

    If the information shown in the following figure is displayed, Nginx is installed successfully.

    ![](figures/2-5.png)

2.  Enter  **systemctl start nginx.service**  to start Nginx.

    >![](/images/icon-note.gif) **NOTE:**   
    >This command applies to CentOS 7.4 64-bit, which is used as an example.  

3.  Enter  **wget http://127.0.0.1**  to test Nginx.

    ![](figures/2-5-2.png)


## Access the Default Web Page<a name="section363712231510"></a>

Open a browser and enter http://_BMS EIP_  in the address box. If the Nginx welcome page is displayed, Nginx is installed successfully.

