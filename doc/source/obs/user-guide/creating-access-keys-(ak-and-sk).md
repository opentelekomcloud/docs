# Creating Access Keys \(AK and SK\)<a name="obs_03_0405"></a>

This section describes how to create access keys \(AK and SK\) in OBS Console. A pair of AK and SK is used to encrypt the signature of a request, ensuring that the request is secure and integral, and that identities of the request sender and receiver are correct.

## Background Information<a name="s6eee9c5cf28244198d6c28ef50ce2276"></a>

AKs and SKs support the authentication mechanism of Identity and Access Management \(IAM\).

-   An Access Key ID \(AK\) defines a user that accesses the OBS system. An AK belongs to only one user, but one user can have multiple AKs. The OBS system recognizes the users who access the system by their AKs.
-   A Secret Access Key \(SK\) is the key used by users to access OBS. It is the authentication information generated based on the AK and the request header. An SK and an AK group into a pair of access keys.

## Restrictions and Limitations<a name="section64691490143136"></a>

Each user can create up to two valid AK/SK pairs.

## Prerequisites<a name="section37631452155356"></a>

An account has been registered and activated.

## Procedure<a name="section7940153915437"></a>

1.  Log in to OBS Console.
2.  On the top navigation menu, click the username and select  **My Credential**.
3.  **My Credential**  page is displayed. Choose  **Access Keys**  \>  **Add Access Key**

    >![](/images/icon-note.gif) **NOTE:**   
    >Each user can create a maximum of two valid access keys.  

4.  In the  **Add Access Key**  dialog box that is displayed, enter the password and its verification code.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If you have not bound an email address or mobile number, enter only the password.  
    >-   If you have bound an email address and a mobile number, you can verify through either one.  

5.  Click  **OK**.
6.  Save the key as prompted. The key is directly saved to the default download folder of the web browser.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   To prevent the access keys from being leaked, keep them secure. If you click  **Cancel**  in the dialog box, the access keys will not be downloaded, and you cannot download them later. You can re-create an access key if you need to use it.  
    >-   The access keys \(AK and SK\) need to be updated regularly.  

7.  Open the downloaded  **credentials.csv**  file to obtain the access keys \(AK and SK\).

