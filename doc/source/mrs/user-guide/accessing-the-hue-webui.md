# Accessing the Hue WebUI<a name="EN-US_TOPIC_0125375326"></a>

## Scenario<a name="sc597efbc2d094060ba8b5effcea1d96a"></a>

After Kerberos authentication is enabled and Hue is installed for an MRS cluster, users can use Hadoop and Hive on the Hue WebUI.

This section describes how to open the Hue WebUI on the MRS cluster supporting Kerberos authentication.

>![](/images/icon-note.gif) **NOTE:**   
>To access the Hue WebUI, you are advised to use a browser that is compatible with the Hue WebUI, for example, Google Chrome 50. The Internet Explorer may be incompatible with the Hue WebUI.  

## Impact on the System<a name="s6bd2144a33dc44f09d12402a373d8f96"></a>

Site trust must be added to the browser when you access MRS Manager and Hue WebUI for the first time. Otherwise, the Hue WebUI cannot be accessed.

## Prerequisites<a name="s8b325905abb54145949da9f84a209221"></a>

The MRS cluster administrator has assigned the permission for using Hive to the user. For details, see  [Creating a User](creating-a-user.md). For example, create **Human-machine** user **hueuser**, add the user to the **hive** group, and assign the user the **System\_administrator**  role.

## Procedure<a name="se5927081116d4ab9a5a36fcb3b27c2be"></a>

1.  Access MRS Manager.

    For details, see  [Accessing MRS Manager Supporting Kerberos Authentication](accessing-mrs-manager-supporting-kerberos-authentication.md).

2.  On MRS Manager, choose  **Service**  \>  **Hue**. In **Hue WebUI** of **Hue Summary**, click **Hue \(Active\)**. The Hue WebUI is opened.

    Hue WebUI provides the following functions:

    -   If Hive is installed in the MRS cluster, you can use  **Query Editors**  to execute query statements of Hive.
    -   If Hive is installed in the MRS cluster, you can use  **Data Browsers**  to manage Hive tables.
    -   If HDFS is installed in the MRS cluster, you can use  **File Browser**  to view directories and files in HDFS.
    -   If Yarn is installed in the MRS cluster, you can use  **Job Browser**  to view all jobs in the MRS cluster.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   After obtaining the URL for accessing the Hue WebUI, user can give the URL to other users who cannot access MRS Manager for accessing the Hue WebUI.  
    >-   If you perform operations on the Hue WebUI only but not on MRS Manager, you must enter the password of the current login user when accessing MRS Manager again.  


