# Querying the Tags of All Load Balancers<a name="EN-US_TOPIC_0109852828"></a>

## Function<a name="en-us_topic_0101983303_section1385705610595"></a>

This API is used to query the tags of all the load balancers.

## URI<a name="en-us_topic_0101983303_section3546433910595"></a>

GET /v2.0/\{project\_id\}/loadbalancers/tags

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="29.099999999999998%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.29%" id="mcps1.2.5.1.2"><p id="p0867102443214"><a name="p0867102443214"></a><a name="p0867102443214"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.219999999999999%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="en-us_topic_0101983303_b842352706151111"><a name="en-us_topic_0101983303_b842352706151111"></a><a name="en-us_topic_0101983303_b842352706151111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45.39%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="29.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.29%" headers="mcps1.2.5.1.2 "><p id="p1986814245322"><a name="p1986814245322"></a><a name="p1986814245322"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.219999999999999%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.39%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0101983303_section5651109010595"></a>

None

## Response<a name="en-us_topic_0101983303_section5885135510595"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0101983303_table4644762610595"></a>
<table><thead align="left"><tr id="en-us_topic_0101983303_row3695888610595"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0101983303_p4087981910595"><a name="en-us_topic_0101983303_p4087981910595"></a><a name="en-us_topic_0101983303_p4087981910595"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="en-us_topic_0101983303_p4547695110595"><a name="en-us_topic_0101983303_p4547695110595"></a><a name="en-us_topic_0101983303_p4547695110595"></a><strong id="b1924779849"><a name="b1924779849"></a><a name="b1924779849"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="en-us_topic_0101983303_p5975438110595"><a name="en-us_topic_0101983303_p5975438110595"></a><a name="en-us_topic_0101983303_p5975438110595"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101983303_row826669210595"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101983303_p6562230710595"><a name="en-us_topic_0101983303_p6562230710595"></a><a name="en-us_topic_0101983303_p6562230710595"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101983303_p4459890810595"><a name="en-us_topic_0101983303_p4459890810595"></a><a name="en-us_topic_0101983303_p4459890810595"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0101983303_p5574176510595"><a name="en-us_topic_0101983303_p5574176510595"></a><a name="en-us_topic_0101983303_p5574176510595"></a>Lists the tags. For details, see <a href="#en-us_topic_0101983303_table1878907810595">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="en-us_topic_0101983303_table1878907810595"></a>
<table><thead align="left"><tr id="en-us_topic_0101983303_row1948255410595"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.4.1.1"><p id="en-us_topic_0101983303_p3458306510595"><a name="en-us_topic_0101983303_p3458306510595"></a><a name="en-us_topic_0101983303_p3458306510595"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.2"><p id="en-us_topic_0101983303_p442316410595"><a name="en-us_topic_0101983303_p442316410595"></a><a name="en-us_topic_0101983303_p442316410595"></a><strong id="b1248100044"><a name="b1248100044"></a><a name="b1248100044"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.4059405940594%" id="mcps1.2.4.1.3"><p id="en-us_topic_0101983303_p2273198410595"><a name="en-us_topic_0101983303_p2273198410595"></a><a name="en-us_topic_0101983303_p2273198410595"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101983303_row2935140910595"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101983303_p2865389410595"><a name="en-us_topic_0101983303_p2865389410595"></a><a name="en-us_topic_0101983303_p2865389410595"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101983303_p2627191810595"><a name="en-us_topic_0101983303_p2627191810595"></a><a name="en-us_topic_0101983303_p2627191810595"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.4.1.3 "><p id="p6434103110106"><a name="p6434103110106"></a><a name="p6434103110106"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a load balancer must be unique.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0101983303_row2620200610595"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0101983303_p4198771810595"><a name="en-us_topic_0101983303_p4198771810595"></a><a name="en-us_topic_0101983303_p4198771810595"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101983303_p6664395210595"><a name="en-us_topic_0101983303_p6664395210595"></a><a name="en-us_topic_0101983303_p6664395210595"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.4.1.3 "><p id="p143885344104"><a name="p143885344104"></a><a name="p143885344104"></a>Lists the tag values.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section171915710244"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/tags
    ```


-   Example response

    ```
    {
        "tags": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }, 
            {
                "key": "key2", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ]
    }
    ```


## Status Code<a name="en-us_topic_0101983303_section4272197910595"></a>

For details, see  [Status Codes](status-codes.md).

