# Modifying a Health Check<a name="EN-US_TOPIC_0096561564"></a>

## Function<a name="en-us_topic_0049139666_section37518984"></a>

This API is used to modify a health check.

## API Format<a name="en-us_topic_0049139666_section2126544"></a>

<a name="en-us_topic_0049139666_table1184116413128"></a><table><thead align="left"><tr id="en-us_topic_0049139666_row6581056513128"><th class="cellrowborder" valign="top" width="10.780000000000001%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139666_p1400970613132"><a name="en-us_topic_0049139666_p1400970613132"></a><a name="en-us_topic_0049139666_p1400970613132"></a><strong id="b842352706172312"><a name="b842352706172312"></a><a name="b842352706172312"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139666_p6104436813132"><a name="en-us_topic_0049139666_p6104436813132"></a><a name="en-us_topic_0049139666_p6104436813132"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139666_p4564677513132"><a name="en-us_topic_0049139666_p4564677513132"></a><a name="en-us_topic_0049139666_p4564677513132"></a><strong id="b842352706192251"><a name="b842352706192251"></a><a name="b842352706192251"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139666_row3119415813128"><td class="cellrowborder" valign="top" width="10.780000000000001%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139666_p4874218213132"><a name="en-us_topic_0049139666_p4874218213132"></a><a name="en-us_topic_0049139666_p4874218213132"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0049139666_p5580268713132"><a name="en-us_topic_0049139666_p5580268713132"></a><a name="en-us_topic_0049139666_p5580268713132"></a>/v2.0/lbaas/healthmonitors/{healthmonitor_id}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0049139666_p2372376813132"><a name="en-us_topic_0049139666_p2372376813132"></a><a name="en-us_topic_0049139666_p2372376813132"></a>Updates information about a specific health check.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139666_section19138897"></a>

-   Only fields  **delay**,  **max\_retries**,  **name**,  **domain\_name**,  **timeout**,  **http\_method**,  **expected\_codes**,  **url\_path**,  **monitor\_port**, and  **admin\_state\_up**  can be modified.
-   If  **provisioning\_status**  of the load balancer for which the health check is configured is not  **ACTIVE**, the health check cannot be updated.

## Request<a name="en-us_topic_0049139666_section60721476"></a>

-   Parameter description

    <a name="en-us_topic_0049139666_table12185309"></a><table><thead align="left"><tr id="en-us_topic_0049139666_row58571242"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.1.5.1.1"><p id="en-us_topic_0049139666_p46650162"><a name="en-us_topic_0049139666_p46650162"></a><a name="en-us_topic_0049139666_p46650162"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.53%" id="mcps1.1.5.1.2"><p id="en-us_topic_0049139666_p20566791"><a name="en-us_topic_0049139666_p20566791"></a><a name="en-us_topic_0049139666_p20566791"></a><strong id="b84235270610580"><a name="b84235270610580"></a><a name="b84235270610580"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="8.25%" id="mcps1.1.5.1.3"><p id="en-us_topic_0049139666_p55297360"><a name="en-us_topic_0049139666_p55297360"></a><a name="en-us_topic_0049139666_p55297360"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.63%" id="mcps1.1.5.1.4"><p id="en-us_topic_0049139666_p49901174"><a name="en-us_topic_0049139666_p49901174"></a><a name="en-us_topic_0049139666_p49901174"></a><strong id="b842352706192251_1"><a name="b842352706192251_1"></a><a name="b842352706192251_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0049139666_row15463264"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0049139666_p44564854"><a name="en-us_topic_0049139666_p44564854"></a><a name="en-us_topic_0049139666_p44564854"></a>healthmonitor</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0049139666_p52983458"><a name="en-us_topic_0049139666_p52983458"></a><a name="en-us_topic_0049139666_p52983458"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0049139666_p63801673"><a name="en-us_topic_0049139666_p63801673"></a><a name="en-us_topic_0049139666_p63801673"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0049139666_p553045"><a name="en-us_topic_0049139666_p553045"></a><a name="en-us_topic_0049139666_p553045"></a>Specifies the health check. For details, see <a href="overview-18.html#en-us_topic_0049139662_table43819641125220">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request 

    ```
    PUT /v2.0/lbaas/healthmonitors/b7633ade-24dc-4d72-8475-06aa22be5412
    {
      "healthmonitor": {
        "delay": "15",
        "name": "health-xx",
        "timeout": "12"
      }
    ```


## Response<a name="en-us_topic_0049139666_section9622376"></a>

-   Parameter description

    <a name="en-us_topic_0049139666_table44796718"></a><table><thead align="left"><tr id="en-us_topic_0049139666_row27530415"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.1.5.1.1"><p id="en-us_topic_0049139666_p15371167"><a name="en-us_topic_0049139666_p15371167"></a><a name="en-us_topic_0049139666_p15371167"></a><strong id="b842352706181819_1"><a name="b842352706181819_1"></a><a name="b842352706181819_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.53%" id="mcps1.1.5.1.2"><p id="en-us_topic_0049139666_p37105032"><a name="en-us_topic_0049139666_p37105032"></a><a name="en-us_topic_0049139666_p37105032"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="8.25%" id="mcps1.1.5.1.3"><p id="en-us_topic_0049139666_p52717585"><a name="en-us_topic_0049139666_p52717585"></a><a name="en-us_topic_0049139666_p52717585"></a><strong id="b8423527061798_1"><a name="b8423527061798_1"></a><a name="b8423527061798_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.63%" id="mcps1.1.5.1.4"><p id="en-us_topic_0049139666_p42265954"><a name="en-us_topic_0049139666_p42265954"></a><a name="en-us_topic_0049139666_p42265954"></a><strong id="b842352706192251_2"><a name="b842352706192251_2"></a><a name="b842352706192251_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0049139666_row990244"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0049139666_p13100926"><a name="en-us_topic_0049139666_p13100926"></a><a name="en-us_topic_0049139666_p13100926"></a>healthmonitor</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0049139666_p54542105"><a name="en-us_topic_0049139666_p54542105"></a><a name="en-us_topic_0049139666_p54542105"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="8.25%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0049139666_p55834397"><a name="en-us_topic_0049139666_p55834397"></a><a name="en-us_topic_0049139666_p55834397"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0049139666_p26292272"><a name="en-us_topic_0049139666_p26292272"></a><a name="en-us_topic_0049139666_p26292272"></a>Specifies the health check. For details, see <a href="overview-18.html#en-us_topic_0049139662_table43819641125220">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "healthmonitor": {
        "name": "health-xx",
        "admin_state_up": true,
        "tenant_id": "145483a5107745e9b3d80f956713e6a3",
        "domain_name": null,
        "delay": 15,
        "expected_codes": "200",
        "max_retries": 10,
        "http_method": "GET",
        "timeout": 12,
        "pools": [
          {
            "id": "bb44bffb-05d9-412c-9d9c-b189d9e14193"
          }
        ],
        "url_path": "/",
        "type": "HTTPS",
        "id": "2dca3867-98c5-4cde-8f2c-b89ae6bd7e36",
        "monitor_port": 112
      }
    }
    ```


## Error Codes<a name="en-us_topic_0049139655_section64643717"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).

