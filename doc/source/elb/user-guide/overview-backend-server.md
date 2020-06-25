# Overview<a name="EN-US_TOPIC_0164706624"></a>

A backend server is an ECS or BMS added to a backend server group associated with a load balancer. When adding a listener to a load balancer, you create or select a backend server group to receive requests from the load balancer using the port and protocol you specify for the backend server group and the load balancing algorithm you select.

You can adjust the number of backend servers to ensure stable and reliable service based on your budget. Load balancers can distribute requests across backend servers in different AZs to prevent SPOFs. You must ensure that at least one backend server is working properly in each AZ.

## Precautions<a name="section9765648163914"></a>

When adding backend servers, pay attention to the following:

-   Backend servers must be in the same VPC as the load balancer.
-   It is recommended that backend servers run the same OS for ease of management and maintenance.
-   You can set a weight for each server in the backend server group. The higher the weight is, the more requests the backend server receives.
-   If you enable the sticky session feature, the proportions of requests processed by backend servers may become unbalanced. In this case, disable the sticky session feature and wait until each backend server receives almost the equal proportion of requests.

