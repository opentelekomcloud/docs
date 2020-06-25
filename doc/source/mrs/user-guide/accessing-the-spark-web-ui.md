# Accessing the Spark Web UI<a name="EN-US_TOPIC_0221415067"></a>

You can view the running status of Spark applications on the Spark web UI.

Spark has two web UIs.

-   Spark UI: used to display the status of running applications.

    The UI includes the following parts: Jobs, Stages, Storage, Environment, Executors, SQL, and JDBC/ODBC Server. The Streaming application has one more Streaming tab.

-   History Server UI: used to display the running status of Spark applications that are complete or incomplete.

    History Server UI includes the application ID, application name, start time, end time, execution time, and owner information.


## Spark UI<a name="section15116141312243"></a>

1.  On MRS Manager, click  **Services**.
2.  Select  **Yarn**. In the  **Yarn Summary**  area, click  **ResourceManager**  corresponding to  **ResourceManager Web UI**  for  **Presto WebUI**  to access the web UI.
3.  Locate the Spark application. Click  **ApplicationMaster**  in the last column of the application information. The Spark UI is displayed.

    **Figure  1**  ApplicationMaster<a name="fig194431716415"></a>  
    ![](figures/applicationmaster.png "applicationmaster")

    **Figure  2**  Spark UI<a name="fig941314811449"></a>  
    ![](figures/spark-ui.png "spark-ui")


## History Server<a name="section203881712162610"></a>

1.  On MRS Manager, click  **Services**.
2.  Select  **Spark**. In the  **Spark Summary**  area, click  **JobHistory**  corresponding to  **Spark Web UI**  to access the web UI.

    **Figure  3**  Spark history server<a name="fig14824556452"></a>  
    ![](figures/spark-history-server.png "spark-history-server")


