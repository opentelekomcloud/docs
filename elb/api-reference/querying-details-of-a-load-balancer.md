# Querying Details of a Load Balancer<a name="EN-US_TOPIC_0096561503"></a>

## Function<a name="en-us_topic_0020100181_section13121422"></a>

This API is used to query details about a load balancer.

## URI<a name="en-us_topic_0020100181_section50983938"></a>

GET /v1.0/\{project\_id\}/elbaas/loadbalancers/\{loadbalancer\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100181_table17662689"></a>
<table><thead align="left"><tr id="en-us_topic_0020100181_row26495667"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100181_p65774263"><a name="en-us_topic_0020100181_p65774263"></a><a name="en-us_topic_0020100181_p65774263"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100181_p26115080"><a name="en-us_topic_0020100181_p26115080"></a><a name="en-us_topic_0020100181_p26115080"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100181_p6229287311465"><a name="en-us_topic_0020100181_p6229287311465"></a><a name="en-us_topic_0020100181_p6229287311465"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53.46534653465347%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100181_p34946701"><a name="en-us_topic_0020100181_p34946701"></a><a name="en-us_topic_0020100181_p34946701"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100181_row1174485311137"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p37601141104616"><a name="p37601141104616"></a><a name="p37601141104616"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100181_p4809228811137"><a name="en-us_topic_0020100181_p4809228811137"></a><a name="en-us_topic_0020100181_p4809228811137"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100181_p1255791511465"><a name="en-us_topic_0020100181_p1255791511465"></a><a name="en-us_topic_0020100181_p1255791511465"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.46534653465347%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100181_p5473755511137"><a name="en-us_topic_0020100181_p5473755511137"></a><a name="en-us_topic_0020100181_p5473755511137"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100181_row130498311137"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100181_p4101250511137"><a name="en-us_topic_0020100181_p4101250511137"></a><a name="en-us_topic_0020100181_p4101250511137"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100181_p3367862711137"><a name="en-us_topic_0020100181_p3367862711137"></a><a name="en-us_topic_0020100181_p3367862711137"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100181_p1055821011465"><a name="en-us_topic_0020100181_p1055821011465"></a><a name="en-us_topic_0020100181_p1055821011465"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.46534653465347%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100181_p4309393211137"><a name="en-us_topic_0020100181_p4309393211137"></a><a name="en-us_topic_0020100181_p4309393211137"></a>Specifies the load balancer ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100181_section56202265"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100181_section36058338"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100181_table38797799154536"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100181_row12879063154536"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100181_p36571173154536"><a name="en-us_topic_0020100181_p36571173154536"></a><a name="en-us_topic_0020100181_p36571173154536"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100181_p66709919173720"><a name="en-us_topic_0020100181_p66709919173720"></a><a name="en-us_topic_0020100181_p66709919173720"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100181_p29280751154536"><a name="en-us_topic_0020100181_p29280751154536"></a><a name="en-us_topic_0020100181_p29280751154536"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100181_row22930619154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p45440811154536"><a name="en-us_topic_0020100181_p45440811154536"></a><a name="en-us_topic_0020100181_p45440811154536"></a>vip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p66880630173720"><a name="en-us_topic_0020100181_p66880630173720"></a><a name="en-us_topic_0020100181_p66880630173720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p39588120154536"><a name="en-us_topic_0020100181_p39588120154536"></a><a name="en-us_topic_0020100181_p39588120154536"></a>Specifies the private IP address of the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row6164181111450"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p2693082811450"><a name="en-us_topic_0020100181_p2693082811450"></a><a name="en-us_topic_0020100181_p2693082811450"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p3391346511450"><a name="en-us_topic_0020100181_p3391346511450"></a><a name="en-us_topic_0020100181_p3391346511450"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p6263616311450"><a name="en-us_topic_0020100181_p6263616311450"></a><a name="en-us_topic_0020100181_p6263616311450"></a>Specifies the time when the load balancer was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row20748768154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p2928667154536"><a name="en-us_topic_0020100181_p2928667154536"></a><a name="en-us_topic_0020100181_p2928667154536"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p34944702173720"><a name="en-us_topic_0020100181_p34944702173720"></a><a name="en-us_topic_0020100181_p34944702173720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p21853298154536"><a name="en-us_topic_0020100181_p21853298154536"></a><a name="en-us_topic_0020100181_p21853298154536"></a>Specifies the time when the load balancer was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row62461962154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p1135078611104"><a name="en-us_topic_0020100181_p1135078611104"></a><a name="en-us_topic_0020100181_p1135078611104"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p4699849111104"><a name="en-us_topic_0020100181_p4699849111104"></a><a name="en-us_topic_0020100181_p4699849111104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p4878139611104"><a name="en-us_topic_0020100181_p4878139611104"></a><a name="en-us_topic_0020100181_p4878139611104"></a>Specifies the load balancer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row631943154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p631479011955"><a name="en-us_topic_0020100181_p631479011955"></a><a name="en-us_topic_0020100181_p631479011955"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p4173598611955"><a name="en-us_topic_0020100181_p4173598611955"></a><a name="en-us_topic_0020100181_p4173598611955"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100181_ul45789432115254"></a><a name="en-us_topic_0020100181_ul45789432115254"></a><ul id="en-us_topic_0020100181_ul45789432115254"><li>Specifies the load balancer status.</li><li>The value can be <strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>, <strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_CREATE</strong>, or <strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row50427566154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p2945151311955"><a name="en-us_topic_0020100181_p2945151311955"></a><a name="en-us_topic_0020100181_p2945151311955"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p3676238611955"><a name="en-us_topic_0020100181_p3676238611955"></a><a name="en-us_topic_0020100181_p3676238611955"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p2496329511955"><a name="en-us_topic_0020100181_p2496329511955"></a><a name="en-us_topic_0020100181_p2496329511955"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row3146654154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p1174043611955"><a name="en-us_topic_0020100181_p1174043611955"></a><a name="en-us_topic_0020100181_p1174043611955"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p1145125111955"><a name="en-us_topic_0020100181_p1145125111955"></a><a name="en-us_topic_0020100181_p1145125111955"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p5513616311955"><a name="en-us_topic_0020100181_p5513616311955"></a><a name="en-us_topic_0020100181_p5513616311955"></a>Specifies the VPC ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row49351679154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p61969157111046"><a name="en-us_topic_0020100181_p61969157111046"></a><a name="en-us_topic_0020100181_p61969157111046"></a>admin_state_up</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p53445833111046"><a name="en-us_topic_0020100181_p53445833111046"></a><a name="en-us_topic_0020100181_p53445833111046"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100181_ul14298889191452"></a><a name="en-us_topic_0020100181_ul14298889191452"></a><ul id="en-us_topic_0020100181_ul14298889191452"><li>Specifies the administrative status of the load balancer.</li><li>The following options are available:<p id="en-us_topic_0020100181_p6220739912018"><a name="en-us_topic_0020100181_p6220739912018"></a><a name="en-us_topic_0020100181_p6220739912018"></a><strong id="b842352706153922"><a name="b842352706153922"></a><a name="b842352706153922"></a>0</strong>: The load balancer is disabled.</p>
    <p id="en-us_topic_0020100181_p2299568012018"><a name="en-us_topic_0020100181_p2299568012018"></a><a name="en-us_topic_0020100181_p2299568012018"></a><strong id="b842352706153248"><a name="b842352706153248"></a><a name="b842352706153248"></a>1</strong>: The load balancer is running properly.</p>
    <p id="en-us_topic_0020100181_p563453512018"><a name="en-us_topic_0020100181_p563453512018"></a><a name="en-us_topic_0020100181_p563453512018"></a><strong id="b842352706153951"><a name="b842352706153951"></a><a name="b842352706153951"></a>2</strong>: The load balancer is frozen.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row41835454154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p48869218111035"><a name="en-us_topic_0020100181_p48869218111035"></a><a name="en-us_topic_0020100181_p48869218111035"></a>vip_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p66092577111035"><a name="en-us_topic_0020100181_p66092577111035"></a><a name="en-us_topic_0020100181_p66092577111035"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p3089518894328"><a name="en-us_topic_0020100181_p3089518894328"></a><a name="en-us_topic_0020100181_p3089518894328"></a>This parameter is unavailable now.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row55880660154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p63091299111035"><a name="en-us_topic_0020100181_p63091299111035"></a><a name="en-us_topic_0020100181_p63091299111035"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p10121556111035"><a name="en-us_topic_0020100181_p10121556111035"></a><a name="en-us_topic_0020100181_p10121556111035"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p244506294115"><a name="en-us_topic_0020100181_p244506294115"></a><a name="en-us_topic_0020100181_p244506294115"></a>Specifies the network type of the load balancer. The value is <strong>External</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row54105599154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p20477368154536"><a name="en-us_topic_0020100181_p20477368154536"></a><a name="en-us_topic_0020100181_p20477368154536"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p54023230173717"><a name="en-us_topic_0020100181_p54023230173717"></a><a name="en-us_topic_0020100181_p54023230173717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p65835154536"><a name="en-us_topic_0020100181_p65835154536"></a><a name="en-us_topic_0020100181_p65835154536"></a>Specifies the load balancer name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row592517154536"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p47993955154536"><a name="en-us_topic_0020100181_p47993955154536"></a><a name="en-us_topic_0020100181_p47993955154536"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p13805519173717"><a name="en-us_topic_0020100181_p13805519173717"></a><a name="en-us_topic_0020100181_p13805519173717"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100181_p13552980154536"><a name="en-us_topic_0020100181_p13552980154536"></a><a name="en-us_topic_0020100181_p13552980154536"></a>Provides supplementary information about the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row23840945191541"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100181_p10873506191544"><a name="en-us_topic_0020100181_p10873506191544"></a><a name="en-us_topic_0020100181_p10873506191544"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100181_p8338814191544"><a name="en-us_topic_0020100181_p8338814191544"></a><a name="en-us_topic_0020100181_p8338814191544"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100181_ul54299390191544"></a><a name="en-us_topic_0020100181_ul54299390191544"></a><ul id="en-us_topic_0020100181_ul54299390191544"><li>Specifies the security group ID.</li><li><strong id="b842352706113355"><a name="b842352706113355"></a><a name="b842352706113355"></a>null</strong> is displayed for this parameter when <strong id="b842352706113359"><a name="b842352706113359"></a><a name="b842352706113359"></a>type</strong> is set to <strong id="b84235270611343"><a name="b84235270611343"></a><a name="b84235270611343"></a>External</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
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
    ```


## Status Code<a name="en-us_topic_0020100181_section56089592"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100181_table36820689151427"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100181_row31910225151427"><th class="cellrowborder" valign="top" width="13.170000000000002%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100181_p34591398151427"><a name="en-us_topic_0020100181_p34591398151427"></a><a name="en-us_topic_0020100181_p34591398151427"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.589999999999996%" id="mcps1.1.4.1.2"><p id="p22841455542"><a name="p22841455542"></a><a name="p22841455542"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100181_p50439831151427"><a name="en-us_topic_0020100181_p50439831151427"></a><a name="en-us_topic_0020100181_p50439831151427"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100181_row59094542151427"><td class="cellrowborder" valign="top" width="13.170000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100181_p21928560151427"><a name="en-us_topic_0020100181_p21928560151427"></a><a name="en-us_topic_0020100181_p21928560151427"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1290961815541"><a name="p1290961815541"></a><a name="p1290961815541"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100181_p31382951151427"><a name="en-us_topic_0020100181_p31382951151427"></a><a name="en-us_topic_0020100181_p31382951151427"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row14011110151427"><td class="cellrowborder" valign="top" width="13.170000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100181_p61158135151427"><a name="en-us_topic_0020100181_p61158135151427"></a><a name="en-us_topic_0020100181_p61158135151427"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p19092188549"><a name="p19092188549"></a><a name="p19092188549"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100181_p54861904151427"><a name="en-us_topic_0020100181_p54861904151427"></a><a name="en-us_topic_0020100181_p54861904151427"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row23995096151427"><td class="cellrowborder" valign="top" width="13.170000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100181_p64554609151427"><a name="en-us_topic_0020100181_p64554609151427"></a><a name="en-us_topic_0020100181_p64554609151427"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p9909111818542"><a name="p9909111818542"></a><a name="p9909111818542"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100181_p61540839151427"><a name="en-us_topic_0020100181_p61540839151427"></a><a name="en-us_topic_0020100181_p61540839151427"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row16996640151427"><td class="cellrowborder" valign="top" width="13.170000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100181_p34550571151427"><a name="en-us_topic_0020100181_p34550571151427"></a><a name="en-us_topic_0020100181_p34550571151427"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p49091918115413"><a name="p49091918115413"></a><a name="p49091918115413"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100181_p47132871151427"><a name="en-us_topic_0020100181_p47132871151427"></a><a name="en-us_topic_0020100181_p47132871151427"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row21542659151427"><td class="cellrowborder" valign="top" width="13.170000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100181_p124922151427"><a name="en-us_topic_0020100181_p124922151427"></a><a name="en-us_topic_0020100181_p124922151427"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1190910188546"><a name="p1190910188546"></a><a name="p1190910188546"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100181_p10118742151427"><a name="en-us_topic_0020100181_p10118742151427"></a><a name="en-us_topic_0020100181_p10118742151427"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100181_row23959822151427"><td class="cellrowborder" valign="top" width="13.170000000000002%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100181_p61697404151427"><a name="en-us_topic_0020100181_p61697404151427"></a><a name="en-us_topic_0020100181_p61697404151427"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1190971835411"><a name="p1190971835411"></a><a name="p1190971835411"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100181_p31433794151427"><a name="en-us_topic_0020100181_p31433794151427"></a><a name="en-us_topic_0020100181_p31433794151427"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


