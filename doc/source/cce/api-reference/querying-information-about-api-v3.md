# Querying Information About API v3<a name="cce_02_0350"></a>

## Function<a name="se2e066518e534a58a022d07edfbd4a3f"></a>

This API is used to query information about API v3.

## URI<a name="s9ba079db556c4be7998a917fb1004946"></a>

GET /v3

## Request<a name="sfa7f4cd949044a198e9f9a0518344e7f"></a>

N/A

## Response<a name="s2eb2c416e8d344619301671f0baffc10"></a>

**Response parameters:**

[Table 1](#table986610460219)  describes the response parameters.

**Table  1**  Response parameters

<a name="table986610460219"></a>
<table><thead align="left"><tr id="row3867846192120"><th class="cellrowborder" valign="top" width="20.392039203920394%" id="mcps1.2.4.1.1"><p id="p1086764618217"><a name="p1086764618217"></a><a name="p1086764618217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.23212321232123%" id="mcps1.2.4.1.2"><p id="p10867184611219"><a name="p10867184611219"></a><a name="p10867184611219"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.37583758375837%" id="mcps1.2.4.1.3"><p id="p08676468210"><a name="p08676468210"></a><a name="p08676468210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20867124611213"><td class="cellrowborder" valign="top" width="20.392039203920394%" headers="mcps1.2.4.1.1 "><p id="p2086715463216"><a name="p2086715463216"></a><a name="p2086715463216"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="21.23212321232123%" headers="mcps1.2.4.1.2 "><p id="p178672046192113"><a name="p178672046192113"></a><a name="p178672046192113"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.37583758375837%" headers="mcps1.2.4.1.3 "><p id="p129231114292"><a name="p129231114292"></a><a name="p129231114292"></a>API version list.</p>
</td>
</tr>
</tbody>
</table>

**Example response:**

```
{
    "versions": [
        {
            "id": "v3",
            "links": [
                {
                    "href": "https://container.eu-de.otc.t-systems.com/v3",
                    "rel": "self"
                }
            ],
            "min_version": "",
            "status": "CURRENT",
            "updated": "2018-09-15T00:00:00Z",
            "version": ""
        }
    ]
}
```

## Status Code<a name="sf5b489c1f62d4d909a30f683dc319340"></a>

[Table 2](#t8935d48c19714740abd2e888a39be462)  describes the status code of the API.

**Table  2**  Status code

<a name="t8935d48c19714740abd2e888a39be462"></a>
<table><thead align="left"><tr id="re974d044247140b79c213fc577abe0ae"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="a9465a1e476c948e4b40095738594daf3"><a name="a9465a1e476c948e4b40095738594daf3"></a><a name="a9465a1e476c948e4b40095738594daf3"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="a88c1c2f27be844b7b79dad7e1a5b06f2"><a name="a88c1c2f27be844b7b79dad7e1a5b06f2"></a><a name="a88c1c2f27be844b7b79dad7e1a5b06f2"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rb535f7f0f62341f7b636e54ce399b342"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="ad1d3b647d2f746cc88b562f3eb1ff493"><a name="ad1d3b647d2f746cc88b562f3eb1ff493"></a><a name="ad1d3b647d2f746cc88b562f3eb1ff493"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="a78dc15895d744bb9affa7db6de6e02e5"><a name="a78dc15895d744bb9affa7db6de6e02e5"></a><a name="a78dc15895d744bb9affa7db6de6e02e5"></a>The query operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).

