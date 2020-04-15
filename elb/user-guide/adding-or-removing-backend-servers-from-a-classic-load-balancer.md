# Adding or Removing Backend Servers from a Classic Load Balancer<a name="EN-US_TOPIC_0164706627"></a>

## Scenarios<a name="section166899516535"></a>

If you need adjust the number of backend servers added to a classic load balancer as traffic changes over time, you can refer to this topic.

## Add Backend Servers<a name="section8273133872011"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Click  **Classic**, locate the target load balancer, and click its name.
5.  Click  **Listeners**, locate the target listener, and click  **Add Backend ECS**  in the  **Operation**  column.
6.  In the  **Add Backend ECS**  dialog box, confirm the subnet, specify the backend port, and select the target backend servers from the list. You can filter servers by name or private IP address.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If a backend server has multiple NICs, you can only select the subnet where the primary NIC resides and use the primary NIC to add the backend server.  

7.  Click  **OK**.

## View Backend Servers<a name="section049293110219"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Click  **Classic**, locate the target load balancer, and click its name.
5.  Click  **Listeners**, locate the target listener, and click the number in the  **Backend ECSs**  column.

## Remove Backend Servers<a name="section1669926112218"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Click  **Classic**, locate the target load balancer, and click its name.
5.  Click  **Listeners**, locate the target listener, and click the number in the  **Backend ECSs**  column.
6.  To remove multiple backend servers, select the target servers and click  **Remove**  above the server list. To remove a server, locate the row that contains the target server and click  **Remove**  in the  **Operation**  column. Alternatively, select the target server and click  **Remove**  above the server list.
7.  In the  **Delete Redirect**  dialog box, click  **Yes**.

