# Restarting a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158716"></a>

## Function<a name="section6488958"></a>

This API is used to restart a single BMS. 

## Constraints<a name="section57278039123222"></a>

Currently, only forcible restart is supported.

## URI<a name="section58400626"></a>

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table6943612162916)  lists the parameters.

**Table  1**  Parameter description

<a name="table6943612162916"></a>
<table><thead align="left"><tr id="row1694351213299"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p17522362913"><a name="p17522362913"></a><a name="p17522362913"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5642312299"><a name="p5642312299"></a><a name="p5642312299"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1391023202918"><a name="p1391023202918"></a><a name="p1391023202918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5943201292911"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p71132302912"><a name="p71132302912"></a><a name="p71132302912"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p91472372914"><a name="p91472372914"></a><a name="p91472372914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19165231293"><a name="p19165231293"></a><a name="p19165231293"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row794311252918"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p318162392918"><a name="p318162392918"></a><a name="p318162392918"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1119162362913"><a name="p1119162362913"></a><a name="p1119162362913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p192032314291"><a name="p192032314291"></a><a name="p192032314291"></a>Specifies the <span id="text1891118159128"><a name="text1891118159128"></a><a name="text1891118159128"></a>BMS</span><span id="text1591114152121"><a name="text1591114152121"></a><a name="text1591114152121"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section55843593"></a>

-   Request parameters

    <a name="table37818817"></a>
    <table><thead align="left"><tr id="row57787318"><th class="cellrowborder" valign="top" width="16.64%" id="mcps1.1.5.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.76%" id="mcps1.1.5.1.2"><p id="p25916685817"><a name="p25916685817"></a><a name="p25916685817"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.28%" id="mcps1.1.5.1.3"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.32%" id="mcps1.1.5.1.4"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13875810"><td class="cellrowborder" valign="top" width="16.64%" headers="mcps1.1.5.1.1 "><p id="p50198807"><a name="p50198807"></a><a name="p50198807"></a>reboot</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.76%" headers="mcps1.1.5.1.2 "><p id="p63270434181210"><a name="p63270434181210"></a><a name="p63270434181210"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.28%" headers="mcps1.1.5.1.3 "><p id="p51181499"><a name="p51181499"></a><a name="p51181499"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.32%" headers="mcps1.1.5.1.4 "><p id="p65893970"><a name="p65893970"></a><a name="p65893970"></a>Specifies the operation of restarting the <span id="text202611519161218"><a name="text202611519161218"></a><a name="text202611519161218"></a>BMS</span><span id="text126115192124"><a name="text126115192124"></a><a name="text126115192124"></a></span>. For details, see <a href="#table10346346162744">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **reboot**  field data structure description

    <a name="table10346346162744"></a>
    <table><thead align="left"><tr id="row45993853162744"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p85714617589"><a name="p85714617589"></a><a name="p85714617589"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.68%" id="mcps1.2.5.1.2"><p id="p84832135211"><a name="p84832135211"></a><a name="p84832135211"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.5.1.3"><p id="p2049218166215"><a name="p2049218166215"></a><a name="p2049218166215"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.37%" id="mcps1.2.5.1.4"><p id="p5615615814"><a name="p5615615814"></a><a name="p5615615814"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41908639162744"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p39156593162744"><a name="p39156593162744"></a><a name="p39156593162744"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.68%" headers="mcps1.2.5.1.2 "><p id="p164835131924"><a name="p164835131924"></a><a name="p164835131924"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.5.1.3 "><p id="p144921162216"><a name="p144921162216"></a><a name="p144921162216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.37%" headers="mcps1.2.5.1.4 "><p id="p34131354162744"><a name="p34131354162744"></a><a name="p34131354162744"></a>Specifies the type of the restart operation.</p>
    <a name="ul1169415154044"></a><a name="ul1169415154044"></a><ul id="ul1169415154044"><li><strong>SOFT</strong>: soft restart</li><li><strong>HARD</strong>: forcible restart<div class="note" id="note3080306151059"><a name="note3080306151059"></a><a name="note3080306151059"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p27722756151059"><a name="p27722756151059"></a><a name="p27722756151059"></a>Currently, value <strong id="b842352706161220"><a name="b842352706161220"></a><a name="b842352706161220"></a>SOFT</strong> is invalid. All BMS restart operations are forcible restart.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/action
    ```

    ```
    {
        "reboot": {
            "type": "HARD"
        }
    }
    ```


## Response Message<a name="section32830290"></a>

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

