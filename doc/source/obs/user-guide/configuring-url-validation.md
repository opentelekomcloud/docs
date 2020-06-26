# Configuring URL Validation<a name="obs_03_0341"></a>

OBS blocks access requests from blacklisted URLs and allows those from whitelisted URLs.

## Prerequisites<a name="section48948668114148"></a>

Static website hosting has been enabled.

## Procedure<a name="section6430701414453"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the  **Basic Configurations**  area, click the  **URL Validation**  label. The  **URL Validation**  page is displayed.

    Alternatively, you can choose  **Basic Configurations**  \>  **URL Validation**  in the navigation pane on the left.

3.  Click  ![](figures/icon-edit.png)  next to the text box of  **Whitelisted Referers**  or  **Blacklisted Referers**, and enter the referers.

    The following describes the principles for setting  **Referers**:

    -   The length of a whitelist or blacklist cannot exceed 1024 characters.
    -   You can enter multiple referers. Use a line break to separate one from another.
    -   When  **Whitelisted Referers**  is empty but  **Blacklisted Referers**  is not, all websites except specified ones in the blacklist are allowed to access data in the target bucket.
    -   When  **Whitelisted Referers**  is not empty and  **Blacklisted Referers**  is empty or not empty, only specified websites in the whitelist are allowed to access data in the target bucket.

    >![](/images/icon-note.gif) **NOTE:**   
    >When  **Whitelisted Referers**  is the same as  **Blacklisted Referers**, the blacklist takes effect. For example, if the fields of both  **Whitelisted Referers**  and  **Blacklisted Referers**  are set to  **www.example.com**, the access request from  **www.example.com**  is blocked.  

    -   When  **Whitelisted Referers**  and  **Blacklisted Referers**  are empty, all websites are allowed to access data in the target bucket by default.
    -   Before determining whether a user has the four types of permissions \(**Read**,  **Write**,  **ACL View**, and  **ACL Edit**\) for a bucket or objects in the bucket, check whether the user complies with the URL validation principles of the  **Referers**  field.

4.  Click  ![](figures/icon-ok.png)  to save the settings.

