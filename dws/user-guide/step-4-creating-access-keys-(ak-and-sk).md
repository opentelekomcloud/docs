# Step 4: Creating Access Keys \(AK and SK\)<a name="dws_01_0087"></a>

When users who have registered with the public cloud call APIs or use SDKs to access OBS, access keys \(AK/SK\) are required for identity authentication and request encryption. This mechanism ensures the confidentiality and integrity of a request, and the correctness of the identities of both parties.

Detailed explanations about Access Key ID \(AK\) and Secret Access Key \(SK\) are as follows:

-   An AK is an Access Key ID on OBS. One AK maps to only one user but one user can have multiple AKs. OBS recognizes users by their AKs.
-   An SK is the Secret Access Key on OBS, which is required as the key to access OBS. Users can generate authentication information based on SKs and request header fields. SKs and AKs are in one-to-one mapping.

In the following scenarios, if you want to connect to the DWS database through a client or a JDBC/ODBC application and access OBS, obtain the access keys \(AK and SK\) required for accessing OBS.

-   Concurrently Importing Data from OBS
-   Exporting Data to OBS in Parallel
-   Querying Data on OBS

    DWS provides the SQL on OBS feature to allow users to query data stored on OBS using  **SELECT**.



For details about the preceding features, see related sections in the  _Data Warehouse Service Database Developer Guide_.

## Creating Access Keys \(AK and SK\)<a name="section5520161143920"></a>

Before creating the AK/SK pair, ensure that your public cloud account \(used to log in to the management console\) has passed real-name authentication.

To create an AK and an SK on the OBS console, perform the following steps:

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  Click the username in the upper right corner and choose  **My Credential**  from the drop-down list.
3.  Click the  **Access Keys**  tab.

    If an AK/SK pair has been created on the  **Access Keys**  page, you can directly use it. However, you can view only  **Access Key ID**  on the  **Access Keys**  tab page. You can download the key file containing the AK and SK only when adding access keys. If you do not have the key file, click  **Add Access Key**  to create one.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Each user can create a maximum of two valid access keys. If two access keys exist, delete one of them and create a new one. To delete an access key, you need to enter the current login password and email address or SMS verification code. Deletion is successful only after the verification is passed.  
    >-   To ensure account security, change your AK/SK pairs periodically and keep them safe.  

4.  Click  **Add Access Key**.
5.  In the  **Add Access Key**  dialog box that is displayed, enter the password and the verification code and click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If you have not bound an email address or mobile phone number, enter only the password.  
    >-   If you have bound an email address and a mobile phone number, you can use either of them for verification.  

6.  In the  **Download Access Key**  dialog box that is displayed, click  **OK**  to save the access keys to default download path of your browser.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   To prevent the access key from being leaked, keep it secure.  
    >-   If you click  **Cancel**  in the dialog box, the AKs will not be downloaded, and you cannot download them later. In this case, re-create an AK.  

7.  Open the downloaded  **credentials.csv**  file to obtain the access keys \(AK and SK\).

## Precautions<a name="sdc9358e59c034ab2a09ee3440e8eca15"></a>

If you find that your AK/SK pair is abnormally used \(for example, the AK/SK pair is lost or leaked\) or will be no longer used, delete your AK/SK pair in the access key list or contact the administrator to reset your AK/SK pair.

When deleting the access keys, you need to enter the login password and either an email or mobile verification code.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Deleted AK/SK pairs cannot be restored.  

