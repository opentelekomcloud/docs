# Setting the Bypassed Mode<a name="EN-US_TOPIC_0193630304"></a>

This section describes how to set the bypassed mode whereby requests are sent directly to the backend server without passing through WAF.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>In special scenarios such as testing, if services need to be restored to the state where the domain name is not connected to WAF, use the bypassed mode.  

## Prerequisites<a name="section1196116321023"></a>

-   Login credentials have been obtained.
-   **Mode**  of the protected domain name is  **Enabled**  or  **Disabled**.
-   Your web server does not use a proxy.

## Procedure<a name="section344311262515"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#en-us_topic_0193630191_fig1217125084313).

    **Figure  1**  Domain configuration<a name="en-us_topic_0193630191_fig1217125084313"></a>  
    ![](figures/domain-configuration.png "domain-configuration")

4.  In the  **Operation**  column of the target domain name, click  **Switch Mode**.
5.  In the dialog box displayed, select  **Bypassed**  and then click  **OK**.

