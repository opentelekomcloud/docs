# Tags<a name="sfs_01_0043"></a>

This section describes how to add tags to existing file systems. You can also add tags when creating file systems. For details, see section  [4.2 Creating a File System](step-1-create-a-file-system.md).

Tags are used to identify and classify file systems. 

-   Tags are composed of key-value pairs.
    -   A tag key can contain a maximum of 36 characters and cannot be left blank. It can only contain letters, digits, hyphens \(-\), and underscores \(\_\).
    -   A tag value can contain a maximum of 43 characters and can be an empty string. It can only contain letters, digits, hyphens \(-\), and underscores \(\_\).

-   You can add a maximum of 10 tags to one file system.
-   The tag keys of the same file system must be unique.
-   Once created, the tag keys of the file system cannot be edited. You can only edit the tag values. You can delete tags.

## Procedure<a name="section177211557153613"></a>

1.  Log in to SFS Console.
2.  In the file system list, find the file system to which you want to add tags and click the name of it. The file system details page is displayed, as shown in  [Figure 1](#fig146683492144).

    **Figure  1**  Managing file system tags<a name="fig146683492144"></a>  
    ![](figures/managing-file-system-tags.png "managing-file-system-tags")

3.  Click the  **Tags**  tab.
4.  On the  **Tags**  tab page, click  **Add Tag**. The  **Add Tag**  dialog box is displayed.
5.  Add the key and value of the tag and click  **OK**.

    -   **Key**: This parameter is mandatory.
    -   **Value**: This parameter is optional.

    Return to the tag list, and you can see the tags you have just added. You can edit and delete the added tags.


