# Access Log<a name="en-us_elb_03_0004"></a>

Access logs record HTTP and HTTPS requests for layer-7 load balancing. Only public network classic load balancers have access logs, and these logs are stored in an OBS bucket.

Before configuring access logs, you need to have created a load balancer and have an OBS bucket available when you configure access logs. For details about how to create an OBS bucket, see section "Creating a Bucket" in the  _Object Storage Service User Guide_.

1.  Grant read and write permissions to the ELB administrator.
    1.  Log in to the management console. On the  **Object Storage Service**  page, click the name of the target bucket.
    2.  In the navigation pane on the left, choose  **Permissions**.
    3.  On the displayed page, click  **ACL**.
    4.  Click  **Add**  and set the parameters.

        **Table  1**  Parameter description

        <a name="table38812372310"></a><table><thead align="left"><tr id="row688153202311"><th class="cellrowborder" valign="top" width="23.56%" id="mcps1.2.4.1.1"><p id="p158811032235"><a name="p158811032235"></a><a name="p158811032235"></a><strong id="b842352706114331"><a name="b842352706114331"></a><a name="b842352706114331"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="47.81%" id="mcps1.2.4.1.2"><p id="p13881173112319"><a name="p13881173112319"></a><a name="p13881173112319"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="28.63%" id="mcps1.2.4.1.3"><p id="p688110316235"><a name="p688110316235"></a><a name="p688110316235"></a><strong id="b842352706185219"><a name="b842352706185219"></a><a name="b842352706185219"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row208811311236"><td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.1 "><p id="p188811631233"><a name="p188811631233"></a><a name="p188811631233"></a>Account</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p16881103112313"><a name="p16881103112313"></a><a name="p16881103112313"></a>Specifies the domain ID of the ELB administrator.</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.3 "><p id="p13881163192316"><a name="p13881163192316"></a><a name="p13881163192316"></a>N/A</p>
        </td>
        </tr>
        <tr id="row3881530237"><td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.1 "><p id="p1088120314231"><a name="p1088120314231"></a><a name="p1088120314231"></a>Bucket Access</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p11881143142315"><a name="p11881143142315"></a><a name="p11881143142315"></a>Specifies the permissions to read data from or write data to an OBS bucket.</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.3 "><p id="p20881143182318"><a name="p20881143182318"></a><a name="p20881143182318"></a>Read/Write</p>
        </td>
        </tr>
        <tr id="row4881733231"><td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.1 "><p id="p48811322311"><a name="p48811322311"></a><a name="p48811322311"></a>Permission Access</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p1088116342317"><a name="p1088116342317"></a><a name="p1088116342317"></a>Specifies the assigned read and write permissions.</p>
        </td>
        <td class="cellrowborder" valign="top" width="28.63%" headers="mcps1.2.4.1.3 "><p id="p58811338239"><a name="p58811338239"></a><a name="p58811338239"></a>Read/Write</p>
        </td>
        </tr>
        </tbody>
        </table>

    5.  Click  **Save**.
2.  Associate OBS with ELB.
    1.  On the  **Elastic Load Balance** page, locate the row that contains the target load balancer and click **More** in the **Operation**  column.
    2.  Select  **Configure Access Log**.
    3.  In the displayed dialog box, enable log backup.
    4.  Select an OBS bucket and configure log information.

        **Figure  1**  Configuring access logs<a name="fig189520322318"></a>
        ![](figures/configuring-access-logs.jpg "Configuring access logs")

        **Table  2**  Parameter description

        <a name="table389515316230"></a><table><thead align="left"><tr id="row089593132313"><th class="cellrowborder" valign="top" width="26.94269426942694%" id="mcps1.2.4.1.1"><p id="p689520342319"><a name="p689520342319"></a><a name="p689520342319"></a><strong id="b842352706114331_1"><a name="b842352706114331_1"></a><a name="b842352706114331_1"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="47.24472447244724%" id="mcps1.2.4.1.2"><p id="p68954362315"><a name="p68954362315"></a><a name="p68954362315"></a><strong id="b8423527061772_1"><a name="b8423527061772_1"></a><a name="b8423527061772_1"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="25.81258125812581%" id="mcps1.2.4.1.3"><p id="p789514302312"><a name="p789514302312"></a><a name="p789514302312"></a><strong id="b842352706194150"><a name="b842352706194150"></a><a name="b842352706194150"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1489583132317"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p19895638231"><a name="p19895638231"></a><a name="p19895638231"></a>Backup Interval</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.24472447244724%" headers="mcps1.2.4.1.2 "><p id="p489593192314"><a name="p489593192314"></a><a name="p489593192314"></a>Log backup interval, which is 60 minutes by default.</p>
        </td>
        <td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.3 "><p id="p168950352315"><a name="p168950352315"></a><a name="p168950352315"></a>60 minutes</p>
        </td>
        </tr>
        <tr id="row10895139239"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p10895538239"><a name="p10895538239"></a><a name="p10895538239"></a>OBS Bucket</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.24472447244724%" headers="mcps1.2.4.1.2 "><p id="p489510312239"><a name="p489510312239"></a><a name="p489510312239"></a>OBS bucket with read and write permissions</p>
        </td>
        <td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.3 "><p id="p1289563132316"><a name="p1289563132316"></a><a name="p1289563132316"></a>obs01</p>
        </td>
        </tr>
        <tr id="row389593132313"><td class="cellrowborder" valign="top" width="26.94269426942694%" headers="mcps1.2.4.1.1 "><p id="p1089513372319"><a name="p1089513372319"></a><a name="p1089513372319"></a>Prefix</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.24472447244724%" headers="mcps1.2.4.1.2 "><p id="p1289512310238"><a name="p1289512310238"></a><a name="p1289512310238"></a>Log storage directory, which is the root directory of the OBS bucket</p>
        </td>
        <td class="cellrowborder" valign="top" width="25.81258125812581%" headers="mcps1.2.4.1.3 "><p id="p189533182311"><a name="p189533182311"></a><a name="p189533182311"></a>log01</p>
        </td>
        </tr>
        </tbody>
        </table>



