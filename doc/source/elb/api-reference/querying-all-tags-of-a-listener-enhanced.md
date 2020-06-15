# Querying All Tags of a Listener<a name="EN-US_TOPIC_0112614717"></a>

## Function<a name="section10810152375120"></a>

This API is used to query all tags of one listener.

## API Format<a name="section138111323135114"></a>

GET /v2.0/\{project\_id\}/listeners/\{listener\_id\}/tags

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.415841584158414%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.415841584158414%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row1686321181111"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p15863201114114"><a name="p15863201114114"></a><a name="p15863201114114"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p486381113115"><a name="p486381113115"></a><a name="p486381113115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p17572199121311"><a name="p17572199121311"></a><a name="p17572199121311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.415841584158414%" headers="mcps1.2.5.1.4 "><p id="p1220014383149"><a name="p1220014383149"></a><a name="p1220014383149"></a>Specifies the ID of the listener whose tags are to be queried.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section6818192319515"></a>

None

## Request<a name="section11819223115112"></a>

None

## Response<a name="section181919235518"></a>

**Table  2**  Response parameters

<a name="table3825192305110"></a>
<table><thead align="left"><tr id="row169191237516"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p49201323165110"><a name="p49201323165110"></a><a name="p49201323165110"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p12920172315511"><a name="p12920172315511"></a><a name="p12920172315511"></a><strong id="b65800984"><a name="b65800984"></a><a name="b65800984"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p179201123145115"><a name="p179201123145115"></a><a name="p179201123145115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13920162385113"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p4920142316512"><a name="p4920142316512"></a><a name="p4920142316512"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0101983303_p4459890810595"><a name="en-us_topic_0101983303_p4459890810595"></a><a name="en-us_topic_0101983303_p4459890810595"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p6920122313513"><a name="p6920122313513"></a><a name="p6920122313513"></a>Lists the tags. For details, see <a href="#table9829182310517">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="table9829182310517"></a>
<table><thead align="left"><tr id="row1792014233515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p109201923175119"><a name="p109201923175119"></a><a name="p109201923175119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p49201423115115"><a name="p49201423115115"></a><a name="p49201423115115"></a><strong id="b2107812107"><a name="b2107812107"></a><a name="b2107812107"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p1692018233514"><a name="p1692018233514"></a><a name="p1692018233514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19201523175116"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p189201923185113"><a name="p189201923185113"></a><a name="p189201923185113"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p6920112314513"><a name="p6920112314513"></a><a name="p6920112314513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p62916971916"><a name="p62916971916"></a><a name="p62916971916"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a listener must be unique.</li></ul>
</td>
</tr>
<tr id="row1920182314511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p69206234515"><a name="p69206234515"></a><a name="p69206234515"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p9920162319514"><a name="p9920162319514"></a><a name="p9920162319514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p12104112111915"><a name="p12104112111915"></a><a name="p12104112111915"></a>Specifies the tag value.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1774210310292"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/7add33ad-11dc-4ab9-a50f-419703f13163/tags
    ```


-   Example response

    ```
    {
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


## Status Code<a name="section0843122311511"></a>

For details, see  [Status Codes](status-codes-enhanced.md).

