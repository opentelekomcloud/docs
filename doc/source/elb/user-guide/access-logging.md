# Access Logging<a name="EN-US_TOPIC_0107412580"></a>

Access logs record HTTP and HTTPS requests made to load balancers, and these logs are stored in an OBS bucket. Only public network classic load balancers support access logging.

Before configuring access logging, ensure that you have created a load balancer and OBS bucket. For details, see "Creating a Bucket" in the  _Object Storage Service User Guide_.

1.  Grant read and write permissions to the ELB administrator.
    1.  Log in to the management console. On the  **Object Storage Service**  page, click the name of the destination bucket.
    2.  In the navigation pane on the left, choose  **Permissions**.
    3.  On the displayed page, click  **Bucket ACL**.
    4.  Click  **Add**  and set the parameters.

        **Table  1**  Parameter description

        <a name="table38812372310"></a>
        <table><thead align="left"><tr id="row688153202311"><th class="cellrowborder" valign="top" width="23.56%" id="mcps1.2.4.1.1"><p id="p158811032235"><a name="p158811032235"></a><a name="p158811032235"></a><strong id="b842352706114331"><a name="b842352706114331"></a><a name="b842352706114331"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="47.81%" id="mcps1.2.4.1.2"><p id="p13881173112319"><a name="p13881173112319"></a><a name="p13881173112319"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="28.63%" id="mcps1.2.4.1.3"><p id="p688110316235"><a name="p688110316235"></a><a name="p688110316235"></a><strong id="b842352706185219"><a name="b842352706185219"></a><a name="b842352706185219"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row208811311236"><td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.1 "><p id="p188811631233"><a name="p188811631233"></a><a name="p188811631233"></a>Account</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p16881103112313"><a name="p16881103112313"></a><a name="p16881103112313"></a>Specifies the account ID or account name of the ELB administrator.</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.3 "><p id="p13881163192316"><a name="p13881163192316"></a><a name="p13881163192316"></a>N/A</p>
        </td>
        </tr>
        <tr id="row15542195681517"><td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.1 "><p id="p254275601515"><a name="p254275601515"></a><a name="p254275601515"></a>Access to Bucket</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p153423531617"><a name="p153423531617"></a><a name="p153423531617"></a>Specifies the permissions to read data from or write data to an OBS bucket.</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.3 "><p id="p12343852163"><a name="p12343852163"></a><a name="p12343852163"></a>Read/Write</p>
        </td>
        </tr>
        <tr id="row4750142981615"><td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.1 "><p id="p175122931613"><a name="p175122931613"></a><a name="p175122931613"></a>Access to ACL</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p1474814394356"><a name="p1474814394356"></a><a name="p1474814394356"></a>Allows the authorized user to read or write the bucket ACL.</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.3 "><p id="p12748203913356"><a name="p12748203913356"></a><a name="p12748203913356"></a>Read/Write</p>
        </td>
        </tr>
        </tbody>
        </table>

    5.  Click  **Save**.

2.  Associate the bucket with a load balancer.
    1.  Locate the target load balancer and click  **More**  in the  **Operation**  column.
    2.  Select  **Configure Access Log**.
    3.  In the  **Configure Access Log**  dialog box, enable access logging.
    4.  Select the associated OBS bucket and configure log information.

        **Figure  1**  Configure Access Log<a name="fig1841692934115"></a>  
        ![](figures/configure-access-log.png "configure-access-log")

        **Table  2**  Parameter description

        <a name="table389515316230"></a>
        <table><thead align="left"><tr id="row089593132313"><th class="cellrowborder" valign="top" width="26.94269426942694%" id="mcps1.2.4.1.1"><p id="p689520342319"><a name="p689520342319"></a><a name="p689520342319"></a><strong id="b1083779569"><a name="b1083779569"></a><a name="b1083779569"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="47.24472447244724%" id="mcps1.2.4.1.2"><p id="p68954362315"><a name="p68954362315"></a><a name="p68954362315"></a><strong id="b459412163"><a name="b459412163"></a><a name="b459412163"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="25.81258125812581%" id="mcps1.2.4.1.3"><p id="p789514302312"><a name="p789514302312"></a><a name="p789514302312"></a><strong id="b842352706194150"><a name="b842352706194150"></a><a name="b842352706194150"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row277023594914"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p12770133517497"><a name="p12770133517497"></a><a name="p12770133517497"></a>Enable Logging</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.24472447244724%" headers="mcps1.2.4.1.2 "><p id="p977043524915"><a name="p977043524915"></a><a name="p977043524915"></a>Whether to enable access logging</p>
        </td>
        <td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.3 "><p id="p677013355491"><a name="p677013355491"></a><a name="p677013355491"></a>N/A</p>
        </td>
        </tr>
        <tr id="row1489583132317"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p19895638231"><a name="p19895638231"></a><a name="p19895638231"></a>Backup Interval (min)</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.24472447244724%" headers="mcps1.2.4.1.2 "><p id="p489593192314"><a name="p489593192314"></a><a name="p489593192314"></a>Log backup interval in minutes, which is 60 minutes by default</p>
        </td>
        <td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.3 "><p id="p168950352315"><a name="p168950352315"></a><a name="p168950352315"></a>60</p>
        </td>
        </tr>
        <tr id="row10895139239"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p10895538239"><a name="p10895538239"></a><a name="p10895538239"></a>OBS Bucket</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.24472447244724%" headers="mcps1.2.4.1.2 "><p id="p489510312239"><a name="p489510312239"></a><a name="p489510312239"></a>Destination bucket with read and write permissions</p>
        </td>
        <td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.3 "><p id="p1289563132316"><a name="p1289563132316"></a><a name="p1289563132316"></a>obs01</p>
        </td>
        </tr>
        <tr id="row389593132313"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p1089513372319"><a name="p1089513372319"></a><a name="p1089513372319"></a>Prefix</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.24472447244724%" headers="mcps1.2.4.1.2 "><p id="p3666621194749"><a name="p3666621194749"></a><a name="p3666621194749"></a>Log storage directory</p>
        <p id="p4073177194758"><a name="p4073177194758"></a><a name="p4073177194758"></a>If this field is left blank, logs will be saved to the root directory of the destination bucket.</p>
        </td>
        <td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.3 "><p id="p189533182311"><a name="p189533182311"></a><a name="p189533182311"></a>log01</p>
        </td>
        </tr>
        </tbody>
        </table>



