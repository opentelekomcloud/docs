# Tasks Are Not Displayed in the Task List When Objects Are Managed Using OBS Browser<a name="obs_03_0443"></a>

## **Question**<a name="scb49866c61fe45fc8458e96e2177af65"></a>

Why are the tasks not displayed in the task list when objects are being uploaded, downloaded, or deleted using OBS Browser?

## **Answer**<a name="s55244099d14b452baabd78f1ce9acdee"></a>

When OBS Browser is used to upload, download, or delete objects, the internal database of OBS Browser is invoked. By default, binary data generated while the database is running is saved in the personal folder of the Windows operating system user.

If the username of the Windows operating system contains non-letter characters, the internal database of OBS Browser cannot identify the save path of data. As a result, upload, download, and deletion tasks cannot be added to the task list. In such a scenario, perform the following operations to specify the save path of the binary data generated while the internal database is running.

1.  In the folder of the OBS Browser installation package, open file  **package.json**.
2.  Add parameter  **dbpath**  after the open brace \(\{\) in the first line in the following format:

    "dbpath":"_Path where data is saved_",

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >The save path of data is user-defined. The folder name complies with the following rules:
    >-   Cannot contain non-letter characters.
    >-   Cannot contain the following special characters:  **\\:/\*?"<\>|**
    >-   Cannot start or end with a period \(.\).
    >If the specified path does not exist, the system will automatically create one. Folders are separated by slashes \(/\) in a multi-level directory. For example, data is saved in the  **obs\\data**  directory in the  **E**  drive. Then, the save path is set to  **E:/obs/data**_._

    >![](public_sys-resources/icon-notice.gif) **NOTICE:** 
    >File  **package.json**  contains configuration information needed by OBS Browser. Do not change the file content unless necessary. Otherwise, OBS Browser is not available.

3.  Save the file and restart OBS Browser.

