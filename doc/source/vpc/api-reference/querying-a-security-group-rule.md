# Querying a Security Group Rule<a name="vpc_sg02_0007"></a>

## Function<a name="section241393816235"></a>

This API is used to query details about a specific security group rule.

## URI<a name="section4708630216235"></a>

GET /v2.0/security-group-rules/\{security\_groups\_rules\_id\}

## Request Message<a name="section1121883416235"></a>

None

## Response Message<a name="section2503267016235"></a>

**Table  1**  Response parameter

<a name="table265337716235"></a>
<table><thead align="left"><tr id="row4122992216235"><th class="cellrowborder" valign="top" width="34.14658534146586%" id="mcps1.2.4.1.1"><p id="p6294639916235"><a name="p6294639916235"></a><a name="p6294639916235"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.628537146285373%" id="mcps1.2.4.1.2"><p id="p6682514016235"><a name="p6682514016235"></a><a name="p6682514016235"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22487751224878%" id="mcps1.2.4.1.3"><p id="p1721315516235"><a name="p1721315516235"></a><a name="p1721315516235"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1324978916235"><td class="cellrowborder" valign="top" width="34.14658534146586%" headers="mcps1.2.4.1.1 "><p id="p510999716235"><a name="p510999716235"></a><a name="p510999716235"></a>security_group_rule</p>
</td>
<td class="cellrowborder" valign="top" width="14.628537146285373%" headers="mcps1.2.4.1.2 "><p id="p1974626116235"><a name="p1974626116235"></a><a name="p1974626116235"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22487751224878%" headers="mcps1.2.4.1.3 "><p id="p4059418616235"><a name="p4059418616235"></a><a name="p4059418616235"></a>Specifies the security group rule list. For details, see <a href="#table655457801607">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Security Group Rule**  objects

<a name="table655457801607"></a>
<table><thead align="left"><tr id="row54478641607"><th class="cellrowborder" valign="top" width="26.669999999999998%" id="mcps1.2.4.1.1"><p id="p389969021607"><a name="p389969021607"></a><a name="p389969021607"></a><strong id="b887703715258"><a name="b887703715258"></a><a name="b887703715258"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.2"><p id="p36789391607"><a name="p36789391607"></a><a name="p36789391607"></a><strong id="b17831123913257"><a name="b17831123913257"></a><a name="b17831123913257"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p433861031607"><a name="p433861031607"></a><a name="p433861031607"></a><strong id="b16938114072519"><a name="b16938114072519"></a><a name="b16938114072519"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row134774871607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p269083981607"><a name="p269083981607"></a><a name="p269083981607"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p630670281607"><a name="p630670281607"></a><a name="p630670281607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p334792201607"><a name="p334792201607"></a><a name="p334792201607"></a>Specifies the security group rule ID.</p>
<p id="p529374054010"><a name="p529374054010"></a><a name="p529374054010"></a>This parameter is not mandatory when you query security group rules.</p>
</td>
</tr>
<tr id="row250554771607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p254411021607"><a name="p254411021607"></a><a name="p254411021607"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p505368621607"><a name="p505368621607"></a><a name="p505368621607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p480145951607"><a name="p480145951607"></a><a name="p480145951607"></a>Provides supplementary information about the security group rule.</p>
</td>
</tr>
<tr id="row569401671607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p115724181607"><a name="p115724181607"></a><a name="p115724181607"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p615991711607"><a name="p615991711607"></a><a name="p615991711607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p587796621607"><a name="p587796621607"></a><a name="p587796621607"></a>Specifies the ID of the belonged security group.</p>
</td>
</tr>
<tr id="row654332091607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p113008931607"><a name="p113008931607"></a><a name="p113008931607"></a>remote_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p170542961607"><a name="p170542961607"></a><a name="p170542961607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p141218971607"><a name="p141218971607"></a><a name="p141218971607"></a>Specifies the peer ID of the belonged security group.</p>
</td>
</tr>
<tr id="row9932071607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p657989401607"><a name="p657989401607"></a><a name="p657989401607"></a>direction</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p507988391607"><a name="p507988391607"></a><a name="p507988391607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p570991491607"><a name="p570991491607"></a><a name="p570991491607"></a>Specifies the direction of the traffic for which the security group rule takes effect.</p>
</td>
</tr>
<tr id="row97529031607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p478834691607"><a name="p478834691607"></a><a name="p478834691607"></a>remote_ip_prefix</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p622759951607"><a name="p622759951607"></a><a name="p622759951607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p146708701607"><a name="p146708701607"></a><a name="p146708701607"></a>Specifies the peer IP address segment.</p>
</td>
</tr>
<tr id="row315033981607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p163656291607"><a name="p163656291607"></a><a name="p163656291607"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p628340441607"><a name="p628340441607"></a><a name="p628340441607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p99902671607"><a name="p99902671607"></a><a name="p99902671607"></a>Specifies the protocol type or the IP protocol number.</p>
</td>
</tr>
<tr id="row551583771607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p97886331607"><a name="p97886331607"></a><a name="p97886331607"></a>port_range_max</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p343603851607"><a name="p343603851607"></a><a name="p343603851607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p188144701607"><a name="p188144701607"></a><a name="p188144701607"></a>Specifies the maximum port number. When ICMP is used, the value is the ICMP code.</p>
</td>
</tr>
<tr id="row456604071607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p630384091607"><a name="p630384091607"></a><a name="p630384091607"></a>port_range_min</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p337362901607"><a name="p337362901607"></a><a name="p337362901607"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p258562691607"><a name="p258562691607"></a><a name="p258562691607"></a>Specifies the minimum port number. If the ICMP protocol is used, this parameter indicates the ICMP type.</p>
<p id="p5690808615417"><a name="p5690808615417"></a><a name="p5690808615417"></a>When the TCP or UDP protocol is used, both <strong id="b395012147582"><a name="b395012147582"></a><a name="b395012147582"></a>port_range_max</strong> and <strong id="b99515141582"><a name="b99515141582"></a><a name="b99515141582"></a>port_range_min</strong> must be specified, and the <strong id="b1895241425813"><a name="b1895241425813"></a><a name="b1895241425813"></a>port_range_max</strong> value must be greater than the <strong id="b79530147587"><a name="b79530147587"></a><a name="b79530147587"></a>port_range_min</strong> value.</p>
<p id="p4241072615417"><a name="p4241072615417"></a><a name="p4241072615417"></a>When the ICMP protocol is used, if you specify the ICMP code (<strong id="b5775141635817"><a name="b5775141635817"></a><a name="b5775141635817"></a>port_range_max</strong>), you must also specify the ICMP type (<strong id="b1477641617584"><a name="b1477641617584"></a><a name="b1477641617584"></a>port_range_min</strong>).</p>
</td>
</tr>
<tr id="row360773491607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p364292801607"><a name="p364292801607"></a><a name="p364292801607"></a>ethertype</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p339523071607"><a name="p339523071607"></a><a name="p339523071607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p34728681607"><a name="p34728681607"></a><a name="p34728681607"></a>Specifies the network type.</p>
<p id="p568898621607"><a name="p568898621607"></a><a name="p568898621607"></a>Only IPv4 is supported.</p>
</td>
</tr>
<tr id="row532124261607"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p593368391607"><a name="p593368391607"></a><a name="p593368391607"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p130282191607"><a name="p130282191607"></a><a name="p130282191607"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row11992111863317"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p169261732143314"><a name="p169261732143314"></a><a name="p169261732143314"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p69311132153317"><a name="p69311132153317"></a><a name="p69311132153317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p142999113115"><a name="p142999113115"></a><a name="p142999113115"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row10903153923318"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p6634195714335"><a name="p6634195714335"></a><a name="p6634195714335"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p12638157153319"><a name="p12638157153319"></a><a name="p12638157153319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1364635713332"><a name="p1364635713332"></a><a name="p1364635713332"></a>Specifies the time (UTC) when the security group rule is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i1731734865817"><a name="i1731734865817"></a><a name="i1731734865817"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1797311427338"><td class="cellrowborder" valign="top" width="26.669999999999998%" headers="mcps1.2.4.1.1 "><p id="p1725445103416"><a name="p1725445103416"></a><a name="p1725445103416"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.2 "><p id="p192601514345"><a name="p192601514345"></a><a name="p192601514345"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1127018513343"><a name="p1127018513343"></a><a name="p1127018513343"></a>Specifies the time (UTC) when the security group rule is updated.</p>
<p id="p457613546135"><a name="p457613546135"></a><a name="p457613546135"></a>Format: <em id="i19709155625820"><a name="i19709155625820"></a><a name="i19709155625820"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section2374028316235"></a>

Example request

```
GET https://{Endpoint}/v2.0/security-group-rules/1755bc80-cf3a-4f57-8ae9-d9796482ddc0
```

Example response

```
{
    "security_group_rule": {
        "remote_group_id": null, 
        "direction": "egress", 
        "remote_ip_prefix": null, 
        "protocol": null, 
        "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f", 
        "port_range_max": null, 
        "security_group_id": "723bc02c-d7f7-49b5-b6ff-d08320f315e2", 
        "port_range_min": null, 
        "ethertype": "IPv4", 
        "description": null, 
        "id": "1755bc80-cf3a-4f57-8ae9-d9796482ddc0",
        "project_id": "6fbe9263116a4b68818cf1edce16bc4f", 
        "created_at": "2018-09-20T02:15:34",
        "updated_at": "2018-09-20T02:15:34"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

