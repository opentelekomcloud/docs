# How Do I Create an Agency for Server Monitoring of the BMS?<a name="EN-US_TOPIC_0142827127"></a>

1.  On the management console homepage, choose  **Service List**  \>  **Management & Deployment**  \>  **Identity and Access Management**.
2.  In the navigation pane on the left, choose  **Agency**  and then click  **Create Agency**  in the upper right corner.
    -   **Agency Name**: Enter  **bms\_monitor\_agency**.
    -   **Agency Type**: Select  **Cloud service**.
    -   **Cloud Service**: This parameter is available if you select  **Cloud service**  for  **Agency Type**. Click  **Select**, select  **ECS BMS**  in the displayed  **Select Cloud Service**  dialog box, and click  **OK**.
    -   **Validity Period**: Select  **Permanent**.
    -   **Description**: This parameter is optional. You can enter  **"Support BMS server monitoring"**.
    -   **Permissions**: Locate the region where the BMS resides or the sub-project of the region and click  **Modify**  in the  **Operation**  column. In the displayed dialog box, enter  **CES**  in the  **Available Policies**  search box. Then select  **CES \(CES Administrator\)**  and click  **OK**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the BMS belongs to a sub-project, ensure that the sub-project has the CES Administrator permission.  


3.  Click  **OK**. 

    The operations to create an agency for server monitoring of the BMS are complete.


