# Deleting a File or Folder<a name="en-us_topic_0045853756"></a>

## Scenarios<a name="section13666357124317"></a>

On OBS Console, you can delete unneeded files or folders to release space and reduce costs.

This topic describes how to manually delete files or folders on OBS Console.

OBS also provides the lifecycle management function to meet your requirements for periodically and automatically deleting files from a bucket or clearing all files and folders in a bucket. For details, see  [Lifecycle Management Overview](lifecycle-management-overview-(console).md).

## Background Information<a name="section4474995017112"></a>

**Object deletion philosophy when versioning is enabled**

OBS adopts different deletion methods for different objects when versioning is enabled.

-   Deleting a file or folder does not delete it permanently. The deleted file or folder will be retained in the  **Deleted Objects**  list and marked with the  **Delete Marker**.
    -   If you want to delete the file or folder permanently, you need to delete it from the  **Deleted Objects**  list. For details, see  [Procedure](#section56466209)  in this section.
    -   To recover a deleted file, you can cancel the deletion by the  **Undelete**  operation. For details, see  [Undeleting a File](undeleting-a-file.md).

-   Deleting a version of an object will permanently delete that version. If the deleted version is the latest one, the next latest version becomes the latest version.

## Procedure<a name="section56466209"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Select the file or folder you want to delete, and choose  **More**  \>  **Delete**  on the right.

    You can select multiple files or folders and click  **Delete**  above the object list to batch delete them.

4.  Click  **Yes**  to confirm the deletion.
5.  If versioning is enabled for the bucket, you need to further delete files or folders in the  **Deleted Objects**  list in order to permanently delete them.
    1.  Click  **Deleted Objects**.
    2.  In the  **Operation**  column of the file or folder to be deleted, click  **Delete**.

        You can select multiple files or folders and click  **Delete**  above the object list to batch delete them.



## Follow-up Procedure<a name="section089519314196"></a>

When versioning is enabled, files in the  **Deleted Objects**  list also have multiple versions. Note the following points when deleting different versions of files:

-   If you delete a version with the  **Delete Marker**, it actually recovers that specific version instead of permanently deleting it. For details, see  [Undeleting a File](undeleting-a-file.md).
-   If you delete a version without the  **Delete Marker**, that specific version is deleted permanently. Even if the object is recovered later, this version will not be recovered.

