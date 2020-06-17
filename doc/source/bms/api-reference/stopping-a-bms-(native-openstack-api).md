# Stopping a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158685"></a>

## Function<a name="section32841145"></a>

This API is used to stop a single BMS. 

## Constraints<a name="section57278039123222"></a>

-   The BMS  **OS-EXT-STS:vm\_state**  attribute \(BMS status\) must be  **active**  or  **error**.
-   Currently, only forcible stopping is supported.

## URI<a name="section27134857"></a>

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table1997078319)  lists the parameters.

**Table  1**  Parameter description

<a name="table1997078319"></a>
<table><thead align="left"><tr id="row1697157163111"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p61356140"><a name="p61356140"></a><a name="p61356140"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3791404"><a name="p3791404"></a><a name="p3791404"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p38668280"><a name="p38668280"></a><a name="p38668280"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1973711316"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p31084503"><a name="p31084503"></a><a name="p31084503"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34816825"><a name="p34816825"></a><a name="p34816825"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1590600"><a name="p1590600"></a><a name="p1590600"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row39716712314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18697032"><a name="p18697032"></a><a name="p18697032"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p38064613"><a name="p38064613"></a><a name="p38064613"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p63334794"><a name="p63334794"></a><a name="p63334794"></a>Specifies the <span id="text10316749132912"><a name="text10316749132912"></a><a name="text10316749132912"></a>BMS</span><span id="text173171499297"><a name="text173171499297"></a><a name="text173171499297"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section42887128"></a>

-   Request parameters

    <a name="table54550461"></a>
    <table><thead align="left"><tr id="row11842506"><th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.1.5.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.21%" id="mcps1.1.5.1.2"><p id="p183901830522"><a name="p183901830522"></a><a name="p183901830522"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.61%" id="mcps1.1.5.1.3"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.14%" id="mcps1.1.5.1.4"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48896832"><td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.1.5.1.1 "><p id="p1220438"><a name="p1220438"></a><a name="p1220438"></a>os-stop</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.21%" headers="mcps1.1.5.1.2 "><p id="p0389123016219"><a name="p0389123016219"></a><a name="p0389123016219"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.1.5.1.3 "><p id="p21345065"><a name="p21345065"></a><a name="p21345065"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.14%" headers="mcps1.1.5.1.4 "><p id="p58405349"><a name="p58405349"></a><a name="p58405349"></a>Specifies the operation of stopping the <span id="text16893205917151"><a name="text16893205917151"></a><a name="text16893205917151"></a>BMS</span><span id="text589315921515"><a name="text589315921515"></a><a name="text589315921515"></a></span>. For details, see <a href="#table10346346162744">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **os-stop**  field data structure description

    <a name="table10346346162744"></a>
    <table><thead align="left"><tr id="row45993853162744"><th class="cellrowborder" valign="top" width="19.11%" id="mcps1.2.5.1.1"><p id="p15821544165817"><a name="p15821544165817"></a><a name="p15821544165817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.5.1.2"><p id="p16821737324"><a name="p16821737324"></a><a name="p16821737324"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.44%" id="mcps1.2.5.1.3"><p id="p105851844185813"><a name="p105851844185813"></a><a name="p105851844185813"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.78%" id="mcps1.2.5.1.4"><p id="p858711445580"><a name="p858711445580"></a><a name="p858711445580"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41908639162744"><td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.2.5.1.1 "><p id="p39156593162744"><a name="p39156593162744"></a><a name="p39156593162744"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p76815371823"><a name="p76815371823"></a><a name="p76815371823"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.44%" headers="mcps1.2.5.1.3 "><p id="p13677446162744"><a name="p13677446162744"></a><a name="p13677446162744"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.78%" headers="mcps1.2.5.1.4 "><p id="p34131354162744"><a name="p34131354162744"></a><a name="p34131354162744"></a>Specifies the type of the BMS stopping operation.</p>
    <a name="ul1169415154044"></a><a name="ul1169415154044"></a><ul id="ul1169415154044"><li><strong id="b504423009171038"><a name="b504423009171038"></a><a name="b504423009171038"></a>SOFT</strong>: normal BMS stopping</li><li><strong id="b8423527061788"><a name="b8423527061788"></a><a name="b8423527061788"></a>HARD</strong>: Forcible BMS stopping<div class="note" id="note3080306151059"><a name="note3080306151059"></a><a name="note3080306151059"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p27722756151059"><a name="p27722756151059"></a><a name="p27722756151059"></a>Currently, this parameter is invalid. All BMS stopping operations are forcible stopping.</p>
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
        "os-stop": {}
    }
    ```


## Response Message<a name="section50439840"></a>

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

