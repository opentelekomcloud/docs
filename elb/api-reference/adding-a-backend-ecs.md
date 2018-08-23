# Adding a Backend ECS<a name="EN-US_TOPIC_0096561556"></a>

## Function<a name="section12327657133113"></a>

This API is used to add a backend ECS of a specific backend ECS group.

## API Format<a name="en-us_topic_0049139657_section1420113"></a>

<a name="en-us_topic_0049139657_table19082474"></a><table><thead align="left"><tr id="en-us_topic_0049139657_row53389951"><th class="firstcol" valign="top" width="12.120000000000001%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139657_p29618759"><a name="en-us_topic_0049139657_p29618759"></a><a name="en-us_topic_0049139657_p29618759"></a><strong id="b842352706172312"><a name="b842352706172312"></a><a name="b842352706172312"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="54.55%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139657_p50309255"><a name="en-us_topic_0049139657_p50309255"></a><a name="en-us_topic_0049139657_p50309255"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139657_p48517864"><a name="en-us_topic_0049139657_p48517864"></a><a name="en-us_topic_0049139657_p48517864"></a><strong id="b842352706192251"><a name="b842352706192251"></a><a name="b842352706192251"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139657_row37632913"><th class="firstcol" valign="top" width="12.120000000000001%" id="mcps1.1.5.1.1" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139657_p28367147"><a name="en-us_topic_0049139657_p28367147"></a><a name="en-us_topic_0049139657_p28367147"></a>POST</p>
</th>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.1.5.1.1 mcps1.1.4.1.2 "><p id="en-us_topic_0049139657_p16037598"><a name="en-us_topic_0049139657_p16037598"></a><a name="en-us_topic_0049139657_p16037598"></a>/v2.0/lbaas/pools/{pool_id}/members</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.5.1.1 mcps1.1.4.1.3 "><p id="en-us_topic_0049139657_p23977041"><a name="en-us_topic_0049139657_p23977041"></a><a name="en-us_topic_0049139657_p23977041"></a>Adds a backend ECS that belongs to a specific backend ECS group.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139657_section12781022"></a>

-   Two backend ECSs in the same backend ECS group must have different IP addresses and ports.
-   The subnet specified during ECS creation and the subnet to which the VIP belongs must be in the same VPC.
-   The value of  **admin\_state\_up** must be **true**.

## Request<a name="en-us_topic_0049139657_section56342274"></a>

-   Parameter description

    <a name="en-us_topic_0049139657_table20060988"></a><table><thead align="left"><tr id="en-us_topic_0049139657_row42045429"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.1"><p id="en-us_topic_0049139657_p50236607"><a name="en-us_topic_0049139657_p50236607"></a><a name="en-us_topic_0049139657_p50236607"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.1.5.1.2"><p id="en-us_topic_0049139657_p42633357"><a name="en-us_topic_0049139657_p42633357"></a><a name="en-us_topic_0049139657_p42633357"></a><strong id="b84235270610580"><a name="b84235270610580"></a><a name="b84235270610580"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.3"><p id="en-us_topic_0049139657_p30749896"><a name="en-us_topic_0049139657_p30749896"></a><a name="en-us_topic_0049139657_p30749896"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.1.5.1.4"><p id="en-us_topic_0049139657_p7713623"><a name="en-us_topic_0049139657_p7713623"></a><a name="en-us_topic_0049139657_p7713623"></a><strong id="b842352706192251_1"><a name="b842352706192251_1"></a><a name="b842352706192251_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0049139657_row20823715"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0049139657_p8999315"><a name="en-us_topic_0049139657_p8999315"></a><a name="en-us_topic_0049139657_p8999315"></a>member</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0049139657_p57855887"><a name="en-us_topic_0049139657_p57855887"></a><a name="en-us_topic_0049139657_p57855887"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0049139657_p55815296"><a name="en-us_topic_0049139657_p55815296"></a><a name="en-us_topic_0049139657_p55815296"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0049139657_p24745166"><a name="en-us_topic_0049139657_p24745166"></a><a name="en-us_topic_0049139657_p24745166"></a>Specifies the backend ECS. For details, see <a href="overview-15.html#en-us_topic_0049139654_table10264733124058">Table 1</a>.</p>
    <p id="en-us_topic_0049139657_p21379907"><a name="en-us_topic_0049139657_p21379907"></a><a name="en-us_topic_0049139657_p21379907"></a>Fields <strong id="b842352706101842"><a name="b842352706101842"></a><a name="b842352706101842"></a>address</strong>,&nbsp;<strong id="b842352706101848"><a name="b842352706101848"></a><a name="b842352706101848"></a>protocol_port</strong>, and&nbsp;<strong id="b842352706101854"><a name="b842352706101854"></a><a name="b842352706101854"></a>subnet_id</strong> are mandatory.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST /v2.0/lbaas/pools/5a9a3e9e-d1aa-448e-af37-a70171f2a332/members
    {
        "member": {
            "subnet_id": "33d8b01a-bbe6-41f4-bc45-78a1d284d503",
            "protocol_port": "88",
            "name": "member-jy-tt-1",
            "address": "192.168.44.11"
        }
    }
    ```


## Response<a name="en-us_topic_0049139657_section37318421"></a>

-   Parameter description

    <a name="en-us_topic_0049139657_table54050919"></a><table><thead align="left"><tr id="en-us_topic_0049139657_row57900534"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.1.5.1.1"><p id="en-us_topic_0049139657_p59431671"><a name="en-us_topic_0049139657_p59431671"></a><a name="en-us_topic_0049139657_p59431671"></a><strong id="b842352706181819_1"><a name="b842352706181819_1"></a><a name="b842352706181819_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.1.5.1.2"><p id="en-us_topic_0049139657_p49236012"><a name="en-us_topic_0049139657_p49236012"></a><a name="en-us_topic_0049139657_p49236012"></a><strong id="b84235270610580_1"><a name="b84235270610580_1"></a><a name="b84235270610580_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.1.5.1.3"><p id="en-us_topic_0049139657_p28694013"><a name="en-us_topic_0049139657_p28694013"></a><a name="en-us_topic_0049139657_p28694013"></a><strong id="b8423527061798_1"><a name="b8423527061798_1"></a><a name="b8423527061798_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.1.5.1.4"><p id="en-us_topic_0049139657_p42513748"><a name="en-us_topic_0049139657_p42513748"></a><a name="en-us_topic_0049139657_p42513748"></a><strong id="b842352706192251_2"><a name="b842352706192251_2"></a><a name="b842352706192251_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0049139657_row21061526"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0049139657_p28262061"><a name="en-us_topic_0049139657_p28262061"></a><a name="en-us_topic_0049139657_p28262061"></a>member</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0049139657_p7525633"><a name="en-us_topic_0049139657_p7525633"></a><a name="en-us_topic_0049139657_p7525633"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0049139657_p5596537"><a name="en-us_topic_0049139657_p5596537"></a><a name="en-us_topic_0049139657_p5596537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0049139657_p50666366"><a name="en-us_topic_0049139657_p50666366"></a><a name="en-us_topic_0049139657_p50666366"></a>Specifies the backend ECS. For details, see <a href="overview-15.html#en-us_topic_0049139654_table10264733124058">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "member": {
            "name": "member-jy-tt-1",
            "weight": 1,
            "admin_state_up": true,
            "subnet_id": "33d8b01a-bbe6-41f4-bc45-78a1d284d503",
            "tenant_id": "145483a5107745e9b3d80f956713e6a3",
            "address": "192.168.44.11",
            "protocol_port": 88,
            "id": "c0042496-e220-44f6-914b-e6ca33bab503"
        }
    }
    ```


## Error Codes<a name="en-us_topic_0049139655_section64643717"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).

