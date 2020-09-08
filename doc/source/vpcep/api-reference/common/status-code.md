# Status Code<a name="vpcep_08_0001"></a>

-   Normal

    **Table  1**  Return values for successful requests

    <a name="ref520876711"></a>
    <table><thead align="left"><tr id="row57387379"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.4.1.1"><p id="p17866107"><a name="p17866107"></a><a name="p17866107"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.2"><p id="p37868539"><a name="p37868539"></a><a name="p37868539"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="61.62%" id="mcps1.2.4.1.3"><p id="p47452828"><a name="p47452828"></a><a name="p47452828"></a>Error Code</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18473861"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p19987807"><a name="p19987807"></a><a name="p19987807"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p8399698"><a name="p8399698"></a><a name="p8399698"></a>OK</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p9286917"><a name="p9286917"></a><a name="p9286917"></a>The results of POST, GET, and PUT operations are returned as expected.</p>
    </td>
    </tr>
    <tr id="row16473390"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p59276196"><a name="p59276196"></a><a name="p59276196"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p36642608"><a name="p36642608"></a><a name="p36642608"></a>No Content</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p15261239"><a name="p15261239"></a><a name="p15261239"></a>The results of the DELETE operation are returned as expected.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Abnormal

    **Table  2**  Return code for failed requests

    <a name="table651062517217"></a>
    <table><thead align="left"><tr id="row251182532119"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.4.1.1"><p id="p7511182512110"><a name="p7511182512110"></a><a name="p7511182512110"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.2"><p id="p19511325192115"><a name="p19511325192115"></a><a name="p19511325192115"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="61.62%" id="mcps1.2.4.1.3"><p id="p1651110257218"><a name="p1651110257218"></a><a name="p1651110257218"></a>Error Code</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row951102515213"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p155111525152112"><a name="p155111525152112"></a><a name="p155111525152112"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p15511225162116"><a name="p15511225162116"></a><a name="p15511225162116"></a>Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p5511425172114"><a name="p5511425172114"></a><a name="p5511425172114"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row951172562119"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1351132512118"><a name="p1351132512118"></a><a name="p1351132512118"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p14511525122120"><a name="p14511525122120"></a><a name="p14511525122120"></a>Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p651102552120"><a name="p651102552120"></a><a name="p651102552120"></a>You must enter a username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1851172512212"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p95115257217"><a name="p95115257217"></a><a name="p95115257217"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1351112517210"><a name="p1351112517210"></a><a name="p1351112517210"></a>Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p8512225112119"><a name="p8512225112119"></a><a name="p8512225112119"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row18512142502116"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p35121825132114"><a name="p35121825132114"></a><a name="p35121825132114"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p151219259211"><a name="p151219259211"></a><a name="p151219259211"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p10512182517211"><a name="p10512182517211"></a><a name="p10512182517211"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row17512192520217"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p5512112562113"><a name="p5512112562113"></a><a name="p5512112562113"></a>405</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p95121825162110"><a name="p95121825162110"></a><a name="p95121825162110"></a>Method Not  Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p15512425172112"><a name="p15512425172112"></a><a name="p15512425172112"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row451222511219"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p95124252216"><a name="p95124252216"></a><a name="p95124252216"></a>406</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p75126258219"><a name="p75126258219"></a><a name="p75126258219"></a>Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p2512162516212"><a name="p2512162516212"></a><a name="p2512162516212"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row8512525192117"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p55121225182120"><a name="p55121225182120"></a><a name="p55121225182120"></a>407</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p17512162542119"><a name="p17512162542119"></a><a name="p17512162542119"></a>Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p175121625182116"><a name="p175121625182116"></a><a name="p175121625182116"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row85128253214"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p0512102512119"><a name="p0512102512119"></a><a name="p0512102512119"></a>408</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p75121925142120"><a name="p75121925142120"></a><a name="p75121925142120"></a>Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p18513125142117"><a name="p18513125142117"></a><a name="p18513125142117"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row11513102562116"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p14513182592117"><a name="p14513182592117"></a><a name="p14513182592117"></a>409</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p9513102542118"><a name="p9513102542118"></a><a name="p9513102542118"></a>Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p135137258213"><a name="p135137258213"></a><a name="p135137258213"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row115131825142116"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p0513102532110"><a name="p0513102532110"></a><a name="p0513102532110"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p9513425112117"><a name="p9513425112117"></a><a name="p9513425112117"></a>Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1451302520217"><a name="p1451302520217"></a><a name="p1451302520217"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row18513122519217"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p4513132532113"><a name="p4513132532113"></a><a name="p4513132532113"></a>501</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1513102519218"><a name="p1513102519218"></a><a name="p1513102519218"></a>Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p16513925102112"><a name="p16513925102112"></a><a name="p16513925102112"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row1351311256216"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p12513625172119"><a name="p12513625172119"></a><a name="p12513625172119"></a>502</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p0513192542112"><a name="p0513192542112"></a><a name="p0513192542112"></a>Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1251332515211"><a name="p1251332515211"></a><a name="p1251332515211"></a>Failed to complete the request because the server has received an invalid response.</p>
    </td>
    </tr>
    <tr id="row2051392522120"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13513102522113"><a name="p13513102522113"></a><a name="p13513102522113"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p25131425112110"><a name="p25131425112110"></a><a name="p25131425112110"></a>Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1951392514213"><a name="p1951392514213"></a><a name="p1951392514213"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row10513625192113"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p105131225112114"><a name="p105131225112114"></a><a name="p105131225112114"></a>504</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1751322517219"><a name="p1751322517219"></a><a name="p1751322517219"></a>Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p11513525132114"><a name="p11513525132114"></a><a name="p11513525132114"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


