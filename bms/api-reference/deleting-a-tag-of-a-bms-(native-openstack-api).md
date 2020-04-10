# Deleting a Tag of a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0060424486"></a>

## Function<a name="section46928615105534"></a>

This API is used to delete a tag of a BMS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the micro version on the client.

## Constraints<a name="section11729622194315"></a>

-   The tag contains a maximum of 80 characters.
-   If a tag contains non-URL-safe characters, perform URL encoding.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Tag  **\_\_type\_baremetal**  is used to identify a BMS. You are not advised to delete this tag. Otherwise, the BMS will be displayed only on the ECS console.  
>-   After deleting the  **\_\_type\_baremetal**  tag, you can add it again by following the instructions in  [Adding a Tag to a BMS \(Native OpenStack API\)](adding-a-tag-to-a-bms-(native-openstack-api).md). After the tag is added, the BMS will be displayed on the BMS console.  

## URI<a name="section3181044105534"></a>

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/tags/\{tag\}

[Table 1](#table105191945325)  lists the parameters.

**Table  1**  Parameter description

<a name="table105191945325"></a>
<table><thead align="left"><tr id="row55201745523"><th class="cellrowborder" valign="top" width="23.03230323032303%" id="mcps1.2.4.1.1"><p id="p67050730103718"><a name="p67050730103718"></a><a name="p67050730103718"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.782478247824784%" id="mcps1.2.4.1.2"><p id="p55073076202321"><a name="p55073076202321"></a><a name="p55073076202321"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="52.185218521852185%" id="mcps1.2.4.1.3"><p id="p21237868103718"><a name="p21237868103718"></a><a name="p21237868103718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row165207451427"><td class="cellrowborder" valign="top" width="23.03230323032303%" headers="mcps1.2.4.1.1 "><p id="p23650911103718"><a name="p23650911103718"></a><a name="p23650911103718"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.782478247824784%" headers="mcps1.2.4.1.2 "><p id="p36675672103718"><a name="p36675672103718"></a><a name="p36675672103718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.185218521852185%" headers="mcps1.2.4.1.3 "><p id="p17939461103718"><a name="p17939461103718"></a><a name="p17939461103718"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row1752024519217"><td class="cellrowborder" valign="top" width="23.03230323032303%" headers="mcps1.2.4.1.1 "><p id="p18738546141829"><a name="p18738546141829"></a><a name="p18738546141829"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.782478247824784%" headers="mcps1.2.4.1.2 "><p id="p41427238141829"><a name="p41427238141829"></a><a name="p41427238141829"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.185218521852185%" headers="mcps1.2.4.1.3 "><p id="p163111141829"><a name="p163111141829"></a><a name="p163111141829"></a>Specifies the <span id="text731729134313"><a name="text731729134313"></a><a name="text731729134313"></a>BMS</span><span id="text9442974311"><a name="text9442974311"></a><a name="text9442974311"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row4520184517219"><td class="cellrowborder" valign="top" width="23.03230323032303%" headers="mcps1.2.4.1.1 "><p id="p54908755151432"><a name="p54908755151432"></a><a name="p54908755151432"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="24.782478247824784%" headers="mcps1.2.4.1.2 "><p id="p18424196151432"><a name="p18424196151432"></a><a name="p18424196151432"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.185218521852185%" headers="mcps1.2.4.1.3 "><p id="p3844311810"><a name="p3844311810"></a><a name="p3844311810"></a>Specifies the tag information.</p>
<p id="p1648373542814"><a name="p1648373542814"></a><a name="p1648373542814"></a>Constraints:</p>
<a name="ul16436151718351"></a><a name="ul16436151718351"></a><ul id="ul16436151718351"><li>A tag can contain a maximum of 80 characters. If a tag contains non-URL-safe characters, perform URL encoding.</li><li>If no key is specified, all tags of the <span id="text14203744549"><a name="text14203744549"></a><a name="text14203744549"></a>BMS</span><span id="text62039475411"><a name="text62039475411"></a><a name="text62039475411"></a></span> are deleted.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section61879170105534"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/53206ed0-56de-4d6b-b7ee-ffc62ca26f43/tags/{tag}
    ```


## Response Message<a name="section33789573105534"></a>

N/A

## Returned Values<a name="section27037160"></a>

Normal values

<a name="en-us_topic_0053158659_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0053158659_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0053158659_p19735204616177"><a name="en-us_topic_0053158659_p19735204616177"></a><a name="en-us_topic_0053158659_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0053158659_p207355465176"><a name="en-us_topic_0053158659_p207355465176"></a><a name="en-us_topic_0053158659_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053158659_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0053158659_p13735144611178"><a name="en-us_topic_0053158659_p13735144611178"></a><a name="en-us_topic_0053158659_p13735144611178"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053158659_p81516575011"><a name="en-us_topic_0053158659_p81516575011"></a><a name="en-us_topic_0053158659_p81516575011"></a>The server has processed the request but did not return any content.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

