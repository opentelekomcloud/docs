# Querying Load Balancers<a name="EN-US_TOPIC_0096561504"></a>

## Function<a name="en-us_topic_0020100182_section16965623"></a>

This API is used to query load balancers and display them in a list.

## URI<a name="en-us_topic_0020100182_section18472885"></a>

GET /v1.0/\{project\_id\}/elbaas/loadbalancers

**Table  1**  Parameter description

<a name="en-us_topic_0020100182_table423243211824"></a>
<table><thead align="left"><tr id="en-us_topic_0020100182_row62399911824"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100182_p5054393511824"><a name="en-us_topic_0020100182_p5054393511824"></a><a name="en-us_topic_0020100182_p5054393511824"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100182_p41808011824"><a name="en-us_topic_0020100182_p41808011824"></a><a name="en-us_topic_0020100182_p41808011824"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100182_p28618744114854"><a name="en-us_topic_0020100182_p28618744114854"></a><a name="en-us_topic_0020100182_p28618744114854"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100182_p3386452111824"><a name="en-us_topic_0020100182_p3386452111824"></a><a name="en-us_topic_0020100182_p3386452111824"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100182_row5867171511824"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p19621559174917"><a name="p19621559174917"></a><a name="p19621559174917"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100182_p868365711824"><a name="en-us_topic_0020100182_p868365711824"></a><a name="en-us_topic_0020100182_p868365711824"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100182_p64087506114854"><a name="en-us_topic_0020100182_p64087506114854"></a><a name="en-us_topic_0020100182_p64087506114854"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100182_p3228758811824"><a name="en-us_topic_0020100182_p3228758811824"></a><a name="en-us_topic_0020100182_p3228758811824"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100182_section32038241"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100182_section19908716"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100182_table34601787174952"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100182_row40266818174952"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100182_p40386800174952"><a name="en-us_topic_0020100182_p40386800174952"></a><a name="en-us_topic_0020100182_p40386800174952"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100182_p50105334174952"><a name="en-us_topic_0020100182_p50105334174952"></a><a name="en-us_topic_0020100182_p50105334174952"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100182_p32000253174952"><a name="en-us_topic_0020100182_p32000253174952"></a><a name="en-us_topic_0020100182_p32000253174952"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100182_row41883692174952"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p37135916174952"><a name="en-us_topic_0020100182_p37135916174952"></a><a name="en-us_topic_0020100182_p37135916174952"></a>loadbalancers</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p1587515694812"><a name="p1587515694812"></a><a name="p1587515694812"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p56614318174952"><a name="en-us_topic_0020100182_p56614318174952"></a><a name="en-us_topic_0020100182_p56614318174952"></a>Lists the load balancers.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row30174695111317"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p16393887111317"><a name="en-us_topic_0020100182_p16393887111317"></a><a name="en-us_topic_0020100182_p16393887111317"></a>instance_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p52836457111317"><a name="en-us_topic_0020100182_p52836457111317"></a><a name="en-us_topic_0020100182_p52836457111317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p51894644111317"><a name="en-us_topic_0020100182_p51894644111317"></a><a name="en-us_topic_0020100182_p51894644111317"></a>Specifies the number of load balancers.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **loadbalancers**  parameter description

    <a name="en-us_topic_0020100182_table291348694313"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100182_row2893288394313"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100182_p1497261194313"><a name="en-us_topic_0020100182_p1497261194313"></a><a name="en-us_topic_0020100182_p1497261194313"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100182_p482201094313"><a name="en-us_topic_0020100182_p482201094313"></a><a name="en-us_topic_0020100182_p482201094313"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.366336633663366%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100182_p5503849294313"><a name="en-us_topic_0020100182_p5503849294313"></a><a name="en-us_topic_0020100182_p5503849294313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100182_row2206588594313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p6186221594313"><a name="en-us_topic_0020100182_p6186221594313"></a><a name="en-us_topic_0020100182_p6186221594313"></a>vip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p4478351994313"><a name="en-us_topic_0020100182_p4478351994313"></a><a name="en-us_topic_0020100182_p4478351994313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p358643694313"><a name="en-us_topic_0020100182_p358643694313"></a><a name="en-us_topic_0020100182_p358643694313"></a>Specifies the private IP address of the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row1347272394313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p6437524194313"><a name="en-us_topic_0020100182_p6437524194313"></a><a name="en-us_topic_0020100182_p6437524194313"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p4701201294313"><a name="en-us_topic_0020100182_p4701201294313"></a><a name="en-us_topic_0020100182_p4701201294313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p4987659994313"><a name="en-us_topic_0020100182_p4987659994313"></a><a name="en-us_topic_0020100182_p4987659994313"></a>Specifies the time when the load balancer was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row969681194313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p5414564794313"><a name="en-us_topic_0020100182_p5414564794313"></a><a name="en-us_topic_0020100182_p5414564794313"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p2372125494313"><a name="en-us_topic_0020100182_p2372125494313"></a><a name="en-us_topic_0020100182_p2372125494313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p4237344294313"><a name="en-us_topic_0020100182_p4237344294313"></a><a name="en-us_topic_0020100182_p4237344294313"></a>Specifies the time when the load balancer was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row922144494313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p2016244094313"><a name="en-us_topic_0020100182_p2016244094313"></a><a name="en-us_topic_0020100182_p2016244094313"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p2254491094313"><a name="en-us_topic_0020100182_p2254491094313"></a><a name="en-us_topic_0020100182_p2254491094313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p1419842194313"><a name="en-us_topic_0020100182_p1419842194313"></a><a name="en-us_topic_0020100182_p1419842194313"></a>Specifies the load balancer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row6013901494313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p1588413994313"><a name="en-us_topic_0020100182_p1588413994313"></a><a name="en-us_topic_0020100182_p1588413994313"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p1154685894313"><a name="en-us_topic_0020100182_p1154685894313"></a><a name="en-us_topic_0020100182_p1154685894313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100182_ul8773172115354"></a><a name="en-us_topic_0020100182_ul8773172115354"></a><ul id="en-us_topic_0020100182_ul8773172115354"><li>Specifies the load balancer status.</li><li>The value can be <strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>, <strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_CREATE</strong>, or <strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row2089948694313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p438021594313"><a name="en-us_topic_0020100182_p438021594313"></a><a name="en-us_topic_0020100182_p438021594313"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p1925312994313"><a name="en-us_topic_0020100182_p1925312994313"></a><a name="en-us_topic_0020100182_p1925312994313"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p1599960394313"><a name="en-us_topic_0020100182_p1599960394313"></a><a name="en-us_topic_0020100182_p1599960394313"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row5811821394313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p5387765194313"><a name="en-us_topic_0020100182_p5387765194313"></a><a name="en-us_topic_0020100182_p5387765194313"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p201363494313"><a name="en-us_topic_0020100182_p201363494313"></a><a name="en-us_topic_0020100182_p201363494313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p2888666194313"><a name="en-us_topic_0020100182_p2888666194313"></a><a name="en-us_topic_0020100182_p2888666194313"></a>Specifies the VPC ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row1505055994313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p5330187194313"><a name="en-us_topic_0020100182_p5330187194313"></a><a name="en-us_topic_0020100182_p5330187194313"></a>admin_state_up</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p2248427694313"><a name="en-us_topic_0020100182_p2248427694313"></a><a name="en-us_topic_0020100182_p2248427694313"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100182_ul6480915994313"></a><a name="en-us_topic_0020100182_ul6480915994313"></a><ul id="en-us_topic_0020100182_ul6480915994313"><li>Specifies the administrative status of the load balancer.</li><li>The following options are available:<p id="en-us_topic_0020100182_p2773489812039"><a name="en-us_topic_0020100182_p2773489812039"></a><a name="en-us_topic_0020100182_p2773489812039"></a><strong id="b842352706153922"><a name="b842352706153922"></a><a name="b842352706153922"></a>0</strong>: The load balancer is disabled.</p>
    <p id="en-us_topic_0020100182_p4828749112039"><a name="en-us_topic_0020100182_p4828749112039"></a><a name="en-us_topic_0020100182_p4828749112039"></a><strong id="b842352706154557"><a name="b842352706154557"></a><a name="b842352706154557"></a>1</strong>: The load balancer is running properly.</p>
    <p id="en-us_topic_0020100182_p3193424012039"><a name="en-us_topic_0020100182_p3193424012039"></a><a name="en-us_topic_0020100182_p3193424012039"></a><strong id="b842352706153951"><a name="b842352706153951"></a><a name="b842352706153951"></a>2</strong>: The load balancer is frozen.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row6669320194313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p123730594313"><a name="en-us_topic_0020100182_p123730594313"></a><a name="en-us_topic_0020100182_p123730594313"></a>vip_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p3311289694313"><a name="en-us_topic_0020100182_p3311289694313"></a><a name="en-us_topic_0020100182_p3311289694313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p4721962494313"><a name="en-us_topic_0020100182_p4721962494313"></a><a name="en-us_topic_0020100182_p4721962494313"></a>This parameter is unavailable now.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row1144074894313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p6336790594313"><a name="en-us_topic_0020100182_p6336790594313"></a><a name="en-us_topic_0020100182_p6336790594313"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p3252666694313"><a name="en-us_topic_0020100182_p3252666694313"></a><a name="en-us_topic_0020100182_p3252666694313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p2251086594313"><a name="en-us_topic_0020100182_p2251086594313"></a><a name="en-us_topic_0020100182_p2251086594313"></a>Specifies the network type of the load balancer. The value is <strong>External</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row4372251194313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p3585787294313"><a name="en-us_topic_0020100182_p3585787294313"></a><a name="en-us_topic_0020100182_p3585787294313"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p1880655694313"><a name="en-us_topic_0020100182_p1880655694313"></a><a name="en-us_topic_0020100182_p1880655694313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p4693603594313"><a name="en-us_topic_0020100182_p4693603594313"></a><a name="en-us_topic_0020100182_p4693603594313"></a>Specifies the load balancer name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row5213068294313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p5795828794313"><a name="en-us_topic_0020100182_p5795828794313"></a><a name="en-us_topic_0020100182_p5795828794313"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p6410964594313"><a name="en-us_topic_0020100182_p6410964594313"></a><a name="en-us_topic_0020100182_p6410964594313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100182_p2549872394313"><a name="en-us_topic_0020100182_p2549872394313"></a><a name="en-us_topic_0020100182_p2549872394313"></a>Provides supplementary information about the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row3793109194313"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100182_p6652295794313"><a name="en-us_topic_0020100182_p6652295794313"></a><a name="en-us_topic_0020100182_p6652295794313"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100182_p1965044094313"><a name="en-us_topic_0020100182_p1965044094313"></a><a name="en-us_topic_0020100182_p1965044094313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100182_ul1041033994313"></a><a name="en-us_topic_0020100182_ul1041033994313"></a><ul id="en-us_topic_0020100182_ul1041033994313"><li>Specifies the security group ID.</li><li><strong id="b842352706113355"><a name="b842352706113355"></a><a name="b842352706113355"></a>null</strong> is displayed for this parameter when <strong id="b842352706113359"><a name="b842352706113359"></a><a name="b842352706113359"></a>type</strong> is set to <strong id="b84235270611343"><a name="b84235270611343"></a><a name="b84235270611343"></a>External</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "loadbalancers": [
            {
                "vip_address": "192.144.62.114",
                "update_time": "2015-09-14 02:34:32",
                "create_time": "2015-09-14 02:34:32",
                "id": "0b07acf06d243925bc24a0ac7445267a",
                "status": "ACTIVE",
                "bandwidth": 1,
                "security_group_id": null,
                "vpc_id": "f54a3ffd-7a55-4568-9e3d-f0ff2d46a107",
                "admin_state_up": 1,
                "vip_subnet_id": null,
                "type": "External",
                "name": "MY_ELB",
                "description": null
            }
        ],
        "instance_num": "1"
    }
    ```


## Status Code<a name="en-us_topic_0020100182_section44960719"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100182_table18047584151435"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100182_row3033869151435"><th class="cellrowborder" valign="top" width="11.469999999999999%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100182_p44416862151435"><a name="en-us_topic_0020100182_p44416862151435"></a><a name="en-us_topic_0020100182_p44416862151435"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.29%" id="mcps1.1.4.1.2"><p id="p1541114817565"><a name="p1541114817565"></a><a name="p1541114817565"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100182_p40996108151435"><a name="en-us_topic_0020100182_p40996108151435"></a><a name="en-us_topic_0020100182_p40996108151435"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100182_row32350462151435"><td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100182_p3141789151435"><a name="en-us_topic_0020100182_p3141789151435"></a><a name="en-us_topic_0020100182_p3141789151435"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.29%" headers="mcps1.1.4.1.2 "><p id="p92632001570"><a name="p92632001570"></a><a name="p92632001570"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100182_p53158352151435"><a name="en-us_topic_0020100182_p53158352151435"></a><a name="en-us_topic_0020100182_p53158352151435"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row8663125151435"><td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100182_p30624514151435"><a name="en-us_topic_0020100182_p30624514151435"></a><a name="en-us_topic_0020100182_p30624514151435"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.29%" headers="mcps1.1.4.1.2 "><p id="p142631095716"><a name="p142631095716"></a><a name="p142631095716"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100182_p64666551151435"><a name="en-us_topic_0020100182_p64666551151435"></a><a name="en-us_topic_0020100182_p64666551151435"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row45128053151435"><td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100182_p31493642151435"><a name="en-us_topic_0020100182_p31493642151435"></a><a name="en-us_topic_0020100182_p31493642151435"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.29%" headers="mcps1.1.4.1.2 "><p id="p172633025720"><a name="p172633025720"></a><a name="p172633025720"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100182_p848187151435"><a name="en-us_topic_0020100182_p848187151435"></a><a name="en-us_topic_0020100182_p848187151435"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row7633690151435"><td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100182_p14349186151435"><a name="en-us_topic_0020100182_p14349186151435"></a><a name="en-us_topic_0020100182_p14349186151435"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.29%" headers="mcps1.1.4.1.2 "><p id="p626311014576"><a name="p626311014576"></a><a name="p626311014576"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100182_p21433402151435"><a name="en-us_topic_0020100182_p21433402151435"></a><a name="en-us_topic_0020100182_p21433402151435"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row58682891151435"><td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100182_p55693759151435"><a name="en-us_topic_0020100182_p55693759151435"></a><a name="en-us_topic_0020100182_p55693759151435"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.29%" headers="mcps1.1.4.1.2 "><p id="p182636055715"><a name="p182636055715"></a><a name="p182636055715"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100182_p14900631151435"><a name="en-us_topic_0020100182_p14900631151435"></a><a name="en-us_topic_0020100182_p14900631151435"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100182_row66996820151435"><td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100182_p58033374151435"><a name="en-us_topic_0020100182_p58033374151435"></a><a name="en-us_topic_0020100182_p58033374151435"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.29%" headers="mcps1.1.4.1.2 "><p id="p626360195711"><a name="p626360195711"></a><a name="p626360195711"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100182_p3082881151435"><a name="en-us_topic_0020100182_p3082881151435"></a><a name="en-us_topic_0020100182_p3082881151435"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


