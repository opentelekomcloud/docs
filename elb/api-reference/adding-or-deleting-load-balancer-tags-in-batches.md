# Adding or Deleting Load Balancer Tags in Batches <a name="EN-US_TOPIC_0109852827"></a>

## Function<a name="en-us_topic_0094115925_section52990618114447"></a>

This API is used to add or delete load balancer tags in batches. 

## Constraints<a name="en-us_topic_0094115925_section9767185772119"></a>

A maximum of 10 tags can be added to a load balancer.

This API is idempotent.

-   Pay attention to the following when adding tags:
    -   If there are duplicate keys in the request body, an error is reported.
    -   If there are no duplicate keys in the request body but the key in the request body exists in the database, the key in the database is overwritten.

-   Pay attention to the following during the deletion:
    -   If the tag to be deleted does not exist, the deletion is considered successful by default.
    -   The value range of the tag character set is not verified.
    -   The tag structure body cannot be missing, and the key cannot be left blank or set to an empty string.


## URI<a name="en-us_topic_0094115925_section42564372114447"></a>

POST /v2.0/\{project\_id\}/loadbalancers/\{loadbalancer\_id\}/tags/action

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="en-us_topic_0094115925_b84235270616735"><a name="en-us_topic_0094115925_b84235270616735"></a><a name="en-us_topic_0094115925_b84235270616735"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="en-us_topic_0094115925_b842352706151111"><a name="en-us_topic_0094115925_b842352706151111"></a><a name="en-us_topic_0094115925_b842352706151111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row33431272113959"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p19792599161649"><a name="p19792599161649"></a><a name="p19792599161649"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p50996812114013"><a name="p50996812114013"></a><a name="p50996812114013"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1958172617518"><a name="p1958172617518"></a><a name="p1958172617518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p8340728114018"><a name="p8340728114018"></a><a name="p8340728114018"></a>Specifies the ID of the load balancer to which tags are to be added or from which tags are to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0094115925_section11352640114447"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0094115925_table60941389114447"></a>
<table><thead align="left"><tr id="en-us_topic_0094115925_row2166302114447"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0094115925_p41252734114447"><a name="en-us_topic_0094115925_p41252734114447"></a><a name="en-us_topic_0094115925_p41252734114447"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0094115925_p53137130114447"><a name="en-us_topic_0094115925_p53137130114447"></a><a name="en-us_topic_0094115925_p53137130114447"></a><strong id="b301017731"><a name="b301017731"></a><a name="b301017731"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0094115925_p9140299114447"><a name="en-us_topic_0094115925_p9140299114447"></a><a name="en-us_topic_0094115925_p9140299114447"></a><strong id="b1956220786"><a name="b1956220786"></a><a name="b1956220786"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0094115925_p2166793114447"><a name="en-us_topic_0094115925_p2166793114447"></a><a name="en-us_topic_0094115925_p2166793114447"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094115925_row41292555114447"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115925_p56362682114447"><a name="en-us_topic_0094115925_p56362682114447"></a><a name="en-us_topic_0094115925_p56362682114447"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115925_p1974525114447"><a name="en-us_topic_0094115925_p1974525114447"></a><a name="en-us_topic_0094115925_p1974525114447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p892419588196"><a name="p892419588196"></a><a name="p892419588196"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0094115925_p2851681114447"><a name="en-us_topic_0094115925_p2851681114447"></a><a name="en-us_topic_0094115925_p2851681114447"></a>Lists the tags. For details, see <a href="#en-us_topic_0094115925_table16812991114447">Table 3</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0094115925_row25665132114447"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115925_p65609826114447"><a name="en-us_topic_0094115925_p65609826114447"></a><a name="en-us_topic_0094115925_p65609826114447"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115925_p12795696114447"><a name="en-us_topic_0094115925_p12795696114447"></a><a name="en-us_topic_0094115925_p12795696114447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0094115925_p29818495114447"><a name="en-us_topic_0094115925_p29818495114447"></a><a name="en-us_topic_0094115925_p29818495114447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p597772653220"><a name="p597772653220"></a><a name="p597772653220"></a>Specifies the operation type.</p>
<p id="p6875837143218"><a name="p6875837143218"></a><a name="p6875837143218"></a>The value can be one of the following:</p>
<a name="ul16838103943212"></a><a name="ul16838103943212"></a><ul id="ul16838103943212"><li><strong id="b842352706113353"><a name="b842352706113353"></a><a name="b842352706113353"></a>create</strong>: adds tags to the load balancer.</li><li><strong id="b842352706194852"><a name="b842352706194852"></a><a name="b842352706194852"></a>delete</strong>: deletes tags from the load balancer.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="en-us_topic_0094115925_table16812991114447"></a>
<table><thead align="left"><tr id="en-us_topic_0094115925_row870873114447"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0094115925_p3431874114447"><a name="en-us_topic_0094115925_p3431874114447"></a><a name="en-us_topic_0094115925_p3431874114447"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0094115925_p9546376114447"><a name="en-us_topic_0094115925_p9546376114447"></a><a name="en-us_topic_0094115925_p9546376114447"></a><strong id="b1978389205"><a name="b1978389205"></a><a name="b1978389205"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0094115925_p35058962114447"><a name="en-us_topic_0094115925_p35058962114447"></a><a name="en-us_topic_0094115925_p35058962114447"></a><strong id="b407269580"><a name="b407269580"></a><a name="b407269580"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0094115925_p21203656114447"><a name="en-us_topic_0094115925_p21203656114447"></a><a name="en-us_topic_0094115925_p21203656114447"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094115925_row39774612114447"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115925_p518107114447"><a name="en-us_topic_0094115925_p518107114447"></a><a name="en-us_topic_0094115925_p518107114447"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115925_p41966727114447"><a name="en-us_topic_0094115925_p41966727114447"></a><a name="en-us_topic_0094115925_p41966727114447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0094115925_p43861760114447"><a name="en-us_topic_0094115925_p43861760114447"></a><a name="en-us_topic_0094115925_p43861760114447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p1395417582912"><a name="p1395417582912"></a><a name="p1395417582912"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a load balancer must be unique.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094115925_row31404187114447"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0094115925_p60711218114447"><a name="en-us_topic_0094115925_p60711218114447"></a><a name="en-us_topic_0094115925_p60711218114447"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0094115925_p18661617114447"><a name="en-us_topic_0094115925_p18661617114447"></a><a name="en-us_topic_0094115925_p18661617114447"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0094115925_p35196033114447"><a name="en-us_topic_0094115925_p35196033114447"></a><a name="en-us_topic_0094115925_p35196033114447"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p877212691013"><a name="p877212691013"></a><a name="p877212691013"></a>Specifies the tag value.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0094115925_section22322523114447"></a>

None

## Example<a name="section67131947171311"></a>

-   Example request 1

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/7add33ad-11dc-4ab9-a50f-419703f13163/tags/action
    
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
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/7add33ad-11dc-4ab9-a50f-419703f13163/tags/action
    
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


## Status Code<a name="en-us_topic_0094115925_section1030264817164"></a>

For details, see  [Status Codes](status-codes.md).

