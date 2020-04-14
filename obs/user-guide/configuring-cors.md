# Configuring CORS<a name="en-us_topic_0066036542"></a>

This section describes how to use CORS in HTML5 to implement cross-origin access.

## Prerequisites<a name="section48948668114148"></a>

Static website hosting has been configured. For details about how to configure static website hosting, see  [Configuring Static Website Hosting](configuring-static-website-hosting.md).

## Procedure<a name="section54298028"></a>

1.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
2.  In the  **Basic Configurations**  area, click the  **CORS Rules**  label. The  **CORS Rules**  page is displayed.

    Alternatively, you can choose  **Basic Configurations**  \>  **CORS Rules**  in the navigation pane on the left.

3.  Click  **Create**. The  **Create CORS Rule**  dialog box is displayed. See  [Figure 1](#fig2425430173411)  for details.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can set a maximum of 100 CORS rules for one bucket.  

    **Figure  1**  Creating a CORS rule<a name="fig2425430173411"></a>  
    ![](figures/creating-a-cors-rule.png "creating-a-cors-rule")

4.  In the  **CORS Rule**  dialog box, configure  **Allowed Origin**,  **Allowed Method**,  **Allowed Header**,  **Exposed Header**, and  **Cache Duration \(s\)**.

    **Table  1**  Parameters in CORS rules

    <a name="obs_console_0010_mmccppss_tab01"></a>
    <table><thead align="left"><tr id="row14261328"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="p14316908"><a name="p14316908"></a><a name="p14316908"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="p18818860"><a name="p18818860"></a><a name="p18818860"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47932664"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p57340601"><a name="p57340601"></a><a name="p57340601"></a>Allowed Origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p43172637202016"><a name="p43172637202016"></a><a name="p43172637202016"></a>Mandatory</p>
    <p id="p14077143"><a name="p14077143"></a><a name="p14077143"></a>Requests from this origin can access the bucket.</p>
    <p id="p59585428"><a name="p59585428"></a><a name="p59585428"></a>Multiple matching rules are allowed. One rule occupies one line, and allows one wildcard character (<strong id="b562579815151012"><a name="b562579815151012"></a><a name="b562579815151012"></a>*</strong>) at most. Example:</p>
    <pre class="screen" id="screen5755676013302"><a name="screen5755676013302"></a><a name="screen5755676013302"></a>http://rds.example.com
    https://*.vbs.example.com</pre>
    </td>
    </tr>
    <tr id="row18342472"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p9345259"><a name="p9345259"></a><a name="p9345259"></a>Allowed Method</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p18768523"><a name="p18768523"></a><a name="p18768523"></a>Mandatory</p>
    <p id="p63231021153331"><a name="p63231021153331"></a><a name="p63231021153331"></a>Specifies the acceptable operation type of buckets and objects.</p>
    <p id="p59725833153419"><a name="p59725833153419"></a><a name="p59725833153419"></a>The methods include Get, Post, Put, Delete, and Head.</p>
    </td>
    </tr>
    <tr id="row34698981"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p59154058"><a name="p59154058"></a><a name="p59154058"></a>Allowed Header</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p6976477153727"><a name="p6976477153727"></a><a name="p6976477153727"></a>Optional</p>
    <p id="p58393322153740"><a name="p58393322153740"></a><a name="p58393322153740"></a>Specifies the allowed header of cross-origin requests.</p>
    <p id="p2773754710645"><a name="p2773754710645"></a><a name="p2773754710645"></a>Only CORS requests matching the allowed header are valid.</p>
    <p id="p5132822810315"><a name="p5132822810315"></a><a name="p5132822810315"></a>You can enter multiple allowed headers (one per line) and each line can contain one wildcard character (*) at most. Spaces and special characters including <strong id="b648117133820"><a name="b648117133820"></a><a name="b648117133820"></a>&amp;:&lt;</strong> are not allowed.</p>
    </td>
    </tr>
    <tr id="row19218446"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p13190333"><a name="p13190333"></a><a name="p13190333"></a>Exposed Header</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p32426730153840"><a name="p32426730153840"></a><a name="p32426730153840"></a>Optional</p>
    <p id="p309847910721"><a name="p309847910721"></a><a name="p309847910721"></a>Specifies the exposed header in CORS responses, providing additional information for clients.</p>
    <p id="p162724431079"><a name="p162724431079"></a><a name="p162724431079"></a>You can enter multiple exposed headers (one per line). Spaces and special characters including <strong id="b5125223280"><a name="b5125223280"></a><a name="b5125223280"></a>*&amp;:&lt;</strong> are not allowed.</p>
    </td>
    </tr>
    <tr id="row38454973"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p27845085"><a name="p27845085"></a><a name="p27845085"></a>Cache Duration (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p5186476154032"><a name="p5186476154032"></a><a name="p5186476154032"></a>Mandatory</p>
    <p id="p40859422"><a name="p40859422"></a><a name="p40859422"></a>Specifies the duration that your browser can cache CORS responses, expressed in seconds. The default value is <strong id="b1843720126201758"><a name="b1843720126201758"></a><a name="b1843720126201758"></a>100</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**.

    A message is displayed indicating that CORS configuration of the bucket is successful. The configuration of CORS takes effect within two minutes.

    After CORS is successfully configured, only the addresses specified in  **Allowed Origin**  can access a bucket in OBS using the method specified in  **Allowed Method**. For example, you can configure CORS parameters of bucket  **testbucket**  as follows:

    -   **Allowed Origin**:  **www.example.com**
    -   **Allowed Method**:  **GET**
    -   **Allowed Header**: left blank
    -   **Exposed Header**: left blank
    -   **Cache Duration \(s\)**:  **100**


