# Using HiveQL Editor on the Hue WebUI<a name="EN-US_TOPIC_0125376126"></a>

## Scenario<a name="s44e510cf8c854f77b052ab1d5ba52e06"></a>

After Kerberos authentication is enabled for an MRS cluster, users can use the Hue WebUI to execute HiveQL statements in the cluster.

## Prerequisites<a name="se3e75c61401242e7871c040d9296745b"></a>

The MRS cluster administrator has assigned the permission for using Hive to the user. For details, see  [Creating a User](creating-a-user.md).

## Accessing  **Query Editors**<a name="section22433809173457"></a>

1.  Access the Hue WebUI and choose  **Query Editors**  \>  **Hive**. The **Hive**  page is displayed.

    **Hive**  supports the following functions.

    -   Executes and manages HiveQL statements.
    -   Queries HiveQL statements saved by the current user in  **Saved Queries**.
    -   Queries HiveQL statements executed by the current user in  **Query History**.

2.  Click  ![](figures/icon_mrs_showdb.jpg)  to display all databases in Hive.

## Executing HiveQL Statements<a name="section3586166217356"></a>

1.  Access  **Query Editors**.
2.  Select a Hive database in  **Databases**. The default database is **default**.

    The system displays all available tables. You can enter a keyword of the table name to search for the desired table.

3.  Click the desired table name. All columns in the table are displayed.

    Move the cursor to the row of the table and click  ![](figures/icon_mrs_dbtablelist.jpg). Column details are displayed.

4.  Enter the query statements in the area for editing HiveQL statements.

    Click  ![](figures/icon_mrs_dbedit.jpg) and choose **Explain**. The editor checks the syntax and execution plan of the entered statements. If the statements have syntax errors, the editor reports **Error while compiling statement**.

5.  Select the engine for executing the HiveQL statements.
    -   **mr**: MapReduce computing framework
    -   **spark**: Spark computing framework

6.  Click  ![](figures/icon_mrs_dbrunning.jpg)  to execute the HiveQL statements.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If you want to use the entered HiveQL statements again, click  ![](figures/icon_mrs_dbsave.jpg)  to save them.  
    >-   To format the HiveQL statements, click  ![](figures/icon_mrs_dbedit.jpg) and choose **Format**.  
    >-   To delete the entered HiveQL statements, click  ![](figures/icon_mrs_dbedit.jpg) and choose **Clear**.  
    >-   To clear the entered statements and start a new query, click  ![](figures/icon_mrs_dbedit.jpg) and choose **New query**.  


## Querying Execution Results<a name="section35608700173522"></a>

1.  View the execution results below the execution area on  **Hive**. The **Query History**  tab is displayed by default.
2.  Click a result to view the executed statements.

## Managing Statements<a name="section61610762173532"></a>

1.  Access  **Query Editors**.
2.  Click  **Saved Queries**.

    Click a saved statement. The system automatically fills the statement in the editing area.


## Modifying  **Query Editors**  Settings<a name="section59956943173543"></a>

1.  On the  **Hive** page, click ![](figures/icon_mrs_dbset.jpg).
2.  Click  ![](figures/icon_mrs_dbadd.jpg) on the right side of **Files**, and click ![](figures/icon_mrs_dbmanu.jpg)  to specify the save path of the file.

    You can click  ![](figures/icon_mrs_dbadd.jpg)  to add a file resource.

3.  Click  ![](figures/icon_mrs_dbadd.jpg) on the right side of **Functions**. Enter the name of the user-defined function and the function class.

    You can click  ![](figures/icon_mrs_dbadd.jpg)  to add a function.

4.  Click  ![](figures/icon_mrs_dbadd.jpg) on the right side of **Settings**. Enter the Hive parameter name in **Key** under **Settings** and the parameter value in **Value**. The session connects to Hive using the user-defined configuration.

    You can click  ![](figures/icon_mrs_dbadd.jpg)  to add a parameter.


