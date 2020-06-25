# What Are the Constraints of Using LTS?<a name="lts_01_0031"></a>

-   You can create a maximum of 100 log groups.
-   You can create a maximum of 100 log topics under a log group.
-   Logs reported to LTS can be stored for seven days and any logs stored longer than the retention period will be automatically deleted if they are not transferred to an OBS bucket.
-   The maximum size of a single log record is 127 KB, and any content exceeding the limit will be deleted.

    >![](/images/icon-note.gif) **NOTE:**   
    >The quota for each user to upload compressed logs every day is 500 MB. If the system displays a message indicating that the quota is insufficient, contact customer service.  


