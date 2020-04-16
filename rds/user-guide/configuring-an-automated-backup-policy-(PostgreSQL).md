# Configuring an Automated Backup Policy<a name="en-us_topic_pg_0029128206"></a>

## Scenarios<a name="en-us_topic_0192954006_section1554605854619"></a>

When you create a DB instance, an automated backup policy is enabled by default. You can also disable the policy after the DB instance is created. However, it is strongly recommended that you enable the automated backup policy for data restoration in production environment. After a DB instance is created, you can modify the automated backup policy as needed. RDS backs up data based on the automated backup policy you have set. 

RDS automatically backs up data at the DB instance level. If a database is faulty or data is damaged, you can restore it from backups to ensure data reliability. Backups are saved as packages in OBS buckets to ensure data confidentiality and durability. Since backing up data affects the database read and write performance, you are advised to enable automated backups during off-peak hours.

The default automated backup policy is as follows:

-   Retention period: 7 days
-   Time window: An hour within 24 hours, such as 01:00-02:00 or 12:00-13:00. The backup time is configured based on UTC time and is adjusted for daylight saving time, which changes at different times depending on the time zone.
-   Backup cycle: Each day of the week

## Enabling or Modifying an Automated Backup Policy<a name="en-us_topic_0192954006_section22744299173619"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  On the  **Backups & Restorations**  page, click  **Modify Backup Policy**. If you want to enable the automated backup policy, click  ![](figures/public.png). 
    -   **Retention Period**  refers to the number of days that your automated backups can be retained. Increasing the retention period will improve data reliability.
    -   If you shorten the retention period, the new backup policy takes effect for all backup files. The backup files that have expired will be deleted.
    -   The backup retention period indicates the number of days you want automated full and incremental backups of your DB instance to be retained. It ranges from 1–732 days. The backup time window is one hour. You are advised to select an off-peak time window for automated backups. By default, each day of the week is selected for  **Backup Cycle**  and you can change it. At least one day must be selected.

6.  Click  **OK**.

## Disabling the Automated Backup Policy<a name="en-us_topic_0192954006_section6125375132158"></a>

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Automated full and incremental backups are created based on the automated backup policy. Once the automated backup policy is disabled, automated backups are no longer created and all incremental backups are deleted immediately. Operations related to the incremental backups, including downloads, replications and restorations may fail.  

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  On the  **Backups & Restorations**  page, click  **Modify Backup Policy**. In the displayed dialog box, click  ![](figures/public.png)  to disable the automated backup policy. 

    You can determine whether to delete automated backups created in a specific period.

    -   If you do not select  **Delete automated backups**, all automated backups within the retention period will be retained.
    -   If you select  **Delete automated backups**, all automated backups within the retention period will be deleted. Operations related to the automated full backups, including downloads, replications, restorations, and rebuilds, may fail.

6.  Click  **OK**.

