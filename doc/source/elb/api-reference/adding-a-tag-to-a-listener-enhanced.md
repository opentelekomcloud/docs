# Adding a Tag to a Listener<a name="EN-US_TOPIC_0112614719"></a>

## Function<a name="section1136314784715"></a>

This API is used to add a tag to a specific listener.

## URI<a name="section3363194719478"></a>

POST /v2.0/\{project\_id\}/listeners/\{listener\_id\}/tags

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p17233719"><a name="p17233719"></a><a name="p17233719"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p31143627171144"><a name="p31143627171144"></a><a name="p31143627171144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row6239103417284"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p17239163472818"><a name="p17239163472818"></a><a name="p17239163472818"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p17239173410285"><a name="p17239173410285"></a><a name="p17239173410285"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p112396344281"><a name="p112396344281"></a><a name="p112396344281"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p8239434172817"><a name="p8239434172817"></a><a name="p8239434172817"></a>Specifies the ID of the listener to which a tag is to be added.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section123701847164719"></a>

-   A maximum of 10 tags can be added to a listener.
-   Pay attention to the following when adding tags:
    -   If there are duplicate keys in the request body, an error is reported.
    -   If there are no duplicate keys in the request body but the key in the request body exists in the database, the key in the database is overwritten.


## Request<a name="section637254784719"></a>

**Table  2**  Request parameters

<a name="table1637474717470"></a>
<table><thead align="left"><tr id="row8480194774711"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="p9480747174718"><a name="p9480747174718"></a><a name="p9480747174718"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1448004754711"><a name="p1448004754711"></a><a name="p1448004754711"></a><strong id="b756269516"><a name="b756269516"></a><a name="b756269516"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p1948084784713"><a name="p1948084784713"></a><a name="p1948084784713"></a><strong id="b2111704113"><a name="b2111704113"></a><a name="b2111704113"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p948064744719"><a name="p948064744719"></a><a name="p948064744719"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row124806476479"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="p84801447114717"><a name="p84801447114717"></a><a name="p84801447114717"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p18480104774713"><a name="p18480104774713"></a><a name="p18480104774713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p0480144712473"><a name="p0480144712473"></a><a name="p0480144712473"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p6480204710477"><a name="p6480204710477"></a><a name="p6480204710477"></a>Specifies the tag. For details, see <a href="#table1537216133220">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="table1537216133220"></a>
<table><thead align="left"><tr id="row437215623217"><th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.1"><p id="p11372106133217"><a name="p11372106133217"></a><a name="p11372106133217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p17372665322"><a name="p17372665322"></a><a name="p17372665322"></a><strong id="b1860558640"><a name="b1860558640"></a><a name="b1860558640"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p537256173218"><a name="p537256173218"></a><a name="p537256173218"></a><strong id="b1377586836"><a name="b1377586836"></a><a name="b1377586836"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p1137213613211"><a name="p1137213613211"></a><a name="p1137213613211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row73726673216"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p15372767320"><a name="p15372767320"></a><a name="p15372767320"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p837212614328"><a name="p837212614328"></a><a name="p837212614328"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p7372364324"><a name="p7372364324"></a><a name="p7372364324"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p1651040121818"><a name="p1651040121818"></a><a name="p1651040121818"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a listener must be unique.</li></ul>
</td>
</tr>
<tr id="row153729614327"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p337215615329"><a name="p337215615329"></a><a name="p337215615329"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p63728615321"><a name="p63728615321"></a><a name="p63728615321"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p8372196173210"><a name="p8372196173210"></a><a name="p8372196173210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p1416194371820"><a name="p1416194371820"></a><a name="p1416194371820"></a>Specifies the tag value.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1390174718479"></a>

None

## Example<a name="section14794113272"></a>

-   Example request

    ```
    POST https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/listeners/7add33ad-11dc-4ab9-a50f-419703f13163/tags
    
    {
        "tag": {
            "key": "key1", 
            "value": "value1"
        }
    }
    ```


-   Example response

    None


## Status Code<a name="section239224711478"></a>

For details, see  [Status Codes](status-codes-enhanced.md).

