# Resetting a Parameter Template<a name="en-us_topic_pg_0049456616"></a>

## **Scenarios**<a name="en-us_topic_0049456616_section732387614651"></a>

You can reset all parameters in a custom parameter template to their default settings.

## Procedure<a name="en-us_topic_0049456616_s35b89f49183c41609d978b23557270a2"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Parameter Template Management**  page, click  **Custom Templates**. Locate the target parameter template and choose  **More**  \>  **Reset**  in the  **Operation**  column.
5.  Click  **Yes**.

    >![](/images/icon-note.gif) **NOTE:**   
    >For details about the parameter template statuses, see  [Parameter Template Statuses](db-instance-statuses.md#sf14afc99d1fe4941b44ffca460288867).  
    >After you reset the parameter template, click the DB instance to which the parameter template applies to view the status of the parameter template. On the displayed  **Basic Information**  page, if the status of the parameter template is  **Pending reboot**, you must reboot the DB instance for the reset to take effect.  


