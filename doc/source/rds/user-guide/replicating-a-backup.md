# Replicating a Backup<a name="en-us_topic_0037000197"></a>

## **Scenarios**<a name="section4332314314536"></a>

This section describes how to  replicate a manual or an automated backup. The new backup must have a different name from that of the original backup.

**Constraints**

You can replicate backups and use them only in the same region.

**Backup Retention Policy**

-   RDS will delete automated backups when they expire or the DB instance for which the backups are created is deleted.
-   If you want to retain the automated backups for a long time, you can replicate them to generate manual backups, which will be always retained unless you delete them.
-   If storage space used for manual backups exceeds the default storage space, additional RDS storage costs may incur.

## Procedure<a name="section56693485162629"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance. On the  **Backups & Restorations**  page, locate the target backup to be replicated and click  **Replicate**  in the  **Operation**  column.

    Alternatively, choose  **Backup Management**. On the displayed page, locate the manual backup to be replicated and choose  **More**  \>  **Replicate**  or locate an automated backup and click  **Replicate**  in the  **Operation**  column.

5.  In the displayed dialog box, enter a new backup name and description and click  **OK**.
    -   The backup name must consist of 4 to 64 characters and start with a letter. It can contain only uppercase letters, lowercase letters, digits, hyphens \(-\), and underscores \(\_\).
    -   The description consists of a maximum of 256 characters and cannot contain the following special characters: \>!<"&'=

6.  After the new backup has been created, you can view and manage it on the  **Backup Management**  page.

