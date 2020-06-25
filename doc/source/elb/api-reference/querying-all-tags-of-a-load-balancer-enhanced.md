# Querying All Tags of a Load Balancer<a name="EN-US_TOPIC_0109852826"></a>

## Function<a name="en-us_topic_0094115924_section51245189114349"></a>

This API is used to query all the tags of one load balancer.

## URI<a name="en-us_topic_0094115924_section45214603114349"></a>

GET /v2.0/\{project\_id\}/loadbalancers/\{loadbalancer\_id\}/tags

**Table  1**  Parameter description

<a name="table33323423"></a>
<table><thead align="left"><tr id="row8420641"><th class="cellrowborder" valign="top" width="28.33%" id="mcps1.2.5.1.1"><p id="p10983320"><a name="p10983320"></a><a name="p10983320"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.06%" id="mcps1.2.5.1.2"><p id="p1398916541313"><a name="p1398916541313"></a><a name="p1398916541313"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.38%" id="mcps1.2.5.1.3"><p id="p4164548117122"><a name="p4164548117122"></a><a name="p4164548117122"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.23%" id="mcps1.2.5.1.4"><p id="p53754023"><a name="p53754023"></a><a name="p53754023"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53906008171138"><td class="cellrowborder" valign="top" width="28.33%" headers="mcps1.2.5.1.1 "><p id="p16126074171144"><a name="p16126074171144"></a><a name="p16126074171144"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.06%" headers="mcps1.2.5.1.2 "><p id="p399015418318"><a name="p399015418318"></a><a name="p399015418318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.38%" headers="mcps1.2.5.1.3 "><p id="p39605860171144"><a name="p39605860171144"></a><a name="p39605860171144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the tag is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row33431272113959"><td class="cellrowborder" valign="top" width="28.33%" headers="mcps1.2.5.1.1 "><p id="p19792599161649"><a name="p19792599161649"></a><a name="p19792599161649"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.06%" headers="mcps1.2.5.1.2 "><p id="p2099385413310"><a name="p2099385413310"></a><a name="p2099385413310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.38%" headers="mcps1.2.5.1.3 "><p id="p18728145714517"><a name="p18728145714517"></a><a name="p18728145714517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.23%" headers="mcps1.2.5.1.4 "><p id="p8340728114018"><a name="p8340728114018"></a><a name="p8340728114018"></a>Specifies the ID of the load balancer whose tags are to be queried.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0094115924_section56720455114349"></a>

None

## Response<a name="en-us_topic_0094115924_section10152064114349"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0094115924_table60666685114349"></a>
<table><thead align="left"><tr id="en-us_topic_0094115924_row54998647114349"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094115924_p25705400114349"><a name="en-us_topic_0094115924_p25705400114349"></a><a name="en-us_topic_0094115924_p25705400114349"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094115924_p1762687114349"><a name="en-us_topic_0094115924_p1762687114349"></a><a name="en-us_topic_0094115924_p1762687114349"></a><strong id="en-us_topic_0094115924_b842352706151111"><a name="en-us_topic_0094115924_b842352706151111"></a><a name="en-us_topic_0094115924_b842352706151111"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.2.4.1.3"><p id="en-us_topic_0094115924_p8559921114349"><a name="en-us_topic_0094115924_p8559921114349"></a><a name="en-us_topic_0094115924_p8559921114349"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094115924_row22265016114349"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094115924_p58635900114349"><a name="en-us_topic_0094115924_p58635900114349"></a><a name="en-us_topic_0094115924_p58635900114349"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094115924_p51887460114349"><a name="en-us_topic_0094115924_p51887460114349"></a><a name="en-us_topic_0094115924_p51887460114349"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0094115924_p42134745114349"><a name="en-us_topic_0094115924_p42134745114349"></a><a name="en-us_topic_0094115924_p42134745114349"></a>Lists the tags. For details, see <a href="#en-us_topic_0094115924_table57471170114349">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tags**  parameter description

<a name="en-us_topic_0094115924_table57471170114349"></a>
<table><thead align="left"><tr id="en-us_topic_0094115924_row17231304114349"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="en-us_topic_0094115924_p53558420114349"><a name="en-us_topic_0094115924_p53558420114349"></a><a name="en-us_topic_0094115924_p53558420114349"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="en-us_topic_0094115924_p43264731114349"><a name="en-us_topic_0094115924_p43264731114349"></a><a name="en-us_topic_0094115924_p43264731114349"></a><strong id="b73903711"><a name="b73903711"></a><a name="b73903711"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.2.4.1.3"><p id="p12011816262"><a name="p12011816262"></a><a name="p12011816262"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0094115924_row56519168114349"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094115924_p14649901114349"><a name="en-us_topic_0094115924_p14649901114349"></a><a name="en-us_topic_0094115924_p14649901114349"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094115924_p45791351114349"><a name="en-us_topic_0094115924_p45791351114349"></a><a name="en-us_topic_0094115924_p45791351114349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p103541615151011"><a name="p103541615151011"></a><a name="p103541615151011"></a>Specifies the tag key.</p>
<a name="ul5708182422218"></a><a name="ul5708182422218"></a><ul id="ul5708182422218"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul18708824152211"></a><a name="ul18708824152211"></a><ul id="ul18708824152211"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li><li>The tag key of a load balancer must be unique.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0094115924_row28789745114349"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0094115924_p50268033114349"><a name="en-us_topic_0094115924_p50268033114349"></a><a name="en-us_topic_0094115924_p50268033114349"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0094115924_p45178890114349"><a name="en-us_topic_0094115924_p45178890114349"></a><a name="en-us_topic_0094115924_p45178890114349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="p20669181812100"><a name="p20669181812100"></a><a name="p20669181812100"></a>Specifies the tag value.</p>
<a name="ul17709124142210"></a><a name="ul17709124142210"></a><ul id="ul17709124142210"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul670952492214"></a><a name="ul670952492214"></a><ul id="ul670952492214"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="section195412017122411"></a>

-   Example request

    ```
    GET https://{Endpoint}/v2.0/6a0de1c3-7d74-4f4a-b75e-e57135bd2b97/loadbalancers/7add33ad-11dc-4ab9-a50f-419703f13163/tags
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


## Status Code<a name="en-us_topic_0094115924_section1030264817164"></a>

For details, see  [Status Codes](status-codes-enhanced.md).

