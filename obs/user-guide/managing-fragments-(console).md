# Managing Fragments<a name="en-us_topic_0045853514"></a>

## Background Information<a name="section30580753"></a>

Fragments are generated when multipart upload tasks fail. Such failures generally occur in the following scenarios:

-   The network is in poor condition, and the connection to the OBS server is interrupted frequently.
-   The upload task is manually suspended.
-   The device is faulty.
-   The device is powered off suddenly.

On OBS Console, storage used by fragments is charged. Clear fragments when they are not needed. If a file upload task fails, upload the file again.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Fragments on OBS consume storage spaces that are charged according to price rates of storage space.  

## Procedure<a name="section6791328"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the navigation pane on the left, click  **Objects**.
3.  Click  **Fragments**, select the fragment that you want to delete, and then click  **Delete**  on the right of the fragment.

    You can also select multiple fragments and click  **Delete**  on the top of fragment list to batch delete them.

4.  Click  **Yes**  to confirm the deletion.

