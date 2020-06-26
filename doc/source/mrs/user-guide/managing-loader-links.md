# Managing Loader Links<a name="EN-US_TOPIC_0125375692"></a>

## Scenario<a name="s89dbaa64490d4108a50a55d066930f7c"></a>

You can create, view, edit, and delete links on the Loader page.

## Prerequisites<a name="s15e2e305b2dd4dd7b9ac42c43bb9da86"></a>

You have accessed the Loader page. For details, see  [Loader Page](introduction_loader.md#s49ec1e4eeb254b4d97c98caf69fa110f).

## Creating a Link<a name="s4b59afa50f404ff7801cfce73104b66f"></a>

1.  On the Loader page, click  **Manage links**.
2.  Click  **New link**  and configure link parameters.

    For details about the parameters, see  [Loader Link Configuration](loader-link-configuration.md).

3.  Click  **Save**.

    If link configurations, for example, IP address, port, and access user information, are incorrect, the link will fail to be verified and saved. In addition, VPC configurations may affect the network connectivity.

    >![](/images/icon-note.gif) **NOTE:**   
    >You can click  **Test**  to immediately check whether the link is available.  


## Viewing a Link<a name="s70a1e37b7bbe4969a5c77491d1b36030"></a>

1.  On the Loader page, click  **Manage links**.
    -   If Kerberos authentication is enabled in the cluster, all links created by the current user are displayed by default and other users' links cannot be displayed.
    -   If Kerberos authentication is disabled in the cluster, all Loader links of the cluster are displayed.

2.  In the search box of the  **Sqoop Links**, enter a link name to filter the link.

## Editing a Link<a name="s27b4b94e73e445c7a9199fda3145329b"></a>

1.  On the Loader page, click  **Manage links**.
2.  Click the link name to go to the edit page.
3.  <a name="l854a0b37ca2246d790f35826c7138b5c"></a>Modify the link configuration parameters based on service requirements.
4.  Click  **Test**.

    If the test is successful, go to  [5](#lda73289aca3144fbaa3e338b4596e469). If OBS Server fails to be connected, repeat  [3](#l854a0b37ca2246d790f35826c7138b5c).

5.  <a name="lda73289aca3144fbaa3e338b4596e469"></a>Click  **Save**.

    If a Loader job has integrated into a Loader link, editing the link parameters may affect Loader running.


## Deleting a Link<a name="s0fd74a77e57e432d812218975dc9d092"></a>

1.  On the Loader page, click  **Manage links**.
2.  In the line of the link, click  **Delete**.
3.  In the dialog box, click  **Yes, delete it**.

    If a Loader job has been integrated into a Loader link, the deletion of the Loader link is not allowed.


