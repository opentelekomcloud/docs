# \(Optional\) Adding a Load Balancer to an AS Group<a name="EN-US_TOPIC_0042018369"></a>

 Elastic Load Balancing \(ELB\) automatically distributes incoming traffic across multiple backend servers based on configured forwarding policies. ELB expands the service capabilities of applications and improves their availability by eliminating single points of failure \(SPOFs\).

If ELB functions are required, perform the operations provided in this section to add a load balancer to your AS group. The load balancer added to an AS group distributes application traffic to all instances in the AS group when an instance is added to or deleted from the AS group.

AS supports only created load balancers. For details about how to create a load balancer, see  _Elastic Load Balance User Guide_. To add a load balancer for an AS group, perform the following operations:

-   When creating an AS group, configure parameter  **Load Balancing**  to add a load balancer. For details, see  [Creating an AS Group](creating-an-as-group.md).
-   If the AS group is not enabled, contains no instance, and has no scaling action ongoing, modify parameter  **Load Balancing**  to add a load balancer for the AS group. For details, see  [Modifying an AS Group](modifying-an-as-group.md).

