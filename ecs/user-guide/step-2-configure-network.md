# Step 2: Configure Network<a name="EN-US_TOPIC_0163572590"></a>

## Network Configurations<a name="section13330112505510"></a>

1.  Set  **Network**  by selecting an available VPC and subnet from the drop-down list and specifying a private IP address assignment mode.

    VPC provides a network, including subnet and security group, for an ECS.

    You can select an existing VPC or create a desired one.

    For more information about VPC, see  _Virtual Private Cloud User Guide_.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Ensure that DHCP is enabled in the VPC to which the ECS belongs.  
    >-   When you use VPC for the first time, the system automatically creates a VPC for you, including the security group and NIC.  

2.  \(Optional\) Add an extension NIC. You can add multiple expansion NICs to an ECS and specify IP addresses for them \(including primary NICs\).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When you specify an IP address for a NIC, if multiple ECSs are created in a batch:  
    >-   This IP address serves as the start IP address.  
    >-   Ensure that the IP addresses required by the NICs are within the subnet, consecutive, and available.  
    >-   This subnet cannot duplicate a subnet with a specified start IP address.  

    -   **MTU Settings**: This parameter is optional.

        If your ECS is of M2, large-memory, H1, or D1 type, you can click  **MTU Settings**  to configure the maximum transmission unit \(MTU\) for a to-be-added extension NIC for improving network performance. An MTU can only be a number, ranging from 1280 to 8888.

3.  Set  **Security Group**  by selecting an available security group from the drop-down list or creating a new one.

    A security group controls ECS access within or between security groups by defining access rules. This enhances ECS security.

    When creating an ECS, you can select multiple \(recommended not more than five\) security groups. In such a case, the access rules of all the selected security groups apply on the ECS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Before initializing an ECS, ensure that the security group rule in the outbound direction meets the following requirements:  
    >-   **Protocol**:  **TCP**  
    >-   **Port Range**:  **80**  
    >-   **Remote End**:  **169.254.0.0/16**  
    >If you use the default security group rule in the outbound direction, the preceding requirements are met, and the ECS can be initialized. The default security group rule in the outbound direction is as follows:  
    >-   **Protocol**:  **ANY**  
    >-   **Port Range**:  **ANY**  
    >-   **Remote End**:  **0.0.0.0/16**  

4.  Set  **EIP**.

    An EIP is a static public IP address bound to an ECS in a VPC. Using the EIP, the ECS provides services externally.

    The following options are provided:

    -   Do not use

        Without an EIP, the ECS cannot access the Internet and is used in the private network or cluster only.

    -   Auto assign

        The system automatically assigns an EIP for the ECS. The EIP provides a dedicated bandwidth that is configurable.

    -   Specify

        An existing EIP is assigned for the ECS. When using an existing EIP, you cannot create ECSs in batches.

5.  Click  **Next: Configure Advanced Settings**.

