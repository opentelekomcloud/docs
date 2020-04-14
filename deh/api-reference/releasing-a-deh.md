# Releasing a DeH<a name="EN-US_TOPIC_0087389320"></a>

## Function<a name="section43680716"></a>

This API is used to release a DeH.

## Constraints<a name="section48477080"></a>

A DeH accommodating ECSs cannot be released.

## URI<a name="section57582125"></a>

DELETE /v1.0/\{project\_id\}/dedicated-hosts/\{dedicated\_host\_id\}

[Table 1](#table572214121015)  describes the parameters.

**Table  1**  Parameters description

<a name="table572214121015"></a>
<table><thead align="left"><tr id="row572516410109"><th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.1"><p id="p107252049107"><a name="p107252049107"></a><a name="p107252049107"></a><strong id="b3748104017259"><a name="b3748104017259"></a><a name="b3748104017259"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.5.1.2"><p id="p726975522919"><a name="p726975522919"></a><a name="p726975522919"></a><strong id="b1611144220256"><a name="b1611144220256"></a><a name="b1611144220256"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.3"><p id="p072564201017"><a name="p072564201017"></a><a name="p072564201017"></a><strong id="b189294272515"><a name="b189294272515"></a><a name="b189294272515"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p47253421017"><a name="p47253421017"></a><a name="p47253421017"></a><strong id="b1570119439251"><a name="b1570119439251"></a><a name="b1570119439251"></a>Description</strong></p>
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

## Request<a name="section34329433"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-hosts/74259164-e63a-4ad9-9c77-a1bd2c9aa187
    ```


## Response<a name="section40529449"></a>

-   Response parameters

    None

-   Example response

    ```
    Http Response Code: 204
    ```


## Status Code<a name="section18068697"></a>

<a name="table61744252"></a>
<table><thead align="left"><tr id="row46013667"><th class="cellrowborder" valign="top" width="38.379999999999995%" id="mcps1.1.3.1.1"><p id="p36119548"><a name="p36119548"></a><a name="p36119548"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="61.62%" id="mcps1.1.3.1.2"><p id="p40002310"><a name="p40002310"></a><a name="p40002310"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24476477"><td class="cellrowborder" valign="top" width="38.379999999999995%" headers="mcps1.1.3.1.1 "><p id="p36437619"><a name="p36437619"></a><a name="p36437619"></a>409 Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.1.3.1.2 "><p id="p65765997"><a name="p65765997"></a><a name="p65765997"></a>A DeH accommodating ECSs cannot be released.</p>
</td>
</tr>
</tbody>
</table>

For more status codes, see  [Status Codes](status-codes.md).

