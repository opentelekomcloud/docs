# Exporting Services Logs<a name="EN-US_TOPIC_0125375522"></a>

## Scenario<a name="section41887183172434"></a>

Export the logs of each service role from MRS Manager.

## Prerequisites<a name="section39303053174421"></a>

-   You have obtained the Access Key ID \(AK\) and Secret Access Key \(SK\) for the corresponding account. For details, see the  _My Credential User Guide_. \(**My Credential \> How Do I Manage User Access keys \(AK/SK\)?**\)
-   You have created a bucket in the Object Storage Service \(OBS\) system for the corresponding account. For details, see the  _Object Storage Service User Guide_. \(**Object Storage Service \> Quick Start**  \>  **Common Operations Using OBS Console**  \>  **Creating a Bucket**\)

## Procedure<a name="section44391364172445"></a>

1.  On MRS Manager, click  **System**.
2.  Click  **Export Log** under **Maintenance**.
3.  Click  **Service**, set **Host**  to the IP address of the host where the service is deployed, and set **Start Time** and **End Time**.
4.  In  **Export to**, specify a path for saving logs. This parameter is available only for clusters with Kerberos authentication enabled.
    -   **Local PC**: stores logs in a local directory. If you select this option, go to [7](#li45613830172536).
    -   **OBS**: stores data in the OBS system and is used by default. If you select this option, go to [5](#li22688946162748).

5.  <a name="li22688946162748"></a>In  **OBS Path**, specify the path where service logs are stored in the OBS system.

    Fill in the full path. The path must not start with  **/**. You do not need to create the path in advance because the system creates it automatically. The full OBS path contains a maximum of 900 bytes.

6.  In  **Bucket Name**, enter the name of the created OBS bucket. In **AK** and **SK**, enter the Access Key ID and Secret Access Key for the account.
7.  <a name="li45613830172536"></a>Click  **OK**  to export logs.

