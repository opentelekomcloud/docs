# Querying Details About a DeH<a name="EN-US_TOPIC_0087389317"></a>

## Function<a name="section32345284"></a>

This API is used to query details about a DeH.

## URI<a name="section22672102"></a>

GET /v1.0/\{project\_id\}/dedicated-hosts/\{dedicated\_host\_id\}

[Table 1](#table572214121015)  describes the parameters.

**Table  1**  Parameters description

<a name="table572214121015"></a>
<table><thead align="left"><tr id="row572516410109"><th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.1"><p id="p107252049107"><a name="p107252049107"></a><a name="p107252049107"></a><strong id="b7893101914414"><a name="b7893101914414"></a><a name="b7893101914414"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.5.1.2"><p id="p726975522919"><a name="p726975522919"></a><a name="p726975522919"></a><strong id="b16213921114414"><a name="b16213921114414"></a><a name="b16213921114414"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.3"><p id="p072564201017"><a name="p072564201017"></a><a name="p072564201017"></a><strong id="b13261102244413"><a name="b13261102244413"></a><a name="b13261102244413"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p47253421017"><a name="p47253421017"></a><a name="p47253421017"></a><strong id="b14400162364419"><a name="b14400162364419"></a><a name="b14400162364419"></a>Description</strong></p>
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
<p id="p127584489356"><a name="p127584489356"></a><a name="p127584489356"></a>You can obtain the DeH ID from the DeH console or using the <a href="querying-dehs.md">Querying DeHs</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section19182316"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-hosts/ab910cf0daebca90c4001
    ```


## Response<a name="section38423121"></a>

-   Response parameters

    <a name="table30686701"></a>
    <table><thead align="left"><tr id="row2338313"><th class="cellrowborder" valign="top" width="21.66%" id="mcps1.1.5.1.1"><p id="p55185655"><a name="p55185655"></a><a name="p55185655"></a><strong id="b11491950174411"><a name="b11491950174411"></a><a name="b11491950174411"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.61%" id="mcps1.1.5.1.2"><p id="p40853074"><a name="p40853074"></a><a name="p40853074"></a><strong id="b105665174411"><a name="b105665174411"></a><a name="b105665174411"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.4%" id="mcps1.1.5.1.3"><p id="p16923123020110"><a name="p16923123020110"></a><a name="p16923123020110"></a><strong id="b4262175220449"><a name="b4262175220449"></a><a name="b4262175220449"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.1.5.1.4"><p id="p179256301419"><a name="p179256301419"></a><a name="p179256301419"></a><strong id="b687125319447"><a name="b687125319447"></a><a name="b687125319447"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54251110"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.5.1.1 "><p id="p32263784"><a name="p32263784"></a><a name="p32263784"></a>dedicated_host</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.5.1.2 "><p id="p63229698"><a name="p63229698"></a><a name="p63229698"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.4%" headers="mcps1.1.5.1.3 "><p id="p148485409586"><a name="p148485409586"></a><a name="p148485409586"></a>Object</p>
    <p id="p21331933"><a name="p21331933"></a><a name="p21331933"></a>For details, see <a href="object-models.md#dedicated_host">Table 1</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.1.5.1.4 "><p id="p63081244"><a name="p63081244"></a><a name="p63081244"></a>Specifies the DeH object.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "dedicated_host": {
            "dedicated_host_id": "ab910cf0daebca90c4001",
            "name": "win_2008 servers",
            "auto_placement": "off",
            "availability_zone": "az1",
            "host_properties": {
                "vcpus": 36,
                "cores": 12,
                "sockets": 2,
                "memory": 1073741824,
                "host_type": "h1",
                "host_type_name": "High performance",
                "available_instance_capacities": [
                    {
                        "flavor": "h1.large"
                    },
                    {
                        "flavor": "h1.2large"
                    },
                    {
                        "flavor": "h1.4large"
                    },
                    {
                        "flavor": "h1.8large"
                    }
                ]
            },
            "state": "available",
            "project_id": "9c53a566cb3443ab910cf0daebca90c4",
            "available_vcpus": 20,
            "available_memory": 1073201821,
            "instance_total": 2,
            "allocated_at": "2016-10-10T14:35:47Z",
            "released_at": null,
            "instance_uuids": [
                "erf5th66cb3443ab912ff0daebca3456",
                "23457h66cb3443ab912ff0daebcaer45"
            ]
        }
    }
    ```


## Status Code<a name="section26059286"></a>

See  [Status Codes](status-codes.md).

