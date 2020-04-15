# Viewing Metadata Configured on a Server<a name="EN-US_TOPIC_0085277563"></a>

## Function<a name="en-us_topic_0085081140_section5314816"></a>

This API is used to view the metadata configured on a server.

## URI<a name="en-us_topic_0085081140_section47833347"></a>

GET /v1/\{project\_id\}/software\_deployments/metadata/\{server\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b10294115020472"><a name="b10294115020472"></a><a name="b10294115020472"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b94031453114719"><a name="b94031453114719"></a><a name="b94031453114719"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b17432125415478"><a name="b17432125415478"></a><a name="b17432125415478"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b2018530204815"><a name="b2018530204815"></a><a name="b2018530204815"></a>Description</strong></p>
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
<tr id="row205605355223"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15899175215302"><a name="p15899175215302"></a><a name="p15899175215302"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p8902752193019"><a name="p8902752193019"></a><a name="p8902752193019"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p690718522302"><a name="p690718522302"></a><a name="p690718522302"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p291110529305"><a name="p291110529305"></a><a name="p291110529305"></a>Specifies the target server ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0085081140_section27846943"></a>

N/A

## Response Parameter<a name="en-us_topic_0085081140_section49295902"></a>

<a name="table193211535404"></a>
<table><thead align="left"><tr id="row16932185311408"><th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b178191929154815"><a name="b178191929154815"></a><a name="b178191929154815"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b239713339482"><a name="b239713339482"></a><a name="b239713339482"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b5695193634816"><a name="b5695193634816"></a><a name="b5695193634816"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.160000000000004%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b192793994815"><a name="b192793994815"></a><a name="b192793994815"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row15933185344013"><td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p20638153931616"><a name="en-us_topic_0085081140_p20638153931616"></a><a name="en-us_topic_0085081140_p20638153931616"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p18609818182419"><a name="p18609818182419"></a><a name="p18609818182419"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p66381339121613"><a name="en-us_topic_0085081140_p66381339121613"></a><a name="en-us_topic_0085081140_p66381339121613"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.160000000000004%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p1563893912161"><a name="en-us_topic_0085081140_p1563893912161"></a><a name="en-us_topic_0085081140_p1563893912161"></a>Specifies the software deployment metadata.</p>
</td>
</tr>
</tbody>
</table>

**metadata**  structure information

<a name="en-us_topic_0085081140_table58541283"></a>
<table><thead align="left"><tr id="en-us_topic_0085081140_row14014710"><th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.1"><p id="p1930983835918"><a name="p1930983835918"></a><a name="p1930983835918"></a><strong id="b10784175410482"><a name="b10784175410482"></a><a name="b10784175410482"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.290000000000001%" id="mcps1.1.5.1.2"><p id="p1031663815591"><a name="p1031663815591"></a><a name="p1031663815591"></a><strong id="b1314813581487"><a name="b1314813581487"></a><a name="b1314813581487"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.1.5.1.3"><p id="p9320838115917"><a name="p9320838115917"></a><a name="p9320838115917"></a><strong id="b177117014911"><a name="b177117014911"></a><a name="b177117014911"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.59%" id="mcps1.1.5.1.4"><p id="p153331938165918"><a name="p153331938165918"></a><a name="p153331938165918"></a><strong id="b380511611496"><a name="b380511611496"></a><a name="b380511611496"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0085081140_row20801079"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p663633981619"><a name="en-us_topic_0085081140_p663633981619"></a><a name="en-us_topic_0085081140_p663633981619"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p075073120225"><a name="p075073120225"></a><a name="p075073120225"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p126361396169"><a name="en-us_topic_0085081140_p126361396169"></a><a name="en-us_topic_0085081140_p126361396169"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p1263619397165"><a name="en-us_topic_0085081140_p1263619397165"></a><a name="en-us_topic_0085081140_p1263619397165"></a>Specifies the configuration script or list.</p>
</td>
</tr>
<tr id="en-us_topic_0085081140_row20715858"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p963703981614"><a name="en-us_topic_0085081140_p963703981614"></a><a name="en-us_topic_0085081140_p963703981614"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p1875093116225"><a name="p1875093116225"></a><a name="p1875093116225"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p3637183971615"><a name="en-us_topic_0085081140_p3637183971615"></a><a name="en-us_topic_0085081140_p3637183971615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="p1756622893716"><a name="p1756622893716"></a><a name="p1756622893716"></a>Specifies the creation time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen203309329372"><a name="screen203309329372"></a><a name="screen203309329372"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
<tr id="en-us_topic_0085081140_row26021030"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p136375398166"><a name="en-us_topic_0085081140_p136375398166"></a><a name="en-us_topic_0085081140_p136375398166"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p1175013315229"><a name="p1175013315229"></a><a name="p1175013315229"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p1063753919167"><a name="en-us_topic_0085081140_p1063753919167"></a><a name="en-us_topic_0085081140_p1063753919167"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p1563773914169"><a name="en-us_topic_0085081140_p1563773914169"></a><a name="en-us_topic_0085081140_p1563773914169"></a>Specifies the name of the software configuration group.</p>
</td>
</tr>
<tr id="en-us_topic_0085081140_row45386595"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p363711393168"><a name="en-us_topic_0085081140_p363711393168"></a><a name="en-us_topic_0085081140_p363711393168"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p575063115222"><a name="p575063115222"></a><a name="p575063115222"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p1463717399166"><a name="en-us_topic_0085081140_p1463717399166"></a><a name="en-us_topic_0085081140_p1463717399166"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p1163711393165"><a name="en-us_topic_0085081140_p1163711393165"></a><a name="en-us_topic_0085081140_p1163711393165"></a>Specifies the software configuration UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0085081140_row23709572"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p963717390165"><a name="en-us_topic_0085081140_p963717390165"></a><a name="en-us_topic_0085081140_p963717390165"></a>inputs</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p875073142219"><a name="p875073142219"></a><a name="p875073142219"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p1363823931610"><a name="en-us_topic_0085081140_p1363823931610"></a><a name="en-us_topic_0085081140_p1363823931610"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p18638193917164"><a name="en-us_topic_0085081140_p18638193917164"></a><a name="en-us_topic_0085081140_p18638193917164"></a>Specifies the software configuration input.</p>
</td>
</tr>
<tr id="en-us_topic_0085081140_row876414818717"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p15638939171613"><a name="en-us_topic_0085081140_p15638939171613"></a><a name="en-us_topic_0085081140_p15638939171613"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p137501931162217"><a name="p137501931162217"></a><a name="p137501931162217"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p14638239201612"><a name="en-us_topic_0085081140_p14638239201612"></a><a name="en-us_topic_0085081140_p14638239201612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p8638139141610"><a name="en-us_topic_0085081140_p8638139141610"></a><a name="en-us_topic_0085081140_p8638139141610"></a>Specifies the name of the software configuration.</p>
</td>
</tr>
<tr id="en-us_topic_0085081140_row14764168173"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p10638639171614"><a name="en-us_topic_0085081140_p10638639171614"></a><a name="en-us_topic_0085081140_p10638639171614"></a>options</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p975033117224"><a name="p975033117224"></a><a name="p975033117224"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p1638439151615"><a name="en-us_topic_0085081140_p1638439151615"></a><a name="en-us_topic_0085081140_p1638439151615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p5638123921610"><a name="en-us_topic_0085081140_p5638123921610"></a><a name="en-us_topic_0085081140_p5638123921610"></a>Contains mapping for the options of the software management tool that this resource uses.</p>
</td>
</tr>
<tr id="en-us_topic_0085081140_row576428579"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p186386396161"><a name="en-us_topic_0085081140_p186386396161"></a><a name="en-us_topic_0085081140_p186386396161"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p18750431102214"><a name="p18750431102214"></a><a name="p18750431102214"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p12638193921610"><a name="en-us_topic_0085081140_p12638193921610"></a><a name="en-us_topic_0085081140_p12638193921610"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0085081140_p5639163916162"><a name="en-us_topic_0085081140_p5639163916162"></a><a name="en-us_topic_0085081140_p5639163916162"></a>Specifies the software configuration output.</p>
</td>
</tr>
<tr id="en-us_topic_0085081140_row17648812714"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0085081140_p20639123921617"><a name="en-us_topic_0085081140_p20639123921617"></a><a name="en-us_topic_0085081140_p20639123921617"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="15.290000000000001%" headers="mcps1.1.5.1.2 "><p id="p177501531122212"><a name="p177501531122212"></a><a name="p177501531122212"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0085081140_p5639153914162"><a name="en-us_topic_0085081140_p5639153914162"></a><a name="en-us_topic_0085081140_p5639153914162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.5.1.4 "><p id="p9134353373"><a name="p9134353373"></a><a name="p9134353373"></a>Specifies the update time. The timestamp uses the ISO 8601 format:</p>
<pre class="screen" id="screen1892811386370"><a name="screen1892811386370"></a><a name="screen1892811386370"></a>CCYY-MM-DDThh:mm:ss&plusmn;hh:mm</pre>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0085081140_section41009935"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/software_deployments/metadata/6a5eca38-6a04-4b26-6af5-543cdbd3d5e4
```

## Response Example<a name="en-us_topic_0085081140_section33545101"></a>

```
{
    "metadata": [
        {
            "inputs": [
                {
                    "default": null,
                    "type": "String",
                    "name": "foo",
                    "value": "fooooo",
                    "description": null
                },
                {
                    "default": null,
                    "type": "String",
                    "name": "bar",
                    "value": "baaaaa",
                    "description": null
                },
                {
                    "type": "String",
                    "name": "deploy_server_id",
                    "value": "ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5",
                    "description": "ID of the server being deployed to"
                },
                {
                    "type": "String",
                    "name": "deploy_action",
                    "value": "CREATE",
                    "description": "Name of the current action being deployed"
                },
                {
                    "type": "String",
                    "name": "deploy_stack_id",
                    "value": "a/9bd57090-8954-48ab-bab9-adf9e1ac70fc",
                    "description": "ID of the stack this deployment belongs to"
                },
                {
                    "type": "String",
                    "name": "deploy_resource_name",
                    "value": "deployment",
                    "description": "Name of this deployment resource in the stack"
                 },
                {
                    "type": "String",
                    "name": "deploy_signal_id",
                    "value": "http://x.x.x.x:8000/v1/signal/arn%3Aopenstack%3Aheat%3A%3Ae2a84fbdaeb047ae8da4b503f3b69f1f%3Astacks%2Fa%2F9bd57090-8954-48ab-bab9-adf9e1ac70fc%2Fresources%2Fdeployment?Timestamp=2014-03-19T20%3A30%3A59Z&SignatureMethod=HmacSHA256&AWSAccessKeyId=ca3571413e4a49998d580215517b3685&SignatureVersion=2&Signature=w6Iu%2BNbg86mqwSOUf1GLuKPO7KaD82PiGpL4ig9Q1l4%3D",
                    "description": "ID of signal to use for signalling output values"
                }
            ],
            "group": "script",
            "name": "a-config-we5zpvyu7b5o",
            "outputs": [
                {
                    "type": "String",
                    "name": "result",
                    "error_output": false,
                    "description": null
                }
            ],
            "options": null,
            "creation_time": "2015-01-31T15:12:36Z",
            "updated_time": "2015-01-31T15:18:21Z",
            "config": "#!/bin/sh -x\necho \"Writing to /tmp/$bar\"\necho $foo > /tmp/$bar\necho -n \"The file /tmp/$bar contains `cat /tmp/$bar` for server $deploy_server_id during $deploy_action\" > $heat_outputs_path.result\necho \"Written to /tmp/$bar\"\necho \"Output to stderr\" 1>&2",
            "id": "3d5ec2a8-7004-43b6-a7f6-542bdbe9d434"
        },
        {
            "inputs": [
                {
                    "default": null,
                    "type": "String",
                    "name": "foo",
                    "value": "fu",
                    "description": null
                },
                {
                    "default": null,
                    "type": "String",
                    "name": "bar",
                    "value": "barmy",
                    "description": null
                },
                {
                    "type": "String",
                    "name": "deploy_server_id",
                    "value": "ec14c864-096e-4e27-bb8a-2c2b4dc6f3f5",
                    "description": "ID of the server being deployed to"
                },
                {
                    "type": "String",
                    "name": "deploy_action",
                    "value": "CREATE",
                    "description": "Name of the current action being deployed"
                },
                {
                    "type": "String",
                    "name": "deploy_stack_id",
                    "value": "a/9bd57090-8954-48ab-bab9-adf9e1ac70fc",
                    "description": "ID of the stack this deployment belongs to"
                },
                {
                    "type": "String",
                    "name": "deploy_resource_name",
                    "value": "other_deployment",
                    "description": "Name of this deployment resource in the stack"
                },
                {
                    "type": "String",
                    "name": "deploy_signal_id",
                    "value": "http://x.x.x.x:8000/v1/signal/arn%3Aopenstack%3Aheat%3A%3Ae2a84fbdaeb047ae8da4b503f3b69f1f%3Astacks%2Fa%2F9bd57090-8954-48ab-bab9-adf9e1ac70fc%2Fresources%2Fother_deployment?Timestamp=2014-03-19T20%3A30%3A59Z&SignatureMethod=HmacSHA256&AWSAccessKeyId=7b761482f8254946bcd3d5ccb36fe939&SignatureVersion=2&Signature=giMfv%2BhrAw6y%2FCMKQIQz2IhO5PkAj5%2BfP5YsL6rul3o%3D",
                    "description": "ID of signal to use for signalling output values"
                }
            ],
            "group": "script",
            "name": "a-config-we5zpvyu7b5o",
            "outputs": [
                {
                    "type": "String",
                    "name": "result",
                    "error_output": false,
                    "description": null
                }
            ],
            "options": null,
            "creation_time": "2015-01-31T16:14:13Z",
            "updated_time": "2015-01-31T16:18:19Z",
            "config": "#!/bin/sh -x\necho \"Writing to /tmp/$bar\"\necho $foo > /tmp/$bar\necho -n \"The file /tmp/$bar contains `cat /tmp/$bar` for server $deploy_server_id during $deploy_action\" > $heat_outputs_path.result\necho \"Written to /tmp/$bar\"\necho \"Output to stderr\" 1>&2",
            "id": "8da95794-2ad9-4979-8ae5-739ce314c5cd"
        }
    ]
}
```

## Return Code<a name="en-us_topic_0085081140_section33470456"></a>

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

<a name="table3304326164315"></a>
<table><thead align="left"><tr id="en-us_topic_0084581290_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581290_p129561510144"><a name="en-us_topic_0084581290_p129561510144"></a><a name="en-us_topic_0084581290_p129561510144"></a><strong id="en-us_topic_0084581290_b1552942884813"><a name="en-us_topic_0084581290_b1552942884813"></a><a name="en-us_topic_0084581290_b1552942884813"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581290_p4959810444"><a name="en-us_topic_0084581290_p4959810444"></a><a name="en-us_topic_0084581290_p4959810444"></a><strong id="en-us_topic_0084581290_b956007905"><a name="en-us_topic_0084581290_b956007905"></a><a name="en-us_topic_0084581290_b956007905"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581290_p9959161020418"><a name="en-us_topic_0084581290_p9959161020418"></a><a name="en-us_topic_0084581290_p9959161020418"></a><strong id="en-us_topic_0084581290_b359171417"><a name="en-us_topic_0084581290_b359171417"></a><a name="en-us_topic_0084581290_b359171417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581290_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p896118101840"><a name="en-us_topic_0084581290_p896118101840"></a><a name="en-us_topic_0084581290_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1296211015416"><a name="en-us_topic_0084581290_p1296211015416"></a><a name="en-us_topic_0084581290_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p9963110146"><a name="en-us_topic_0084581290_p9963110146"></a><a name="en-us_topic_0084581290_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p18134027201912"><a name="en-us_topic_0084581290_p18134027201912"></a><a name="en-us_topic_0084581290_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1713419274191"><a name="en-us_topic_0084581290_p1713419274191"></a><a name="en-us_topic_0084581290_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p11134162718196"><a name="en-us_topic_0084581290_p11134162718196"></a><a name="en-us_topic_0084581290_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p125520290312"><a name="en-us_topic_0084581290_p125520290312"></a><a name="en-us_topic_0084581290_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row196097477276"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p19789174972712"><a name="en-us_topic_0084581290_p19789174972712"></a><a name="en-us_topic_0084581290_p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p779364918272"><a name="en-us_topic_0084581290_p779364918272"></a><a name="en-us_topic_0084581290_p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p196546319198"><a name="en-us_topic_0084581290_p196546319198"></a><a name="en-us_topic_0084581290_p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

