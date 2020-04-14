# Adding a Tag to a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0060410929"></a>

## Function<a name="section63429208111321"></a>

This API is used to add a tag to a BMS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the micro version on the client.

## Constraints<a name="section26150540144115"></a>

-   A BMS can have a maximum of 50 tags.
-   The tag contains a maximum of 80 characters.
-   The tag cannot start with a period \(.\).
-   An empty tag cannot be created.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>It is recommended that you add the  **\_\_type\_baremetal**  tag to BMSs to distinguish BMSs from ECSs.  

## URI<a name="section1885963111321"></a>

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}/tags/\{tag\}

[Table 1](#table19718185512020)  lists the parameters.

**Table  1**  Parameter description

<a name="table19718185512020"></a>
<table><thead align="left"><tr id="row371913559014"><th class="cellrowborder" valign="top" width="26.862686268626863%" id="mcps1.2.4.1.1"><p id="p67050730103718"><a name="p67050730103718"></a><a name="p67050730103718"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.402840284028404%" id="mcps1.2.4.1.2"><p id="p62400032103718"><a name="p62400032103718"></a><a name="p62400032103718"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="44.73447344734473%" id="mcps1.2.4.1.3"><p id="p21237868103718"><a name="p21237868103718"></a><a name="p21237868103718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row207198551306"><td class="cellrowborder" valign="top" width="26.862686268626863%" headers="mcps1.2.4.1.1 "><p id="p23650911103718"><a name="p23650911103718"></a><a name="p23650911103718"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.402840284028404%" headers="mcps1.2.4.1.2 "><p id="p36675672103718"><a name="p36675672103718"></a><a name="p36675672103718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.73447344734473%" headers="mcps1.2.4.1.3 "><p id="p17939461103718"><a name="p17939461103718"></a><a name="p17939461103718"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row1871913551206"><td class="cellrowborder" valign="top" width="26.862686268626863%" headers="mcps1.2.4.1.1 "><p id="p18738546141829"><a name="p18738546141829"></a><a name="p18738546141829"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.402840284028404%" headers="mcps1.2.4.1.2 "><p id="p41427238141829"><a name="p41427238141829"></a><a name="p41427238141829"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.73447344734473%" headers="mcps1.2.4.1.3 "><p id="p163111141829"><a name="p163111141829"></a><a name="p163111141829"></a>Specifies the <span id="text718713247535"><a name="text718713247535"></a><a name="text718713247535"></a>BMS</span><span id="text1118792412539"><a name="text1118792412539"></a><a name="text1118792412539"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row2071917554012"><td class="cellrowborder" valign="top" width="26.862686268626863%" headers="mcps1.2.4.1.1 "><p id="p66048515144318"><a name="p66048515144318"></a><a name="p66048515144318"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="28.402840284028404%" headers="mcps1.2.4.1.2 "><p id="p48329483144318"><a name="p48329483144318"></a><a name="p48329483144318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.73447344734473%" headers="mcps1.2.4.1.3 "><p id="p133533233165"><a name="p133533233165"></a><a name="p133533233165"></a>Specifies the tag information.</p>
<p id="p6856153762712"><a name="p6856153762712"></a><a name="p6856153762712"></a>Constraints:</p>
<a name="ul31181225141619"></a><a name="ul31181225141619"></a><ul id="ul31181225141619"><li>The tag contains a maximum of 80 characters.</li><li>The tag cannot start with a period (.).</li><li>An empty tag cannot be created.</li><li>URL encoding is required for special characters.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section26704907111321"></a>

-   Request parameters

    None

-   Example request

    ```
    PUT https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/53206ed0-56de-4d6b-b7ee-ffc62ca26f43/tags/{tag}
    ```


## Response Message<a name="section6307065111321"></a>

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

