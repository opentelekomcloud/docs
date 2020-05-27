# Querying a Virtual Gateway List<a name="en-dc_topic_0055025323"></a>

## Function<a name="section17487184"></a>

This API is used to query a virtual gateway list.

## URI<a name="section23166934"></a>

GET /v2.0/dcaas/virtual-gateways

## Request<a name="section64582388"></a>

[Table 1](#table2198437322244)  lists the request parameter.

**Table  1**  Request parameter

<a name="table2198437322244"></a>
<table><thead align="left"><tr id="row4304807922244"><th class="cellrowborder" valign="top" width="17.88178817881788%" id="mcps1.2.5.1.1"><p id="p6505580022244"><a name="p6505580022244"></a><a name="p6505580022244"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.43164316431643%" id="mcps1.2.5.1.2"><p id="p329696222244"><a name="p329696222244"></a><a name="p329696222244"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.94179417941794%" id="mcps1.2.5.1.3"><p id="p3257067222244"><a name="p3257067222244"></a><a name="p3257067222244"></a><strong id="b842352706192549"><a name="b842352706192549"></a><a name="b842352706192549"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.74477447744774%" id="mcps1.2.5.1.4"><p id="p5470821922244"><a name="p5470821922244"></a><a name="p5470821922244"></a><strong id="b84235270615331"><a name="b84235270615331"></a><a name="b84235270615331"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5451891922244"><td class="cellrowborder" valign="top" width="17.88178817881788%" headers="mcps1.2.5.1.1 "><p id="p6157819622316"><a name="p6157819622316"></a><a name="p6157819622316"></a>fields</p>
</td>
<td class="cellrowborder" valign="top" width="16.43164316431643%" headers="mcps1.2.5.1.2 "><p id="p757920222316"><a name="p757920222316"></a><a name="p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.94179417941794%" headers="mcps1.2.5.1.3 "><p id="p4706384922316"><a name="p4706384922316"></a><a name="p4706384922316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="47.74477447744774%" headers="mcps1.2.5.1.4 "><p id="p63361141143756"><a name="p63361141143756"></a><a name="p63361141143756"></a>Specifies the parameters expected to be returned.</p>
<p id="p970883222316"><a name="p970883222316"></a><a name="p970883222316"></a>If you do not specify it, all parameters will be returned.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section44370581"></a>

[Table 2](#table50992744154526)  lists the response parameter.

**Table  2**  Response parameter

<a name="table50992744154526"></a>
<table><thead align="left"><tr id="row20073554154526"><th class="cellrowborder" valign="top" width="23.09%" id="mcps1.2.4.1.1"><p id="p15345186154526"><a name="p15345186154526"></a><a name="p15345186154526"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.590000000000003%" id="mcps1.2.4.1.2"><p id="p35000534154526"><a name="p35000534154526"></a><a name="p35000534154526"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.32%" id="mcps1.2.4.1.3"><p id="p59082508154526"><a name="p59082508154526"></a><a name="p59082508154526"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20953821154526"><td class="cellrowborder" valign="top" width="23.09%" headers="mcps1.2.4.1.1 "><p id="p19537972154526"><a name="p19537972154526"></a><a name="p19537972154526"></a>virtual_gateways</p>
</td>
<td class="cellrowborder" valign="top" width="25.590000000000003%" headers="mcps1.2.4.1.2 "><p id="p39071862154526"><a name="p39071862154526"></a><a name="p39071862154526"></a>List data structure</p>
</td>
<td class="cellrowborder" valign="top" width="51.32%" headers="mcps1.2.4.1.3 "><p id="p61739489154526"><a name="p61739489154526"></a><a name="p61739489154526"></a>Specifies the virtual gateway list.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **virtual\_gateways**

<a name="table14681450"></a>
<table><thead align="left"><tr id="row21069217"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.1.4.1.1"><p id="p28885026"><a name="p28885026"></a><a name="p28885026"></a><strong id="b762460439"><a name="b762460439"></a><a name="b762460439"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.1.4.1.2"><p id="p57985771"><a name="p57985771"></a><a name="p57985771"></a><strong id="b2005236602"><a name="b2005236602"></a><a name="b2005236602"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.1.4.1.3"><p id="p4499576"><a name="p4499576"></a><a name="p4499576"></a><strong id="b96699412"><a name="b96699412"></a><a name="b96699412"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6614602622620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p4410666095934"><a name="p4410666095934"></a><a name="p4410666095934"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p6119820395934"><a name="p6119820395934"></a><a name="p6119820395934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p3725148995934"><a name="p3725148995934"></a><a name="p3725148995934"></a>Specifies the virtual gateway ID.</p>
</td>
</tr>
<tr id="row4620915422620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p4142756795934"><a name="p4142756795934"></a><a name="p4142756795934"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p474352395934"><a name="p474352395934"></a><a name="p474352395934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p4213020095934"><a name="p4213020095934"></a><a name="p4213020095934"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row1146602622620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p1771069495934"><a name="p1771069495934"></a><a name="p1771069495934"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p2802222795934"><a name="p2802222795934"></a><a name="p2802222795934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p1927422595934"><a name="p1927422595934"></a><a name="p1927422595934"></a>Specifies the virtual gateway name.</p>
</td>
</tr>
<tr id="row2411573022620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p5772182395934"><a name="p5772182395934"></a><a name="p5772182395934"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p5016039595934"><a name="p5016039595934"></a><a name="p5016039595934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p3667684995934"><a name="p3667684995934"></a><a name="p3667684995934"></a>Provides supplementary information about the virtual gateway.</p>
</td>
</tr>
<tr id="row1544898622620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p2229284495934"><a name="p2229284495934"></a><a name="p2229284495934"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p4585369595934"><a name="p4585369595934"></a><a name="p4585369595934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p3904531295934"><a name="p3904531295934"></a><a name="p3904531295934"></a>Specifies the ID of the VPC to be accessed.</p>
</td>
</tr>
<tr id="row1078246722620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p2632726195934"><a name="p2632726195934"></a><a name="p2632726195934"></a>local_ep_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p2826674395934"><a name="p2826674395934"></a><a name="p2826674395934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p1358305195934"><a name="p1358305195934"></a><a name="p1358305195934"></a>Specifies the ID of the local endpoint group that records CIDRs of the VPC.</p>
</td>
</tr>
<tr id="row6138324222620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p6675646995934"><a name="p6675646995934"></a><a name="p6675646995934"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p2459927595934"><a name="p2459927595934"></a><a name="p2459927595934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p6206511595934"><a name="p6206511595934"></a><a name="p6206511595934"></a>Specifies the ID of the physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row1031192022620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p1704743995934"><a name="p1704743995934"></a><a name="p1704743995934"></a>redundant_device_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p2710879795934"><a name="p2710879795934"></a><a name="p2710879795934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p6438210695934"><a name="p6438210695934"></a><a name="p6438210695934"></a>Specifies the ID of the redundant physical device used by the virtual gateway.</p>
</td>
</tr>
<tr id="row29937037142658"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p57549299142715"><a name="p57549299142715"></a><a name="p57549299142715"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p30981615142715"><a name="p30981615142715"></a><a name="p30981615142715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p64741166142715"><a name="p64741166142715"></a><a name="p64741166142715"></a>Specifies the virtual gateway type. The value can be <strong id="b842352706232310"><a name="b842352706232310"></a><a name="b842352706232310"></a>default</strong> or <strong id="b842352706232316"><a name="b842352706232316"></a><a name="b842352706232316"></a>double ipsec</strong>.</p>
</td>
</tr>
<tr id="row27628292163342"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p1829987416347"><a name="p1829987416347"></a><a name="p1829987416347"></a>bgp_asn</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p589485016347"><a name="p589485016347"></a><a name="p589485016347"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p2140981216347"><a name="p2140981216347"></a><a name="p2140981216347"></a>Specifies the AS number of the BGP peer.</p>
</td>
</tr>
<tr id="row25712038104241"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p21235294104244"><a name="p21235294104244"></a><a name="p21235294104244"></a>ipsec_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p42337257104244"><a name="p42337257104244"></a><a name="p42337257104244"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p11156324104244"><a name="p11156324104244"></a><a name="p11156324104244"></a>Specifies the IPsec VPN access bandwidth in Mbit/s.</p>
</td>
</tr>
<tr id="row5093362822620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p2832203195934"><a name="p2832203195934"></a><a name="p2832203195934"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p4114450195934"><a name="p4114450195934"></a><a name="p4114450195934"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p14681583143836"><a name="p14681583143836"></a><a name="p14681583143836"></a>Specifies the virtual gateway status.</p>
<p id="p4594310595934"><a name="p4594310595934"></a><a name="p4594310595934"></a>The value can be <strong id="b84235270617169"><a name="b84235270617169"></a><a name="b84235270617169"></a>ACTIVE</strong>, <strong id="b842352706171613"><a name="b842352706171613"></a><a name="b842352706171613"></a>DOWN</strong>, <strong id="b842352706171618"><a name="b842352706171618"></a><a name="b842352706171618"></a>BUILD</strong>, <strong id="b842352706171622"><a name="b842352706171622"></a><a name="b842352706171622"></a>ERROR</strong>, <strong id="b842352706171626"><a name="b842352706171626"></a><a name="b842352706171626"></a>PENDING_CREATE</strong>, <strong id="b842352706171630"><a name="b842352706171630"></a><a name="b842352706171630"></a>PENDING_UPDATE</strong>, or <strong id="b842352706171633"><a name="b842352706171633"></a><a name="b842352706171633"></a>PENDING_DELETE</strong>.</p>
</td>
</tr>
<tr id="row1902755522620"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p4615681195934"><a name="p4615681195934"></a><a name="p4615681195934"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p5200368295934"><a name="p5200368295934"></a><a name="p5200368295934"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p62295959143844"><a name="p62295959143844"></a><a name="p62295959143844"></a>Specifies the administrative state of the virtual gateway.</p>
<p id="p5896416595934"><a name="p5896416595934"></a><a name="p5896416595934"></a>The value can be <strong id="b842352706154840"><a name="b842352706154840"></a><a name="b842352706154840"></a>true</strong> or <strong id="b842352706154844"><a name="b842352706154844"></a><a name="b842352706154844"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section63790914"></a>

-   Example request

    1.  All parameters are returned:

    ```
    GET /v2.0/dcaas/virtual-gateways
    ```

    1.  Filtered parameters are returned \(for example, the filter is ID\):

    ```
    GET /v2.0/dcaas/virtual-gateways?id=7ec892f3-ca64-46c7-863f-a2eb1b9e8389
    ```


-   Example response

    ```
    {
        "virtual_gateways" : [{
            "id" : "7ec892f3-ca64-46c7-863f-a2eb1b9e8389",                       
            "tenant_id" : "6fbe9263116a4b68818cf1edce16bc4f",
            "name" : "virtual gateway1",
            "description" : "",
            "vpc_id" : "908d9cf3-da64-4acb-393f-e5eb6b9e838a",
            "local_ep_group_id" : "f8834cf1-5468-87c7-223d-56e78b9699ab",
            "device_id" : "aaa_01"
        }]
    }
    ```


## Returned Value<a name="section43233365173224"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

