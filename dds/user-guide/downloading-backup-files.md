# Downloading Backup Files<a name="en-us_topic_backup_download"></a>

## **Scenarios**<a name="en-us_topic_0060142340_section59211223171826"></a>

This section describes how to download manual or automated backup files for local data backup or restoration.

## Procedure<a name="section3831182116522"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  In the navigation pane on the left, click  **Backup Management**.
3.  On the  **Backup Management**  page, locate the available backup you want to download and click  **Download**  in the  **Operation**  column.
4.  Download  [OBS Browser](https://obs.otc.t-systems.com/obsbrowser/OBSBrowser.zip)  and install it.
5.  Log in to the OBS Browser.

    For details on how to log in to OBS Browser, see section  [Logging In to OBS Browser](https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853477.html)  in the  _Object Storage Service User Guide_.

6.  Disable certificate verification on OBS Browser.

    For details on how to configure OBS Browser, see section  [Configuring the System](https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853630.html)  in the  _Object Storage Service User Guide_.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The OBS bucket names displayed on the  **Download Backup File**  page on the DDS console do not support certificate verification. Therefore, you need to disable OBS Browser certificate verification before adding external buckets and enable it after the backup files are downloaded.  

7.  Add an external bucket.

    In the  **Create Bucket**  dialog box of OBS Browser, select  **Add external bucket**  and enter the bucket name displayed on  **Download Backup File**  of the DDS console.

    For details about how to add external buckets, see section  [Adding External Buckets](https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853737.html)  in the  _Object Storage Service User Guide_.

8.  Download the backup files.

    In the search box on the right of OBS Browser, enter the backup file name displayed on  **Download Backup File**  of the DDS console.

9.  After the backup file is downloaded, enable OBS Browser certificate verification.

