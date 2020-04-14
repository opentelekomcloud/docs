# Applying a Policy to Your Domain Names<a name="EN-US_TOPIC_0193630199"></a>

This section describes how to apply a policy to your domain names.

## Prerequisites<a name="section19405123413428"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section109781412104317"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Policies**. The  **Policies**  page is displayed.
4.  In the row containing the target policy name, click  **Bind Domain**  in the  **Operation**  column. See  [Figure 1](#fig169858225460).

    **Figure  1**  Bind Domain<a name="fig169858225460"></a>  
    ![](figures/bind-domain.png "bind-domain")

5.  Select one or more domain names from the  **Domain Name**  drop-down list. See  [Figure 2](#fig4167335513).

    To view information about all domain names, click  **View Domains**.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >-   A protected domain name can use only one policy, but one policy can be applied to multiple domain names.  
    >-   To delete a policy bound to domain names, bind these domain names to other policies, and click  **Delete**  in the  **Operation**  column of the target policy name.  

    **Figure  2**  Selecting one or more domain names<a name="fig4167335513"></a>  
    ![](figures/selecting-one-or-more-domain-names.png "selecting-one-or-more-domain-names")

6.  Click  **OK**.

