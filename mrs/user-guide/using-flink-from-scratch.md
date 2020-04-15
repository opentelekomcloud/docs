# Using Flink from Scratch<a name="EN-US_TOPIC_0221415088"></a>

This section describes how to use Flink to run wordcount jobs.

## Prerequisites<a name="section148416033913"></a>

The Flink component has been installed in an MRS cluster.

## Procedure<a name="section286111359366"></a>

1.  Download and log in to an MRS client. For details, see  [Updating the Client](updating-the-client.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If a client has been installed on the node, skip this step.  

2.  Run the following command to initialize environment variables:

    **source /opt/client/bigdata\_env**

3.  If Kerberos authentication is enabled for the cluster, perform the following steps. If Kerberos authentication is not enabled for the cluster, skip this step.
    1.  Prepare a user that is used to submit Flink jobs.
    2.  Log in to MRS Manager using the newly created user, choose  **System**  \>  **Manage User**. Locate the row that contains the new user, and choose  **More**  \>  **Download Authentication Credential**  in the  **Operation**  column.
    3.  Decompress the downloaded authentication credential package and copy the  **user.keytab**  file to the client node, for example, the  **/opt/client/Flink/flink/conf**  directory on the client node.
    4.  Configure security authentication by adding the  **keytab**  path and username in the  **/opt/client/Flink/flink/flink-conf.yaml**  configuration file.

        **security.kerberos.login.keytab:  _<user.keytab file path\>_**

        **security.kerberos.login.principal:  _<Username\>_**

        Example:

        **security.kerberos.login.keytab: /opt/client/Flink/flink/conf/user.keytab**

        **security.kerberos.login.principal: test**

    5.  In the  **bin**  directory of the Flink client, run the following command to perform security hardening. Set  **password**  to a new password for submitting jobs.

        **sh generate\_keystore.sh <password\>**

        This script automatically replaces the SSL value in the  **/opt/client/Flink/flink/conf/flink-conf.yaml**  file. By default, the external SSL is disabled in a cluster in security mode. If you want to enable the external SSL, configure it by referring to  [Security Hardening](security-hardening.md)  and run the script again.

    6.  Configure paths for the client to access the  **flink.keystore**  and  **flink.truststore**  files.
        -   Absolute path: After the script is executed, the  **flink.keystore**  and  **flink.truststore**  file paths are automatically set to the absolute path  **/opt/client/Flink/flink/conf/**  in the  **flink-conf.yaml**  file. In this case, you need to move the  **flink.keystore**  and  **flink.truststore**  files from the  **conf**  directory to the absolute path on the Flink client and Yarn nodes.
        -   Relative path: Perform the following steps to set the paths of the  **flink.keystore**  and  **flink.truststore**  files to relative paths and ensure that the directory where the Flink client command is executed can directly access the relative paths.
            1.  Create a directory, for example,  **ssl**, in  **/opt/client/Flink/flink/conf/**.
            2.  Move the  **flink.keystore**  and  **flink.truststore**  files to the  **/opt/client/Flink/flink/conf/ssl/**  directory.
            3.  Change the values of the following parameters to relative paths in the  **flink-conf.yaml**  file:

                security.ssl.internal.keystore: ./ssl/flink.keystore

                security.ssl.internal.truststore: ./ssl/flink.truststore



4.  Run a wordcount job.
    -   Normal cluster \(Kerberos authentication disabled\)
        -   Run the following command to start a session and submit a job in the session:

            **yarn-session.sh -nm "session-name"**

            **flink run /opt/client/Flink/flink/examples/streaming/WordCount.jar**

        -   Run the following command to submit a single job on Yarn:

            **flink run -m yarn-cluster /opt/client/Flink/flink/examples/streaming/WordCount.jar**

    -   Security cluster \(Kerberos authentication enabled\)
        -   When the  **flink.keystore**  and  **flink.truststore**  files are stored in absolute paths:
            -   Run the following command to start a session and submit a job in the session:

                **yarn-session.sh -nm "session-name"**

                **flink run /opt/client/Flink/flink/examples/streaming/WordCount.jar**

            -   Run the following command to submit a single job on Yarn:

                **flink run -m yarn-cluster /opt/client/Flink/flink/examples/streaming/WordCount.jar**

        -   When the  **flink.keystore**  and  **flink.truststore**  files are stored in relative paths:
            -   Run the following command to start a session and submit a job in the session:

                **yarn-session.sh -t ssl/ -nm "session-name"**

                **flink run /opt/client/Flink/flink/examples/streaming/WordCount.jar**

            -   Run the following command to submit a single job on Yarn:

                **flink run -m yarn-cluster -yt ssl/ /opt/client/Flink/flink/examples/streaming/WordCount.jar**



5.  After the job has been successfully submitted, the following information is displayed on the client:

    **Figure  1**  Job submitted successfully on Yarn<a name="fig7572041542"></a>  
    ![](figures/job-submitted-successfully-on-yarn.png "job-submitted-successfully-on-yarn")

    **Figure  2**  Session started successfully<a name="fig2211144410227"></a>  
    ![](figures/session-started-successfully.png "session-started-successfully")

    **Figure  3**  Job submitted successfully in the session<a name="fig1343995812714"></a>  
    ![](figures/job-submitted-successfully-in-the-session.png "job-submitted-successfully-in-the-session")

6.  On MRS Manager, click  **Services**  \>  **Yarn**.
7.  In the  **Yarn Summary**  area on the  **Service Status**  tab, click  **ResourceManager \(Active\)**  in  **ResourceManager Web UI**.
8.  Go to the native Yarn service page, find the application of the job, and click the application name to go to the job details page.
    -   If the job is not complete, click  **Tracking URL**  to go to the native Flink service page and view the job running information.
    -   If the job submitted in a session has been completed, you can click  **Tracking URL**  to log in to the native Flink service page to view job information.

        **Figure  4**  application<a name="fig1043856121716"></a>  
        ![](figures/application.png "application")



