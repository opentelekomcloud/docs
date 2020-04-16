# Replicating a Parameter Template<a name="en-us_topic_0049456617"></a>

## **Scenarios**<a name="section3995969114636"></a>

You can replicate a parameter template you have created. When you have already created a parameter template and want to include most of the custom parameters and values from that template in a new parameter template, you can replicate that parameter template. 

After the parameter template is replicated, you should wait at least 5 minutes before using it to create a DB instance.

Default parameter templates cannot be replicated. You can create parameter templates based on the default ones.

## Procedure<a name="s761901cf52004ac2bf067f6b7565c00d"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Parameter Template Management**  page, click  **Custom Templates**. Locate the target parameter template and click  **Replicate**  in the  **Operation**  column.

    Alternatively, click the target DB instance on the  **Instance Management**  page. On the  **Parameters**  page, click  **Export**  to generate a new parameter template for future use.

5.  In the displayed dialog box, configure required information and click  **OK**.

    -   The template name must consist of 1 to 64 characters. It can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\).
    -   The description consists of a maximum of 256 characters and cannot contain the carriage return character or the following special characters: \>!<"&'=

    After the parameter template is replicated, a new template is generated in the list on the  **Parameter Template Management**  page.


