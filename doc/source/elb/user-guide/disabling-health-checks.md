# Disabling Health Checks<a name="EN-US_TOPIC_0164706631"></a>

## Scenarios<a name="section1481212713114"></a>

You can disable the health check function if you do not need health checks. If you have already configured a health check, you can also disable the health check function to stop checking server health statuses.

After the health check function is disabled, backend servers will not be detected, and the load balancer will consider the backend servers healthy. If a backend server becomes faulty or is working improperly, the load balancer will still route requests to this server. As a result, applications on this server are inaccessible. If this happens, you need to ensure that the ports of backend servers are normal. It is recommended that do not disable the health check function unless necessary.

Disabling the health check function is not supported for classic load balancers.

## Procedure<a name="section3986711219"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.

1.  Click  **Backend Server Groups**, locate the target backend server group, and click its name.
2.  Click  **More**  in the  **Operation**  column.
3.  Select  **Configure Health Check**  from the drop-down list.

1.  In the  **Configure Health Check**  dialog box, disable the health check function.

1.  Click  **OK**.

