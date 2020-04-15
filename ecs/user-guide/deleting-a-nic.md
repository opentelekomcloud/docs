# Deleting a NIC<a name="EN-US_TOPIC_0093492519"></a>

## Scenarios<a name="section165134053512"></a>

An ECS can have up to 12 NICs, including one primary NIC that cannot be deleted and extension NICs. This section describes how to delete an extension NIC.

## Procedure<a name="section226511133385"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png) in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.

    The page providing details about the ECS is displayed.

5.  Click the  **NICs**  tab. Then, click  **Delete**  in the row of the target NIC.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You are not allowed to delete the primary ECS NIC. By default, the primary ECS NIC is the first NIC displayed in the NIC list.  

6.  Click  **OK**  in the displayed dialog box.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Certain ECSs do not support NIC deletion when they are running. For details about these ECSs, see the GUI display. To delete a NIC from such an ECS, stop the ECS.  


