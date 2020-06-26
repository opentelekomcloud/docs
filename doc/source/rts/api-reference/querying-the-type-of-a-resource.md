# Querying the Type of a Resource<a name="EN-US_TOPIC_0084581311"></a>

## Function<a name="en-us_topic_0057973148_section48372134"></a>

This API is used to query the type of a resource.

## URI<a name="en-us_topic_0057973148_section32696025"></a>

GET /v1/\{project\_id\}/resource\_types/\{type\_name\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b19478126111615"><a name="b19478126111615"></a><a name="b19478126111615"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b54291476165"><a name="b54291476165"></a><a name="b54291476165"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b519617814160"><a name="b519617814160"></a><a name="b519617814160"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b530169171612"><a name="b530169171612"></a><a name="b530169171612"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1765464961019"><a name="p1765464961019"></a><a name="p1765464961019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0655184916104"><a name="p0655184916104"></a><a name="p0655184916104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p865694971017"><a name="p865694971017"></a><a name="p865694971017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13658144921010"><a name="p13658144921010"></a><a name="p13658144921010"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row205605355223"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5414363327"><a name="p5414363327"></a><a name="p5414363327"></a>type_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p124171268327"><a name="p124171268327"></a><a name="p124171268327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1342216693211"><a name="p1342216693211"></a><a name="p1342216693211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1642526163220"><a name="p1642526163220"></a><a name="p1642526163220"></a>Specifies the resource type name.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973148_section25828772"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973148_section31132360"></a>

<a name="en-us_topic_0057973148_table47295947"></a>
<table><thead align="left"><tr id="en-us_topic_0057973148_row61351301"><th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b1438182071610"><a name="b1438182071610"></a><a name="b1438182071610"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b11953212160"><a name="b11953212160"></a><a name="b11953212160"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b18251422191615"><a name="b18251422191615"></a><a name="b18251422191615"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b1413982361613"><a name="b1413982361613"></a><a name="b1413982361613"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973148_row11565568"><td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973148_p64395783"><a name="en-us_topic_0057973148_p64395783"></a><a name="en-us_topic_0057973148_p64395783"></a>attributes</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.2 "><p id="p1549441552715"><a name="p1549441552715"></a><a name="p1549441552715"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973148_p48675955"><a name="en-us_topic_0057973148_p48675955"></a><a name="en-us_topic_0057973148_p48675955"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973148_p58971801"><a name="en-us_topic_0057973148_p58971801"></a><a name="en-us_topic_0057973148_p58971801"></a>Specifies the resource feature dictionary.</p>
</td>
</tr>
<tr id="en-us_topic_0057973148_row13307271"><td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973148_p4147127"><a name="en-us_topic_0057973148_p4147127"></a><a name="en-us_topic_0057973148_p4147127"></a>properties</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.2 "><p id="p15494101513273"><a name="p15494101513273"></a><a name="p15494101513273"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973148_p372979"><a name="en-us_topic_0057973148_p372979"></a><a name="en-us_topic_0057973148_p372979"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973148_p31201458"><a name="en-us_topic_0057973148_p31201458"></a><a name="en-us_topic_0057973148_p31201458"></a>Specifies the resource attributes, including the description and type.</p>
</td>
</tr>
<tr id="en-us_topic_0057973148_row53924066"><td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973148_p5773211"><a name="en-us_topic_0057973148_p5773211"></a><a name="en-us_topic_0057973148_p5773211"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.2 "><p id="p34941715182719"><a name="p34941715182719"></a><a name="p34941715182719"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973148_p64976945"><a name="en-us_topic_0057973148_p64976945"></a><a name="en-us_topic_0057973148_p64976945"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973148_p38232849"><a name="en-us_topic_0057973148_p38232849"></a><a name="en-us_topic_0057973148_p38232849"></a>Specifies the resource type.</p>
</td>
</tr>
<tr id="en-us_topic_0057973148_row8551329"><td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973148_p21569045"><a name="en-us_topic_0057973148_p21569045"></a><a name="en-us_topic_0057973148_p21569045"></a>support_status</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.2 "><p id="p1549481517272"><a name="p1549481517272"></a><a name="p1549481517272"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973148_p2262250"><a name="en-us_topic_0057973148_p2262250"></a><a name="en-us_topic_0057973148_p2262250"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973148_p11568342"><a name="en-us_topic_0057973148_p11568342"></a><a name="en-us_topic_0057973148_p11568342"></a>Specifies the current status.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973148_section11755791"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/resource_types/OS%3A%3AHeat%3A%3ARandomString
```

## Response Example<a name="en-us_topic_0057973148_section38693256"></a>

```
{
    "attributes": {
        "an_attribute": {
            "description": "A runtime value of the resource."
        }
    },
    "properties": {
        "a_property": {
            "constraints": [
                {
                    "description": "Must be between 1 and 255 characters",
                    "length": {
                        "max": 255,
                        "min": 1
                    }
                }
            ],
            "description": "A resource description.",
            "required": true,
            "type": "string",
            "update_allowed": false
        }
    },
    "resource_type": "OS::Heat::AResourceName",
    "support_status": {
        "message": "A status message",
        "status": "SUPPORTED",
        "version": "2014.1"
    }
}
```

## Return Code<a name="en-us_topic_0057973148_section12694990"></a>

**Table  2**  Normal return code

<a name="table01411862119"></a>
<table><thead align="left"><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581285_b14910172512114"><a name="en-us_topic_0084581285_b14910172512114"></a><a name="en-us_topic_0084581285_b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table8571828153012"></a>
<table><thead align="left"><tr id="en-us_topic_0084581294_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581294_p129561510144"><a name="en-us_topic_0084581294_p129561510144"></a><a name="en-us_topic_0084581294_p129561510144"></a><strong id="en-us_topic_0084581294_b1235759101013"><a name="en-us_topic_0084581294_b1235759101013"></a><a name="en-us_topic_0084581294_b1235759101013"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581294_p4959810444"><a name="en-us_topic_0084581294_p4959810444"></a><a name="en-us_topic_0084581294_p4959810444"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581294_p9959161020418"><a name="en-us_topic_0084581294_p9959161020418"></a><a name="en-us_topic_0084581294_p9959161020418"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581294_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p896118101840"><a name="en-us_topic_0084581294_p896118101840"></a><a name="en-us_topic_0084581294_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1296211015416"><a name="en-us_topic_0084581294_p1296211015416"></a><a name="en-us_topic_0084581294_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p9963110146"><a name="en-us_topic_0084581294_p9963110146"></a><a name="en-us_topic_0084581294_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p18134027201912"><a name="en-us_topic_0084581294_p18134027201912"></a><a name="en-us_topic_0084581294_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1713419274191"><a name="en-us_topic_0084581294_p1713419274191"></a><a name="en-us_topic_0084581294_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p11134162718196"><a name="en-us_topic_0084581294_p11134162718196"></a><a name="en-us_topic_0084581294_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p125520290312"><a name="en-us_topic_0084581294_p125520290312"></a><a name="en-us_topic_0084581294_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
</tbody>
</table>

