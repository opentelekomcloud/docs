# Limitations<a name="EN-US_TOPIC_0125375337"></a>

Before using MRS, ensure that you have read and understand the following limitations.

-   MRS clusters must be created in VPC subnets.
-   You are advised to use any of the following browsers to access MRS:
    -   Google Chrome 36.0 or later
    -   Internet Explorer 9.0 or later

        If you use Internet Explorer 9.0, you may fail to log in to the MRS management console because user  **Administrator**  is disabled by default in some Windows systems, such as Windows 7 Ultimate. Internet Explorer automatically selects a system user for installation. As a result, Internet Explorer cannot access the management console. You are advised to reinstall Internet Explorer 9.0 or later as the administrator \(recommended\) or alternatively run Internet Explorer 9.0 as the administrator.


-   To prevent illegal access, only assign access permission for security groups used by MRS where necessary.
-   Do not perform the following operations because they will cause cluster exceptions:
    -   Deleting or modifying the default security group that is created when you create an MRS cluster.
    -   Powering off, restarting, or deleting cluster nodes displayed in ECS, changing or reinstalling their OS, or modifying their specifications when you use MRS.
    -   Deleting the processes, installed applications  or files that already exist on the cluster node.
    -   Deleting MRS cluster nodes. Deleted nodes will still be charged.

-   If a cluster exception occurs when no incorrect operations have been performed, contact technical support engineers. The technical support engineers will ask you for your key and then perform troubleshooting.
-   MRS clusters are still charged during exceptions. Contact technical support engineers to handle cluster exceptions.
-   Plan disks of cluster nodes based on service requirements. If you want to store a large volume of service data, add EVS disks or storage space to prevent insufficient storage space from affecting node running.
-   The cluster nodes store only users' service data. Non-service data can be stored in the OBS or other ECS nodes.
-   The cluster nodes only run MRS cluster programs. Other client applications or user service programs are deployed on separate ECS nodes.

