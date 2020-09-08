# Modifying the Alarm Page<a name="waf_01_0094"></a>

If a visitor triggers block by WAF, the  **Default**  block page of WAF is returned by default. You can also configure  **Custom**  or  **Redirection**  for the block page to be returned as required.

-   **Custom**: The content of the text/html, text/xml, and application/json pages can be configured on the custom block page to be returned.
-   **Redirection**: The root domain name of the redirection address must be the same as the currently protected domain name, including a wildcard domain name. Examples:
    -   If the protected domain name is  **www.example.com**  and the port number is  **8080**, the redirection URL can be set to  **http://www.example.com:8080/error.html**.
    -   If the protected wildcard domain name is  **\*.example.com**  and the port number is  **8080**, the redirection URL can be set to  **http://\*.example.com:8080/error.html**.


## Prerequisites<a name="section5903171661012"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been added.

## Procedure<a name="section20611115122612"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  in the upper right corner of the page and choose  **Security**  \>  **Web Application Firewall**  \>  **Domains**.

    **Figure  1**  Entrance to  **Domains**<a name="waf_01_0093_fig1174417294716"></a>  
    ![](figures/entrance-to-domains.png "entrance-to-domains")

4.  In the  **Name**  column, click the target domain name to go to the basic information page.
5.  Click  ![](figures/icon-edit.png)  next to the template name in the row where  **Alarm Page**  locates.

    **Figure  2**  Modifying Alarm Page<a name="fig812323482919"></a>  
    ![](figures/modifying-alarm-page.png "modifying-alarm-page")

6.  In the  **Alarm Page**  dialog box, select a template in the  **Page Template**  field.
    -   If  **Default**  is selected for  **Page Template**, the block page with the built-in HTTP return code 418 is returned by default.

        **Figure  3**  Default alarm page<a name="fig68101714381"></a>  
        ![](figures/default-alarm-page.png "default-alarm-page")

    -   If  **Custom**  is selected for  **Page Template**, configure the parameters as needed.  [Table 1](#table292835123913)  describes the parameters.

        **Figure  4**  Custom alarm page<a name="fig1539442518417"></a>  
        ![](figures/custom-alarm-page.png "custom-alarm-page")

        **Table  1**  Parameters for the custom alarm page

        <a name="table292835123913"></a>
        <table><thead align="left"><tr id="row99363543912"><th class="cellrowborder" valign="top" width="25.1%" id="mcps1.2.3.1.1"><p id="p1993135173911"><a name="p1993135173911"></a><a name="p1993135173911"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="74.9%" id="mcps1.2.3.1.2"><p id="p17931335163911"><a name="p17931335163911"></a><a name="p17931335163911"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row393153518398"><td class="cellrowborder" valign="top" width="25.1%" headers="mcps1.2.3.1.1 "><p id="p1993535103916"><a name="p1993535103916"></a><a name="p1993535103916"></a>HTTP Return Code</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.9%" headers="mcps1.2.3.1.2 "><p id="p1527203518403"><a name="p1527203518403"></a><a name="p1527203518403"></a>Return code configured on a custom page</p>
        </td>
        </tr>
        <tr id="row79333533913"><td class="cellrowborder" valign="top" width="25.1%" headers="mcps1.2.3.1.1 "><p id="p109312352399"><a name="p109312352399"></a><a name="p109312352399"></a>Block Page Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.9%" headers="mcps1.2.3.1.2 "><p id="p09353543918"><a name="p09353543918"></a><a name="p09353543918"></a>The options are <strong id="b1564017280298"><a name="b1564017280298"></a><a name="b1564017280298"></a>text/html</strong>, <strong id="b13641152815295"><a name="b13641152815295"></a><a name="b13641152815295"></a>text/xml</strong>, and <strong id="b15641102852912"><a name="b15641102852912"></a><a name="b15641102852912"></a>application/json</strong>.</p>
        </td>
        </tr>
        <tr id="row1993143514399"><td class="cellrowborder" valign="top" width="25.1%" headers="mcps1.2.3.1.1 "><p id="p1593203517393"><a name="p1593203517393"></a><a name="p1593203517393"></a>Page Content</p>
        </td>
        <td class="cellrowborder" valign="top" width="74.9%" headers="mcps1.2.3.1.2 "><p id="p6931735163918"><a name="p6931735163918"></a><a name="p6931735163918"></a>Configure the page content based on the page type specified in <strong id="b1733203308"><a name="b1733203308"></a><a name="b1733203308"></a>Block Page Type</strong>.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   If  **Redirection**  is selected for  **Page Template**, configure the redirection URL as prompted.

        The root domain name of the redirection URL must be the same as the currently protected domain name, including a wildcard domain name. Examples:

        -   If the protected domain name is  **www.example.com**  and the port number is  **8080**, the redirection URL can be set to  **http://www.example.com:8080/error.html**.
        -   If the protected wildcard domain name is  **\*.example.com**  and the port number is  **8080**, the redirection URL can be set to  **http://\*.example.com:8080/error.html**.

        **Figure  5**  Redirection alarm page<a name="fig08821956121618"></a>  
        ![](figures/redirection-alarm-page.png "redirection-alarm-page")

7.  Click  **OK**.

