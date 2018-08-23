# Classic Load Balancer<a name="en-us_elb_04_0002"></a>

## Scenarios<a name="section24702498154616"></a>

-   TCP is used to forward the requests.
-   There is a large number of persistent connections.
-   Backend ECSs can evenly process requests.
-   All requests from the same client are forwarded to the same ECS.

## Configuration Reference<a name="section42291715154652"></a>

1.  Create a load balancer. Specify the following information as required:
    -   Enter a name for the load balancer.
    -   Select  **Public network**  for  **Type**.
    -   Select a VPC.
    -   Set the bandwidth.
2.  Add a listener. Specify the following information as required:
    -   Select  **TCP**  for  **Frontend Protocol**.
    -   Select  **TCP**  for  **ECS Protocol**.
    -   Select  **Round robin**  for  **Load Balancing Algorithm**.
    -   Enable  **Sticky Session**.
    -   Configure  **Stickiness Duration**, which must be longer than the session timeout duration. For example, if the session timeout duration is 3000s, you can set  **Stickiness Duration**  to  **3600**.
    -   Select  **TCP**  for  **Health Check Protocol**.
3.  Select and add target backend ECSs.
4.  Check the health status of target ECSs.

