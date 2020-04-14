# Step 5: Importing Sample Data to a Data Warehouse Cluster<a name="dws_01_0015"></a>

## Scenario<a name="section6082040915224"></a>

DWS users can import data from external sources to a data warehouse cluster. This section describes how to import sample data from OBS to a data warehouse cluster. The sample data is generated based on the TPC-DS benchmark test.

## Prerequisites<a name="section320498914613"></a>

-   You have created a data warehouse cluster. For details, see section  [Step 2: Creating a Cluster](step-2-creating-a-cluster.md).
-   You have logged in to the ECS and configured the DWS client. For details, see section  [Using the ECS to Connect to a Cluster](step-3-connecting-to-a-cluster.md#section99729517811).
-   You have obtained the AK and SK. For details, see section  [Creating Access Keys \(AK and SK\)](step-4-creating-access-keys-(ak-and-sk).md#section5520161143920).

## Procedure<a name="section5555805414531"></a>

1.  In the ECS Linux command window, run the following commands to switch to a specific directory and set the AK and SK for importing sample data and the OBS access address:

    **cd ./sample**

    **/bin/bash setup.sh -ak <_Access\_Key\_Id\>_  -sk <_Secret\_Access\_Key\>_  -obs\_location obs.otc.t-systems.com**

    If the following information is displayed, the setting is successful:

    ```
    setup successfully!
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Obtain values of  **Access\_Key\_Id**  and  **Secret\_Access\_Key**  from section  [Creating Access Keys \(AK and SK\)](step-4-creating-access-keys-(ak-and-sk).md#section5520161143920).  

2.  In the ECS Linux command window, run the following command to import the sample data to the data warehouse cluster:

    **gsql -d <_Database name_\> -h <_Public network address of the cluster\>_  -U <_Administrator\>_  -p <_Data warehouse port number\>_  -f <_Path for storing the sample data script\> -r_**

    **gsql -d postgres -h 10.168.0.74 -U dbadmin -p 8000 -f tpcds\_load\_data\_from\_obs.sql -r**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >In the preceding command, sample data script  **tpcds\_load\_data\_from\_obs.sql**  is stored in the  **sample**  directory \(for example,  **dws\_client\_redhat\_x64\\sample**\) of the DWS client.  

    After you enter the administrator password and successfully connect to the database in the cluster, the system will automatically create a foreign table with the sample data to associate data outside the cluster, create a table, and then import data to the table.

    When information similar to the following is displayed, the data is successfully imported.

    ```
    Time:1845600.524 ms
    ```


