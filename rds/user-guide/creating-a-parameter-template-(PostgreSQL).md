# Creating a Parameter Template<a name="en-us_topic_pg_parameter_group"></a>

You can use database parameter templates to manage the DB engine configuration. A database parameter template acts as a container for engine configuration values that can be applied to one or more DB instances.

When you create a DB instance, RDS will automatically allocate a default database parameter template for you, not allowing you to select parameter templates. This default template contains DB engine defaults and RDS system defaults based on the engine, compute class, and allocated storage of the instance. You cannot modify the parameter settings of a default parameter template. You must create your own parameter template to change parameter settings.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Not all DB engine parameters can be changed in a custom parameter template.  

If you want to use your custom parameter template, you simply create a parameter template and select it when you create a DB instance or apply it to an existing DB instance following the instructions provided in section  [Applying a Parameter Template](applying-a-parameter-template.md).

When you have already created a parameter template and want to include most of the custom parameters and values from that template in a new parameter template, you can replicate that parameter template following the instructions provided in section  [Replicating a Parameter Template](replicating-a-parameter-template.md).

The following are the key points you should know when using parameters in a parameter template:

-   When you change a dynamic parameter value in a parameter template and save the change, the change takes effect immediately. When you change a static parameter value in a parameter template and save the change, the change will take effect only after you manually reboot the DB instances to which the parameter template applies.
-   Improperly setting parameters in a parameter template may have unintended adverse effects, including degraded performance and system instability. Exercise caution when modifying database parameters and you need to back up data before modifying parameters in a parameter template. Before applying parameter template changes to a production DB instance, you should try out these changes on a test DB instance.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>RDS does not share parameter template quotas with DDS.  
>By default, each user can create a maximum of 100 parameter template for RDS DB instances. All RDS DB engines share the parameter template quota.  

## Procedure<a name="en-us_topic_parameter_group_s1d4b577d340b4a0baa353efbd0219c2d"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Parameter Template Management**  page, click  **Create Parameter Template**.
5.  In the displayed dialog box, configure required information and click  **OK**.
    -   Select a DB engine for the parameter template.
    -   The template name must consist of 1 to 64 characters. It can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\).
    -   The description consists of a maximum of 256 characters and cannot contain the carriage return character or the following special characters: \>!<"&'=


