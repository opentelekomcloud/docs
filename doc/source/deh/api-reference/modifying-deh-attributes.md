# Modifying DeH Attributes<a name="EN-US_TOPIC_0087389319"></a>

## Function<a name="section2129750"></a>

This API is used to modify the  **auto\_placement**  and  **name**  attributes of a DeH.

## URI<a name="section19167756"></a>

PUT /v1.0/\{project\_id\}/dedicated-hosts/\{dedicated\_host\_id\}

[Table 1](#table572214121015)  describes the parameters.

**Table  1**  Parameters description

<a name="table572214121015"></a>
<table><thead align="left"><tr id="row572516410109"><th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.1"><p id="p107252049107"><a name="p107252049107"></a><a name="p107252049107"></a><strong id="b212574719219"><a name="b212574719219"></a><a name="b212574719219"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.5.1.2"><p id="p726975522919"><a name="p726975522919"></a><a name="p726975522919"></a><strong id="b105121348202117"><a name="b105121348202117"></a><a name="b105121348202117"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.3"><p id="p072564201017"><a name="p072564201017"></a><a name="p072564201017"></a><strong id="b549624952117"><a name="b549624952117"></a><a name="b549624952117"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p47253421017"><a name="p47253421017"></a><a name="p47253421017"></a><strong id="b1834714506210"><a name="b1834714506210"></a><a name="b1834714506210"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row107256481017"><td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.1 "><p id="p1872514451016"><a name="p1872514451016"></a><a name="p1872514451016"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.5.1.2 "><p id="p12269175511291"><a name="p12269175511291"></a><a name="p12269175511291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.3 "><p id="p147251646108"><a name="p147251646108"></a><a name="p147251646108"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p6725747104"><a name="p6725747104"></a><a name="p6725747104"></a>Specifies the project ID.</p>
<p id="p7376194915119"><a name="p7376194915119"></a><a name="p7376194915119"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row184436404555"><td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.1 "><p id="p164455404556"><a name="p164455404556"></a><a name="p164455404556"></a>dedicated_host_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.5.1.2 "><p id="p29241051175512"><a name="p29241051175512"></a><a name="p29241051175512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.3 "><p id="p1592535185519"><a name="p1592535185519"></a><a name="p1592535185519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1544524011550"><a name="p1544524011550"></a><a name="p1544524011550"></a>Specifies the DeH ID.</p>
<p id="p858154817367"><a name="p858154817367"></a><a name="p858154817367"></a>You can obtain the DeH ID from the DeH console or using the <a href="querying-dehs.md">Querying DeHs</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section14650458"></a>

-   Request parameters

    <a name="table13105749"></a>
    <table><thead align="left"><tr id="row64305920"><th class="cellrowborder" valign="top" width="16.03%" id="mcps1.1.6.1.1"><p id="p41397042"><a name="p41397042"></a><a name="p41397042"></a><strong id="b76877419229"><a name="b76877419229"></a><a name="b76877419229"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.04%" id="mcps1.1.6.1.2"><p id="p64826129"><a name="p64826129"></a><a name="p64826129"></a><strong id="b117919712226"><a name="b117919712226"></a><a name="b117919712226"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.459999999999999%" id="mcps1.1.6.1.3"><p id="p16425092"><a name="p16425092"></a><a name="p16425092"></a><strong id="b13462118112211"><a name="b13462118112211"></a><a name="b13462118112211"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.790000000000003%" id="mcps1.1.6.1.4"><p id="p55364084"><a name="p55364084"></a><a name="p55364084"></a><strong id="b6347591221"><a name="b6347591221"></a><a name="b6347591221"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.68%" id="mcps1.1.6.1.5"><p id="p55305800"><a name="p55305800"></a><a name="p55305800"></a><strong id="b19400141010221"><a name="b19400141010221"></a><a name="b19400141010221"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17937528"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.1.6.1.1 "><p id="p43653635"><a name="p43653635"></a><a name="p43653635"></a>auto_placement</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.1.6.1.2 "><p id="p46283551"><a name="p46283551"></a><a name="p46283551"></a>in</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.6.1.3 "><p id="p57980147"><a name="p57980147"></a><a name="p57980147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.1.6.1.4 "><p id="p65880360"><a name="p65880360"></a><a name="p65880360"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.68%" headers="mcps1.1.6.1.5 "><p id="OLE_LINK105"><a name="OLE_LINK105"></a><a name="OLE_LINK105"></a>Specifies whether to allow an ECS to be placed on any available DeH if its DeH ID is not specified during its creation.</p>
    <p id="p56666602"><a name="p56666602"></a><a name="p56666602"></a>The value can be <strong id="b1588844916239"><a name="b1588844916239"></a><a name="b1588844916239"></a>on</strong> or <strong id="b1889074982311"><a name="b1889074982311"></a><a name="b1889074982311"></a>off</strong>.</p>
    </td>
    </tr>
    <tr id="row25151514"><td class="cellrowborder" valign="top" width="16.03%" headers="mcps1.1.6.1.1 "><p id="p24006753"><a name="p24006753"></a><a name="p24006753"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.1.6.1.2 "><p id="p65498832"><a name="p65498832"></a><a name="p65498832"></a>in</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.6.1.3 "><p id="p3805200"><a name="p3805200"></a><a name="p3805200"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.1.6.1.4 "><p id="p39785801"><a name="p39785801"></a><a name="p39785801"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.68%" headers="mcps1.1.6.1.5 "><p id="p1424418"><a name="p1424418"></a><a name="p1424418"></a>Specifies the DeH name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-hosts/74259164-e63a-4ad9-9c77-a1bd2c9aa187
    {
        "dedicated_host": {
            "auto_placement": "off",
            "name": "DeH_vm3"
        }
    }
    ```


## Response<a name="section64745266"></a>

-   Response parameters

    None

-   Example response

    ```
    Http Response Code: 204
    ```


## Status Code<a name="section21768161"></a>

See  [Status Codes](status-codes.md).

