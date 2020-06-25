# Adding a CMK Tag<a name="kms_02_0046"></a>

## Function<a name="en-us_topic_0112992283_section912191015404"></a>

This API allows you to add a CMK tag.

## URI<a name="en-us_topic_0112992283_section19957618204018"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/\{key\_id\}/tags

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992283_table17974014153316"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992283_row3976714153316"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992283_p1577110425210"><a name="en-us_topic_0112992283_p1577110425210"></a><a name="en-us_topic_0112992283_p1577110425210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992283_p167751142326"><a name="en-us_topic_0112992283_p167751142326"></a><a name="en-us_topic_0112992283_p167751142326"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992283_p157711420214"><a name="en-us_topic_0112992283_p157711420214"></a><a name="en-us_topic_0112992283_p157711420214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992283_p1877644212217"><a name="en-us_topic_0112992283_p1877644212217"></a><a name="en-us_topic_0112992283_p1877644212217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992283_row29761214103314"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992283_p338945184111"><a name="en-us_topic_0112992283_p338945184111"></a><a name="en-us_topic_0112992283_p338945184111"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992283_p917437134211"><a name="en-us_topic_0112992283_p917437134211"></a><a name="en-us_topic_0112992283_p917437134211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992283_p98782051592"><a name="en-us_topic_0112992283_p98782051592"></a><a name="en-us_topic_0112992283_p98782051592"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992283_p103893514112"><a name="en-us_topic_0112992283_p103893514112"></a><a name="en-us_topic_0112992283_p103893514112"></a>Project ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0112992283_row997631410332"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992283_p33891452417"><a name="en-us_topic_0112992283_p33891452417"></a><a name="en-us_topic_0112992283_p33891452417"></a>key_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992283_p20443118194218"><a name="en-us_topic_0112992283_p20443118194218"></a><a name="en-us_topic_0112992283_p20443118194218"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992283_p1890415514913"><a name="en-us_topic_0112992283_p1890415514913"></a><a name="en-us_topic_0112992283_p1890415514913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992283_p1838925194110"><a name="en-us_topic_0112992283_p1838925194110"></a><a name="en-us_topic_0112992283_p1838925194110"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992283_parmvalue80435593163333"><a name="en-us_topic_0112992283_parmvalue80435593163333"></a><a name="en-us_topic_0112992283_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
    <p id="en-us_topic_0112992283_p1138935114119"><a name="en-us_topic_0112992283_p1138935114119"></a><a name="en-us_topic_0112992283_p1138935114119"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992283_section141071427144114"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992283_table11568102202317"></a>
<table><thead align="left"><tr id="en-us_topic_0112992283_row6568162292317"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992283_p22411085515"><a name="en-us_topic_0112992283_p22411085515"></a><a name="en-us_topic_0112992283_p22411085515"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992283_p824111815512"><a name="en-us_topic_0112992283_p824111815512"></a><a name="en-us_topic_0112992283_p824111815512"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992283_p1024114817516"><a name="en-us_topic_0112992283_p1024114817516"></a><a name="en-us_topic_0112992283_p1024114817516"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992283_p132419818518"><a name="en-us_topic_0112992283_p132419818518"></a><a name="en-us_topic_0112992283_p132419818518"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992283_row45681622122314"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992283_p1056892252318"><a name="en-us_topic_0112992283_p1056892252318"></a><a name="en-us_topic_0112992283_p1056892252318"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992283_p192971138172319"><a name="en-us_topic_0112992283_p192971138172319"></a><a name="en-us_topic_0112992283_p192971138172319"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992283_p556842222317"><a name="en-us_topic_0112992283_p556842222317"></a><a name="en-us_topic_0112992283_p556842222317"></a>Array of object</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992283_p156862211236"><a name="en-us_topic_0112992283_p156862211236"></a><a name="en-us_topic_0112992283_p156862211236"></a>Tag. For details, see <a href="#en-us_topic_0112992283_table1756962210239">Table 3</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992283_row656473162623"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992283_p2243639162757"><a name="en-us_topic_0112992283_p2243639162757"></a><a name="en-us_topic_0112992283_p2243639162757"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992283_p23679401162757"><a name="en-us_topic_0112992283_p23679401162757"></a><a name="en-us_topic_0112992283_p23679401162757"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992283_p4386100291125"><a name="en-us_topic_0112992283_p4386100291125"></a><a name="en-us_topic_0112992283_p4386100291125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992283_p38983337162757"><a name="en-us_topic_0112992283_p38983337162757"></a><a name="en-us_topic_0112992283_p38983337162757"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992283_p15305715162757"><a name="en-us_topic_0112992283_p15305715162757"></a><a name="en-us_topic_0112992283_p15305715162757"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  field description

<a name="en-us_topic_0112992283_table1756962210239"></a>
<table><thead align="left"><tr id="en-us_topic_0112992283_row16568132272312"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992283_p14301412358"><a name="en-us_topic_0112992283_p14301412358"></a><a name="en-us_topic_0112992283_p14301412358"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992283_p1143081214518"><a name="en-us_topic_0112992283_p1143081214518"></a><a name="en-us_topic_0112992283_p1143081214518"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992283_p2430912359"><a name="en-us_topic_0112992283_p2430912359"></a><a name="en-us_topic_0112992283_p2430912359"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992283_p1743015125511"><a name="en-us_topic_0112992283_p1743015125511"></a><a name="en-us_topic_0112992283_p1743015125511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992283_row135691122122311"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992283_p1256819224230"><a name="en-us_topic_0112992283_p1256819224230"></a><a name="en-us_topic_0112992283_p1256819224230"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992283_p2568322122312"><a name="en-us_topic_0112992283_p2568322122312"></a><a name="en-us_topic_0112992283_p2568322122312"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992283_p2025431171020"><a name="en-us_topic_0112992283_p2025431171020"></a><a name="en-us_topic_0112992283_p2025431171020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992283_p3415153758"><a name="en-us_topic_0112992283_p3415153758"></a><a name="en-us_topic_0112992283_p3415153758"></a>Key.</p>
<p id="en-us_topic_0112992283_p15568922122310"><a name="en-us_topic_0112992283_p15568922122310"></a><a name="en-us_topic_0112992283_p15568922122310"></a>The value contains a maximum of 36 Unicode characters. The value of <strong id="en-us_topic_0112992283_b842352706204238"><a name="en-us_topic_0112992283_b842352706204238"></a><a name="en-us_topic_0112992283_b842352706204238"></a>key</strong> cannot be empty, and cannot contain the following characters: ASCII (0-31) and <strong id="en-us_topic_0112992283_b842352706152859_1"><a name="en-us_topic_0112992283_b842352706152859_1"></a><a name="en-us_topic_0112992283_b842352706152859_1"></a>*&lt;&gt;\=</strong></p>
</td>
</tr>
<tr id="en-us_topic_0112992283_row0569112232318"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992283_p15569522202313"><a name="en-us_topic_0112992283_p15569522202313"></a><a name="en-us_topic_0112992283_p15569522202313"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992283_p13569122214230"><a name="en-us_topic_0112992283_p13569122214230"></a><a name="en-us_topic_0112992283_p13569122214230"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992283_p142571713108"><a name="en-us_topic_0112992283_p142571713108"></a><a name="en-us_topic_0112992283_p142571713108"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992283_p113482615510"><a name="en-us_topic_0112992283_p113482615510"></a><a name="en-us_topic_0112992283_p113482615510"></a>Value.</p>
<p id="en-us_topic_0112992283_p1056942262319"><a name="en-us_topic_0112992283_p1056942262319"></a><a name="en-us_topic_0112992283_p1056942262319"></a>Each value contains a maximum of 43 Unicode characters and can be an empty string. The value cannot contain the following characters: ASCII (0-31) and <strong id="en-us_topic_0112992283_b842352706152859_3"><a name="en-us_topic_0112992283_b842352706152859_3"></a><a name="en-us_topic_0112992283_b842352706152859_3"></a>*&lt;&gt;\=</strong></p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992283_section85549592421"></a>

None

## Examples<a name="en-us_topic_0112992283_section166631211114317"></a>

The following example describes how to add a tag, the key and value of which are  **DEV**  and  **DEV1**  respectively.

-   Example request

    ```
    {   
      "tag":
         {  
            "key":"DEV",
            "value":"DEV1"
         }
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


## Status Codes<a name="en-us_topic_0112992283_section192111133389"></a>

[Table 4](#en-us_topic_0112992283_en-us_topic_0112992301_table3885195311010)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992283_en-us_topic_0112992301_table3885195311010"></a>
<table><thead align="left"><tr id="en-us_topic_0112992283_en-us_topic_0112992301_row08858533011"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992283_en-us_topic_0112992301_p18885105310016"><a name="en-us_topic_0112992283_en-us_topic_0112992301_p18885105310016"></a><a name="en-us_topic_0112992283_en-us_topic_0112992301_p18885105310016"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992283_en-us_topic_0112992301_p488513536011"><a name="en-us_topic_0112992283_en-us_topic_0112992301_p488513536011"></a><a name="en-us_topic_0112992283_en-us_topic_0112992301_p488513536011"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992283_en-us_topic_0112992301_p188852531708"><a name="en-us_topic_0112992283_en-us_topic_0112992301_p188852531708"></a><a name="en-us_topic_0112992283_en-us_topic_0112992301_p188852531708"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992283_en-us_topic_0112992301_row6885125316018"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992283_en-us_topic_0112992301_p188851853102"><a name="en-us_topic_0112992283_en-us_topic_0112992301_p188851853102"></a><a name="en-us_topic_0112992283_en-us_topic_0112992301_p188851853102"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992283_en-us_topic_0112992301_p2123920113816"><a name="en-us_topic_0112992283_en-us_topic_0112992301_p2123920113816"></a><a name="en-us_topic_0112992283_en-us_topic_0112992301_p2123920113816"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992283_en-us_topic_0112992301_p151239205384"><a name="en-us_topic_0112992283_en-us_topic_0112992301_p151239205384"></a><a name="en-us_topic_0112992283_en-us_topic_0112992301_p151239205384"></a>The request is processed successfully and no content is returned.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

