# Querying Information About a Disk Attached to a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158665"></a>

## Function<a name="section21764736"></a>

This API is used to query information about a single disk attached to a BMS based on the disk ID.

## URI<a name="section61664903"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments/\{volume\_id\}

[Table 1](#table17269134917502)  lists the parameters.

**Table  1**  Parameter description

<a name="table17269134917502"></a>
<table><thead align="left"><tr id="row127284919508"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p52189740"><a name="p52189740"></a><a name="p52189740"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p66619401"><a name="p66619401"></a><a name="p66619401"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p27462382"><a name="p27462382"></a><a name="p27462382"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5272549205014"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3763337517142"><a name="p3763337517142"></a><a name="p3763337517142"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2840453517142"><a name="p2840453517142"></a><a name="p2840453517142"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1906601217142"><a name="p1906601217142"></a><a name="p1906601217142"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row139591881618"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p139602087161"><a name="p139602087161"></a><a name="p139602087161"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1960128101613"><a name="p1960128101613"></a><a name="p1960128101613"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1196018841619"><a name="p1196018841619"></a><a name="p1196018841619"></a>Specifies the <span id="text116665122393"><a name="text116665122393"></a><a name="text116665122393"></a>BMS</span><span id="text106661612193910"><a name="text106661612193910"></a><a name="text106661612193910"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row92726495508"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2068039117144"><a name="p2068039117144"></a><a name="p2068039117144"></a>volume_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6449900717144"><a name="p6449900717144"></a><a name="p6449900717144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p5703706317144"><a name="p5703706317144"></a><a name="p5703706317144"></a>Specifies the EVS disk ID.</p>
<p id="p1765372715476"><a name="p1765372715476"></a><a name="p1765372715476"></a>You can query attached EVS disks attached to a <span id="text1798918157392"><a name="text1798918157392"></a><a name="text1798918157392"></a>BMS</span><span id="text10990131533919"><a name="text10990131533919"></a><a name="text10990131533919"></a></span> using the <a href="querying-information-about-the-disks-attached-to-a-bms-(native-openstack-api).md">Querying Information About the Disks Attached to a BMS (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section18113219"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-volume_attachments/b53f23bd-ee8f-49ec-9420-d1acfeaf91d6
    ```


## Response Message<a name="section28801245"></a>

-   Response parameters

    <a name="table769899"></a>
    <table><thead align="left"><tr id="row6968742"><th class="cellrowborder" valign="top" width="28.4%" id="mcps1.1.4.1.1"><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.69%" id="mcps1.1.4.1.2"><p id="p4546697"><a name="p4546697"></a><a name="p4546697"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.910000000000004%" id="mcps1.1.4.1.3"><p id="p32738149"><a name="p32738149"></a><a name="p32738149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13299239"><td class="cellrowborder" valign="top" width="28.4%" headers="mcps1.1.4.1.1 "><p id="p3496541"><a name="p3496541"></a><a name="p3496541"></a>volumeAttachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.1.4.1.2 "><p id="p56686067"><a name="p56686067"></a><a name="p56686067"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.910000000000004%" headers="mcps1.1.4.1.3 "><p id="p52192065"><a name="p52192065"></a><a name="p52192065"></a>Specifies information about the disk attached to the <span id="text047892014396"><a name="text047892014396"></a><a name="text047892014396"></a>BMS</span><span id="text174787201398"><a name="text174787201398"></a><a name="text174787201398"></a></span>. For details, see <a href="#table42716605">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **volumeAttachment**  field data structure description

    <a name="table42716605"></a>
    <table><thead align="left"><tr id="row6429"><th class="cellrowborder" valign="top" width="28.050000000000004%" id="mcps1.2.4.1.1"><p id="p144716112213"><a name="p144716112213"></a><a name="p144716112213"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.39%" id="mcps1.2.4.1.2"><p id="p184476111218"><a name="p184476111218"></a><a name="p184476111218"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.56%" id="mcps1.2.4.1.3"><p id="p0448211142115"><a name="p0448211142115"></a><a name="p0448211142115"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54793251"><td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.1 "><p id="p9068361"><a name="p9068361"></a><a name="p9068361"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.2 "><p id="p39066822"><a name="p39066822"></a><a name="p39066822"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.4.1.3 "><p id="p25555552"><a name="p25555552"></a><a name="p25555552"></a>Specifies the mount directory, for example, <strong id="b16720191214261"><a name="b16720191214261"></a><a name="b16720191214261"></a>/dev/vdb</strong>.</p>
    </td>
    </tr>
    <tr id="row28673382"><td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.1 "><p id="p40842582"><a name="p40842582"></a><a name="p40842582"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.2 "><p id="p2490560"><a name="p2490560"></a><a name="p2490560"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.4.1.3 "><p id="p3679585"><a name="p3679585"></a><a name="p3679585"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    <tr id="row33116269"><td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.1 "><p id="p65172112"><a name="p65172112"></a><a name="p65172112"></a>serverId</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.2 "><p id="p43655223"><a name="p43655223"></a><a name="p43655223"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.4.1.3 "><p id="p15056362"><a name="p15056362"></a><a name="p15056362"></a>Specifies the ID of the <span id="text610094122518"><a name="text610094122518"></a><a name="text610094122518"></a>BMS</span><span id="text171015413258"><a name="text171015413258"></a><a name="text171015413258"></a></span> to which the disks are attached.</p>
    </td>
    </tr>
    <tr id="row1289536"><td class="cellrowborder" valign="top" width="28.050000000000004%" headers="mcps1.2.4.1.1 "><p id="p37343614"><a name="p37343614"></a><a name="p37343614"></a>volumeId</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.39%" headers="mcps1.2.4.1.2 "><p id="p64098994"><a name="p64098994"></a><a name="p64098994"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.56%" headers="mcps1.2.4.1.3 "><p id="p20397636"><a name="p20397636"></a><a name="p20397636"></a>Specifies the ID of the disk attached to the BMS.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "volumeAttachment": {
            "device": "/dev/vdb",
            "serverId": "820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa",
            "id": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
            "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6"
        }
                    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

