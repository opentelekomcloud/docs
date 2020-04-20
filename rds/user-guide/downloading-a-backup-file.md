# Downloading a Backup File<a name="en-us_topic_0044703401"></a>

## **Scenarios**<a name="sb7b1b629a51e4229a30150ae0d342811"></a>

This section describes how to  download a manual or an automated backup file  to a local device and restore data from the backup file.

RDS for MySQL enables you to download  full backup files.

## Procedure<a name="section134981429162111"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Backup Management**  page, locate the target backup to be downloaded and click  **Download**  in the  **Operation**  column.

    Alternatively, click the target DB instance. In the navigation pane on the left, choose  **Backups & Restorations**. On the  **Full Backups**  page, locate the target backup to be downloaded and click  **Download**  in the  **Operation**  column.

5.  In the displayed dialog box, select a method to download backup data.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the size of the backup data is greater than 400 MB, you are advised to use OBS Browser to download the backup data.  

    -   **Use OBS Browser**
        1.  Download OBS Browser
        2.  Decompress and install OBS Browser.
        3.  Log in to OBS Browser.

            For details about how to log in to OBS Browser, see section  [Logging In to OBS Browser](https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853477.html)  in the  _Object Storage Service User Guide_.

        4.  Disable certificate verification on OBS Browser.

            For details on how to configure OBS Browser, see section  [Configuring the System](https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853630.html)  in the  _Object Storage Service User Guide_.

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >The OBS bucket name displayed in the  **Download Backup File**  pane on the RDS console does not support certificate verification. Therefore, you need to disable OBS Browser certificate verification before adding the external bucket and then enable it after the backup file is downloaded.  

        5.  Add an external bucket.

            In the  **Create Bucket**  dialog box of OBS Browser, select  **Add external bucket**  and enter the bucket name displayed on  **Download the Backup File**  of the RDS console.

            For details about how to add external buckets, see section  [Adding External Buckets](https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853737.html)  in the  _Object Storage Service User Guide_.

        6.  Download the backup file.

            On the OBS Browser page, click the bucket that has been successfully added. In the search box on the right of OBS Browser, enter the backup file name displayed on  **Download the Backup File**  of the RDS console. In the search result, locate the target backup and download it.

        7.  After the backup file is downloaded, enable OBS Browser certificate verification.

    -   **Use Current Browser**

        Download the backup file directly from the current browser.

    -   **Use the URL**

        Click  ![](figures/copy_btn.png)  to copy the URL within the validity period to download backup data.

        A valid URL for downloading the backup data is displayed.

        -   You can use other download tools to download backup data.
        -   You can also run the wget command to download backup data.

            **wget -O**_FILE\_NAME_**--no-check-certificate"**_DOWNLOAD\_URL_**"**

            Variables in the commands are described as follows:

            **_FILE\_NAME_**: indicates the new backup file name after the download. The original backup file name may be too long and exceed the maximum characters allowed by the client file system. You are advised to add  **-O**  in the wget command to rename the backup file name.

            **_DOWNLOAD\_URL_**: indicates the path of the backup file to be downloaded.


6.  Follow the instructions provided in  [Restoring Data from MySQL Backup Files](restoring-data-from-mysql-backup-files.md)  to restore data locally as required.

