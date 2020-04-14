# Creating a Folder<a name="obs_03_0316"></a>

This section describes how to create a folder on OBS Console. Folders facilitate data management in OBS.

## Background Information<a name="section53108166"></a>

-   Unlike a file system, OBS does not involve the concepts of file and folder. For easy data management, OBS provides a method to simulate folders. In OBS, an object is simulated as a folder by adding a slash \(/\) to the end of the object name on OBS Console. When objects are listed by calling the API, the obtained object name is the path of the object, and the content following the last slash \(/\) is the actual object name. If the path ends with a slash \(/\), it indicates that the object is a folder. The hierarchical depth of the object does not affect the performance of accessing the object.
-   OBS Console does not support the download of folders. You can use OBS Browser to download folders.

## Procedure<a name="section8211449"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Click  **Create Folder**, or click a folder in the object list to open it, and then click  **Create Folder**.
4.  In the  **Folder Name**  text box, enter a name for the folder.
    -   You can create single-level or multi-level folders.
    -   The name cannot contain the following special characters:  **\\:\*?"<\>|**
    -   The name cannot start or end with a period \(.\) or slash \(/\).
    -   The absolute path of the folder cannot exceed 1023 characters.
    -   Any single slash \(/\) separates and creates multiple levels of folders at once.
    -   Cannot contain two or more adjacent slashes \(/\).

5.  Click  **OK**.

## Follow-up Procedure<a name="section184966221382"></a>

You can click  **Copy Path**  next to a folder to copy the path of the folder. You can share the path with other users. Then they open the bucket where the object is stored and enter the path in the search box to find the object.

