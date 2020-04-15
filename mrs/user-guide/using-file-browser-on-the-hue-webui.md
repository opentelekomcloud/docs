# Using File Browser on the Hue WebUI<a name="EN-US_TOPIC_0125375467"></a>

## Scenario<a name="sa47e6f20ae8a4ac4adbcfbbe5aaedca1"></a>

After Kerberos authentication is enabled for an MRS cluster, users can use the Hue WebUI to manage files in HDFS.

## Prerequisites<a name="s8996367bf0df412ba01b4ee0842955af"></a>

An MRS cluster administrator has granted users with permission to view, create, modify, and delete files in HDFS. For details, see  [Creating a User](creating-a-user.md).

## Accessing  **File Browser**<a name="section30320920173825"></a>

1.  Access the Hue WebUI and click  **File Browser**.
2.  You can view the home directory of the current login user.

    On the  **File Browser**  page, the following information about subdirectories or files in the directory is displayed.

    **Table  1**  HDFS file attributes

    <a name="table9337634173829"></a>
    <table><thead align="left"><tr id="row6132691173829"><th class="cellrowborder" valign="top" width="30.259999999999998%" id="mcps1.2.3.1.1"><p id="p24549216173829"><a name="p24549216173829"></a><a name="p24549216173829"></a>Attribute</p>
    </th>
    <th class="cellrowborder" valign="top" width="69.74000000000001%" id="mcps1.2.3.1.2"><p id="p42329441173829"><a name="p42329441173829"></a><a name="p42329441173829"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60479164173829"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p41546955173829"><a name="p41546955173829"></a><a name="p41546955173829"></a><span class="parmname" id="parmname26985949173829"><a name="parmname26985949173829"></a><a name="parmname26985949173829"></a><b>Name</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p9860205173829"><a name="p9860205173829"></a><a name="p9860205173829"></a>Name of a directory or file</p>
    </td>
    </tr>
    <tr id="row55413571173829"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p66974111173829"><a name="p66974111173829"></a><a name="p66974111173829"></a><span class="parmname" id="parmname7441567173829"><a name="parmname7441567173829"></a><a name="parmname7441567173829"></a><b>Size</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p56193919173829"><a name="p56193919173829"></a><a name="p56193919173829"></a>File size</p>
    </td>
    </tr>
    <tr id="row63666810173829"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p59314260173829"><a name="p59314260173829"></a><a name="p59314260173829"></a><span class="parmname" id="parmname28960094173829"><a name="parmname28960094173829"></a><a name="parmname28960094173829"></a><b>User</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p39725721173829"><a name="p39725721173829"></a><a name="p39725721173829"></a>Owner of a directory or file</p>
    </td>
    </tr>
    <tr id="row5261146173829"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p56738017173829"><a name="p56738017173829"></a><a name="p56738017173829"></a><span class="parmname" id="parmname36130385173829"><a name="parmname36130385173829"></a><a name="parmname36130385173829"></a><b>Group</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p32376627173829"><a name="p32376627173829"></a><a name="p32376627173829"></a>Group of a directory or file</p>
    </td>
    </tr>
    <tr id="row32539995173829"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p23499710173829"><a name="p23499710173829"></a><a name="p23499710173829"></a><span class="parmname" id="parmname47350321173829"><a name="parmname47350321173829"></a><a name="parmname47350321173829"></a><b>Permissions</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p24428358173829"><a name="p24428358173829"></a><a name="p24428358173829"></a>Permission of a directory or file</p>
    </td>
    </tr>
    <tr id="row5812340173829"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p18493924173829"><a name="p18493924173829"></a><a name="p18493924173829"></a><span class="parmname" id="parmname24424501173829"><a name="parmname24424501173829"></a><a name="parmname24424501173829"></a><b>Date</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p21612874173829"><a name="p21612874173829"></a><a name="p21612874173829"></a>Time when a directory or file is created</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  In the search box, enter a keyword. The system automatically searches directories or files in the current directory.
4.  Clear the search box. The system displays all directories or files.

## Performing Operations<a name="section27925330173837"></a>

1.  On  **File Browser**, select one or more directories or files.
2.  Click  **Actions**. On the menu that is displayed, select an operation.
    -   **Rename**: renames a directory or file.
    -   **Move**: moves a file. In **Move to**, select a new directory and click **Move**.
    -   **Copy**: copies the selected files or directories.
    -   **Download**: downloads the selected files. Directories are not supported.
    -   **Change permissions**: changes permission to access the selected directory or file.
        -   You can grant the owner, the group, or other users with the  **Read**, **Write**, and **Execute**  permission.
        -   **Sticky**  indicates that only HDFS administrators, directory owners, and file owners can delete or move files in the directory.
        -   **Recursive**  indicates that permission is granted to subdirectories recursively.

    -   **Storage policies**: sets the policies for storing files or directories in HDFS.
    -   **Summary**: views HDFS storage information about the selected file or directory.


## Deleting Directories or Files<a name="section23049141173846"></a>

1.  On  **File Browser**, select one or more directories or files.
2.  Click  **Move to trash**. In **Confirm Delete**, click **Yes**  to move them to the recycle bin.

    If you want to directly delete the files without moving them to the recycle bin, click  ![](figures/en-us_image_0125375452.jpg) and select **Delete forever**. In **Confirm Delete**, click **Yes**  to confirm the operation.


## Accessing Other Directories<a name="section61809860173857"></a>

1.  Click the directory name, type a full path you want to access, for example,  **/mr-history/tmp**, and press **Enter.**

    The current user must have permission to access other directories.

2.  Click  **Home**  to go to the home directory.
3.  Click  **History**. The history records of directory access are displayed and the directories can be accessed again.
4.  Click  **Trash**  to access the recycle bin of the current directory.

    Click  **Empty trash**  to clean up the recycle bin.


## Uploading User Files<a name="section1394825217396"></a>

1.  On  **File Browser**, click **Upload**.
2.  Select an operation.
    -   **Files**: uploads user files to the current user.
    -   **Zip/Tgz/Bz2 file**: uploads a compressed file. In the dialog box that is displayed, click **Zip, Tgz or Bz2 file** to select the compressed file to be uploaded. The system automatically decompresses the file in HDFS. Compressed files in **ZIP**, **TGZ**, and **BZ2**  formats are supported.


## Creating a New File or Directory<a name="section47635052173915"></a>

1.  On  **File Browser**, click **New**.
2.  Select an operation.
    -   **File**: creates a file. Enter a file name and click **Create**.
    -   **Directory**: creates a directory. Enter a directory name and click **Create**.


