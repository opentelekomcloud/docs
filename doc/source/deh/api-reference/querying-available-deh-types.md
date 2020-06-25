# Querying Available DeH Types<a name="EN-US_TOPIC_0087389321"></a>

## Function<a name="section36279478"></a>

This API is used to query available DeH types in an AZ.

## URI<a name="section58079852"></a>

Get /v1.0/\{project\_id\}/availability-zone/\{availability\_zone\}/dedicated-host-types

[Table 1](#table572214121015)  describes the parameters.

**Table  1**  Parameters description

<a name="table572214121015"></a>
<table><thead align="left"><tr id="row572516410109"><th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.1"><p id="p107252049107"><a name="p107252049107"></a><a name="p107252049107"></a><strong id="b334893110258"><a name="b334893110258"></a><a name="b334893110258"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.5.1.2"><p id="p726975522919"><a name="p726975522919"></a><a name="p726975522919"></a><strong id="b13444183213253"><a name="b13444183213253"></a><a name="b13444183213253"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.3"><p id="p072564201017"><a name="p072564201017"></a><a name="p072564201017"></a><strong id="b041613338256"><a name="b041613338256"></a><a name="b041613338256"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p47253421017"><a name="p47253421017"></a><a name="p47253421017"></a><strong id="b1030643472510"><a name="b1030643472510"></a><a name="b1030643472510"></a>Description</strong></p>
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
<tr id="row184436404555"><td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.1 "><p id="p164455404556"><a name="p164455404556"></a><a name="p164455404556"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.5.1.2 "><p id="p29241051175512"><a name="p29241051175512"></a><a name="p29241051175512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.3 "><p id="p1592535185519"><a name="p1592535185519"></a><a name="p1592535185519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1544524011550"><a name="p1544524011550"></a><a name="p1544524011550"></a>Specifies the AZ.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section61627937"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/availability-zone/az1/dedicated-host-types
    ```


## Response<a name="section17780525"></a>

-   Response parameters

    <a name="table34453949"></a>
    <table><thead align="left"><tr id="row7748772"><th class="cellrowborder" valign="top" width="22.617738226177384%" id="mcps1.1.5.1.1"><p id="p0917228174615"><a name="p0917228174615"></a><a name="p0917228174615"></a><strong id="b192781257112517"><a name="b192781257112517"></a><a name="b192781257112517"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.1.5.1.2"><p id="p8918122810460"><a name="p8918122810460"></a><a name="p8918122810460"></a><strong id="b11294585258"><a name="b11294585258"></a><a name="b11294585258"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.1.5.1.3"><p id="p8919628124616"><a name="p8919628124616"></a><a name="p8919628124616"></a><strong id="b9511259152518"><a name="b9511259152518"></a><a name="b9511259152518"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.66583341665834%" id="mcps1.1.5.1.4"><p id="p14922328134614"><a name="p14922328134614"></a><a name="p14922328134614"></a><strong id="b6818959172518"><a name="b6818959172518"></a><a name="b6818959172518"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36008632"><td class="cellrowborder" valign="top" width="22.617738226177384%" headers="mcps1.1.5.1.1 "><p id="p31018066"><a name="p31018066"></a><a name="p31018066"></a>dedicated_host_types</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.2 "><p id="p29435437"><a name="p29435437"></a><a name="p29435437"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p35460209"><a name="p35460209"></a><a name="p35460209"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.66583341665834%" headers="mcps1.1.5.1.4 "><p id="p55108945"><a name="p55108945"></a><a name="p55108945"></a>Specifies the available DeH types.</p>
    </td>
    </tr>
    <tr id="row26218460"><td class="cellrowborder" valign="top" width="22.617738226177384%" headers="mcps1.1.5.1.1 "><p id="p43320496"><a name="p43320496"></a><a name="p43320496"></a>host_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.2 "><p id="p19299281"><a name="p19299281"></a><a name="p19299281"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p19737894"><a name="p19737894"></a><a name="p19737894"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.66583341665834%" headers="mcps1.1.5.1.4 "><p id="p47325326"><a name="p47325326"></a><a name="p47325326"></a>Specifies the DeH type.</p>
    </td>
    </tr>
    <tr id="row97082225319"><td class="cellrowborder" valign="top" width="22.617738226177384%" headers="mcps1.1.5.1.1 "><p id="p07097275310"><a name="p07097275310"></a><a name="p07097275310"></a>host_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.2 "><p id="p670911212532"><a name="p670911212532"></a><a name="p670911212532"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.5.1.3 "><p id="p17709224533"><a name="p17709224533"></a><a name="p17709224533"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.66583341665834%" headers="mcps1.1.5.1.4 "><p id="p187091221534"><a name="p187091221534"></a><a name="p187091221534"></a>Specifies the name of the DeH type.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "dedicated_host_types": [
            {
                "host_type": "General",
                "host_type_name": "General Computing"
            },
            {
                "host_type": "m1",
                "host_type_name": "Memory-optimized"
            },
            {
                "host_type": "h2",
                "host_type_name": "High performance"
            },
            {
                "host_type": "d1",
                "host_type_name": "Disk intensive"
            }
        ]
    }
    ```


## Status Code<a name="section9992350"></a>

See  [Status Codes](status-codes.md).

