# Managing Fragments<a name="en-us_topic_0045853710"></a>

## Background Information<a name="se3f4c5059d9b4121bf14b13aa64c29db"></a>

Because OBS uploads data in the multipart mode, fragments may be generated due to any of the following data upload failures \(but not limited to these failures\):

-   The network is in poor condition, and the connection to the OBS server is interrupted frequently.
-   The upload task is manually interrupted.
-   The device is faulty.
-   The device is powered off suddenly.

If a file fails to be uploaded or the upload task is suspended, fragments are generated and stored in OBS. You can resume the upload through task management. After the resumable upload completes, the fragments will be cleared automatically.

You can also use the fragment management function to clear fragments. If you resume an upload task after clearing the fragments, the upload progress will be lost and the task needs to be re-uploaded.

>![](public_sys-resources/icon-notice.gif) **NOTICE:** 
>The fragment storage in OBS is billed.

## Procedure<a name="s19685a34959d4e409918327070cd8f12"></a>

1.  Log in to OBS Browser.
2.  Click the blank area in the row of the bucket and choose  **More**  \>  **Manage Fragment**.
3.  In the  **Manage Fragment**  dialog box, click  **Check**  to refresh the fragment list. Select a fragment and click  ![](figures/icon-delete-1.png)  on the right to delete it.

    You can click  **Delete All**  above the fragment list to delete all the fragments.

4.  In the dialog box that is displayed, confirm the information and click  **Yes**.
5.  In the displayed dialog box, click  **Close**  to close the dialog box.
6.  In the  **Manage Fragment**  dialog box, click  **Close**  to close the dialog box and return to the OBS Browser home page.

