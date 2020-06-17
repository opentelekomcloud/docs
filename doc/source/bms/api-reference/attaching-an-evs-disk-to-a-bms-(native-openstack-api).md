# Attaching an EVS Disk to a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158614"></a>

## Function<a name="section53922917165259"></a>

This API is used to attach an EVS disk to a BMS.

## Constraints<a name="section64211377173223"></a>

-   A bootable disk cannot be attached to a BMS.
-   A disk cannot be attached to a BMS when the BMS is in the  **SUSPENDED**  or  **PAUSED**  state, which is specified using the  **OS-EXT-STS:vm\_state**  parameter.
-   Only a shared disk or a disk in the  **available**  state can be attached to a BMS.
-   Only EVS disks whose device type is  **SCSI**  can be attached to a BMS.

## URI<a name="section51121191165259"></a>

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments

[Table 1](#table12701051155110)  lists the parameters.

**Table  1**  Parameter description

<a name="table12701051155110"></a>
<table><thead align="left"><tr id="row97265111518"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p58268319165259"><a name="p58268319165259"></a><a name="p58268319165259"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p22113407165259"><a name="p22113407165259"></a><a name="p22113407165259"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p46355523165259"><a name="p46355523165259"></a><a name="p46355523165259"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row972551165120"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1624545165259"><a name="p1624545165259"></a><a name="p1624545165259"></a>Specifies the project ID.</p>
<p id="p13397185821014"><a name="p13397185821014"></a><a name="p13397185821014"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row57216516518"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28142050151519"><a name="p28142050151519"></a><a name="p28142050151519"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64913614151519"><a name="p64913614151519"></a><a name="p64913614151519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23511349151519"><a name="p23511349151519"></a><a name="p23511349151519"></a>Specifies the BMS ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section8194118165259"></a>

-   Request parameters

    <a name="table38613152151549"></a>
    <table><thead align="left"><tr id="row40874938151549"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.1.5.1.2"><p id="p54711237974"><a name="p54711237974"></a><a name="p54711237974"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.05%" id="mcps1.1.5.1.3"><p id="p4546697"><a name="p4546697"></a><a name="p4546697"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.72%" id="mcps1.1.5.1.4"><p id="p32738149"><a name="p32738149"></a><a name="p32738149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62881453151549"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p60232972151549"><a name="p60232972151549"></a><a name="p60232972151549"></a>volumeAttachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p1647112371173"><a name="p1647112371173"></a><a name="p1647112371173"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.5.1.3 "><p id="p47032596151549"><a name="p47032596151549"></a><a name="p47032596151549"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.72%" headers="mcps1.1.5.1.4 "><p id="p14307644151549"><a name="p14307644151549"></a><a name="p14307644151549"></a>Specifies the disks to be attached. For details, see <a href="#table40707503151632">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **volumeAttachment**  field data structure description

    <a name="table40707503151632"></a>
    <table><thead align="left"><tr id="row46910609151632"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p136661044172118"><a name="p136661044172118"></a><a name="p136661044172118"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.2.5.1.2"><p id="p3250145875"><a name="p3250145875"></a><a name="p3250145875"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.5.1.3"><p id="p1866954412110"><a name="p1866954412110"></a><a name="p1866954412110"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="38.53%" id="mcps1.2.5.1.4"><p id="p467394452117"><a name="p467394452117"></a><a name="p467394452117"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56436699151632"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7969910151632"><a name="p7969910151632"></a><a name="p7969910151632"></a>volumeId</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.5.1.2 "><p id="p1425034513716"><a name="p1425034513716"></a><a name="p1425034513716"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.3 "><p id="p41582949151632"><a name="p41582949151632"></a><a name="p41582949151632"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.5.1.4 "><p id="p28198497151632"><a name="p28198497151632"></a><a name="p28198497151632"></a>Specifies the ID of the disk to be attached to a BMS.</p>
    </td>
    </tr>
    <tr id="row52459882151632"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p21392044151632"><a name="p21392044151632"></a><a name="p21392044151632"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.2.5.1.2 "><p id="p1259612401874"><a name="p1259612401874"></a><a name="p1259612401874"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.5.1.3 "><p id="p55033990151632"><a name="p55033990151632"></a><a name="p55033990151632"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.53%" headers="mcps1.2.5.1.4 "><p id="p7777719105553"><a name="p7777719105553"></a><a name="p7777719105553"></a>Specifies the mount point, such as <strong id="b14157163336"><a name="b14157163336"></a><a name="b14157163336"></a>/dev/sda</strong> and <strong id="b41611613338"><a name="b41611613338"></a><a name="b41611613338"></a>/dev/sdb</strong>.</p>
    <p id="p58233871152743"><a name="p58233871152743"></a><a name="p58233871152743"></a>The new disk mount point cannot be the same as an existing one.</p>
    <p id="p22488653151632"><a name="p22488653151632"></a><a name="p22488653151632"></a>The mount point must be specified based on the sequence of existing device names. Otherwise, the system automatically generates a mount point.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-volume_attachments
    ```

    ```
    {
        "volumeAttachment": {
            "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
            "device": "/dev/sdb"
        }
    }
    ```


## Response Message<a name="section58140617165259"></a>

-   Response parameters

    <a name="table769899"></a>
    <table><thead align="left"><tr id="row6968742"><th class="cellrowborder" valign="top" width="24.55%" id="mcps1.1.4.1.1"><p id="p27597234"><a name="p27597234"></a><a name="p27597234"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.6%" id="mcps1.1.4.1.2"><p id="p5740187"><a name="p5740187"></a><a name="p5740187"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.849999999999994%" id="mcps1.1.4.1.3"><p id="p62302025"><a name="p62302025"></a><a name="p62302025"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13299239"><td class="cellrowborder" valign="top" width="24.55%" headers="mcps1.1.4.1.1 "><p id="p3496541"><a name="p3496541"></a><a name="p3496541"></a>volumeAttachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.6%" headers="mcps1.1.4.1.2 "><p id="p56686067"><a name="p56686067"></a><a name="p56686067"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.849999999999994%" headers="mcps1.1.4.1.3 "><p id="p52192065"><a name="p52192065"></a><a name="p52192065"></a>Specifies the disks attached to a BMS. For details, see <a href="#table548498215180">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **volumeAttachment**  field data structure description

    <a name="table548498215180"></a>
    <table><thead align="left"><tr id="row3759039515180"><th class="cellrowborder" valign="top" width="24.85%" id="mcps1.2.4.1.1"><p id="p2669287225"><a name="p2669287225"></a><a name="p2669287225"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.61%" id="mcps1.2.4.1.2"><p id="p7666288227"><a name="p7666288227"></a><a name="p7666288227"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.54%" id="mcps1.2.4.1.3"><p id="p157112818226"><a name="p157112818226"></a><a name="p157112818226"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4742233715180"><td class="cellrowborder" valign="top" width="24.85%" headers="mcps1.2.4.1.1 "><p id="p1600407115180"><a name="p1600407115180"></a><a name="p1600407115180"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.4.1.2 "><p id="p2126141115180"><a name="p2126141115180"></a><a name="p2126141115180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.54%" headers="mcps1.2.4.1.3 "><p id="p4389880615180"><a name="p4389880615180"></a><a name="p4389880615180"></a>Specifies the device name, for example, <strong id="b170320163315"><a name="b170320163315"></a><a name="b170320163315"></a>/dev/vdb</strong>.</p>
    </td>
    </tr>
    <tr id="row5954494215180"><td class="cellrowborder" valign="top" width="24.85%" headers="mcps1.2.4.1.1 "><p id="p5841097215180"><a name="p5841097215180"></a><a name="p5841097215180"></a>serverId</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.4.1.2 "><p id="p3366825815180"><a name="p3366825815180"></a><a name="p3366825815180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.54%" headers="mcps1.2.4.1.3 "><p id="p4217250415180"><a name="p4217250415180"></a><a name="p4217250415180"></a>Specifies the ID of the BMS to which the disk is to be attached. The ID is in UUID format.</p>
    </td>
    </tr>
    <tr id="row4400822315180"><td class="cellrowborder" valign="top" width="24.85%" headers="mcps1.2.4.1.1 "><p id="p789628615180"><a name="p789628615180"></a><a name="p789628615180"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.4.1.2 "><p id="p3561941815180"><a name="p3561941815180"></a><a name="p3561941815180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.54%" headers="mcps1.2.4.1.3 "><p id="p2593706215180"><a name="p2593706215180"></a><a name="p2593706215180"></a>Specifies the disk UUID.</p>
    </td>
    </tr>
    <tr id="row3210697315180"><td class="cellrowborder" valign="top" width="24.85%" headers="mcps1.2.4.1.1 "><p id="p5052800715180"><a name="p5052800715180"></a><a name="p5052800715180"></a>volumeId</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.4.1.2 "><p id="p6623678615180"><a name="p6623678615180"></a><a name="p6623678615180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.54%" headers="mcps1.2.4.1.3 "><p id="p4966276115180"><a name="p4966276115180"></a><a name="p4966276115180"></a>Specifies the attaching ID, which is the same as the UUID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "volumeAttachment": {
            "id": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
            "volumeId": "b53f23bd-ee8f-49ec-9420-d1acfeaf91d6",
            "serverId": "820abbd0-2d8e-4bc5-ae46-69cacfd4fbaa",
            "device": "/dev/vdb"
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

