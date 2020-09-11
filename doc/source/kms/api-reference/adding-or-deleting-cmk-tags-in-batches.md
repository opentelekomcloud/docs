# Adding or Deleting CMK Tags in Batches<a name="kms_02_0045"></a>

## Function<a name="en-us_topic_0112992301_section19958056162916"></a>

This API enables you to add or delete CMK tags in batches.

## URI<a name="en-us_topic_0112992301_section38441247183015"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/\{key\_id\}/tags/action

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992301_table040511290318"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992301_row1340502913116"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992301_p1577110425210"><a name="en-us_topic_0112992301_p1577110425210"></a><a name="en-us_topic_0112992301_p1577110425210"></a><strong id="en-us_topic_0112992301_b842352706202545"><a name="en-us_topic_0112992301_b842352706202545"></a><a name="en-us_topic_0112992301_b842352706202545"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992301_p167751142326"><a name="en-us_topic_0112992301_p167751142326"></a><a name="en-us_topic_0112992301_p167751142326"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992301_p157711420214"><a name="en-us_topic_0112992301_p157711420214"></a><a name="en-us_topic_0112992301_p157711420214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992301_p1877644212217"><a name="en-us_topic_0112992301_p1877644212217"></a><a name="en-us_topic_0112992301_p1877644212217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992301_row1440562943115"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992301_p72101340183118"><a name="en-us_topic_0112992301_p72101340183118"></a><a name="en-us_topic_0112992301_p72101340183118"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992301_p16210164083114"><a name="en-us_topic_0112992301_p16210164083114"></a><a name="en-us_topic_0112992301_p16210164083114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992301_p0266239291"><a name="en-us_topic_0112992301_p0266239291"></a><a name="en-us_topic_0112992301_p0266239291"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992301_p32105405312"><a name="en-us_topic_0112992301_p32105405312"></a><a name="en-us_topic_0112992301_p32105405312"></a>Project ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0112992301_row1405429123118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992301_p122110409319"><a name="en-us_topic_0112992301_p122110409319"></a><a name="en-us_topic_0112992301_p122110409319"></a>key_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992301_p1021115409312"><a name="en-us_topic_0112992301_p1021115409312"></a><a name="en-us_topic_0112992301_p1021115409312"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992301_p1926983917917"><a name="en-us_topic_0112992301_p1926983917917"></a><a name="en-us_topic_0112992301_p1926983917917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992301_p16211140183113"><a name="en-us_topic_0112992301_p16211140183113"></a><a name="en-us_topic_0112992301_p16211140183113"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992301_parmvalue80435593163333"><a name="en-us_topic_0112992301_parmvalue80435593163333"></a><a name="en-us_topic_0112992301_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
    <p id="en-us_topic_0112992301_p2211114018310"><a name="en-us_topic_0112992301_p2211114018310"></a><a name="en-us_topic_0112992301_p2211114018310"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992301_section7153105111310"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992301_table3249442123412"></a>
<table><thead align="left"><tr id="en-us_topic_0112992301_row132496420340"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992301_p558017281137"><a name="en-us_topic_0112992301_p558017281137"></a><a name="en-us_topic_0112992301_p558017281137"></a><strong id="en-us_topic_0112992301_b1016481984"><a name="en-us_topic_0112992301_b1016481984"></a><a name="en-us_topic_0112992301_b1016481984"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992301_p158022817315"><a name="en-us_topic_0112992301_p158022817315"></a><a name="en-us_topic_0112992301_p158022817315"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992301_p195801328635"><a name="en-us_topic_0112992301_p195801328635"></a><a name="en-us_topic_0112992301_p195801328635"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992301_p13580928534"><a name="en-us_topic_0112992301_p13580928534"></a><a name="en-us_topic_0112992301_p13580928534"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992301_row15249942133415"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992301_p924914220342"><a name="en-us_topic_0112992301_p924914220342"></a><a name="en-us_topic_0112992301_p924914220342"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992301_p52498427345"><a name="en-us_topic_0112992301_p52498427345"></a><a name="en-us_topic_0112992301_p52498427345"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992301_p12249242203419"><a name="en-us_topic_0112992301_p12249242203419"></a><a name="en-us_topic_0112992301_p12249242203419"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992301_p5135135794311"><a name="en-us_topic_0112992301_p5135135794311"></a><a name="en-us_topic_0112992301_p5135135794311"></a>list of tags, including tag keys and tag values.<a name="en-us_topic_0112992301_ul17835144253711"></a><a name="en-us_topic_0112992301_ul17835144253711"></a><ul id="en-us_topic_0112992301_ul17835144253711"><li><strong id="en-us_topic_0112992301_b842352706165737"><a name="en-us_topic_0112992301_b842352706165737"></a><a name="en-us_topic_0112992301_b842352706165737"></a>key</strong> indicates the tag key. A CMK can have a maximum of 10 keys, and each of them is unique and cannot be empty. A key cannot have duplicate values. The value of <strong id="en-us_topic_0112992301_b842352706165433"><a name="en-us_topic_0112992301_b842352706165433"></a><a name="en-us_topic_0112992301_b842352706165433"></a>key</strong> contains a maximum of 36 characters.</li><li><strong id="en-us_topic_0112992301_b842352706165447"><a name="en-us_topic_0112992301_b842352706165447"></a><a name="en-us_topic_0112992301_b842352706165447"></a>value</strong> indicates the tag value. Each tag value can contain a maximum of 43 characters. The relationship between values is <strong id="en-us_topic_0112992301_b842352706165526"><a name="en-us_topic_0112992301_b842352706165526"></a><a name="en-us_topic_0112992301_b842352706165526"></a>AND</strong>.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992301_row152491442143420"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992301_p6249184263419"><a name="en-us_topic_0112992301_p6249184263419"></a><a name="en-us_topic_0112992301_p6249184263419"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992301_p142499423347"><a name="en-us_topic_0112992301_p142499423347"></a><a name="en-us_topic_0112992301_p142499423347"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992301_p18169242499"><a name="en-us_topic_0112992301_p18169242499"></a><a name="en-us_topic_0112992301_p18169242499"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992301_p17339133112203"><a name="en-us_topic_0112992301_p17339133112203"></a><a name="en-us_topic_0112992301_p17339133112203"></a>Operation ID.</p>
<p id="en-us_topic_0112992301_p20249042163413"><a name="en-us_topic_0112992301_p20249042163413"></a><a name="en-us_topic_0112992301_p20249042163413"></a>The value can be <strong id="en-us_topic_0112992301_b842352706101829"><a name="en-us_topic_0112992301_b842352706101829"></a><a name="en-us_topic_0112992301_b842352706101829"></a>create</strong> or <strong id="en-us_topic_0112992301_b842352706101833"><a name="en-us_topic_0112992301_b842352706101833"></a><a name="en-us_topic_0112992301_b842352706101833"></a>delete</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992301_row1249134213412"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992301_p19249204213342"><a name="en-us_topic_0112992301_p19249204213342"></a><a name="en-us_topic_0112992301_p19249204213342"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992301_p15249114243411"><a name="en-us_topic_0112992301_p15249114243411"></a><a name="en-us_topic_0112992301_p15249114243411"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992301_p1217464214918"><a name="en-us_topic_0112992301_p1217464214918"></a><a name="en-us_topic_0112992301_p1217464214918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992301_p52491442123410"><a name="en-us_topic_0112992301_p52491442123410"></a><a name="en-us_topic_0112992301_p52491442123410"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992301_p1249124213345"><a name="en-us_topic_0112992301_p1249124213345"></a><a name="en-us_topic_0112992301_p1249124213345"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992301_section0907192213412"></a>

None

## Examples<a name="en-us_topic_0112992301_section207874128353"></a>

The following example describes how to add tags, the keys and values of which are  **key1**,  **key**,  **value1**, and  **value3**  respectively.

-   Example request

    ```
    { 
        "action": "create",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key",
                "value": "value3"
            }
        ]
    }
    ```

    or

    ```
    {
        "action": "delete",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


-   Example response

    ```
    { 
    }
    ```

    or

    ```
    {    
           "error": {        
                  "error_code": "KMS.XXXX",        
                  "error_msg": "XXX"     
         } 
    }
    ```


## Status Codes<a name="en-us_topic_0112992301_section188513533011"></a>

[Table 3](#en-us_topic_0112992301_table3885195311010)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992301_table3885195311010"></a>
<table><thead align="left"><tr id="en-us_topic_0112992301_row08858533011"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992301_p18885105310016"><a name="en-us_topic_0112992301_p18885105310016"></a><a name="en-us_topic_0112992301_p18885105310016"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992301_p488513536011"><a name="en-us_topic_0112992301_p488513536011"></a><a name="en-us_topic_0112992301_p488513536011"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992301_p188852531708"><a name="en-us_topic_0112992301_p188852531708"></a><a name="en-us_topic_0112992301_p188852531708"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992301_row6885125316018"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992301_p188851853102"><a name="en-us_topic_0112992301_p188851853102"></a><a name="en-us_topic_0112992301_p188851853102"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992301_p2123920113816"><a name="en-us_topic_0112992301_p2123920113816"></a><a name="en-us_topic_0112992301_p2123920113816"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992301_p151239205384"><a name="en-us_topic_0112992301_p151239205384"></a><a name="en-us_topic_0112992301_p151239205384"></a>The request is processed successfully and no content is returned.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

