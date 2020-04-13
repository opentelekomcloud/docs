# Running a Sample Project<a name="EN-US_TOPIC_0086094043"></a>

1.  Download the sample code and decompress the package.
2.  Open Eclipse. Choose  **File**  \>  **Import...**  to import an existing Maven project. Select the directory generated after  **DMSHttpClient**  is decompressed to import the sample project.
3.  Modify the  **dms-service-config.properties**  configuration file based on the information obtained in  [Table 1](environment-preparation.md#table621111583614). Set the parameters as follows:

    ```
    dms.service.endpoint.url=https://dms.****.com/ 
    dms.service.region= 
    dms.service.ak=************
    dms.service.sk=************
    dms.service.projectId=bd67aaead60940d688b872c31bdc663b
    ```

4.  Right-click the  **dms.httpclient**  project and choose  **Run As**  \>  **Java Application**  from the shortcut menu to run the sample project and test RESTful APIs.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >A queue is used for running the DMSHttpClient sample project, and the queue will be automatically released after the project is run.  


