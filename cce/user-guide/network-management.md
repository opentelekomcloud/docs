# Network Management<a name="cce_01_0020"></a>

-   **[Network Overview](network-overview.md)**  
CCE provides different workload access types to address diverse scenarios.
-   **[Intra-Cluster Access \(ClusterIP\)](intra-cluster-access-(clusterip).md)**  
A workload is accessible to other workloads in the same cluster through the use of an internal domain name.
-   **[NodePort](nodeport.md)**  

-   **[LoadBalancer](loadbalancer.md)**  
A workload can be accessed from  public networks  through a  load balancer. LoadBalancer provides higher reliability than EIP-based NodePort because an EIP is no longer bound to a single node. The LoadBalancer access type is applicable to the scenario in which a service exposed to public networks is required.
-   **[DNAT](dnat.md)**  
A  **destination network address translation \(DNAT\) gateway**  is situated between  cluster nodes  and public networks and assigned an EIP. After receiving inbound requests from public networks, the NAT gateway translates the EIP \(destination address in the inbound requests\) into a cluster-internal address. It appears to workload users as if all nodes running the workload share the same EIP.
-   **[Layer 7 Load Balancing \(Ingress\)](layer-7-load-balancing-(ingress).md)**  
Layer-7 load balancing uses enhanced load balancers. Compared with layer-4 load balancing, layer-7 load balancing additionally supports Uniform Resource Identifier \(URI\) configurations and  distributes access traffic  to services based on URIs. In addition, different functions are implemented based on various URIs.
-   **[Network Policy](network-policy.md)**  
CCE has enhanced the Kubernetes-based network policy function, allowing network isolation in a cluster by configuring network policies. This means that a firewall can be set between instances \(pods\).

