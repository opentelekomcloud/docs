# HTTP Redirection to HTTPS<a name="EN-US_TOPIC_0138592367"></a>

## Scenarios<a name="section10243515132111"></a>

HTTPS is an extension of HTTP. HTTPS enables data between a web server and a browser to be encrypted. Redirection allows you to redirect requests from HTTP to HTTPS.

After redirection is enabled, all HTTP requests to access your website are transmitted over HTTPS connections, improving service security.

Currently, only enhanced load balancers support this function.

## Prerequisites<a name="section87044214500"></a>

-   An HTTPS listener has been added.
-   An HTTP listener has been added.

## Create a Redirect<a name="section0460104412272"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0138671519.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Listeners**, locate the target HTTP listener, and click its name.
6.  Click  **Redirects**  and then  **Create**  on the right.

    **Table  1**  Parameters for configuring redirection

    <a name="table5765638104311"></a>
    <table><thead align="left"><tr id="row16766173884314"><th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.4.1.1"><p id="p16337205034318"><a name="p16337205034318"></a><a name="p16337205034318"></a><strong id="b129781819155518"><a name="b129781819155518"></a><a name="b129781819155518"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.2.4.1.2"><p id="p2033814509436"><a name="p2033814509436"></a><a name="p2033814509436"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.2.4.1.3"><p id="p9339165064318"><a name="p9339165064318"></a><a name="p9339165064318"></a><strong id="b842352706194150"><a name="b842352706194150"></a><a name="b842352706194150"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37661383435"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.1 "><p id="p133414501436"><a name="p133414501436"></a><a name="p133414501436"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.2 "><p id="p73421750174316"><a name="p73421750174316"></a><a name="p73421750174316"></a>Specifies the redirect name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p143171818484"><a name="p143171818484"></a><a name="p143171818484"></a>redirect-g8h9</p>
    </td>
    </tr>
    <tr id="row9766113813431"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.1 "><p id="p19345250184318"><a name="p19345250184318"></a><a name="p19345250184318"></a>Redirected To</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.2 "><p id="p3347150204315"><a name="p3347150204315"></a><a name="p3347150204315"></a>Specifies the HTTPS listener to which requests are redirected.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p85582571488"><a name="p85582571488"></a><a name="p85582571488"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1176663812438"><td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.4.1.1 "><p id="p16350450104312"><a name="p16350450104312"></a><a name="p16350450104312"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.2.4.1.2 "><p id="p935219504434"><a name="p935219504434"></a><a name="p935219504434"></a>Provides supplementary information about the redirect.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p9352155014316"><a name="p9352155014316"></a><a name="p9352155014316"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If requests to an HTTP listener are redirected, its configuration becomes invalid except for access control.  


## Modify a Redirect<a name="section143162510568"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0146400364.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Listeners**, locate the target HTTP listener, and click its name.
6.  Click  **Redirects**, locate the target redirect, and click  **Modify**  in the  **Operation**  column.
7.  In the  **Modify Redirect**  dialog box, modify the redirect name or description, or select another listener to be redirected to, and click  **OK**.

## Delete a Redirect<a name="section4978153735217"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0138671515.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Listeners**, locate the target listener, and click its name.
6.  Click  **Redirects**, locate the target redirect, and click  **Delete**  in the  **Operation**  column.
7.  In the  **Delete Redirect**  dialog box, click  **Yes**.

