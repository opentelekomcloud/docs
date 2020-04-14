# Querying API Versions<a name="eip_openstackapi_0002"></a>

## Function<a name="en-us_topic_0201534229_section47928120"></a>

This API is used to query all available versions of a native OpenStack API.

## URI<a name="en-us_topic_0201534229_section28699899"></a>

GET /

## Request Message<a name="en-us_topic_0201534229_section42990474"></a>

Request parameter

None

Example request

```
GET https://{Endpoint}/
```

## Response Message<a name="en-us_topic_0201534229_section51369953"></a>

Response parameter

**Table  1**  Response parameter

<a name="en-us_topic_0201534229_table51277242"></a>
<table><thead align="left"><tr id="en-us_topic_0201534229_row64740644"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534229_p9500791"><a name="en-us_topic_0201534229_p9500791"></a><a name="en-us_topic_0201534229_p9500791"></a><strong id="en-us_topic_0201534229_b842352706193648"><a name="en-us_topic_0201534229_b842352706193648"></a><a name="en-us_topic_0201534229_b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534229_p31366578"><a name="en-us_topic_0201534229_p31366578"></a><a name="en-us_topic_0201534229_p31366578"></a><strong id="en-us_topic_0201534229_b842352706193653"><a name="en-us_topic_0201534229_b842352706193653"></a><a name="en-us_topic_0201534229_b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534229_p40344834"><a name="en-us_topic_0201534229_p40344834"></a><a name="en-us_topic_0201534229_p40344834"></a><strong id="en-us_topic_0201534229_b8423527061645"><a name="en-us_topic_0201534229_b8423527061645"></a><a name="en-us_topic_0201534229_b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534229_row46706151"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534229_p25101909"><a name="en-us_topic_0201534229_p25101909"></a><a name="en-us_topic_0201534229_p25101909"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534229_p1668082023018"><a name="en-us_topic_0201534229_p1668082023018"></a><a name="en-us_topic_0201534229_p1668082023018"></a>Array of <a href="#en-us_topic_0201534229_table7472653181512">version</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534229_p15291872"><a name="en-us_topic_0201534229_p15291872"></a><a name="en-us_topic_0201534229_p15291872"></a>Specifies the API version list. For details, see <a href="#en-us_topic_0201534229_table7472653181512">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **version**  objects

<a name="en-us_topic_0201534229_table7472653181512"></a>
<table><thead align="left"><tr id="en-us_topic_0201534229_row24721153191511"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534229_p7472853151518"><a name="en-us_topic_0201534229_p7472853151518"></a><a name="en-us_topic_0201534229_p7472853151518"></a><strong id="en-us_topic_0201534229_b04872545271"><a name="en-us_topic_0201534229_b04872545271"></a><a name="en-us_topic_0201534229_b04872545271"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534229_p1647210534155"><a name="en-us_topic_0201534229_p1647210534155"></a><a name="en-us_topic_0201534229_p1647210534155"></a><strong id="en-us_topic_0201534229_b842352706193653_1"><a name="en-us_topic_0201534229_b842352706193653_1"></a><a name="en-us_topic_0201534229_b842352706193653_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534229_p11472185317150"><a name="en-us_topic_0201534229_p11472185317150"></a><a name="en-us_topic_0201534229_p11472185317150"></a><strong id="en-us_topic_0201534229_b13097052814"><a name="en-us_topic_0201534229_b13097052814"></a><a name="en-us_topic_0201534229_b13097052814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534229_row18472155310158"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534229_p147217533154"><a name="en-us_topic_0201534229_p147217533154"></a><a name="en-us_topic_0201534229_p147217533154"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534229_p947255320159"><a name="en-us_topic_0201534229_p947255320159"></a><a name="en-us_topic_0201534229_p947255320159"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534229_p47752014191"><a name="en-us_topic_0201534229_p47752014191"></a><a name="en-us_topic_0201534229_p47752014191"></a>Specifies the API version status. Possible values are as follows:</p>
<a name="en-us_topic_0201534229_ul1053872581218"></a><a name="en-us_topic_0201534229_ul1053872581218"></a><ul id="en-us_topic_0201534229_ul1053872581218"><li><strong id="en-us_topic_0201534229_b84235270619587"><a name="en-us_topic_0201534229_b84235270619587"></a><a name="en-us_topic_0201534229_b84235270619587"></a>CURRENT</strong></li><li><strong id="en-us_topic_0201534229_b1776824032913"><a name="en-us_topic_0201534229_b1776824032913"></a><a name="en-us_topic_0201534229_b1776824032913"></a>STABLE</strong></li><li><strong id="en-us_topic_0201534229_b1095445010297"><a name="en-us_topic_0201534229_b1095445010297"></a><a name="en-us_topic_0201534229_b1095445010297"></a>DEPRECATED</strong></li></ul>
</td>
</tr>
<tr id="en-us_topic_0201534229_row747215312152"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534229_p10472115381512"><a name="en-us_topic_0201534229_p10472115381512"></a><a name="en-us_topic_0201534229_p10472115381512"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534229_p9472115313158"><a name="en-us_topic_0201534229_p9472115313158"></a><a name="en-us_topic_0201534229_p9472115313158"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534229_p647375331518"><a name="en-us_topic_0201534229_p647375331518"></a><a name="en-us_topic_0201534229_p647375331518"></a>Specifies the API version.</p>
</td>
</tr>
<tr id="en-us_topic_0201534229_row174734534159"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534229_p18473105321516"><a name="en-us_topic_0201534229_p18473105321516"></a><a name="en-us_topic_0201534229_p18473105321516"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534229_p984011365304"><a name="en-us_topic_0201534229_p984011365304"></a><a name="en-us_topic_0201534229_p984011365304"></a>Array of <a href="#en-us_topic_0201534229_table62331111162">link</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534229_p164731253181513"><a name="en-us_topic_0201534229_p164731253181513"></a><a name="en-us_topic_0201534229_p164731253181513"></a>Specifies the link list. For details, see <a href="#en-us_topic_0201534229_table62331111162">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **link**  objects

<a name="en-us_topic_0201534229_table62331111162"></a>
<table><thead align="left"><tr id="en-us_topic_0201534229_row1823611191619"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534229_p19231111161619"><a name="en-us_topic_0201534229_p19231111161619"></a><a name="en-us_topic_0201534229_p19231111161619"></a><strong id="en-us_topic_0201534229_b1991194683010"><a name="en-us_topic_0201534229_b1991194683010"></a><a name="en-us_topic_0201534229_b1991194683010"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534229_p112301121618"><a name="en-us_topic_0201534229_p112301121618"></a><a name="en-us_topic_0201534229_p112301121618"></a><strong id="en-us_topic_0201534229_b842352706193653_2"><a name="en-us_topic_0201534229_b842352706193653_2"></a><a name="en-us_topic_0201534229_b842352706193653_2"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534229_p1323611171617"><a name="en-us_topic_0201534229_p1323611171617"></a><a name="en-us_topic_0201534229_p1323611171617"></a><strong id="en-us_topic_0201534229_b97191050153010"><a name="en-us_topic_0201534229_b97191050153010"></a><a name="en-us_topic_0201534229_b97191050153010"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534229_row15260111169"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534229_p192851171616"><a name="en-us_topic_0201534229_p192851171616"></a><a name="en-us_topic_0201534229_p192851171616"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534229_p122815111167"><a name="en-us_topic_0201534229_p122815111167"></a><a name="en-us_topic_0201534229_p122815111167"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534229_p12813117167"><a name="en-us_topic_0201534229_p12813117167"></a><a name="en-us_topic_0201534229_p12813117167"></a>Specifies the API link.</p>
</td>
</tr>
<tr id="en-us_topic_0201534229_row132891118162"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534229_p1728171118161"><a name="en-us_topic_0201534229_p1728171118161"></a><a name="en-us_topic_0201534229_p1728171118161"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534229_p42820114167"><a name="en-us_topic_0201534229_p42820114167"></a><a name="en-us_topic_0201534229_p42820114167"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534229_p5289119162"><a name="en-us_topic_0201534229_p5289119162"></a><a name="en-us_topic_0201534229_p5289119162"></a>Specifies the relationship between the API link and the API version.</p>
</td>
</tr>
</tbody>
</table>

Example response

```
{
    "versions": [
        {
            "status": "CURRENT", 
            "id": "v2.0", 
            "links": [
                {
                    "href": "https://None/v2.0", 
                    "rel": "self"
                }
            ]
        }
    ]
}
```

## Status Code<a name="en-us_topic_0201534229_section10470352390"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534229_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).

