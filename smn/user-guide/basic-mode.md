# Basic Mode<a name="en-us_topic_0043394891"></a>

The topic creator has the right to configure topic policies. Using topic policies, you can specify which users and cloud services can perform which topic operations, for example, querying topic details and publishing messages. Topic creators always have permissions over a topic even if they grant topic permissions to other users.

## Configuring Topic Policies in Basic Mode<a name="section123941655999"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Topics**.

    The  **Topics**  page is displayed.

5.  Locate a topic, click  **More**  under  **Operation**, and select  **Configure Topic Policy**.
6.  In the  **Configure Topic Policy**  box, configure the topic policy in basic mode.

    The basic mode simply specifies which users or cloud services have permissions to publish messages to a topic. For details, see  [Table 1](#table41411027111244).

    The advanced mode provides more flexible permission settings. For details, see section  [Advanced Mode](advanced-mode.md).

    **Table  1**  Description for configuring topic policies in basic mode

    <a name="table41411027111244"></a>
    <table><thead align="left"><tr id="row13344231111244"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.4.1.1"><p id="p33478231112118"><a name="p33478231112118"></a><a name="p33478231112118"></a>Item</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p18000631111244"><a name="p18000631111244"></a><a name="p18000631111244"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.63999999999999%" id="mcps1.2.4.1.3"><p id="p48765019111244"><a name="p48765019111244"></a><a name="p48765019111244"></a><strong id="b2461889016144"><a name="b2461889016144"></a><a name="b2461889016144"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18473302111244"><td class="cellrowborder" rowspan="3" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p5383640695554"><a name="p5383640695554"></a><a name="p5383640695554"></a>Users who can publish messages to this topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p47398656111244"><a name="p47398656111244"></a><a name="p47398656111244"></a>Topic creator</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p14085905111244"><a name="p14085905111244"></a><a name="p14085905111244"></a>Only the topic creator has permission to publish messages to the topic.</p>
    </td>
    </tr>
    <tr id="row11395712111244"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p43476026111244"><a name="p43476026111244"></a><a name="p43476026111244"></a>All users</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p31897252111244"><a name="p31897252111244"></a><a name="p31897252111244"></a>All users have permission to publish messages to the topic.</p>
    </td>
    </tr>
    <tr id="row23505339111244"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1329320191815"><a name="p1329320191815"></a><a name="p1329320191815"></a>Specified user domains</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p850910222516"><a name="p850910222516"></a><a name="p850910222516"></a>Only specified users have permission to publish messages to the topic. Users are specified in the format <strong id="b842352706143516"><a name="b842352706143516"></a><a name="b842352706143516"></a>urn:csp:iam::domainId:root</strong>.</p>
    <p id="p13818194012327"><a name="p13818194012327"></a><a name="p13818194012327"></a>You only need to enter the domain ID and click <strong id="b842352706162312"><a name="b842352706162312"></a><a name="b842352706162312"></a>OK</strong>. The system completes all other required information for you. SMN does not limit the number of IDs you enter, but the total length of a topic policy cannot exceed 30 KB.</p>
    <p id="p9731817181012"><a name="p9731817181012"></a><a name="p9731817181012"></a>All settings in the basic mode are also presented in the advanced policy. You can modify them in the advanced mode if necessary. For details, see section <a href="advanced-mode.md">Advanced Mode</a>.</p>
    <p id="p1068720613235"><a name="p1068720613235"></a><a name="p1068720613235"></a>To obtain a user's domain ID, log in to the SMN console and click <strong id="b842352706161841"><a name="b842352706161841"></a><a name="b842352706161841"></a>My Credentials</strong> in the username drop-down list on the upper right.</p>
    </td>
    </tr>
    <tr id="row6059372111244"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p27095394111244"><a name="p27095394111244"></a><a name="p27095394111244"></a>Services that can publish messages to this topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1450115341985"><a name="p1450115341985"></a><a name="p1450115341985"></a>The services that can publish messages vary according to regions.</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p1504539111244"><a name="p1504539111244"></a><a name="p1504539111244"></a>The selected cloud services have operation permissions of the topic.</p>
    <div class="note" id="note52989799155357"><a name="note52989799155357"></a><a name="note52989799155357"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p65029791171837"><a name="p65029791171837"></a><a name="p65029791171837"></a>By default, Cloud Eye and Anti-DDoS have permissions to publish messages to topics created by all users.</p>
    <p id="p53660708171840"><a name="p53660708171840"></a><a name="p53660708171840"></a>For details about how to use SMN in other cloud services, see user guides of the related services.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


