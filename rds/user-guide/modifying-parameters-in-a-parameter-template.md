# Modifying Parameters in a Parameter Template<a name="en-us_topic_configuration"></a>

You can modify parameters in a custom parameter template as required for optimal RDS database performance.

You can change parameter values in custom parameter templates only and cannot change parameter values in default parameter templates. When you change parameter values in a custom parameter template, the changes take effect for all DB instances to which the parameter template applies.

If you change a parameter value, when the change takes effect is determined by the type of parameter.

The RDS console displays the statuses of DB instances to which the parameter template applies. For example, if the DB instance has not used the latest changes made to its parameter template, its status is  **Pending reboot**. You need to manually reboot the DB instance for the latest parameter changes to take effect for that DB instance.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>RDS has default parameter templates whose parameter values cannot be changed. You can view these parameter values by clicking the default parameter templates. If a custom parameter template is set incorrectly and causes a database reboot to fail, you can configure the custom parameter template by referring to the configurations of the default parameter template.  

## Modifying Parameters in Batches<a name="section1759510381059"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  Choose  **Parameter Template Management**  in the navigation pane on the left. On the  **Custom Templates**  page, click the target parameter template.
5.  Modify the parameters as required.

    For detailed parameter description, see section  [Precautions for Modifying MySQL Parameters](precautions-for-modifying-mysql-parameters.md).

    Available operations are as follows:

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >After you modify parameters in a parameter template, some modifications immediately take effect for the DB instance to which the parameter template applies. Exercise caution when performing this operation.  

    -   To save the modifications, click  **Save**.
    -   To cancel the modifications, click  **Cancel**.
    -   To preview the modifications, click  **Preview**.

6.  After the parameters are modified, you can click  **Change History**  to view the modification details.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >The modifications take effect only after you apply the parameter template to DB instances. For details, see  [Applying a Parameter Template](applying-a-parameter-template.md).  

    -   If you have modified parameters of a primary DB instance, you need to reboot the primary DB instance for the modifications to take effect. \(For primary/standby DB instances, the parameter modifications also apply to the standby DB instance.\)
    -   If you have modified parameters of a read replica, you need to reboot the read replica for the modifications to take effect.


## Modifying Instance Parameters<a name="section360115386520"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Parameters**. On the displayed page, modify parameters as required.

    Available operations are as follows:

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >After you modify parameters in a parameter template, the modifications immediately take effect for the DB instance to which the parameter template applies.  
    >Check the value in the  **Effective upon Reboot**  column.  
    >-   If the value is  **Yes**  and the DB instance status on the  **Instance Management**  page is  **Pending reboot**, you must reboot the DB instance for the modifications to take effect.  
    >-   If the value is  **No**, the modifications take effect immediately.  

    -   To save the modifications, click  **Save**.
    -   To cancel the modifications, click  **Cancel**.
    -   To preview the modifications, click  **Preview**.

    After parameters are modified, you can click  **Change History**  to view parameter modification details.


