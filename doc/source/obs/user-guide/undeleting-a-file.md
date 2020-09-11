# Undeleting a File<a name="en-us_topic_0066176932"></a>

## Scenarios<a name="section1428382164518"></a>

If a bucket has the  [versioning](versioning-overview.md)  function enabled, you can recover a deleted object through the  **Undelete**  operation.

## Background Information<a name="section1131791617239"></a>

**Object deletion mechanism when versioning is enabled**

When versioning is enabled, OBS uses different deletion methods for different objects.

-   Deleting a file or folder does not delete it permanently. The deleted file or folder will be retained in the  **Deleted Objects**  list and marked with the  **Delete Marker**.
    -   If you want to delete the file or folder permanently, you need to delete it from the  **Deleted Objects**  list. For details, see  [Deleting a File or Folder](deleting-a-file-(console).md).
    -   To recover a deleted file, you can cancel the deletion by the  **Undelete**  operation. For details, see  [Procedure](#section50464659154530)  in this section.

-   Deleting a version of an object will permanently delete that version. If the deleted version is the latest one, the next latest version becomes the latest version.

**Object recovery mechanism when versioning is enabled**

When a bucket has the versioning function enabled, deleting a file from the  **Objects**  list does not permanently delete it. The deleted file will be retained with the  **Delete Marker**  in the  **Deleted Objects**  list. You can recover a deleted object by the  **Undelete**  operation.

When performing the  **Undelete**  operation, note the following points:

1.  You can only undelete deleted files but not folders.

    After you undelete a deleted file, the file is recovered and will appear in the  **Objects**  list. Then you can perform basic operations on the file as you normally do on other objects. If the file was stored in a folder before the deletion, it will be recovered to its original path after you undelete it.

2.  Deleted files in the  **Deleted Objects**  also have multiple versions. When deleting different versions of files, note the following points:
    -   If you delete a version with the  **Delete Marker**, it actually recovers that specific version instead of permanently deleting it. For details, see  [Follow-up Procedure](#section27691114163422).
    -   If you delete a version without the  **Delete Marker**, that specific version is deleted permanently. Even if the object is recovered later, this version will not be recovered.

3.  At least one version without the  **Delete Marker**  exists in the  **Deleted Objects**  list. Otherwise, the deletion cannot be canceled.

## Prerequisites<a name="section64593482542"></a>

-   Versioning has been enabled for the bucket. For details about how to enable versioning, see  [Configuring Versioning](configuring-versioning.md).
-   The file to be recovered is in the  **Deleted Objects**  list, and at least one version without the  **Delete Marker**  exists.

## Procedure<a name="section50464659154530"></a>

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Click  **Deleted Objects**.
4.  In the row of the deleted object that you want to recover, click  **Undelete**  on the right.

    You can select multiple files and click  **Undelete**  above the object list to batch recover them.


## Follow-up Procedure<a name="section27691114163422"></a>

**Recover a file by deleting its version with the Delete Marker:**

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Click  **Deleted Objects**.
4.  Click the deleted file that you want to recover. The file information is displayed.
5.  On the  **Versions**  tab, view all versions of the file.
    -   If you delete a version with the  **Delete Marker**, the file is recovered and will appear in the  **Objects**  list.
    -   If you delete a version without the  **Delete Marker**, that version is permanently deleted.


