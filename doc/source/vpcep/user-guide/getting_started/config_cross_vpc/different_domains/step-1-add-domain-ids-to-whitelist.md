# Step 1: Add Domain IDs to Whitelist<a name="vpcep_02_02034"></a>

## Scenarios<a name="section18589131781412"></a>

This section describes how to obtain your own domain ID and add it to the whitelist of an existing VPC endpoint service in another domain.

## Prerequisites<a name="section1135143913517"></a>

The target VPC endpoint service already exists in the other domain.

## Obtain the Authorized Domain ID<a name="section6149132111515"></a>

1.  Log in to the management console.
2.  View the domain information in the upper right corner and choose  **My Credentials**.

    **Figure  1**  My Credentials<a name="fig1194755744"></a>  
    ![](/vpcep/user-guide/figures/my-credentials.png "my-credentials")

    The  **My Credentials**  page is displayed. You can view and record the domain ID.

    **Figure  2**  Domain ID<a name="fig14537232717"></a>  
    ![](/vpcep/user-guide/figures/domain-id.png "domain-id")


## Add an Authorized Domain ID to the Whitelist of a VPC Endpoint Service<a name="section19390104303219"></a>

1.  Log in to the management console.
2.  Click  ![](/vpcep/user-guide/figures/icon-region.png)  in the upper left corner and select the desired region and project.

1.  Click  **Service List**  and choose  **VPC Endpoint**  under  **Network**.

1.  In the navigation pane on the left, choose  **VPC Endpoint**  \>  **VPC Endpoint Services**.
2.  On the displayed page, click the name of the VPC endpoint service for which a whitelist record will be added.
3.  On the displayed page, select the  **Permission Management**  tab and click  **Add to Whitelist**.
4.  On the displayed page, enter the authorized domain ID as prompted.

    **Figure  3**  Add to Whitelist<a name="fig5958154114813"></a>  
    ![](/vpcep/user-guide/figures/add-to-whitelist.png "add-to-whitelist")

5.  Click  **OK**.

    >![](/images/icon-note.gif) **NOTE:** 
    >-   Your domain is in the whitelist of your own VPC endpoint service by default.
    >-   The authorized domain ID is in the  **iam:domain::domain\_id**  format, for example,  **iam:domain::1564ec50ef2a47c791ea5536353ed4b9**
    >-   Adding  **\***  to the whitelist means that all users can access the VPC endpoint service.


