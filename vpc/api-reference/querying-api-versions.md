# Querying API Versions<a name="vpc_version_0001"></a>

## Function<a name="section47928120"></a>

This API is used to query all available versions of a native OpenStack API.

## URI<a name="section28699899"></a>

GET /

## Request Message<a name="section42990474"></a>

Request parameter

None

Example request

```
GET https://{Endpoint}/
```

## Response Message<a name="section51369953"></a>

Response parameter

**Table  1**  Response parameter

<a name="table51277242"></a>
<table><thead align="left"><tr id="row64740644"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="p9500791"><a name="p9500791"></a><a name="p9500791"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="p31366578"><a name="p31366578"></a><a name="p31366578"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="p40344834"><a name="p40344834"></a><a name="p40344834"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row46706151"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p25101909"><a name="p25101909"></a><a name="p25101909"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p1668082023018"><a name="p1668082023018"></a><a name="p1668082023018"></a>Array of <a href="#table7472653181512">version</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p15291872"><a name="p15291872"></a><a name="p15291872"></a>Specifies the API version list. For details, see <a href="#table7472653181512">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **version**  objects

<a name="table7472653181512"></a>
<table><thead align="left"><tr id="row24721153191511"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="p7472853151518"><a name="p7472853151518"></a><a name="p7472853151518"></a><strong id="b04872545271"><a name="b04872545271"></a><a name="b04872545271"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="p1647210534155"><a name="p1647210534155"></a><a name="p1647210534155"></a><strong id="b842352706193653_1"><a name="b842352706193653_1"></a><a name="b842352706193653_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="p11472185317150"><a name="p11472185317150"></a><a name="p11472185317150"></a><strong id="b13097052814"><a name="b13097052814"></a><a name="b13097052814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18472155310158"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p147217533154"><a name="p147217533154"></a><a name="p147217533154"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p947255320159"><a name="p947255320159"></a><a name="p947255320159"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p47752014191"><a name="p47752014191"></a><a name="p47752014191"></a>Specifies the API version status. Possible values are as follows:</p>
<a name="ul1053872581218"></a><a name="ul1053872581218"></a><ul id="ul1053872581218"><li><strong id="b84235270619587"><a name="b84235270619587"></a><a name="b84235270619587"></a>CURRENT</strong></li><li><strong id="b1776824032913"><a name="b1776824032913"></a><a name="b1776824032913"></a>STABLE</strong></li><li><strong id="b1095445010297"><a name="b1095445010297"></a><a name="b1095445010297"></a>DEPRECATED</strong></li></ul>
</td>
</tr>
<tr id="row747215312152"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p10472115381512"><a name="p10472115381512"></a><a name="p10472115381512"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p9472115313158"><a name="p9472115313158"></a><a name="p9472115313158"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p647375331518"><a name="p647375331518"></a><a name="p647375331518"></a>Specifies the API version.</p>
</td>
</tr>
<tr id="row174734534159"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p18473105321516"><a name="p18473105321516"></a><a name="p18473105321516"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p984011365304"><a name="p984011365304"></a><a name="p984011365304"></a>Array of <a href="#table62331111162">link</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p164731253181513"><a name="p164731253181513"></a><a name="p164731253181513"></a>Specifies the link list. For details, see <a href="#table62331111162">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **link**  objects

<a name="table62331111162"></a>
<table><thead align="left"><tr id="row1823611191619"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="p19231111161619"><a name="p19231111161619"></a><a name="p19231111161619"></a><strong id="b1991194683010"><a name="b1991194683010"></a><a name="b1991194683010"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="p112301121618"><a name="p112301121618"></a><a name="p112301121618"></a><strong id="b842352706193653_2"><a name="b842352706193653_2"></a><a name="b842352706193653_2"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="p1323611171617"><a name="p1323611171617"></a><a name="p1323611171617"></a><strong id="b97191050153010"><a name="b97191050153010"></a><a name="b97191050153010"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row15260111169"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p192851171616"><a name="p192851171616"></a><a name="p192851171616"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p122815111167"><a name="p122815111167"></a><a name="p122815111167"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p12813117167"><a name="p12813117167"></a><a name="p12813117167"></a>Specifies the API link.</p>
</td>
</tr>
<tr id="row132891118162"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p1728171118161"><a name="p1728171118161"></a><a name="p1728171118161"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p42820114167"><a name="p42820114167"></a><a name="p42820114167"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p5289119162"><a name="p5289119162"></a><a name="p5289119162"></a>Specifies the relationship between the API link and the API version.</p>
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

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

