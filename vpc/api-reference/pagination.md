# Pagination<a name="vpc_version_0003"></a>

## Function<a name="section3385602995157"></a>

Neutron APIs v2.0 provides the pagination function. You can set parameters  **limit**  and  **marker**  in the URL to enable the desired number of items to be returned. All returned items are displayed in the ascending order of ID.

-   To access the next page of the request, perform the following configurations:
    -   Replace the value of  **marker**  in the original access request URL. Replace the value of  **marker**  to the value of  **marker**  in the value of  **herf**  if the value of  **rel**  in the response is  **next**.
    -   Set the value of  **page\_reverse**  to  **False**.

-   To access the previous page of the request, perform the following configurations:
    -   Replace the value of  **marker**  in the original access request URL. Replace the value of  **marker**  to the value of  **marker**  in the value of  **herf**  if the value of  **rel**  in the response is  **previous**.
    -   Set the value of  **page\_reverse**  to  **True**.


## Request Message<a name="section483652795144"></a>

Request parameter

**Table  1**  Request parameter

<a name="table5621437795144"></a>
<table><thead align="left"><tr id="row2739272895144"><th class="cellrowborder" valign="top" width="16.97%" id="mcps1.2.5.1.1"><p id="p421851895144"><a name="p421851895144"></a><a name="p421851895144"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.78%" id="mcps1.2.5.1.2"><p id="p615565295144"><a name="p615565295144"></a><a name="p615565295144"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.81%" id="mcps1.2.5.1.3"><p id="p2884577095144"><a name="p2884577095144"></a><a name="p2884577095144"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.5.1.4"><p id="p5480603395144"><a name="p5480603395144"></a><a name="p5480603395144"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1010368095144"><td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.5.1.1 "><p id="p1309177695144"><a name="p1309177695144"></a><a name="p1309177695144"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.2.5.1.2 "><p id="p5380095395144"><a name="p5380095395144"></a><a name="p5380095395144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.3 "><p id="p6290990695144"><a name="p6290990695144"></a><a name="p6290990695144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.5.1.4 "><p id="p6253758795144"><a name="p6253758795144"></a><a name="p6253758795144"></a>Specifies the number of items displayed per page.</p>
</td>
</tr>
<tr id="row2596737495144"><td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.5.1.1 "><p id="p2298257595144"><a name="p2298257595144"></a><a name="p2298257595144"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.2.5.1.2 "><p id="p4964932595144"><a name="p4964932595144"></a><a name="p4964932595144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.3 "><p id="p6217239995144"><a name="p6217239995144"></a><a name="p6217239995144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.5.1.4 "><p id="p279958295144"><a name="p279958295144"></a><a name="p279958295144"></a>Specifies the ID of the last item in the previous list. If the marker value is invalid, error code 400 will be returned.</p>
</td>
</tr>
<tr id="row2519624195144"><td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.5.1.1 "><p id="p2762967895144"><a name="p2762967895144"></a><a name="p2762967895144"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="12.78%" headers="mcps1.2.5.1.2 "><p id="p2341143595144"><a name="p2341143595144"></a><a name="p2341143595144"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.2.5.1.3 "><p id="p1727806495144"><a name="p1727806495144"></a><a name="p1727806495144"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.5.1.4 "><p id="p5734595895144"><a name="p5734595895144"></a><a name="p5734595895144"></a>Specifies the page direction. The value can be <strong id="b842352706114342"><a name="b842352706114342"></a><a name="b842352706114342"></a>True</strong> or <strong id="b842352706114350"><a name="b842352706114350"></a><a name="b842352706114350"></a>False</strong>.</p>
</td>
</tr>
</tbody>
</table>

Example request 1

```
GET https://{Endpoint}/v2.0/networks?limit=2&marker=3d42a0d4-a980-4613-ae76-a2cddecff054&page_reverse=False
```

Example request 2

```
GET https://{Endpoint}/v2.0/vpc/peerings?limit=2&marker=e5a0c88e-228e-4e62-a8b0-90825b1b7958&page_reverse=True
```

## Response Message<a name="section3454265995144"></a>

Response parameter

None

Example response 1

```
{
    "networks": [
        {
            "status": "ACTIVE",
            "subnets": [],
            "name": "liudongtest ",
            "admin_state_up": false,
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "id": "60c809cb-6731-45d0-ace8-3bf5626421a9"
        },
        {
            "status": "ACTIVE",
            "subnets": [
                "132dc12d-c02a-4c90-9cd5-c31669aace04"
            ],
            "name": "publicnet",
            "admin_state_up": true,
            "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
            "id": "9daeac7c-a98f-430f-8e38-67f9c044e299"
        }
    ],
    "networks_links": [
        {
            "href": "http://192.168.82.231:9696/v2.0/networks?limit=2&marker=9daeac7c-a98f-430f-8e38-67f9c044e299",
            "rel": "next"
        },
        {
            "href": "http://192.168.82.231:9696/v2.0/networks?limit=2&marker=60c809cb-6731-45d0-ace8-3bf5626421a9&page_reverse=True",
            "rel": "previous"
        }
    ]
}
```

Example response 2

```
{
    "peerings_links": [
        {
            "marker": "dd442819-5638-401c-bd48-a82703cf0464",
            "rel": "next"
        },
        {
            "marker": "1e13cbaf-3ce4-413d-941f-66d855dbfa7f",
            "rel": "previous"
        }
    ],
    "peerings": [
        {
            "status": "ACTIVE",
            "accept_vpc_info": {
                "vpc_id": "83a48834-b9bc-4f70-aa46-074568594650",
                "tenant_id": "e41a43bf06e249678413c6d61536eff9"
            },
            "request_vpc_info": {
                "vpc_id": "db8e7687-e43b-4fc1-94cf-16f69f484d6d",
                "tenant_id": "e41a43bf06e249678413c6d61536eff9"
            },
            "name": "peering1",
            "id": "1e13cbaf-3ce4-413d-941f-66d855dbfa7f"
        },
        {
            "status": "ACTIVE",
            "accept_vpc_info": {
                "vpc_id": "83a48834-b9bc-4f70-aa46-074568594650",
                "tenant_id": "e41a43bf06e249678413c6d61536eff9"
            },
            "request_vpc_info": {
                "vpc_id": "bd63cc9e-e7b8-4d4e-a0e9-055031470ffc",
                "tenant_id": "e41a43bf06e249678413c6d61536eff9"
            },
            "name": "peering2",
            "id": "dd442819-5638-401c-bd48-a82703cf0464"
        }
    ]
}
```

## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

