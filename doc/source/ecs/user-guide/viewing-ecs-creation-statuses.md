# Viewing ECS Creation Statuses<a name="EN-US_TOPIC_0039588795"></a>

## Scenarios<a name="section52267161284"></a>

After submitting the request for creating an ECS, you can view the creation status. This section describes how to view the creation status of an ECS.

## Procedure<a name="section40936232171845"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  After creating an ECS, view the creation status in the task status area on the right side of common operations, such as  **Start**,  **Stop**, and  **More**.
5.  Click the number displayed above  **Creating**  and view details about the tasks.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   An ECS that is being created is in one of the following states:  
    >    -   **Creating**: The ECS is being created.  
    >    -   **Failures**: Creating the ECS failed. In such a case, the system automatically rolls the task back and displays an error code on the GUI, for example,  **Ecs.0013 Insufficient EIP quota**.  
    >    -   **Running**: The request of creating the ECS has been processed, and the ECS is running properly. An ECS in this state can provide services for you.  
    >        See  [How Do I Handle Error Messages Displayed on the Management Console?](how-do-i-handle-error-messages-displayed-on-the-management-console.md)  for troubleshooting.  
    >-   If you find that the task status area shows an ECS creation failure but the ECS list displays the created ECS, see  [Why Does the Failures Area Show an ECS Creation Failure But the ECS List Displays the Created ECS?](why-does-the-failures-area-show-an-ecs-creation-failure-but-the-ecs-list-displays-the-created-ecs.md)  


