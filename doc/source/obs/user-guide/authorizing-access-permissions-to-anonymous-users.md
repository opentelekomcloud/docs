# Authorizing Access Permissions to Anonymous Users<a name="obs_03_0132"></a>

An enterprise stores a large volume of map data in OBS, and offers the data for public query. This enterprise sets a read permission for anonymous users, and provides the data URLs on the Internet. Then all users can read or download the data through the URLs.

## Procedure<a name="section6287125010910"></a>

1.  Log in to OBS Console and click  **Create Bucket**  to create a bucket.
2.  In the bucket list, click the name of the newly created bucket. On the page that is displayed, click  **Objects**  in the pane on the left, and upload the map data as an object to the new bucket.
3.  Click the object to be operated and click  **Object ACL**.
4.  In  **Object ACL**  \>  **Public Permissions**  \>  **Anonymous User**, click  **Edit**  to set  **Access to Object**  to  **Read**. For details, see  [Figure 1](#fig58496641194012).

    **Figure  1**  Setting an object read permission for anonymous users<a name="fig58496641194012"></a>  
    ![](figures/setting-an-object-read-permission-for-anonymous-users.png "setting-an-object-read-permission-for-anonymous-users")

5.  Click  **Save**  to save the permission setting.

## Verification<a name="section228918509915"></a>

1.  Click the object. Its URL is displayed under  **Link**. Share the URL over the Internet, so that all users can access or download the object through the Internet.
2.  An anonymous user can view the object by copying the URL of the object to the web browser.

