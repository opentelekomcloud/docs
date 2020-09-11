# Binding and Unbinding an EIP<a name="dds_02_0006"></a>

## **Scenarios**<a name="section055104935914"></a>

You can access DDS through a private IP address or an EIP. The application scenario of the connection address is as follows:

-   Use a private IP address when:

    DDS provides a private IP address by default.

    Your applications are deployed on an ECS in a region where your cluster instance is located.


-   Use an EIP when:
    -   Your applications are deployed on an ECS in a region separated from the region where your cluster instance is located.
    -   Your applications are deployed on another cloud platform.


## Precautions<a name="section1130510262514"></a>

-   Before accessing a database, you need to apply for an EIP on the VPC console. Then, add an inbound rule to allow the IP addresses or IP address ranges of ECSs. For details, see section  [Setting a Security Group](setting-a-security-group(cluster).md).
-   In the cluster instance, only mongos can be bound to an EIP. To change the EIP that has been bound to a node, you need to unbind it from the node first.

## Binding an EIP<a name="section3199593620428"></a>

1.  On the  **Instance Management**  page, click the target cluster instance.
2.  On the  **mongos**  tab, choose  **More**  \>  **Bind EIP**.
3.  In the displayed dialog box, all EIPs in the unbound status are listed. Select the required EIP and click  **OK**. If no available EIPs are displayed, click  **View EIP**  and create an EIP on the VPC console.
4.  In the  **EIP**  column on the  **mongos**  tab, view the EIP that is successfully bound.

    To unbind an EIP from the DB instance, see  [Unbinding an EIP](#section186511510267).


## Unbinding an EIP<a name="section186511510267"></a>

1.  On the  **Instance Management**  page, click the target cluster instance.
2.  On the  **mongos**  tab in the  **Node Information**  area, locate the node with an EIP assigned and choose  **More**  \>  **Unbind EIP**.
3.  Click  **Yes**.

    To bind an EIP to the DB instance again, see  [Binding an EIP](#section3199593620428).


