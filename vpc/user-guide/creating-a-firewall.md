# Creating a Firewall<a name="en-us_topic_0051746698"></a>

## Scenarios<a name="section61389724143414"></a>

A firewall consists of one or more access control lists \(ACLs\). The firewall determines whether data packets are allowed in or out of any associated subnet based on inbound and outbound rules. You can create a custom firewall, but any newly created firewall will be disabled by default. It will not have any inbound or outbound rules, or have any subnets associated. Each user can create up to 200 firewalls by default.

## Procedure<a name="section4636069144430"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Firewalls**.
5.  In the right pane displayed, click  **Create Firewall**.
6.  In the displayed  **Create Firewall**  area, enter firewall information as prompted.  [Table 1](#table145313414319)  lists the parameters to be configured.

    **Figure  1**  Create Firewall<a name="fig1853328517154"></a>  
    ![](figures/create-firewall.png "create-firewall")

    **Table  1**  Parameter description

    <a name="table145313414319"></a>
    <table><thead align="left"><tr id="row05304110314"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.4.1.1"><p id="p5530411336"><a name="p5530411336"></a><a name="p5530411336"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.76%" id="mcps1.2.4.1.2"><p id="p35314117314"><a name="p35314117314"></a><a name="p35314117314"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.81%" id="mcps1.2.4.1.3"><p id="p75313411731"><a name="p75313411731"></a><a name="p75313411731"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2053541033"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.1 "><p id="p155314118320"><a name="p155314118320"></a><a name="p155314118320"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p105334113312"><a name="p105334113312"></a><a name="p105334113312"></a>Specifies the firewall name. This parameter is mandatory.</p>
    <p id="p453441837"><a name="p453441837"></a><a name="p453441837"></a>The firewall name contains a maximum of 64 characters, which may consist of letters, digits, underscores (_), and hyphens (-). The name cannot contain spaces.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.81%" headers="mcps1.2.4.1.3 "><p id="p15319411234"><a name="p15319411234"></a><a name="p15319411234"></a>fw-92d3</p>
    </td>
    </tr>
    <tr id="row1753541637"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.1 "><p id="p16535411332"><a name="p16535411332"></a><a name="p16535411332"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.76%" headers="mcps1.2.4.1.2 "><p id="p55384117316"><a name="p55384117316"></a><a name="p55384117316"></a>Provides supplementary information about the firewall. This parameter is optional.</p>
    <p id="p185324110315"><a name="p185324110315"></a><a name="p185324110315"></a>The firewall description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.81%" headers="mcps1.2.4.1.3 "><p id="p95315415313"><a name="p95315415313"></a><a name="p95315415313"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    The firewall is created.


