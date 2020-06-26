# Collecting ECS Information \(Deprecated\)<a name="evs_01_0025"></a>

## Scenarios<a name="section44945912112556"></a>

This topic is used to guide users to collect the production ECS and DR ECS information, including the ECS IDs and the IDs of the EVS disks attached the ECSs.

Two EVS disks form an EVS replication pair. Therefore, the production disk ID, DR disk ID, and EVS replication pair ID can be used to identify disks and the EVS replication pair.

>![](/images/icon-note.gif) **NOTE:**   
>EVS replication APIs have been deprecated. If you need to use the replication function, see  [Storage Disaster Recovery Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/sdrs/en-us_topic_0125068221.html)  and  [Storage Disaster Recovery Service API Reference](https://docs.otc.t-systems.com/en-us/api/sdrs/en-us_topic_0108184470.html).  

## Procedure<a name="section5471394711362"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.

    The  **Elastic Cloud Server**  page is displayed.

4.  <a name="li23677833165924"></a>Click the name of the production ECS.

    The ECS details page is displayed.

5.  <a name="li3726148311399"></a>Perform the following operations to take note of the production ECS information:
    1.  Take note of the production ECS ID.

        Example ID: 4686b400-5a53-42f9-96f6-d2fe32bb9542

    2.  Click the  **Disks**  tab. Click  ![](figures/icon-next.jpg)  to view the details of the corresponding disk and take note of all the production disk IDs.

        You need to take note of the IDs of all the system disks and data disks attached to the production ECS.

        Example ID: ce86f381-99dc-422c-bb10-8014604cf5b9

    3.  Click the  **NICs**  tab. Click  ![](figures/icon-next.jpg)  to view the private IP address, elastic IP address \(EIP\), virtual IP address, and MAC address of a production NIC and take note of the private IP addresses, EIPs, virtual IP addresses, and MAC addresses of all NICs accordingly.

        You need to take note of IP addresses of all NICs bound to the production ECS.

        Example: 192.168.12.2, 10.154.52.0, 192.168.145.162, fa:16:3e:9e:74:ed

6.  Take note of the DR ECS information. For details, see  [4](#li23677833165924)  to  [5](#li3726148311399).

