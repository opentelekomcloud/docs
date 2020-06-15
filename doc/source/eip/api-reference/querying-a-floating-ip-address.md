# Querying a Floating IP Address<a name="eip_apifloatip_0002"></a>

## Function<a name="en-us_topic_0201534088_section3531165915238"></a>

This API is used to query details about a specific floating IP address accessible to the tenant submitting the request.

## URI<a name="en-us_topic_0201534088_section1853275913236"></a>

GET /v2.0/eip/floatingips\_v6/\{floatingip\_id\}

## Request Message<a name="en-us_topic_0201534088_section185401459192310"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}//v2.0/eip/floatingips_v6/2dedb5e7-cb70-4e78-b50f-d88c8321d161
    ```


## Response Message<a name="en-us_topic_0201534088_section1354175922310"></a>

-   Response parameter

    **Table  1**  Response parameter

    <a name="en-us_topic_0201534088_table854120598236"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534088_row14732159202314"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534088_p37325591234"><a name="en-us_topic_0201534088_p37325591234"></a><a name="en-us_topic_0201534088_p37325591234"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="8.89%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534088_p37321059132317"><a name="en-us_topic_0201534088_p37321059132317"></a><a name="en-us_topic_0201534088_p37321059132317"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534088_p873214590235"><a name="en-us_topic_0201534088_p873214590235"></a><a name="en-us_topic_0201534088_p873214590235"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534088_row973325912318"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p197331559192314"><a name="en-us_topic_0201534088_p197331559192314"></a><a name="en-us_topic_0201534088_p197331559192314"></a>floatingip</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p673318596231"><a name="en-us_topic_0201534088_p673318596231"></a><a name="en-us_topic_0201534088_p673318596231"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p673315592232"><a name="en-us_topic_0201534088_p673315592232"></a><a name="en-us_topic_0201534088_p673315592232"></a>Specifies the floating IP address list. For details, see <a href="#en-us_topic_0201534088_table870410995611">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **floatingip**  objects

    <a name="en-us_topic_0201534088_table870410995611"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534088_row0700189135615"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534088_p9993174855413"><a name="en-us_topic_0201534088_p9993174855413"></a><a name="en-us_topic_0201534088_p9993174855413"></a><strong id="en-us_topic_0201534088_b17507145211371"><a name="en-us_topic_0201534088_b17507145211371"></a><a name="en-us_topic_0201534088_b17507145211371"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.521952195219523%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534088_p16993194812541"><a name="en-us_topic_0201534088_p16993194812541"></a><a name="en-us_topic_0201534088_p16993194812541"></a><strong id="en-us_topic_0201534088_b8821145418376"><a name="en-us_topic_0201534088_b8821145418376"></a><a name="en-us_topic_0201534088_b8821145418376"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.14471447144714%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534088_p99938485541"><a name="en-us_topic_0201534088_p99938485541"></a><a name="en-us_topic_0201534088_p99938485541"></a><strong id="en-us_topic_0201534088_b1063157123716"><a name="en-us_topic_0201534088_b1063157123716"></a><a name="en-us_topic_0201534088_b1063157123716"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534088_row37012912566"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p109931248105412"><a name="en-us_topic_0201534088_p109931248105412"></a><a name="en-us_topic_0201534088_p109931248105412"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p209935484543"><a name="en-us_topic_0201534088_p209935484543"></a><a name="en-us_topic_0201534088_p209935484543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p1099384811549"><a name="en-us_topic_0201534088_p1099384811549"></a><a name="en-us_topic_0201534088_p1099384811549"></a>Specifies the floating IP address status. The value can be <strong id="en-us_topic_0201534088_b146573175592"><a name="en-us_topic_0201534088_b146573175592"></a><a name="en-us_topic_0201534088_b146573175592"></a>ACTIVE</strong>, <strong id="en-us_topic_0201534088_b7660111718599"><a name="en-us_topic_0201534088_b7660111718599"></a><a name="en-us_topic_0201534088_b7660111718599"></a>DOWN</strong>, or <strong id="en-us_topic_0201534088_b14663111755914"><a name="en-us_topic_0201534088_b14663111755914"></a><a name="en-us_topic_0201534088_b14663111755914"></a>ERROR</strong>.</p>
    <a name="en-us_topic_0201534088_ul10994124825413"></a><a name="en-us_topic_0201534088_ul10994124825413"></a><ul id="en-us_topic_0201534088_ul10994124825413"><li><strong id="en-us_topic_0201534088_b147921664381"><a name="en-us_topic_0201534088_b147921664381"></a><a name="en-us_topic_0201534088_b147921664381"></a>ACTIVE</strong> indicates that the floating IP address has been bound.</li><li><strong id="en-us_topic_0201534088_b29810710384"><a name="en-us_topic_0201534088_b29810710384"></a><a name="en-us_topic_0201534088_b29810710384"></a>ERROR</strong> indicates that the floating IP address is abnormal.</li><li><strong id="en-us_topic_0201534088_b35439916385"><a name="en-us_topic_0201534088_b35439916385"></a><a name="en-us_topic_0201534088_b35439916385"></a>DOWN</strong> indicates that the floating IP address has not been bound.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534088_row167025913568"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p6994144818541"><a name="en-us_topic_0201534088_p6994144818541"></a><a name="en-us_topic_0201534088_p6994144818541"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p1399416486549"><a name="en-us_topic_0201534088_p1399416486549"></a><a name="en-us_topic_0201534088_p1399416486549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p1899418480541"><a name="en-us_topic_0201534088_p1899418480541"></a><a name="en-us_topic_0201534088_p1899418480541"></a>Specifies the floating IP address ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534088_row0702139205615"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p29942484542"><a name="en-us_topic_0201534088_p29942484542"></a><a name="en-us_topic_0201534088_p29942484542"></a>floating_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p9994348155412"><a name="en-us_topic_0201534088_p9994348155412"></a><a name="en-us_topic_0201534088_p9994348155412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p8994174818549"><a name="en-us_topic_0201534088_p8994174818549"></a><a name="en-us_topic_0201534088_p8994174818549"></a>Specifies the floating IPv6 address.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534088_row1703179145613"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p119948483548"><a name="en-us_topic_0201534088_p119948483548"></a><a name="en-us_topic_0201534088_p119948483548"></a>floating_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p89942482546"><a name="en-us_topic_0201534088_p89942482546"></a><a name="en-us_topic_0201534088_p89942482546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p59942486544"><a name="en-us_topic_0201534088_p59942486544"></a><a name="en-us_topic_0201534088_p59942486544"></a>Specifies the external network ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534088_row17703189195616"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p99954487543"><a name="en-us_topic_0201534088_p99954487543"></a><a name="en-us_topic_0201534088_p99954487543"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p1999574817544"><a name="en-us_topic_0201534088_p1999574817544"></a><a name="en-us_topic_0201534088_p1999574817544"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p1199594812543"><a name="en-us_topic_0201534088_p1199594812543"></a><a name="en-us_topic_0201534088_p1199594812543"></a>Specifies the ID of the belonged router.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534088_row57031095569"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p399515488546"><a name="en-us_topic_0201534088_p399515488546"></a><a name="en-us_topic_0201534088_p399515488546"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p499534814543"><a name="en-us_topic_0201534088_p499534814543"></a><a name="en-us_topic_0201534088_p499534814543"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p16995248135411"><a name="en-us_topic_0201534088_p16995248135411"></a><a name="en-us_topic_0201534088_p16995248135411"></a>Specifies the port ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534088_row1670489145611"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p2099514875417"><a name="en-us_topic_0201534088_p2099514875417"></a><a name="en-us_topic_0201534088_p2099514875417"></a>fixed_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p1599514484541"><a name="en-us_topic_0201534088_p1599514484541"></a><a name="en-us_topic_0201534088_p1599514484541"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p6995134819542"><a name="en-us_topic_0201534088_p6995134819542"></a><a name="en-us_topic_0201534088_p6995134819542"></a>Specifies the private IP address of the associated port.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534088_row270409105619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534088_p139951748155418"><a name="en-us_topic_0201534088_p139951748155418"></a><a name="en-us_topic_0201534088_p139951748155418"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.521952195219523%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534088_p209957480545"><a name="en-us_topic_0201534088_p209957480545"></a><a name="en-us_topic_0201534088_p209957480545"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.14471447144714%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534088_p10487112"><a name="en-us_topic_0201534088_p10487112"></a><a name="en-us_topic_0201534088_p10487112"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "floatingip": {
        "id": "861a4c5b-b17b-4a1d-b653-f3e95dcb3345",
        "status": "DOWN",
        "router_id": null,
        "tenant_id": "26ae5181a416420998eb2093aaed84d9",
        "project_id": "26ae5181a416420998eb2093aaed84d9",
        "floating_network_id": "0a2228f2-7f8a-45f1-8e09-9039e1d09975",
        "fixed_ip_address": null,
        "floating_ip_address": "cdcd:910a:2222:5498:8475:1111:c613:16e3",
        "port_id": null,
        "created_at": "2019-03-26T09:52:41",
        "updated_at": "2019-03-26T09:52:45"
      }
    }
    ```


## Status Code<a name="en-us_topic_0201534088_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534088_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

