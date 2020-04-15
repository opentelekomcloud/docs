# Adding or Deleting Listener Tags in Batches<a name="EN-US_TOPIC_0109852833"></a>

## Function<a name="en-us_topic_0094115927_section39566685114623"></a>

This API is used to add or delete listener tags in batches.

## Constraints<a name="section825626125015"></a>

-   A maximum of 10 tags can be added to a listener.
-   This API is idempotent.
-   Pay attention to the following when adding tags:
    -   If there are duplicate keys in the request body, an error is reported.
    -   If there are no duplicate keys in the request body but the key in the request body exists in the database, the key in the database is overwritten.

-   Pay attention to the following during the deletion:
    -   If the tag to be deleted does not exist, the deletion is considered successful by default.
    -   The value range of the tag character set is not verified.
    -   The tag structure body cannot be missing, and the key cannot be left blank or set to an empty string.


## URI<a name="en-us_topic_0094115927_section54411029114623"></a>

POST /v2.0/\{project\_id\}/listeners/\{listener\_id\}/tags/action

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="en-us_topic_0094115927_b84235270616735"><a name="en-us_topic_0094115927_b84235270616735"></a><a name="en-us_topic_0094115927_b84235270616735"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="en-us_topic_0094115927_b842352706151111"><a name="en-us_topic_0094115927_b842352706151111"></a><a name="en-us_topic_0094115927_b842352706151111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row1686321181111"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p15863201114114"><a name="p15863201114114"></a><a name="p15863201114114"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p486381113115"><a name="p486381113115"></a><a name="p486381113115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p77219019124"><a name="p77219019124"></a><a name="p77219019124"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.5.1.4 "><p id="p1220014383149"><a name="p1220014383149"></a><a name="p1220014383149"></a>Specifies the ID of the listener to which tags are to be added or from which tags are to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0094115927_section9515851114623"></a>

**Table  2**  Parameter description

<a name="en-us_topic_0094115927_table22255723114623"></a>
<table><thead align="left"><tr id="en-us_topic_0094115927_row22053842114623"><th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.1"><p id="en-us_topic_0094115927_p41530752114623"><a name="en-us_topic_0094115927_p41530752114623"></a><a name="en-us_topic_0094115927_p41530752114623"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.2"><p id="en-us_topic_0094115927_p8547718114623"><a name="en-us_topic_0094115927_p8547718114623"></a><a name="en-us_topic_0094115927_p8547718114623"></a><strong id="b1145222958"><a name="b1145222958"></a><a name="b1145222958"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.3"><p id="en-us_topic_0094115927_p21276557114623"><a name="en-us_topic_0094115927_p21276557114623"></a><a name="en-us_topic_0094115927_p21276557114623"></a><strong id="b1548442891"><a name="b1548442891"></a><a name="b1548442891"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63.366336633663366%" id="mcps1.2.5.1.4"><p id="en-us_topic_0094115927_p45679548114623"><a name="en-us_topic_0094115927_p45679548114623"></a><a name="en-us_topic_0094115927_p45679548114623"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094115927_row9055932114623"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115927_p62441909114623"><a name="en-us_topic_0094115927_p62441909114623"></a><a name="en-us_topic_0094115927_p62441909114623"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115927_p24629838114623"><a name="en-us_topic_0094115927_p24629838114623"></a><a name="en-us_topic_0094115927_p24629838114623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0094115927_p48859823114623"><a name="en-us_topic_0094115927_p48859823114623"></a><a name="en-us_topic_0094115927_p48859823114623"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0094115927_p65331585114623"><a name="en-us_topic_0094115927_p65331585114623"></a><a name="en-us_topic_0094115927_p65331585114623"></a>Lists the tags. For details, see <a href="#en-us_topic_0094115927_table27826557114623">Table 3</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0094115927_row51113355114623"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115927_p46541129114623"><a name="en-us_topic_0094115927_p46541129114623"></a><a name="en-us_topic_0094115927_p46541129114623"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115927_p11735115114623"><a name="en-us_topic_0094115927_p11735115114623"></a><a name="en-us_topic_0094115927_p11735115114623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0094115927_p11020282114623"><a name="en-us_topic_0094115927_p11020282114623"></a><a name="en-us_topic_0094115927_p11020282114623"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.5.1.4 "><p id="p15275172865210"><a name="p15275172865210"></a><a name="p15275172865210"></a>Specifies the operation identifier.</p>
<p id="p0368439185218"><a name="p0368439185218"></a><a name="p0368439185218"></a>The value can be one of the following:</p>
<a name="ul268144110523"></a><a name="ul268144110523"></a><ul id="ul268144110523"><li><strong id="b116221454154313"><a name="b116221454154313"></a><a name="b116221454154313"></a>create</strong>: adds tags to the load balancer.</li><li><strong id="b842352706114722"><a name="b842352706114722"></a><a name="b842352706114722"></a>delete</strong>: deletes tags from the load balancer.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **resource\_tag**  parameter description

<a name="en-us_topic_0094115927_table27826557114623"></a>
<table><thead align="left"><tr id="en-us_topic_0094115927_row40402544114623"><th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.1"><p id="en-us_topic_0094115927_p51380671114623"><a name="en-us_topic_0094115927_p51380671114623"></a><a name="en-us_topic_0094115927_p51380671114623"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.2"><p id="en-us_topic_0094115927_p1084855114623"><a name="en-us_topic_0094115927_p1084855114623"></a><a name="en-us_topic_0094115927_p1084855114623"></a><strong id="b1887706628"><a name="b1887706628"></a><a name="b1887706628"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.3"><p id="en-us_topic_0094115927_p20764415114623"><a name="en-us_topic_0094115927_p20764415114623"></a><a name="en-us_topic_0094115927_p20764415114623"></a><strong id="b1849340027"><a name="b1849340027"></a><a name="b1849340027"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63.366336633663366%" id="mcps1.2.5.1.4"><p id="en-us_topic_0094115927_p4196031114623"><a name="en-us_topic_0094115927_p4196031114623"></a><a name="en-us_topic_0094115927_p4196031114623"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094115927_row4334240114623"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115927_p15529161114623"><a name="en-us_topic_0094115927_p15529161114623"></a><a name="en-us_topic_0094115927_p15529161114623"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115927_p49902563114623"><a name="en-us_topic_0094115927_p49902563114623"></a><a name="en-us_topic_0094115927_p49902563114623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0094115927_p15575830114623"><a name="en-us_topic_0094115927_p15575830114623"></a><a name="en-us_topic_0094115927_p15575830114623"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.5.1.4 "><p id="p15785205219187"><a name="p15785205219187"></a><a name="p15785205219187"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a listener must be unique.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094115927_row13382226114623"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115927_p10218504114623"><a name="en-us_topic_0094115927_p10218504114623"></a><a name="en-us_topic_0094115927_p10218504114623"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115927_p22392532114623"><a name="en-us_topic_0094115927_p22392532114623"></a><a name="en-us_topic_0094115927_p22392532114623"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0094115927_p1855771114623"><a name="en-us_topic_0094115927_p1855771114623"></a><a name="en-us_topic_0094115927_p1855771114623"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.5.1.4 "><p id="p1052616114195"><a name="p1052616114195"></a><a name="p1052616114195"></a>Specifies the tag value.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0094115927_section10680327114623"></a>

None

## Example<a name="section15444194552712"></a>

-   Example request 1

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/7add33ad-11dc-4ab9-a50f-419703f13163/tags/action
    
    {
        "action": "create", 
        "tags": [
            {
                "key": "key1", 
                "value": "value1"
            }, 
            {
                "key": "key2", 
                "value": "value2"
            }
        ]
    }
    ```


-   Example response 1

    None

-   Example request 2

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/7add33ad-11dc-4ab9-a50f-419703f13163/tags/action
    
    {
        "action": "delete", 
        "tags": [
            {
                "key": "key1", 
                "value": "value1"
            }, 
            {
                "key": "key2", 
                "value": "value2"
            }
        ]
    }
    ```

-   Example response 2

    None


## Status Code<a name="en-us_topic_0094115927_section1030264817164"></a>

For details, see  [Status Codes](status-codes.md).

