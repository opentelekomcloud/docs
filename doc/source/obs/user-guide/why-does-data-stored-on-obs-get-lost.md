# Why Does Data Stored on OBS Get Lost?<a name="obs_03_0138"></a>

-   Check whether a lifecycle rule is configured to automatically delete objects upon expiration date.
-   Check whether the write permission to the bucket has been assigned to other users. If yes, other users can delete objects from the bucket. If you have enabled the logging function, you can check the logs to find out the user who deleted the objects.

