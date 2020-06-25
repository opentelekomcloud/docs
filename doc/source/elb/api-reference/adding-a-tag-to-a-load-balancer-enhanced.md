# Adding a Tag to a Load Balancer<a name="EN-US_TOPIC_0109852830"></a>

## Function<a name="en-us_topic_0101985069_section64730638115249"></a>

This API is used to add a tag to a specific load balancer. This API is used to add a tag to a specific load balancer for easier management.

## URI<a name="en-us_topic_0101985069_section53003617115310"></a>

POST /v2.0/\{project\_id\}/loadbalancers/\{loadbalancer\_id\}/tags

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="en-us_topic_0101985069_b84235270616735"><a name="en-us_topic_0101985069_b84235270616735"></a><a name="en-us_topic_0101985069_b84235270616735"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="en-us_topic_0101985069_b842352706151111"><a name="en-us_topic_0101985069_b842352706151111"></a><a name="en-us_topic_0101985069_b842352706151111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row1686321181111"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p15863201114114"><a name="p15863201114114"></a><a name="p15863201114114"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p486381113115"><a name="p486381113115"></a><a name="p486381113115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p57281241445"><a name="p57281241445"></a><a name="p57281241445"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p937914204113"><a name="p937914204113"></a><a name="p937914204113"></a>Specifies the ID of the load balancer to which a tag is to be added.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0101985069_section60866968115418"></a>

A maximum of 10 tags can be added to a load balancer.

Pay attention to the following when adding tags:

-   If there are duplicate keys in the request body, an error is reported.
-   If there are no duplicate keys in the request body but the key in the request body exists in the database, the key in the database is overwritten.

## Request<a name="en-us_topic_0101985069_section63626232115513"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0101985069_table50726759115539"></a>
<table><thead align="left"><tr id="en-us_topic_0101985069_row18976657115539"><th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.5.1.1"><p id="en-us_topic_0101985069_p5676213115548"><a name="en-us_topic_0101985069_p5676213115548"></a><a name="en-us_topic_0101985069_p5676213115548"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="en-us_topic_0101985069_p57120100115548"><a name="en-us_topic_0101985069_p57120100115548"></a><a name="en-us_topic_0101985069_p57120100115548"></a><strong id="b884167363"><a name="b884167363"></a><a name="b884167363"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="en-us_topic_0101985069_p63325412115548"><a name="en-us_topic_0101985069_p63325412115548"></a><a name="en-us_topic_0101985069_p63325412115548"></a><strong id="b1054905652"><a name="b1054905652"></a><a name="b1054905652"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.5.1.4"><p id="en-us_topic_0101985069_p29084765115548"><a name="en-us_topic_0101985069_p29084765115548"></a><a name="en-us_topic_0101985069_p29084765115548"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101985069_row54496294115539"><td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985069_p34643543115548"><a name="en-us_topic_0101985069_p34643543115548"></a><a name="en-us_topic_0101985069_p34643543115548"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985069_p54663593115548"><a name="en-us_topic_0101985069_p54663593115548"></a><a name="en-us_topic_0101985069_p54663593115548"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985069_p65674899115548"><a name="en-us_topic_0101985069_p65674899115548"></a><a name="en-us_topic_0101985069_p65674899115548"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0101985069_p18066622115548"><a name="en-us_topic_0101985069_p18066622115548"></a><a name="en-us_topic_0101985069_p18066622115548"></a>Specifies the tag. For details, see <a href="#en-us_topic_0101985069_table3507237511564">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="en-us_topic_0101985069_table3507237511564"></a>
<table><thead align="left"><tr id="en-us_topic_0101985069_row3238611511564"><th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.1"><p id="en-us_topic_0101985069_p52006935115616"><a name="en-us_topic_0101985069_p52006935115616"></a><a name="en-us_topic_0101985069_p52006935115616"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="en-us_topic_0101985069_p51812215115616"><a name="en-us_topic_0101985069_p51812215115616"></a><a name="en-us_topic_0101985069_p51812215115616"></a><strong id="b1170997432"><a name="b1170997432"></a><a name="b1170997432"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0101985069_p36039867115616"><a name="en-us_topic_0101985069_p36039867115616"></a><a name="en-us_topic_0101985069_p36039867115616"></a><strong id="b224228931"><a name="b224228931"></a><a name="b224228931"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="en-us_topic_0101985069_p33548108115616"><a name="en-us_topic_0101985069_p33548108115616"></a><a name="en-us_topic_0101985069_p33548108115616"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0101985069_row2415422611564"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985069_p59171954115616"><a name="en-us_topic_0101985069_p59171954115616"></a><a name="en-us_topic_0101985069_p59171954115616"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985069_p28199001115616"><a name="en-us_topic_0101985069_p28199001115616"></a><a name="en-us_topic_0101985069_p28199001115616"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985069_p2417707115616"><a name="en-us_topic_0101985069_p2417707115616"></a><a name="en-us_topic_0101985069_p2417707115616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p25114429911"><a name="p25114429911"></a><a name="p25114429911"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a load balancer must be unique.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0101985069_row214066011564"><td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0101985069_p22667626115616"><a name="en-us_topic_0101985069_p22667626115616"></a><a name="en-us_topic_0101985069_p22667626115616"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0101985069_p24138419115616"><a name="en-us_topic_0101985069_p24138419115616"></a><a name="en-us_topic_0101985069_p24138419115616"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0101985069_p9054957115616"><a name="en-us_topic_0101985069_p9054957115616"></a><a name="en-us_topic_0101985069_p9054957115616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p2051574616914"><a name="p2051574616914"></a><a name="p2051574616914"></a>Specifies the tag value.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0101985069_section15955578115757"></a>

None

## Example<a name="section1119216512139"></a>

-   Example request

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/7add33ad-11dc-4ab9-a50f-419703f13163/tags
    
    {
        "tag": {
            "key": "key1", 
            "value": "value1"
        }
    }
    ```


-   Example response

    None


## Status Code<a name="en-us_topic_0101985069_section503512012042"></a>

For details, see  [Status Codes](status-codes-enhanced.md).

