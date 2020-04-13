# Creating a VPC Flow Log<a name="FlowLog_0003"></a>

## Scenarios<a name="section15598193716333"></a>

A VPC flow log records information about the traffic going to and from a VPC.

## Prerequisites<a name="section48811154114711"></a>

Ensure that the following operations have been performed on the LTS console:

-   Create a log group.
-   Create a log topic.

For more information about the LTS service, see the  _Log Tank Service User Guide_.

## Procedure<a name="section7359352124511"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **VPC Flow Logs**.
5.  In the upper right corner, click  **Create VPC Flow Log**. On the displayed page, configure parameters as prompted.

    **Figure  1**  Create VPC Flow Log<a name="fig4520438111212"></a>  
    ![](figures/create-vpc-flow-log.png "create-vpc-flow-log")

    **Table  1**  Parameter description

    <a name="table134731712211"></a>
    <table><thead align="left"><tr id="row1434717171627"><th class="cellrowborder" valign="top" width="19.24%" id="mcps1.2.4.1.1"><p id="p234731711214"><a name="p234731711214"></a><a name="p234731711214"></a><strong id="b729481085112"><a name="b729481085112"></a><a name="b729481085112"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="55.7%" id="mcps1.2.4.1.2"><p id="p934711715210"><a name="p934711715210"></a><a name="p934711715210"></a><strong id="b761217124516"><a name="b761217124516"></a><a name="b761217124516"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.3"><p id="p23473171214"><a name="p23473171214"></a><a name="p23473171214"></a><strong id="b9956614115118"><a name="b9956614115118"></a><a name="b9956614115118"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2034718171526"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p63477171520"><a name="p63477171520"></a><a name="p63477171520"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p0347817222"><a name="p0347817222"></a><a name="p0347817222"></a>Specifies the VPC flow log name.</p>
    <p id="p3691035194820"><a name="p3691035194820"></a><a name="p3691035194820"></a>The VPC flow log name can contain a maximum of 64 characters, which may consist of letters, digits, underscores (_), hyphens (-), and periods (.). The name cannot contain spaces.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p14347191710216"><a name="p14347191710216"></a><a name="p14347191710216"></a>flowlog-495d</p>
    </td>
    </tr>
    <tr id="row183478171729"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p11347141710216"><a name="p11347141710216"></a><a name="p11347141710216"></a>Resource Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p834721711219"><a name="p834721711219"></a><a name="p834721711219"></a>Specifies the type of resources whose traffic is to be logged. Currently, <strong id="b1451420710532"><a name="b1451420710532"></a><a name="b1451420710532"></a>Resource Type</strong> can be <strong id="b319411435314"><a name="b319411435314"></a><a name="b319411435314"></a>NIC</strong>, <strong id="b99451145134910"><a name="b99451145134910"></a><a name="b99451145134910"></a>Subnet</strong>, and <strong id="b13946194519492"><a name="b13946194519492"></a><a name="b13946194519492"></a>VPC</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p6347317525"><a name="p6347317525"></a><a name="p6347317525"></a>NIC</p>
    </td>
    </tr>
    <tr id="row83477171628"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p1081611984120"><a name="p1081611984120"></a><a name="p1081611984120"></a>Resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p143471917921"><a name="p143471917921"></a><a name="p143471917921"></a>Specifies the specific NIC whose traffic is to be logged.</p>
    <div class="note" id="note81381412191719"><a name="note81381412191719"></a><a name="note81381412191719"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p111391812141715"><a name="p111391812141715"></a><a name="p111391812141715"></a>We recommend that you select an ECS that is in the running state. If an ECS in the stopped state is selected, restart the ECS after creating the VPC flow log for accurately recording information about the traffic going to and from a NIC.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p4347517128"><a name="p4347517128"></a><a name="p4347517128"></a>N/A</p>
    </td>
    </tr>
    <tr id="row734713175216"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p934719178215"><a name="p934719178215"></a><a name="p934719178215"></a>Filter</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><a name="ul1934716177219"></a><a name="ul1934716177219"></a><ul id="ul1934716177219"><li><strong id="b934111133020"><a name="b934111133020"></a><a name="b934111133020"></a>All traffic</strong>: specifies that both accepted and rejected traffic of the specified resource will be logged.</li><li><strong id="b918513514319"><a name="b918513514319"></a><a name="b918513514319"></a>Accepted traffic</strong>: specifies that only accepted traffic of the specified resource will be logged. Accepted traffic refers to the traffic permitted by the security group or firewall.</li><li><strong id="b16278316812"><a name="b16278316812"></a><a name="b16278316812"></a>Rejected traffic</strong>: specifies that only rejected traffic of the specified resource will be logged. Rejected traffic refers to the traffic not permitted by the firewall.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p93471617626"><a name="p93471617626"></a><a name="p93471617626"></a>All</p>
    </td>
    </tr>
    <tr id="row143475171327"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p734771710219"><a name="p734771710219"></a><a name="p734771710219"></a>Log Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p16347111715218"><a name="p16347111715218"></a><a name="p16347111715218"></a>Specifies the log group created in LTS.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151016581_p634714176216"><a name="en-us_topic_0151016581_p634714176216"></a><a name="en-us_topic_0151016581_p634714176216"></a>lts-group-wule</p>
    </td>
    </tr>
    <tr id="row63479171326"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p133476171224"><a name="p133476171224"></a><a name="p133476171224"></a>Log Topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p2347101712216"><a name="p2347101712216"></a><a name="p2347101712216"></a>Specifies the log topic created in LTS.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0151016581_p43470173218"><a name="en-us_topic_0151016581_p43470173218"></a><a name="en-us_topic_0151016581_p43470173218"></a>LogTopic1</p>
    </td>
    </tr>
    <tr id="row1834761720219"><td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.2.4.1.1 "><p id="p113471171229"><a name="p113471171229"></a><a name="p113471171229"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.7%" headers="mcps1.2.4.1.2 "><p id="p43473171124"><a name="p43473171124"></a><a name="p43473171124"></a>Provides supplementary information about the VPC flow log. This parameter is optional.</p>
    <p id="p17347181718216"><a name="p17347181718216"></a><a name="p17347181718216"></a>The VPC flow log description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p3347141715212"><a name="p3347141715212"></a><a name="p3347141715212"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Only two flow logs, each with a different filter, can be created for a single resource under the same log group and log topic. Each VPC flow log must be unique.  

6.  Click  **OK**.

