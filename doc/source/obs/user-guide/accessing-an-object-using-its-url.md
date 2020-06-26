# Accessing an Object Using Its URL<a name="obs_03_0319"></a>

If you set the permission for an object to allow anonymous users to read it, anonymous users can access the object through the URL that you shared.

## Prerequisites<a name="section30275088154354"></a>

A read permission has been set for anonymous users. For details about how to set the permission, see  [Authorizing Access Permissions to Anonymous Users](authorizing-access-permissions-to-anonymous-users.md).

>![](/images/icon-note.gif) **NOTE:**   
>Encrypted objects cannot be shared.  

## Procedure<a name="section5800216"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Click the object to be shared. The object information is displayed on the top part of the page. The  **Link**  displays the shared link of the object. For details, see  [Figure 1](#fig36534596192426).

    Anonymous users can access the object by clicking the URL. The object URL is in the format of  **https://**_bucket name_._domain name_/_directory level_/_object name_. If the object resides in the root directory of the bucket, its URL does not contain the directory level.

    **Figure  1**  Object link<a name="fig36534596192426"></a>  
    ![](figures/object-link.png "object-link")

    >![](/images/icon-note.gif) **NOTE:**   
    >-   To allow anonymous users to access objects whose storage classes are  **Cold**  using the URL, ensure that the objects are in the  **Restored**  state.  
    >-   The method of using a browser to access objects varies depending on the object type. You can directly open  **.txt**  and  **.html**  files using a browser. However, when you open  **.exe**  and  **.dat**  files using a browser, the files are automatically downloaded to your local computer.  


