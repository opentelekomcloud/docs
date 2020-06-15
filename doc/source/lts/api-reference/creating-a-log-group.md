# Creating a Log Group<a name="lts_02_0003"></a>

This API is used to create a log group. All API URLs described in this section must be case-sensitive.

## Function<a name="section4621333"></a>

This function describes how to create a log group for log storage and query. You can create a maximum of 100 log groups.

## URI<a name="section41592000"></a>

-   URI format

    POST /v2.0/\{project\_id\}/log-groups


-   Parameter description

    **Table  1**  Parameter description

    <a name="table48105459"></a>
    <table><thead align="left"><tr id="row60866610"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p31248367"><a name="p31248367"></a><a name="p31248367"></a><strong id="b1337963223918"><a name="b1337963223918"></a><a name="b1337963223918"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p48089780"><a name="p48089780"></a><a name="p48089780"></a><strong id="b481373363911"><a name="b481373363911"></a><a name="b481373363911"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p2958122"><a name="p2958122"></a><a name="p2958122"></a><strong id="b18346435193915"><a name="b18346435193915"></a><a name="b18346435193915"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p38281336"><a name="p38281336"></a><a name="p38281336"></a><strong id="b2026411366395"><a name="b2026411366395"></a><a name="b2026411366395"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13780551"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p42482879"><a name="p42482879"></a><a name="p42482879"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p18561159"><a name="p18561159"></a><a name="p18561159"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p27058887"><a name="p27058887"></a><a name="p27058887"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p44286248"><a name="p44286248"></a><a name="p44286248"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section38783684"></a>

-   Request parameters

    **Table  2**  Parameter description

    <a name="table47804267"></a>
    <table><thead align="left"><tr id="row48525468"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.1"><p id="p38248803"><a name="p38248803"></a><a name="p38248803"></a><strong id="b1124318619407"><a name="b1124318619407"></a><a name="b1124318619407"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.2"><p id="p11145359"><a name="p11145359"></a><a name="p11145359"></a><strong id="afd1c772bc0d34dd0954eb451c30339a1"><a name="afd1c772bc0d34dd0954eb451c30339a1"></a><a name="afd1c772bc0d34dd0954eb451c30339a1"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.3"><p id="p30358920"><a name="p30358920"></a><a name="p30358920"></a><strong id="b07871114164011"><a name="b07871114164011"></a><a name="b07871114164011"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.6.1.4"><p id="p43153461"><a name="p43153461"></a><a name="p43153461"></a><strong id="b24681157403"><a name="b24681157403"></a><a name="b24681157403"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.2.6.1.5"><p id="p5769471"><a name="p5769471"></a><a name="p5769471"></a><strong id="b05215168400"><a name="b05215168400"></a><a name="b05215168400"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64673997"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p4102408"><a name="p4102408"></a><a name="p4102408"></a>log_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.2 "><p id="p63859607"><a name="p63859607"></a><a name="p63859607"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.3 "><p id="p5245667"><a name="p5245667"></a><a name="p5245667"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.6.1.4 "><p id="p22245843"><a name="p22245843"></a><a name="p22245843"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.6.1.5 "><p id="p57082831"><a name="p57082831"></a><a name="p57082831"></a>Specifies the log group name.</p>
    <p id="a85abdc81ab8744b69765ad68746d242f"><a name="a85abdc81ab8744b69765ad68746d242f"></a><a name="a85abdc81ab8744b69765ad68746d242f"></a>The configuration rules are as follows:</p>
    <a name="u171738f158ec47de86f1dcc16cd98255"></a><a name="u171738f158ec47de86f1dcc16cd98255"></a><ul id="u171738f158ec47de86f1dcc16cd98255"><li>Must be a string of 1 to 64 characters.</li><li>Only allows uppercase and lowercase letters, digits, special characters, underscores (_), hyphens (-), and periods (.). The name cannot start or end with a period.</li></ul>
    </td>
    </tr>
    <tr id="row43983438"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p5888712"><a name="p5888712"></a><a name="p5888712"></a>ttl_in_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.2 "><p id="p7223683"><a name="p7223683"></a><a name="p7223683"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.3 "><p id="p48247463"><a name="p48247463"></a><a name="p48247463"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.6.1.4 "><p id="p15730394"><a name="p15730394"></a><a name="p15730394"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.6.1.5 "><p id="p66202439"><a name="p66202439"></a><a name="p66202439"></a>Specifies the log expiration time. The value is fixed to 7 days.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST /v2.0/{project_id}/log-groups 
    { 
    "log_group_name":"test01",
    "ttl_in_days": 7
    }
    ```


## Response<a name="section13508843"></a>

-   Response parameters

    **Table  3**  Parameter description

    <a name="table32993388"></a>
    <table><thead align="left"><tr id="row9385709"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.5.1.1"><p id="p22044993"><a name="p22044993"></a><a name="p22044993"></a><strong id="b129413310598"><a name="b129413310598"></a><a name="b129413310598"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.772277227722775%" id="mcps1.2.5.1.2"><p id="p40814009"><a name="p40814009"></a><a name="p40814009"></a><strong id="b1788932445"><a name="b1788932445"></a><a name="b1788932445"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.3"><p id="p17600446"><a name="p17600446"></a><a name="p17600446"></a><strong id="b151384295920"><a name="b151384295920"></a><a name="b151384295920"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.693069306930692%" id="mcps1.2.5.1.4"><p id="p16350007"><a name="p16350007"></a><a name="p16350007"></a><strong id="b2021484365911"><a name="b2021484365911"></a><a name="b2021484365911"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49282189"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p32434343"><a name="p32434343"></a><a name="p32434343"></a>log_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.772277227722775%" headers="mcps1.2.5.1.2 "><p id="p9936109"><a name="p9936109"></a><a name="p9936109"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.3 "><p id="p66627401"><a name="p66627401"></a><a name="p66627401"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.5.1.4 "><p id="p28110368"><a name="p28110368"></a><a name="p28110368"></a>Specifies the log group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
     "log_group_id":"56b4b31f-3024-11e9-9023-286ed488ce71"
    } 
    ```


## Returned Value<a name="section54470724"></a>

-   Normal

    201


-   Abnormal

    For details about status code, see  [Status Code](status-code.md).


