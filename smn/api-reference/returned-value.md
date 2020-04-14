# Returned Value<a name="smn_api_63002"></a>

-   Normal

    <a name="table56484750195335"></a>
    <table><thead align="left"><tr id="row57491589195335"><th class="cellrowborder" valign="top" width="35.35%" id="mcps1.1.3.1.1"><p id="p26307160195335"><a name="p26307160195335"></a><a name="p26307160195335"></a><strong id="b84235270617451"><a name="b84235270617451"></a><a name="b84235270617451"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64.64999999999999%" id="mcps1.1.3.1.2"><p id="p50505195195335"><a name="p50505195195335"></a><a name="p50505195195335"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64388966195335"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.1.3.1.1 "><p id="p48123762195335"><a name="p48123762195335"></a><a name="p48123762195335"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64999999999999%" headers="mcps1.1.3.1.2 "><p id="p5710646195335"><a name="p5710646195335"></a><a name="p5710646195335"></a>The task is submitted successfully.</p>
    </td>
    </tr>
    <tr id="row1074452974212"><td class="cellrowborder" valign="top" width="35.35%" headers="mcps1.1.3.1.1 "><p id="p8745172944218"><a name="p8745172944218"></a><a name="p8745172944218"></a>201</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.64999999999999%" headers="mcps1.1.3.1.2 "><p id="p18745112914212"><a name="p18745112914212"></a><a name="p18745112914212"></a>Resource creation succeeds.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    <a name="table59272457195335"></a>
    <table><thead align="left"><tr id="row50751459195335"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p17227532195335"><a name="p17227532195335"></a><a name="p17227532195335"></a><strong id="b84235270617540"><a name="b84235270617540"></a><a name="b84235270617540"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p53252821195335"><a name="p53252821195335"></a><a name="p53252821195335"></a><strong id="b84235270619115_1"><a name="b84235270619115_1"></a><a name="b84235270619115_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18511206195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p23012712195335"><a name="p23012712195335"></a><a name="p23012712195335"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p52090370195335"><a name="p52090370195335"></a><a name="p52090370195335"></a>Incorrect request parameters.</p>
    </td>
    </tr>
    <tr id="row1071615458810"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p8716124516810"><a name="p8716124516810"></a><a name="p8716124516810"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p191516591208"><a name="p191516591208"></a><a name="p191516591208"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row66160152195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p57372106195335"><a name="p57372106195335"></a><a name="p57372106195335"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p16629033195335"><a name="p16629033195335"></a><a name="p16629033195335"></a>No permission to access the requested resource.</p>
    </td>
    </tr>
    <tr id="row15443572195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p42969857195335"><a name="p42969857195335"></a><a name="p42969857195335"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p58006382195335"><a name="p58006382195335"></a><a name="p58006382195335"></a>The requested resource does not exist.</p>
    </td>
    </tr>
    <tr id="row52295392195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p8068353195335"><a name="p8068353195335"></a><a name="p8068353195335"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p49556822195335"><a name="p49556822195335"></a><a name="p49556822195335"></a>The request fails because the server is abnormal.</p>
    </td>
    </tr>
    <tr id="row43358215195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p22354566195335"><a name="p22354566195335"></a><a name="p22354566195335"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p65889454195335"><a name="p65889454195335"></a><a name="p65889454195335"></a>The request fails because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row56134176195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p50574423195335"><a name="p50574423195335"></a><a name="p50574423195335"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2887627195335"><a name="p2887627195335"></a><a name="p2887627195335"></a>The request fails because the returned response is invalid.</p>
    </td>
    </tr>
    <tr id="row25988647195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p24705664195335"><a name="p24705664195335"></a><a name="p24705664195335"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p55001802195335"><a name="p55001802195335"></a><a name="p55001802195335"></a>The request fails because the system is abnormal.</p>
    </td>
    </tr>
    <tr id="row25254177195335"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p32322455195335"><a name="p32322455195335"></a><a name="p32322455195335"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p873169195335"><a name="p873169195335"></a><a name="p873169195335"></a>Gateway times out.</p>
    </td>
    </tr>
    </tbody>
    </table>


