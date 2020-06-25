# Querying Data in Pages<a name="EN-US_TOPIC_0109430488"></a>

APIs v2.0 allow users to query data in pages by adding the limit and marker parameters to the URL of the list request. The query results are displayed in the ascending order of ID.

-   **next ref**  in the response indicates the URL of the next page.
-   **previous ref**  in the response indicates the URL of the previous page.

## Request<a name="en-us_topic_0049143234_section52468780"></a>

**Table  1**  Parameter description

<a name="en-us_topic_0049143234_table2460041"></a>
<table><thead align="left"><tr id="en-us_topic_0049143234_row40101120"><th class="cellrowborder" valign="top" width="19.368063193680634%" id="mcps1.2.5.1.1"><p id="en-us_topic_0049143234_p26965262"><a name="en-us_topic_0049143234_p26965262"></a><a name="en-us_topic_0049143234_p26965262"></a><strong id="en-us_topic_0049143234_b842352706164319"><a name="en-us_topic_0049143234_b842352706164319"></a><a name="en-us_topic_0049143234_b842352706164319"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.33856614338566%" id="mcps1.2.5.1.2"><p id="en-us_topic_0049143234_p36702580"><a name="en-us_topic_0049143234_p36702580"></a><a name="en-us_topic_0049143234_p36702580"></a><strong id="en-us_topic_0049143234_b8423527061617"><a name="en-us_topic_0049143234_b8423527061617"></a><a name="en-us_topic_0049143234_b8423527061617"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.558244175582445%" id="mcps1.2.5.1.3"><p id="en-us_topic_0049143234_p20119003"><a name="en-us_topic_0049143234_p20119003"></a><a name="en-us_topic_0049143234_p20119003"></a><strong id="en-us_topic_0049143234_b842352706192658"><a name="en-us_topic_0049143234_b842352706192658"></a><a name="en-us_topic_0049143234_b842352706192658"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.735126487351266%" id="mcps1.2.5.1.4"><p id="en-us_topic_0049143234_p19026538"><a name="en-us_topic_0049143234_p19026538"></a><a name="en-us_topic_0049143234_p19026538"></a><strong id="en-us_topic_0049143234_b84235270695939"><a name="en-us_topic_0049143234_b84235270695939"></a><a name="en-us_topic_0049143234_b84235270695939"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049143234_row64754634"><td class="cellrowborder" valign="top" width="19.368063193680634%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049143234_p10634019"><a name="en-us_topic_0049143234_p10634019"></a><a name="en-us_topic_0049143234_p10634019"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.33856614338566%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0049143234_p56049180"><a name="en-us_topic_0049143234_p56049180"></a><a name="en-us_topic_0049143234_p56049180"></a>int</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049143234_p43689693"><a name="en-us_topic_0049143234_p43689693"></a><a name="en-us_topic_0049143234_p43689693"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48.735126487351266%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049143234_p49204239"><a name="en-us_topic_0049143234_p49204239"></a><a name="en-us_topic_0049143234_p49204239"></a>Specifies the number of records on each page.</p>
<p id="en-us_topic_0049143234_p184521154391"><a name="en-us_topic_0049143234_p184521154391"></a><a name="en-us_topic_0049143234_p184521154391"></a>The value ranges from <strong id="b1045513253378"><a name="b1045513253378"></a><a name="b1045513253378"></a>0</strong> to <strong id="b245616259371"><a name="b245616259371"></a><a name="b245616259371"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0049143234_row40184969"><td class="cellrowborder" valign="top" width="19.368063193680634%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049143234_p33757095"><a name="en-us_topic_0049143234_p33757095"></a><a name="en-us_topic_0049143234_p33757095"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.33856614338566%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0049143234_p49970185"><a name="en-us_topic_0049143234_p49970185"></a><a name="en-us_topic_0049143234_p49970185"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049143234_p21053208"><a name="en-us_topic_0049143234_p21053208"></a><a name="en-us_topic_0049143234_p21053208"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48.735126487351266%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049143234_en-us_topic_0020100172_p65836146103218"><a name="en-us_topic_0049143234_en-us_topic_0020100172_p65836146103218"></a><a name="en-us_topic_0049143234_en-us_topic_0020100172_p65836146103218"></a>Specifies the resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="en-us_topic_0049143234_row46967960"><td class="cellrowborder" valign="top" width="19.368063193680634%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0049143234_p46308405"><a name="en-us_topic_0049143234_p46308405"></a><a name="en-us_topic_0049143234_p46308405"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="14.33856614338566%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0049143234_p59993306"><a name="en-us_topic_0049143234_p59993306"></a><a name="en-us_topic_0049143234_p59993306"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0049143234_p27619632"><a name="en-us_topic_0049143234_p27619632"></a><a name="en-us_topic_0049143234_p27619632"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48.735126487351266%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0049143234_p22597726"><a name="en-us_topic_0049143234_p22597726"></a><a name="en-us_topic_0049143234_p22597726"></a>Specifies the paging sequence. The value can be <strong id="en-us_topic_0049143234_b842352706153910"><a name="en-us_topic_0049143234_b842352706153910"></a><a name="en-us_topic_0049143234_b842352706153910"></a>true</strong> or <strong id="en-us_topic_0049143234_b842352706153913"><a name="en-us_topic_0049143234_b842352706153913"></a><a name="en-us_topic_0049143234_b842352706153913"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0049143234_section22112815"></a>

None

## Example<a name="section1790101219242"></a>

-   Example request

    ```
    GET /v2.0/networks?limit=2&marker=3d42a0d4-a980-4613-ae76-a2cddecff054&page_reverse=False
    ```


-   Example response

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


