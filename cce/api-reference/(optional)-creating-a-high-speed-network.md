# \(Optional\) Creating a High-Speed Network<a name="cce_02_0270"></a>

## Context<a name="section92509191007"></a>

Before creating a Bare Metal Server \(BMS\) cluster, you need to create a VPC. Besides, you also need to create a high-speed network for the cluster and obtain the subnet ID of the high-speed network.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Ensure that the subnet segment of the new high-speed network does not conflict with the existing VPC network segment.  

## Procedure<a name="section75441847918"></a>

1.  Log in to the management console and choose  **Computing**  \>  **Bare Metal Server**  from the service list.
2.  <a name="li179971013215"></a>On the  **Bare Metal Server**  page, click the  **High-Speed Networks**  tab and click  **Create High-Speed Network**.

    Ensure that the subnet segment of the new high-speed network does not conflict with the existing VPC network segment.

3.  Obtain the endpoint of the VPC in the current environment.
4.  Run the following command to obtain information about all high-speed networks created by the current user:

    curl -i -k -H "Content-Type:application/json" -H "X-Auth-Token:$**\{Token\}**" -X GET https://**\{Endpoint\}**/**\{URI\}**

    -   **Token**: token of a common user.
    -   **Endpoint**: endpoint of the VPC service.
    -   **URI**: URI for obtaining high-speed network information. Here, set the value to  **v2.0/networks?provider:network\_type=geneve**.

5.  In the returned response body, find the high-speed network created in  [2](#li179971013215)  and the  **subnets**  field of this high-speed network. The value of this field is the subnet ID of the high-speed network.

    Assuming that the name of the created high-speed network is  **highway-ec86**, record the corresponding subnet ID of the  **highway-ec86**  high-speed network. The subnet ID will be used when you create a BMS cluster in  [Creating a Cluster](creating-a-cluster.md).

    ```
    {
        "networks": [
            {
                "id": "3cfe3cf3-4354-4924-9f4b-818e0d307833",
                "name": "highway-ec86",
                "status": "ACTIVE",
                "shared": false,
                "subnets": [
                    "86208959-1b1e-46dc-b7de-b815d7a323c2"
                ],
                "availability_zone_hints": [],
                "availability_zones": [
                    "eu-de-01",
                    "kvmxen.dc1",
                    "ceshishouqing"
                ],
                "admin_state_up": false,
                "tenant_id": "aef929d2de9249d6ae55466a72b6be25",
                "provider:network_type": "geneve",
                "router:external": false,
                "port_security_enabled": true,
                "dns_domain": "eu-de.compute.internal."
            },
            {
                "id": "f17e2a39-a7e3-4438-a866-e8b362df5fcf",
                "name": "highway-0405",
                "status": "ACTIVE",
                "shared": false,
                "subnets": [
                    "c0c564fd-f25a-466a-827c-ee4d3aa51a6a"
                ],
                "availability_zone_hints": [],
                "availability_zones": [
                    "eu-de-01",
                    "kvmxen.dc1",
                    "ceshishouqing"
                ],
                "admin_state_up": false,
                "tenant_id": "aef929d2de9249d6ae55466a72b6be25",
                "provider:network_type": "geneve",
                "router:external": false,
                "port_security_enabled": true,
                "dns_domain": "eu-de.compute.internal."
            }
        ]
    }
    ```


