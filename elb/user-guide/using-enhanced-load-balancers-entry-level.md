# Using Enhanced Load Balancers — Entry Level<a name="EN-US_TOPIC_0167652100"></a>

## Scenarios<a name="section18950295143553"></a>

You have a web application that is deployed on two ECSs, and the application often needs to handle heavy workload.

You can create a load balancer to distribute traffic evenly across the two ECSs, which not only makes your application more available, but eliminates SPOFs.

## Prerequisites<a name="section3453061616119"></a>

-   You have to create two ECSs with each having an EIP bound.
-   The ports used by the two ECSs have been configured in the security group. \(You can enable all ports first and then disable the ports that are not used after service deployment.\) 
-   To ensure normal health checks, the security group for the two ECSs allows traffic from 100.125.0.0/16.

## Create ECSs<a name="section1973682033616"></a>

In this topic, ECSs are used as backend servers. Perform the following operations to create two ECSs:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Computing**, click  **Elastic Cloud Server**.
4.  Click  **Create ECS**. On the displayed page, set the parameters and click  **Create Now**.
5.  The following table lists the specifications of the two ECSs.

**Table  1**  ECS specifications

<a name="table9439114212376"></a>
<table><thead align="left"><tr id="row144381942113712"><th class="cellrowborder" valign="top" width="46.949999999999996%" id="mcps1.2.3.1.1"><p id="p2437164211370"><a name="p2437164211370"></a><a name="p2437164211370"></a><strong id="b28748415542"><a name="b28748415542"></a><a name="b28748415542"></a>Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.05%" id="mcps1.2.3.1.2"><p id="p1437144223718"><a name="p1437144223718"></a><a name="p1437144223718"></a><strong id="b577911814548"><a name="b577911814548"></a><a name="b577911814548"></a>Example Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19438184219379"><td class="cellrowborder" valign="top" width="46.949999999999996%" headers="mcps1.2.3.1.1 "><p id="p143814421375"><a name="p143814421375"></a><a name="p143814421375"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="53.05%" headers="mcps1.2.3.1.2 "><p id="p443818423371"><a name="p443818423371"></a><a name="p443818423371"></a>ECS01 and ECS02</p>
</td>
</tr>
<tr id="row4438164219374"><td class="cellrowborder" valign="top" width="46.949999999999996%" headers="mcps1.2.3.1.1 "><p id="p143834210373"><a name="p143834210373"></a><a name="p143834210373"></a>OS</p>
</td>
<td class="cellrowborder" valign="top" width="53.05%" headers="mcps1.2.3.1.2 "><p id="p7438154214376"><a name="p7438154214376"></a><a name="p7438154214376"></a>CentOS 7.2 64bit</p>
</td>
</tr>
<tr id="row124388426378"><td class="cellrowborder" valign="top" width="46.949999999999996%" headers="mcps1.2.3.1.1 "><p id="p34381142143710"><a name="p34381142143710"></a><a name="p34381142143710"></a>CPU</p>
</td>
<td class="cellrowborder" valign="top" width="53.05%" headers="mcps1.2.3.1.2 "><p id="p743854273713"><a name="p743854273713"></a><a name="p743854273713"></a>2 vCPUs</p>
</td>
</tr>
<tr id="row54398427375"><td class="cellrowborder" valign="top" width="46.949999999999996%" headers="mcps1.2.3.1.1 "><p id="p84381942143717"><a name="p84381942143717"></a><a name="p84381942143717"></a>Memory</p>
</td>
<td class="cellrowborder" valign="top" width="53.05%" headers="mcps1.2.3.1.2 "><p id="p74385422371"><a name="p74385422371"></a><a name="p74385422371"></a>4 GB</p>
</td>
</tr>
<tr id="row104391342163719"><td class="cellrowborder" valign="top" width="46.949999999999996%" headers="mcps1.2.3.1.1 "><p id="p134396423373"><a name="p134396423373"></a><a name="p134396423373"></a>System disk</p>
</td>
<td class="cellrowborder" valign="top" width="53.05%" headers="mcps1.2.3.1.2 "><p id="p44391842123715"><a name="p44391842123715"></a><a name="p44391842123715"></a>40 GB</p>
</td>
</tr>
<tr id="row64392042193716"><td class="cellrowborder" valign="top" width="46.949999999999996%" headers="mcps1.2.3.1.1 "><p id="p1843964233713"><a name="p1843964233713"></a><a name="p1843964233713"></a>Data disk</p>
</td>
<td class="cellrowborder" valign="top" width="53.05%" headers="mcps1.2.3.1.2 "><p id="p1443984283717"><a name="p1443984283717"></a><a name="p1443984283717"></a>100 GB</p>
</td>
</tr>
<tr id="row74391842173712"><td class="cellrowborder" valign="top" width="46.949999999999996%" headers="mcps1.2.3.1.1 "><p id="p13439144213370"><a name="p13439144213370"></a><a name="p13439144213370"></a>Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="53.05%" headers="mcps1.2.3.1.2 "><p id="p19439174293718"><a name="p19439174293718"></a><a name="p19439174293718"></a>5 Mbit/s</p>
</td>
</tr>
</tbody>
</table>

6.  Click  **Submit**.

## Deploy the Backend Service<a name="section12375217165718"></a>

Deploy Nginx on the two ECSs and edit two HTML pages for the web applications so that a page with message "Welcome to ELB test page one!" is returned when ECS01 is accessed, and the other page with message "Welcome to ELB test page two!" is returned when ECS02 is accessed.

1.  Log in to the ECSs.
2.  Install Nginx.
    1.  Run the following command to install Nginx:

        **yum -y install nginx**

    2.  Run the following command to start Nginx:

        **systemctl start nginx.service**

    3.  Enter  **http://**_ECS IP address_  in the browser address bar.

        If the following page is displayed, Nginx has been installed.

        **Figure  1**  Nginx installed successfully<a name="fig321841941611"></a>  
        ![](figures/nginx-installed-successfully.jpg "nginx-installed-successfully")

3.  Modify the HTML page of ECS01.

    The default root directory of Nginx is  **/usr/share/nginx/html**. Modify the  **index.html**  file to identify access to ECS01.

    1.  Run the following command to open the  **index.html**  file:

        **vim /usr/share/nginx/html**/**index.html**

    2.  Press  **i**  to enter editing mode.
    3.  Modify the  **index.html**  file.

        The following displays the content to be modified:

        ```
         ...
            <body>
                <h1>Welcome to <strong>ELB</strong> test page one!</h1>
        
                <div class="content">
                    <p>This page is used to test the <strong>ELB</strong>!</p>
        
                    <div class="alert">
                        <h2>ELB01</h2>
                        <div class="content">
                            <p><strong>ELB test (page one)!</strong></p>
                            <p><strong>ELB test (page one)!</strong></p>
                            <p><strong>ELB test (page one)!</strong></p>
                        </div>
                    </div>
                </div>
            </body>
        ```

    4.  Press  **Esc**  to exit editing mode. Then, enter  **:wq**  to save the settings and exit the file.

4.  Modify the HTML page of ECS02.

    The default root directory of Nginx is  **/usr/share/nginx/html**. Modify the  **index.html**  file to identify access to ECS02.

    1.  Run the following command to open the  **index.html**  file:

        **vim /usr/share/nginx/html**/**index.html**

    2.  Press  **i**  to enter editing mode.
    3.  Modify the  **index.html**  file.

        The following displays the content to be modified:

        ```
        ...
            <body>
                <h1>Welcome to <strong>ELB</strong> test page two!</h1>
        
                <div class="content">
                    <p>This page is used to test the <strong>ELB</strong>!</p>
        
                    <div class="alert">
                        <h2>ELB02</h2>
                        <div class="content">
                            <p><strong>ELB test (page two)!</strong></p>
                            <p><strong>ELB test (page two)!</strong></p>
                            <p><strong>ELB test (page two)!</strong></p>
                        </div>
                     </div>
                </div>
            </body>
        ```

    4.  Press  **Esc**  to exit editing mode. Then, enter  **:wq**  to save the settings and exit the file.

5.  Use a browser to access  **http://**_ECS01 EIP_  and  **http://**_ECS02 EIP_  to verify the Nginx service.

    If the modified HTML pages are displayed, Nginx has been deployed.

    -   HTML page of ECS01

        **Figure  2**  Nginx service successfully deployed on ECS01<a name="fig1823119513251"></a>  
        ![](figures/nginx-service-successfully-deployed-on-ecs01.png "nginx-service-successfully-deployed-on-ecs01")

    -   HTML page of ECS02

        **Figure  3**  Nginx service successfully deployed on ECS02<a name="fig17457132212516"></a>  
        ![](figures/nginx-service-successfully-deployed-on-ecs02.png "nginx-service-successfully-deployed-on-ecs02")



## Create a Load Balancer<a name="section15436447172917"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Click  **Create Enhanced Load Balancer**. On the displayed page, set the parameters as needed.
5.  Click  **Create Now**.
6.  Confirm the configuration and click  **Submit**. 
7.  View the newly created load balancer in the load balancer list.

## Add a Listener<a name="section184861920245"></a>

A listener is a set of configurations that specify the protocol and port to receive requests from the clients, and the protocol, port, and load balancing algorithm to forward requests to one or more backend server groups. A listener also defines the health check configuration, through which the load balancer automatically checks running statuses of backend servers. If a backend server becomes faulty, the load balancer automatically forwards traffic to other healthy ones. Traffic forwarding to this server resumes once it recovers.

**Figure  4**  Traffic forwarding<a name="fig1748151712518"></a>  
![](figures/traffic-forwarding.png "traffic-forwarding")

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the created load balancer and click its name \(**elb-mq01**\).
5.  Under  **Listeners**, click  **Add Listener**.
6.  Configure the listener and click  **Next**.
    -   **Name**: specifies the listener name, for example,  **listener-HTTP**.
    -   **Frontend Protocol/Port**: specifies the protocol and port number the load balancer uses to receive requests. For example, set it to  **HTTP**  and  **80**.

7.  Add the backend server group and configure the health check, and click  **Finish**.
    -   Backend server group
        -   **Name**: specifies the backend server group name, for example,  **server\_group-ELB**.
        -   **Load Balancing Algorithm**: specifies the algorithm the load balancer uses to route requests. Select  **Weighted round robin**.

    -   Health check
        -   **Protocol**: specifies the protocol the load balancer uses to perform health checks on backend servers. If the load balancer uses TCP, HTTP, or HTTPS to receive requests, the health check protocol can be TCP or HTTP. Set it to  **HTTP**, which cannot be changed after being set.
        -   **Domain Name**: specifies the domain name in the health check request, for example, www.example.com.
        -   **Port**: specifies the port number the load balancer uses to perform health checks on backend servers, for example,  **80**.

            If no port is specified, the port of each backend server is used for health checks by default.


8.  Locate the newly added listener. On the  **Backend Server Groups**  tab page on the right, click  **Add**.
9.  Set the backend port, select the servers to be added, and click  **OK**.
    -   **Backend Port**: specifies the port number used by the servers, for example,  **80**.
    -   Select ECS01 and ECS02 as backend servers.


## Verify Load Balancing<a name="section164467272278"></a>

After the load balancer is configured, you can access the corresponding domain name to check whether the two ECSs are accessible.

1.  Modify the  **C:\\Windows\\System32\\drivers\\etc\\hosts**  file on your PC to map the domain name to the load balancer EIP.

    You can view the load balancer EIP on the basic information page of the load balancer.

    **Figure  5** **hosts**  file on your PC<a name="fig11400732555"></a>  
    ![](figures/hosts-file-on-your-pc.png "hosts-file-on-your-pc")

2.  In the CLI of the PC, run the following command to check whether the domain name is mapped to the load balancer EIP:

    **ping www.example.com**

    If data packets are returned, the domain name has been mapped to the load balancer EIP.

3.  Use a browser to access  **http://www.example.com**. If the following page is displayed, the load balancer has routed the request to ECS01.

    **Figure  6**  Accessing ECS01<a name="fig174313116258"></a>  
    ![](figures/accessing-ecs01.png "accessing-ecs01")

4.  Use a browser to access  **http://www.example.com**. If the following page is displayed, the load balancer has routed the request to ECS02.

    **Figure  7**  Accessing ECS02<a name="fig897020534220"></a>  
    ![](figures/accessing-ecs02.png "accessing-ecs02")


