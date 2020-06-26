# Querying Details About a Specified SNAT Rule<a name="nat_api_0008"></a>

## Function<a name="section59567946"></a>

This API is used to query details about a specified SNAT rule.

## URI<a name="section66349468"></a>

GET /v2.0/snat\_rules/\{snat\_rule\_id\}

**Table  1**  Parameter description

<a name="table1910716134591"></a>
<table><thead align="left"><tr id="row3169413135915"><th class="cellrowborder" valign="top" width="21.272127212721273%" id="mcps1.2.5.1.1"><p id="p16169131375910"><a name="p16169131375910"></a><a name="p16169131375910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.842084208420843%" id="mcps1.2.5.1.2"><p id="p151699135593"><a name="p151699135593"></a><a name="p151699135593"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.781578157815781%" id="mcps1.2.5.1.3"><p id="p1716915133591"><a name="p1716915133591"></a><a name="p1716915133591"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.104210421042104%" id="mcps1.2.5.1.4"><p id="p016991320594"><a name="p016991320594"></a><a name="p016991320594"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row131691913145916"><td class="cellrowborder" valign="top" width="21.272127212721273%" headers="mcps1.2.5.1.1 "><p id="p116919133595"><a name="p116919133595"></a><a name="p116919133595"></a>snat_rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.842084208420843%" headers="mcps1.2.5.1.2 "><p id="p6169171310597"><a name="p6169171310597"></a><a name="p6169171310597"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.781578157815781%" headers="mcps1.2.5.1.3 "><p id="p101695138597"><a name="p101695138597"></a><a name="p101695138597"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.104210421042104%" headers="mcps1.2.5.1.4 "><p id="p31691313145913"><a name="p31691313145913"></a><a name="p31691313145913"></a>Specifies the SNAT rule ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section5597798"></a>

None

## Response<a name="section50380184"></a>

[Table 2](#table65459315)  lists response parameters.

**Table  2**  Response parameters

<a name="table65459315"></a>
<table><thead align="left"><tr id="row47811128"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p47496137"><a name="p47496137"></a><a name="p47496137"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.050000000000004%" id="mcps1.2.4.1.2"><p id="p21981920"><a name="p21981920"></a><a name="p21981920"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p6428601"><a name="p6428601"></a><a name="p6428601"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row50954701"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p33690117"><a name="p33690117"></a><a name="p33690117"></a>snat_rule</p>
</td>
<td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p44544970"><a name="p44544970"></a><a name="p44544970"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p447513"><a name="p447513"></a><a name="p447513"></a>Specifies the SNAT rule object. For details, see <a href="#table113261845122312">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **snat\_rule**  field

<a name="table113261845122312"></a>
<table><thead align="left"><tr id="row3326164512310"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p144282010346"><a name="p144282010346"></a><a name="p144282010346"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1742881017412"><a name="p1742881017412"></a><a name="p1742881017412"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1442813106416"><a name="p1442813106416"></a><a name="p1442813106416"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row73267459231"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4180209175512"><a name="p4180209175512"></a><a name="p4180209175512"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p318018955517"><a name="p318018955517"></a><a name="p318018955517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p418017905520"><a name="p418017905520"></a><a name="p418017905520"></a>Specifies the SNAT rule ID.</p>
</td>
</tr>
<tr id="row11326845102317"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2180189185519"><a name="p2180189185519"></a><a name="p2180189185519"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11801797556"><a name="p11801797556"></a><a name="p11801797556"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6180499553"><a name="p6180499553"></a><a name="p6180499553"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row13261445132318"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1718019914553"><a name="p1718019914553"></a><a name="p1718019914553"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p318009145510"><a name="p318009145510"></a><a name="p318009145510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p21801692559"><a name="p21801692559"></a><a name="p21801692559"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row2032617455238"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1518016915520"><a name="p1518016915520"></a><a name="p1518016915520"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p181803945519"><a name="p181803945519"></a><a name="p181803945519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13180179195519"><a name="p13180179195519"></a><a name="p13180179195519"></a>Specifies the network ID used by the SNAT rule.</p>
</td>
</tr>
<tr id="row1632610451230"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p201802919559"><a name="p201802919559"></a><a name="p201802919559"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7180592555"><a name="p7180592555"></a><a name="p7180592555"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16180139205514"><a name="p16180139205514"></a><a name="p16180139205514"></a>Specifies a subset of the VPC subnet CIDR block or a CIDR block of Direct Connect connection.</p>
</td>
</tr>
<tr id="row11326645162317"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p0180129105513"><a name="p0180129105513"></a><a name="p0180129105513"></a>source_type</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1118089165512"><a name="p1118089165512"></a><a name="p1118089165512"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1118010920557"><a name="p1118010920557"></a><a name="p1118010920557"></a><strong id="b667415014212"><a name="b667415014212"></a><a name="b667415014212"></a>0</strong>: Either <strong id="b116749506215"><a name="b116749506215"></a><a name="b116749506215"></a>network_id</strong> or <strong id="b1767575012212"><a name="b1767575012212"></a><a name="b1767575012212"></a>cidr</strong> can be specified in a VPC.</p>
<p id="p61801291556"><a name="p61801291556"></a><a name="p61801291556"></a><strong id="b1717016385527"><a name="b1717016385527"></a><a name="b1717016385527"></a>1</strong>: Only <strong id="b18170438165213"><a name="b18170438165213"></a><a name="b18170438165213"></a>cidr</strong> can be specified over a Direct Connect connection.</p>
<p id="p131806910557"><a name="p131806910557"></a><a name="p131806910557"></a>If no value is entered, the default value <strong id="b14717415339"><a name="b14717415339"></a><a name="b14717415339"></a>0</strong> (VPC) is used.</p>
</td>
</tr>
<tr id="row4326104512234"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p891724055516"><a name="p891724055516"></a><a name="p891724055516"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39177408550"><a name="p39177408550"></a><a name="p39177408550"></a>String(4096)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul391714011555"></a><a name="ul391714011555"></a><ul id="ul391714011555"><li>Specifies the EIP ID. Multiple EIPs are separated using commas (,).</li><li>The maximum length of the ID is 4096 bytes.</li><li>The number of EIP IDs cannot exceed 20.</li></ul>
</td>
</tr>
<tr id="row2785103161819"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1791083317183"><a name="p1791083317183"></a><a name="p1791083317183"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p491023317185"><a name="p491023317185"></a><a name="p491023317185"></a>String(1024)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul39101233161818"></a><a name="ul39101233161818"></a><ul id="ul39101233161818"><li>Specifies the EIP. Multiple EIPs are separated using commas (,).</li><li>The maximum length is 1024 bytes.</li></ul>
</td>
</tr>
<tr id="row932614518236"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9917640115517"><a name="p9917640115517"></a><a name="p9917640115517"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1917204015553"><a name="p1917204015553"></a><a name="p1917204015553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul191724018551"></a><a name="ul191724018551"></a><ul id="ul191724018551"><li>Specifies the status of the SNAT rule.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row3326134518239"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1491714408557"><a name="p1491714408557"></a><a name="p1491714408557"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the SNAT rule is enabled or disabled.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b15680145614597"><a name="b15680145614597"></a><a name="b15680145614597"></a>true</strong>: The SNAT rule is enabled.</li><li><strong id="b142981259105917"><a name="b142981259105917"></a><a name="b142981259105917"></a>false</strong>: The SNAT rule is disabled.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row1932664512234"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p09171040115511"><a name="p09171040115511"></a><a name="p09171040115511"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1291734045514"><a name="p1291734045514"></a><a name="p1291734045514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1356911211605"><a name="p1356911211605"></a><a name="p1356911211605"></a>Specifies when the SNAT rule is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section50768476"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/snat_rules/5b95c675-69c2-4656-ba06-58ff72e1d338
    ```


-   Example response

    ```
    {
        "snat_rule": {
            "floating_ip_id": "bdc10a4c-d81a-41ec-adf7-de857f7c812a",
            "status": "ACTIVE",
            "nat_gateway_id": "a78fb3eb-1654-4710-8742-3fc49d5f04f8",
            "admin_state_up": true,
            "network_id": "eaad9cd6-2372-4be1-9535-9bd37210ae7b",
            "cidr": "null",
            "source_type":0,
            "tenant_id": "27e25061336f4af590faeabeb7fcd9a3",
            "created_at": "2017-11-18 07:54:21.665430",
            "id": "5b95c675-69c2-4656-ba06-58ff72e1d338",
            "floating_ip_address": "5.21.11.226"
        }
    }
    ```


## Status Code<a name="section1941962013172"></a>

See  [Status Codes](status-codes.md).

