# Principal<a name="obs_03_0049"></a>

This parameter specifies users on whom the bucket policy takes effect, including accounts, federated users or federated user groups, and IAM users. Target users can be specified in either of the following ways:

-   **Include**: Specifies the user on whom the bucket policy statement takes effect.
-   **Exclude**: Specifies that on all users except the specified user the bucket policy statement takes effect.

## Cloud Service User<a name="section1896613422547"></a>

-   IAM users in the current account

    When the  **Principal**  is set to  **Current account**, you can select IAM users in the account, so that the bucket policy applies to the selected users.

-   Other account

    When the  **Principal**  is set to  **Other account**, you can enter the ID of other accounts. If you want to apply the bucket policy to IAM users in that account, you need to enter the user IDs, and use commas \(,\) to separate one from another.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >An authorized user can go to the  **My Credential**  page to obtain the domain ID and user ID after login.  
    >For  **Account ID**, input the  **Domain ID**  that can be found on the  **My Credential**  page.  

-   Anyone \(anonymous users\)

    To grant the bucket access permission to anyone, set the  **Principal**  to  **Other account**  and enter an asterisk \(\*\) as the account ID.

    >![](public_sys-resources/icon-caution.gif) **CAUTION:**   
    >Exercise caution when granting the bucket access permissions to anonymous users. If you grant the bucket access permission to anonymous users, anyone can access your bucket, and the traffic and storage fees generated will be borne by the bucket owner \(cloud service account\). You are advised to set restrictions on access requests. For example, you can allow the access request from only one IP address.  


## Federated User<a name="section1726117455582"></a>

The  **Principal**  of a bucket policy can also be a federated user or a federated user group.

