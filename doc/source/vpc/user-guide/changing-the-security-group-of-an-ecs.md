# Changing the Security Group of an ECS<a name="SecurityGroup_0006"></a>

## Scenarios<a name="section181956227265"></a>

Change the security group associated with an ECS NIC.

## Procedure<a name="section15810103716296"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.
5.  Click the  **Security Groups**  tab. Then, click  **Change Security Group**.
6.  Select the new security group to be associated with the ECS NIC.

    You can select multiple security groups. In such a case, the access rules of all the selected security groups apply to the ECS.

    >![](/images/icon-note.gif) **NOTE:**   
    >Using multiple security groups may impact the network performance of your ECS. We recommend that you select no more than five security groups for each ECS.  

7.  Click  **OK**.

