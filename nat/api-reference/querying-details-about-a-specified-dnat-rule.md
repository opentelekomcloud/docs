# Querying Details About a Specified DNAT Rule<a name="nat_api_0013"></a>

## Function<a name="section242916116504"></a>

This API is used to query details about a specified DNAT rule.

## URI<a name="section55252672165026"></a>

GET /v2.0/dnat\_rules/\{dnat\_rule\_id\}

**Table  1**  Parameter description

<a name="table41603310017"></a>
<table><thead align="left"><tr id="row323012314017"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p1023043508"><a name="p1023043508"></a><a name="p1023043508"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.2"><p id="p1823017318015"><a name="p1823017318015"></a><a name="p1823017318015"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p52301036011"><a name="p52301036011"></a><a name="p52301036011"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.5.1.4"><p id="p7230330014"><a name="p7230330014"></a><a name="p7230330014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9230031106"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p1823033907"><a name="p1823033907"></a><a name="p1823033907"></a>dnat_rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.2 "><p id="p42301335017"><a name="p42301335017"></a><a name="p42301335017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p623013311018"><a name="p623013311018"></a><a name="p623013311018"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p5230735019"><a name="p5230735019"></a><a name="p5230735019"></a>Specifies the DNAT rule ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section30445355165052"></a>

None

## Response<a name="section1412948816517"></a>

[Table 2](#table66411570165117)  lists response parameters.

**Table  2**  Response parameters

<a name="table66411570165117"></a>
<table><thead align="left"><tr id="row43436947165117"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p28731843165117"><a name="p28731843165117"></a><a name="p28731843165117"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="38%" id="mcps1.2.4.1.2"><p id="p45577964165117"><a name="p45577964165117"></a><a name="p45577964165117"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.2.4.1.3"><p id="p67033414165117"><a name="p67033414165117"></a><a name="p67033414165117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row60997448165117"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p41846242165117"><a name="p41846242165117"></a><a name="p41846242165117"></a>dnat_rule</p>
</td>
<td class="cellrowborder" valign="top" width="38%" headers="mcps1.2.4.1.2 "><p id="p34102461165117"><a name="p34102461165117"></a><a name="p34102461165117"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.4.1.3 "><p id="p5298260165117"><a name="p5298260165117"></a><a name="p5298260165117"></a>Specifies the DNAT rule object. For details, see <a href="#table9899152414719">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **dnat\_rule**  field

<a name="table9899152414719"></a>
<table><thead align="left"><tr id="row198997241973"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p3368163219712"><a name="p3368163219712"></a><a name="p3368163219712"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p23681832770"><a name="p23681832770"></a><a name="p23681832770"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p23681432671"><a name="p23681432671"></a><a name="p23681432671"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row88993241676"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1136816321074"><a name="p1136816321074"></a><a name="p1136816321074"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1236803212715"><a name="p1236803212715"></a><a name="p1236803212715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p636818322071"><a name="p636818322071"></a><a name="p636818322071"></a>Specifies the DNAT rule ID.</p>
</td>
</tr>
<tr id="row198999241712"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15368632273"><a name="p15368632273"></a><a name="p15368632273"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6368132672"><a name="p6368132672"></a><a name="p6368132672"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4368193211713"><a name="p4368193211713"></a><a name="p4368193211713"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row18993246715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10368143213712"><a name="p10368143213712"></a><a name="p10368143213712"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p03681132579"><a name="p03681132579"></a><a name="p03681132579"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p0368163220715"><a name="p0368163220715"></a><a name="p0368163220715"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
<tr id="row1899924074"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p0368183220715"><a name="p0368183220715"></a><a name="p0368183220715"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12368932672"><a name="p12368932672"></a><a name="p12368932672"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3368132676"><a name="p3368132676"></a><a name="p3368132676"></a>Specifies the port ID of an ECS or a BMS.</p>
</td>
</tr>
<tr id="row38991524672"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p836823213715"><a name="p836823213715"></a><a name="p836823213715"></a>private_ip</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1636843210716"><a name="p1636843210716"></a><a name="p1636843210716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2036803210718"><a name="p2036803210718"></a><a name="p2036803210718"></a>Specifies the private IP address, for example, the IP address of a Direct Connect connection.</p>
</td>
</tr>
<tr id="row48998241373"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p936811322076"><a name="p936811322076"></a><a name="p936811322076"></a>internal_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6368153211712"><a name="p6368153211712"></a><a name="p6368153211712"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15368123218715"><a name="p15368123218715"></a><a name="p15368123218715"></a>Specifies the port used by ECSs or BMSs to provide services for external systems.</p>
</td>
</tr>
<tr id="row1789914241878"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43681532970"><a name="p43681532970"></a><a name="p43681532970"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p123684326717"><a name="p123684326717"></a><a name="p123684326717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p93683323710"><a name="p93683323710"></a><a name="p93683323710"></a>Specifies the EIP ID.</p>
</td>
</tr>
<tr id="row7899102413716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1336843213714"><a name="p1336843213714"></a><a name="p1336843213714"></a>floating_ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p536820321572"><a name="p536820321572"></a><a name="p536820321572"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p193681532072"><a name="p193681532072"></a><a name="p193681532072"></a>Specifies the EIP.</p>
</td>
</tr>
<tr id="row889916241373"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p73686321175"><a name="p73686321175"></a><a name="p73686321175"></a>external_service_port</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1836813210719"><a name="p1836813210719"></a><a name="p1836813210719"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p73683325711"><a name="p73683325711"></a><a name="p73683325711"></a>Specifies the port for providing external services.</p>
</td>
</tr>
<tr id="row489932414710"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17368232474"><a name="p17368232474"></a><a name="p17368232474"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p163683321719"><a name="p163683321719"></a><a name="p163683321719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p336893219716"><a name="p336893219716"></a><a name="p336893219716"></a>Specifies the protocol type. Currently, TCP, UDP, and ANY are supported.</p>
<p id="p9368432271"><a name="p9368432271"></a><a name="p9368432271"></a>The protocol number of TCP, UDP, and ANY are 6, 17, and 0, respectively.</p>
</td>
</tr>
<tr id="row389917241879"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1736833215711"><a name="p1736833215711"></a><a name="p1736833215711"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p736853214714"><a name="p736853214714"></a><a name="p736853214714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul113681321476"></a><a name="ul113681321476"></a><ul id="ul113681321476"><li>Specifies the status of the DNAT rule.</li><li>For details about all its values, see <a href="resource-status-description.md#table1390614366107">Table 1</a>.</li></ul>
</td>
</tr>
<tr id="row1589910244715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1836883218715"><a name="p1836883218715"></a><a name="p1836883218715"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1764614265487"><a name="p1764614265487"></a><a name="p1764614265487"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul71858556358"></a><a name="ul71858556358"></a><ul id="ul71858556358"><li>Specifies whether the DNAT rule is enabled or disabled.</li><li>The value can be:<a name="ul16205638124410"></a><a name="ul16205638124410"></a><ul id="ul16205638124410"><li><strong id="b11463142018248"><a name="b11463142018248"></a><a name="b11463142018248"></a>true</strong>: The DNAT rule is enabled.</li><li><strong id="b15330112114246"><a name="b15330112114246"></a><a name="b15330112114246"></a>false</strong>: The DNAT rule is disabled.</li></ul>
</li></ul>
</td>
</tr>
<tr id="row28997241277"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13368332977"><a name="p13368332977"></a><a name="p13368332977"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p136853217716"><a name="p136853217716"></a><a name="p136853217716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15924948201"><a name="p15924948201"></a><a name="p15924948201"></a>Specifies when the DNAT rule is created (UTC time). Its value rounds to 6 decimal places for seconds. The format is yyyy-mm-dd hh:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section24779297165121"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/dnat_rules/5b95c675-69c2-4656-ba06-58ff72e1d338
    ```


-   Example response

    ```
    {              
    　　"dnat_rule": {
        　　"floating_ip_id": "bf99c679-9f41-4dac-8513-9c9228e713e1",
       　　 "status": "ACTIVE",
        　　"nat_gateway_id": "cda3a125-2406-456c-a11f-598e10578541",
       　　 "admin_state_up": true,
       　　 "port_id": "9a469561-daac-4c94-88f5-39366e5ea193",
        　　"internal_service_port": 993,
        　　"protocol": "TCP",
        　　"tenant_id": "abc",
        　　"created_at": "2017-11-15 15:44:42.595173",
        　　"id": "79195d50-0271-41f1-bded-4c089b2502ff",
        　　"floating_ip_address": "5.21.11.226",
       　　 "external_service_port": 242
        　　"private_ip": ""  
       }
    }
    ```


## Status Code<a name="section16249219165526"></a>

See  [Status Codes](status-codes.md).

