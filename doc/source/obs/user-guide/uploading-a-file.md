# Uploading a File<a name="en-us_topic_0045853663"></a>

This section describes how to upload local files to OBS over the Internet. These files can be texts, images, videos, or any other type of files.

## Restrictions and Limitations<a name="section37191890113846"></a>

-   You can upload a file of up to 50 MB using OBS Console.
-   You cannot batch upload files through OBS Console. If you need to upload multiple files at a time, it is recommended that you use OBS clients, APIs, SDKs, or third-party tools \(for example,  [S3cmd](https://docs.otc.t-systems.com/en-us/ugs3cmd/obs/en-us_topic_0051518473.html)\) to upload.
-   If versioning is disabled and the name of a newly uploaded file is the same as that of a file in the bucket, the newly uploaded file automatically overwrites the existing file and does not retain the ACL information of the existing file. If the name of the newly uploaded folder is the same as that of a folder in the bucket, the two folders will be merged, and files in the new folder will overwrite namesake files in the old folder.
-   If versioning is enabled and the name of a newly uploaded file is the same as that of a file in the bucket, a new version is added to the existing file. For details about versioning, see  [Versioning Overview](versioning-overview.md).

## Prerequisites<a name="section1750515815466"></a>

-   At least one bucket has been created.
-   If you want to classify files, you can create folders and upload files to different folders. For details about how to create a folder, see  [Creating a Folder](creating-a-folder-(console).md)

## Procedure<a name="section64292661113931"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Go to the folder to which objects are uploaded. Click  **Upload Object**. The  **Upload Object**  dialog box is displayed.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the files to be uploaded to OBS are stored in Microsoft OneDrive, it is recommended that the names of these files contain a maximum of 32 characters.  

    **Figure  1**  Uploading objects<a name="obs_03_0307_fig188654349118"></a>  
    ![](figures/uploading-objects.png "uploading-objects")

4.  Click  ![](figures/icon-more.png)  to open the local file browser dialog box.
5.  Select the file that you want to upload and click  **Open**.
6.  Select a storage class. If no storage class is selected, the file will inherit the storage class of the bucket.
7.  **Optional**: Select KMS encryption to encrypt the uploaded file. For details, see  [Uploading a File with Server-Side Encryption](uploading-a-file-with-server-side-encryption-(console).md).
8.  Click  **Upload**.

## Related Operations<a name="section2680481145652"></a>

You can specify its storage class when uploading an object or change its storage class after the object is uploaded. The procedure is as follows:

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Select the target object and choose  **More**  \>  **Change Storage Class**  on the right.
4.  Select the desired storage class and click  **OK**.

>![](/images/icon-note.gif) **NOTE:**   
>-   Objects can be changed from the  **Standard**  storage class to  **Warm**  or  **Cold**  storage class. Objects can be changed from the  **Warm**  storage class to  **Standard**  or  **Cold**  storage class. Objects of the  **Cold**  storage class must be restored before being changed to  **Standard**  or  **Warm**  storage class. The latter two changes incur penalty and restoration fees. Determine an appropriate change path based on your actual needs.  
>-   When the storage class is changed to Cold, the object restoration status changes to  **Unrestored**.  
>-   You can also configure a lifecycle rule to change the storage class of an object. For details, see  [Lifecycle Management Overview](lifecycle-management-overview-(console).md).  

## Follow-up Procedure<a name="section6158112111499"></a>

You can click  **Copy Path**  on the right of an object to copy the path of the object.

You can share the path with other users. Then they open the bucket where the object is stored and enter the path in the search box to find the object.

