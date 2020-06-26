# Applying a Parameter Template<a name="rds_05_0018"></a>

## **Scenarios**<a name="section732387614651"></a>

Changes to parameters in a custom parameter template take effect for DB instances only after you apply this parameter template to target DB instances.

-   The parameter  **innodb\_buffer\_pool\_size**  is determined by the memory. DB instances of different specifications have different value ranges. If this parameter value is out of range of the DB instance to which the parameter template applies, the maximum value within the range is used.
-   A parameter template can be applied only to DB instances of the same DB engine version.

## Procedure<a name="section05781558132917"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Parameter Template Management**  page, perform the following operations based on the type of the parameter template to be applied:

    -   If you intend to apply a default parameter template to DB instances, click  **Default Templates**, locate the target parameter template, and click  **Apply**  in the  **Operation**  column.
    -   If you intend to apply a custom parameter template to DB instances, click  **Custom Templates**, locate the target parameter template, and choose  **More**  \>  **Apply**  in the  **Operation**  column.

    A parameter template can be applied to one or more DB instances.

5.  In the displayed dialog box, select one or more DB instances to which the parameter template will be applied and click  **OK**.

    After the parameter template is successfully applied, you can view the application records by referring to section  [Viewing Application Records of a Parameter Template](viewing-application-records-of-a-parameter-template.md).


