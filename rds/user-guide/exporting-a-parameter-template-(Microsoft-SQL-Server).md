# Exporting a Parameter Template<a name="rds_sqlserver_08_0042"></a>

## **Scenarios**<a name="en-us_topic_0171122608_section2406221536"></a>

-   You can export a parameter template of a DB instance for future use. You can apply the exported parameter template to DB instances by referring to section  [Applying a Parameter Template](applying-a-parameter-template-(Microsoft-SQL-Server).md).
-   You can export the parameter template information \(parameter names, values, and descriptions\) of a DB instance to a CSV file for viewing and analysis.

## Procedure<a name="en-us_topic_0171122608_section1472455119616"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Parameters**. On the displayed page, click  **Export**  above the parameter list.
    -   Exporting to a custom template

        In the displayed dialog box, configure required information and click  **OK**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   The template name must consist of 1 to 64 characters. It can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\).  
        >-   The description consists of a maximum of 256 characters and cannot contain the carriage return character or the following special characters: \>!<"&'=  

        After the parameter template is exported, a new template is generated in the list on the  **Parameter Template Management**  page.

    -   Exporting to a file

        The parameter template information \(parameter names, values, and descriptions\) of a DB instance is exported to a CSV file. In the displayed dialog box, enter the file name and click  **OK**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >The file name must start with a letter and consist of 4 to 64 characters. It can contain only letters, digits, hyphens \(-\), and underscores \(\_\).  



