# How to Use ELB in a Cluster<a name="cce_02_0087"></a>

This section describes how to use the Elastic Load Balancer \(ELB\) in a cluster created by CCE.

## Procedure<a name="section50156865193415"></a>

Create a service. For details about how to use an open-source API to create a service, see  [Creating a Service](creating-a-service.md).

```
{
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {
        "annotations":[
             {
		  "kubernetes.io/elb.class": "elasticity",
		  "kubernetes.io/elb.vpc.id": "a95ef7c1-34b4-48c4-9c4f-ae9ea6cc442b",
		  "kubernetes.io/elb.subnet-id": "bf04639b-9e67-4f02-ac63-379e9ce48ea2"
	     }
       ],
	"name": "test-service"
    },
    "spec": {
        "loadBalancerIP": "172.16.78.223",
        "ports": [
            {
                "name": "elbtest",
                "port": 80,
                "protocol": "TCP",
                "targetPort": 80
            }
        ],
        "selector": {
            "name": "elbtest"
        },
        "type": "LoadBalancer"
    }
}
```

In the preceding information:

-   **Kubernetes.io/elb.class**: This parameter is required for the system to interconnect with the ELB. Set this parameter to  **elasticity**  if the system interconnects with a classic ELB; set this parameter to  **union**  if the system interconnects with an enhanced ELB.
-   **Kubernetes.io/elb.vpc.id**: This parameter is used to specify the ID of the VPC where the ELB instance resides when the system interconnects with a classic ELB and the network is a private network.
-   **Kubernetes.io/elb.subnet-id**: This parameter is used to specify the ID of the subnet where the ELB instance resides when the system interconnects with an enhanced ELB.
-   **loadBalancerIP**: This parameter indicates the IP address allocated when an ELB is created on ECS.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >Check whether the selected ELB has a sufficient listener quota. If the quota is insufficient, create another ELB instance and set the value of  **loadBalancerIP**  to the IP address allocated when the ELB is created.  

-   **protocol**:  **TCP**  and  **UDP**  are supported.
-   **targetPort**: The value of this parameter cannot be the same as the listening port.
-   **Type**: The value must be  **LoadBalancer**.

