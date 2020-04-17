# Sticky Session<a name="EN-US_TOPIC_0166390465"></a>

Sticky sessions are a mechanism that checks whether the processes of exchanges between the client and server are associated. This ensures that requests can be routed to the same server before a session elapses.

Here we use an example to explain what sticky sessions can do. Suppose that you have logged in to a server. After a while, you send another request. If sticky sessions are not enabled, the request may be routed to another server, and you will be asked to log in again. If sticky sessions are enabled, all your requests are processed by the same server, and you just need to log in once.

## Sticky Sessions at Layer 4<a name="section11814219164710"></a>

Sticky sessions at Layer 4 use source IP addresses to maintain sessions. Requests from the same IP address are routed to the same backend server during the session.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   You can set the stickiness duration only when you select  **Weighted round robin**  as the load balancing algorithm.  
>-   The default stickiness duration is 20 minutes, and the maximum duration is 60 minutes \(that is, 1 hour\).  

## Sticky Sessions at Layer 7<a name="section16751037115412"></a>

Sticky sessions at Layer 7 allow you to use load balancer cookies or application cookies to maintain sessions. Choose an appropriate sticky session type to better distribute requests across backend servers.

-   **Load balancer cookie**: The load balancer generates a cookie after receiving a request from the client. All subsequent requests with the cookie are routed to the same backend server for processing.
-   **Application cookie**: The application deployed on the backend server generates a cookie after receiving the first request from the client. All requests with the cookie are routed to this backend server.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   You can set the stickiness duration only when you select  **Weighted round robin**  as the load balancing algorithm.  
>-   The default stickiness duration is 20 minutes, and the maximum duration is 1440 minutes \(that is, 24 hours\).  

Enhanced load balancers support three types of sticky session, including  **Source IP address**,  **Load balancer cookie**, and  **Application cookie**.

Classic load balancers support two types of sticky session,  **Source IP address**  and  **Load balancer cookie**.

## Enable Sticky Sessions<a name="section8831828124420"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  For an enhanced load balancer, click  **Backend Server Groups**, locate the target backend server group, and click  ![](figures/icon-edit.png)  on the right of its name.

    For a classic load balancer, click  **Listeners**, locate the target listener, and click  **Modify**  in the  **Operation**  column.

6.  Enable the sticky session feature, select the sticky session type, and set the session stickiness duration.
7.  Click  **OK**.

