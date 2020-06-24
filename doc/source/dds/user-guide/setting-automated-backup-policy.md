# Setting Automated Backup Policy<a name="en-us_topic_backup_restore"></a>

## **Scenarios**<a name="section16563082183254"></a>

DDS backs up data automatically based on the automated backup policy you set. You are advised to regularly back up data in your database. If the database becomes faulty or data is damaged, you can restore it with the backup, ensuring data reliability.

>![](/images/icon-notice.gif) **NOTICE:**   
>-   DDS checks existing automated backup files. If the retention period of a file exceeds the backup retention period you set, DDS will delete the file.  
>-   After the backup policy is modified, an automated backup will be triggered based on the new backup policy. The retention period of the previously generated automated backups remains unchanged.  

-   Backup files are stored in OBS buckets.
-   When a DB instance is created, DDS enables the automated backup policy by default. The default settings of the parameters are as follows. You can modify them after a DB instance is created.
    -   Backups are retained for 7 days by default.
    -   The time window is in UTC by default.
    -   Data is backed up every day by default.


## Enabling or Modifying an Automated Backup Policy<a name="section553508110238"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target DB instance.
3.  In the navigation pane on the left, click  **Backups & Restorations**.
4.  On the  **Backups & Restorations**  page, click  **Modify Backup Policy**. If you want to enable the automated backup policy, click  ![](figures/icon-off.png). 

    Retention period refers to the number of days that data is kept. You can increase the retention period to improve data reliability.

    The backup retention period can range from 1 to 732 days, with a time window of one hour. The backup cycle varies according to the retention period you have set.

    -   If you set the retention period to 1 to 6 days, data is automatically backed up each day of the week.
    -   If you set the retention period to 7 to 732 days, you must select at least one day of the week for the backup cycle.

5.  Click  **OK**  to save the modification.
6.  View the backup result.
    -   If the automated backup policy is enabled, an automated full backup is immediately triggered. The time it takes to complete the backup depends on the size of the job. 
    -   If the automated backup policy is modified, an automated full backup is randomly triggered during the time window you set. The time it takes to complete the backup depends on the size of the job.
    -   During the creation of an automated backup, you can query the backup status on the  **Backup Management**  page or the  **Backups & Restorations**  tab. The backup status is  **Backing up**.
    -   In the upper right corner of the backup list, click  ![](figures/icon-fresh.png)  to refresh the list. The backup status changes to  **Complete**. The backup type is  **Automated**  and the backup method is  **Physical**.


## Disabling an Automated Backup Policy<a name="section5411044193812"></a>

>![](/images/icon-notice.gif) **NOTICE:**   
>Observe the following constraints when disabling the automated backup policy:  
>-   Your data cannot be backed up.  
>-   If you choose to delete all the existing automated backup when disabling the automated backup policy, related restoration or download operations will fail.  

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target DB instance.
3.  In the navigation pane on the left, click  **Backups & Restorations**.
4.  On the  **Backups & Restorations**  page, click  **Modify Backup Policy**. On the displayed page, click  ![](figures/icon-on.png)  to disable the automated backup policy. 

    You can determine whether to delete all automated backup files:

    -   If you do not select  **Delete automated backups**, all backup files within the retention period will be retained. You can manually delete them. For details, see section  [Deleting an Automated Backup](deleting-an-automated-backup.md).
    -   If you select  **Delete automated backups**, all backup files within the retention period will be deleted.

5.  Click  **OK**.

