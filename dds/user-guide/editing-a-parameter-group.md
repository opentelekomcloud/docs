# Editing a Parameter Group<a name="en-us_topic_configuration"></a>

## **Scenarios**<a name="section61774358144918"></a>

This section guides you on how to edit parameters in the parameter groups that you have created to meet your service requirements and achieve optimal performance.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Default parameter groups are unchangeable. You can only view them by clicking their names. If inappropriate settings of user-created parameter groups lead to a database reboot failure, you can refer to the settings of the default parameter groups to reset them.  

## Procedure<a name="section30073268144833"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  In the navigation pane on the left, click  **Parameter Group Management**.
3.  On the  **Parameter Group Management**  page, locate the target parameter group, and click its name.
4.  Modify the required parameters.

    Related parameters are described as follows:

    -   For details on parameter descriptions, visit  [MongoDB official website](https://docs.mongodb.com/v3.2/reference/parameters/).
    -   The default value of the  **net.maxIncomingConnections**  parameter varies according to DB instance specifications. Therefore, this parameter is set to  **default**  before being specified.

    Possible operations are as follows:

    -   If you want to save the modifications, click  **Save**.
    -   If you want to cancel the modifications, click  **Cancel**.
    -   If you want to preview the modifications, click  **Preview**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For details on the description of parameter group status, see section  [Database Status](database-status.md).  
    >After modifying a parameter, you need to view the associated instance status in the instance list. If  **Pending restart**  is displayed, you need to restart the instance for the modification to take effect.  


