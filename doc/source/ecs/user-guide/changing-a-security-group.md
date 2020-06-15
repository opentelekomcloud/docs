# Changing a Security Group<a name="EN-US_TOPIC_0093492517"></a>

## Scenarios<a name="section5630193654713"></a>

To change the security group of an ECS NIC, perform the operations described in this section.

## Procedure<a name="section148110439474"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  Locate the row containing the target ECS, click  **More**  in the  **Operation**  column, and select  **Change Security Group**.

    The  **Change Security Group**  dialog box is displayed.

    **Figure  1**  Change Security Group<a name="fig1673733486"></a>  
    ![](figures/change-security-group.png "change-security-group")

5.  Select the target NIC and security group as prompted.

    You can select multiple security groups. In such a case, the access rules of all the selected security groups apply on the ECS. To create a security group, click  **Create Security Group**.

    >![](/images/icon-note.gif) **NOTE:**   
    >Using multiple security groups may deteriorate ECS network performance. You are suggested to select no more than five security groups.  

6.  Click  **OK**.

