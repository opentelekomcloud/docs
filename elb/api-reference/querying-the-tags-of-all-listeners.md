# Querying the Tags of All Listeners<a name="EN-US_TOPIC_0112614718"></a>

## Function<a name="section4125165416533"></a>

This API is used to query the tags of all listeners.

## URI<a name="section11126135485310"></a>

GET /v2.0/\{project\_id\}/listeners/tags

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section7136125419536"></a>

None

## Request<a name="section1213745445317"></a>

None

## Response<a name="section121381454165317"></a>

**Table  2**  Response parameters

<a name="table5145175465317"></a>
<table><thead align="left"><tr id="row730511549531"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p030515417533"><a name="p030515417533"></a><a name="p030515417533"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p13059547535"><a name="p13059547535"></a><a name="p13059547535"></a><strong id="b48639653"><a name="b48639653"></a><a name="b48639653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="p163051554115318"><a name="p163051554115318"></a><a name="p163051554115318"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63051545535"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p153051454155319"><a name="p153051454155319"></a><a name="p153051454155319"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p2030519544531"><a name="p2030519544531"></a><a name="p2030519544531"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p830565495316"><a name="p830565495316"></a><a name="p830565495316"></a>Lists the tags, which are aggregated by the tag key. For details, see <a href="#table13591257182417">Table 3</a>.</p>
<p id="p16525344121615"><a name="p16525344121615"></a><a name="p16525344121615"></a>For example, if you have two listeners, the tag key of both listeners is "test", the tag value of listener A is "value1", and the tag value of listener B is "value2." Two tags are queried. The key of both tags is "test", and the tag values are ["value1","value2"].</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="table13591257182417"></a>
<table><thead align="left"><tr id="row935985722417"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p63593579244"><a name="p63593579244"></a><a name="p63593579244"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p8359195752416"><a name="p8359195752416"></a><a name="p8359195752416"></a><strong id="b2068383661"><a name="b2068383661"></a><a name="b2068383661"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p935925742420"><a name="p935925742420"></a><a name="p935925742420"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53591357152410"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p14359557192417"><a name="p14359557192417"></a><a name="p14359557192417"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p16359757162414"><a name="p16359757162414"></a><a name="p16359757162414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p78621423151913"><a name="p78621423151913"></a><a name="p78621423151913"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a listener must be unique.</li></ul>
</td>
</tr>
<tr id="row1835925712243"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1635995717247"><a name="p1635995717247"></a><a name="p1635995717247"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101983303_p4459890810595"><a name="en-us_topic_0101983303_p4459890810595"></a><a name="en-us_topic_0101983303_p4459890810595"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p5513221171914"><a name="p5513221171914"></a><a name="p5513221171914"></a>Lists the tag values.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1020207183011"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/tags
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


## Status Code<a name="en-us_topic_0094115927_section1030264817164"></a>

For details, see  [Status Codes](status-codes.md).

