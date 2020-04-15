# Preparing an ECS as the gsql Client Host<a name="dws_01_0128"></a>

The gsql command line client provided by DWS runs on the Linux OS. Before using it to remotely connect to a data warehouse cluster, you need to prepare a Linux host for installing and running the gsql client. If you use a public network address to access the cluster, you can install the gsql client on your own Linux host. Ensure that the Linux host has a public network address. For your convenience, you are advised to purchase a Linux ECS. This section describes how to prepare an ECS. If you already have a qualified ECS, skip this section.

## Preparing an ECS<a name="section595518354145"></a>

For details about how to create an ECS, see section  **Getting Started \> Logging In to an ECS**  in the  _Elastic Cloud Server User Guide_.

The ECS must meet the following requirements:

-   The ECS and data warehouse cluster must belong to the same region and AZ.
-   If you use the gsql client provided by DWS to connect to the data warehouse cluster, the ECS image must meet the following requirements:

    There is no special requirement for the image's specifications. The image's OS must be one of the following Linux OSs supported by the gsql client:

    -   The  **RedHat x64**  client can be used on the following OSs:
        -   RHEL 6.4/6.5/6.6/6.7/7.1/7.2
        -   CentOS 6.4/6.5/6.6/6.7
        -   EulerOS 2.0 SP2

    -   The  **SUSE x64**  client can be used on the following OSs:

        SLES11 SP1/SP2/SP3/SP4


-   If the client accesses the cluster using the private network address, ensure that the created ECS is in the same VPC as the data warehouse cluster.

    For details about VPC operations, see section  **VPC and Subnet**  in the  _Virtual Private Cloud User Guide_.

-   If the client accesses the cluster using the public network address, ensure that both created ECS and the data warehouse cluster have an EIP.

    When creating an ECS, you need to set  **EIP**  to  **Automatically assign**  to bind to the EIP.

    For details about how to bind to an EIP, see section  **Elastic IP Address**  in the  _Virtual Private Cloud User Guide_.

-   The security group rules of the ECS must enable communication between the ECS and the port that the data warehouse cluster uses to provide services.

    For details about security group operations, see  **Security**  \>  **Security Group**  in the  _Virtual Private Cloud User Guide_.

    Ensure that the security group of the ECS contains rules meeting the following requirements. If the rules do not exist, add them to the security group:

    -   **Transfer Direction**:  **Outbound**
    -   **Protocol/Application**: The value must contain  **TCP**, for example,  **TCP**  and  **All**.
    -   **Port Range**: The value must contain the database port that provides services in the data warehouse cluster. For example, set this parameter to  **1-65535**  or a specific DWS database port.
    -   **Destination:**  The IP address set here must contain the IP address of the cluster to be connected. For example, set this parameter to  **0.0.0.0/0**  or the specific connection address of the data warehouse cluster.

-   The security group rules of the data warehouse cluster must ensure that DWS can receive network access requests from clients.

    Ensure that the cluster's security group contains rules meeting the following requirements. If the rules do not exist, add them to the security group:

    -   **Transfer Direction**:  **Inbound**
    -   **Protocol/Application**: The value must contain  **TCP**, for example,  **TCP**  and  **All**.
    -   **Port Range**: Set this parameter to the database port that provides services in the data warehouse cluster, for example,  **8000**.
    -   **Source**: The IP address set here must contain the IP address of the DWS client host, for example,  **192.168.0.10/32**.


