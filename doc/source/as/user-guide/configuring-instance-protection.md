# Configuring Instance Protection<a name="EN-US_TOPIC_0076979345"></a>

## Scenarios<a name="section68401743312"></a>

Configure instance protection if you want to specify one or more ECSs not to be automatically removed from an AS group. After the configuration, when AS automatically reduces the number of ECSs in an AS group, the in-service ECSs with instance protection enabled will not be removed.

## Prerequisites<a name="section33767911104059"></a>

In the following scenarios, ECSs will still be removed from the AS group even if instance protection is enabled:

-   The ECS is not healthy according to the health check.
-   The ECS is manually removed from the AS group.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Instances in the abnormal health status cannot provide services. The AS group preferentially ensures that all instances in the group are normal. Therefore, instance protection cannot protect abnormal instances.  
    >-   By default, instance protection does not take effect on the ECSs that are newly created in or added to an AS group.  
    >-   Instance protection becomes invalid immediately when the target ECS is removed from the AS group.  


## Enabling Instance Protection<a name="section35538053104144"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Click the name of the target ECS.
5.  Click the  **Instances**  tab. Select one or more ECSs and choose  **Enable Instance Protection**  from the  **More**  drop-down list. In the displayed  **Enable Instance Protection**  dialog box, click  **Yes**.

    You can also locate the row containing the target ECS and click  **Enable Instance Protection**  in the  **Operation**  column. Then, in the  **Enable Instance Protection**  dialog box, click  **Yes**.


## Disabling Instance Protection<a name="section42597752104218"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  Click the name of the target ECS.
5.  Click the  **Instances**  tab. Select one or more ECSs and choose  **Disable Instance Protection**  from the  **More**  drop-down list. In the displayed  **Disable Instance Protection**  dialog box, click  **Yes**.

    You can also locate the row containing the target ECS and click  **Disable Instance Protection**  in the  **Operation**  column. Then, in the  **Disable Instance Protection**  dialog box, click  **Yes**.


