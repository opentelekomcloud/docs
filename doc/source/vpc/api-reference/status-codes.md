# Status Codes<a name="vpc_api_0002"></a>

**Table  1**  Normal values

<a name="table4260888320514"></a>
<table><thead align="left"><tr id="row3348120820514"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.1"><p id="p2762331220514"><a name="p2762331220514"></a><a name="p2762331220514"></a><strong id="b842352706151047"><a name="b842352706151047"></a><a name="b842352706151047"></a>Normal Response Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.4.1.2"><p id="p2289577620514"><a name="p2289577620514"></a><a name="p2289577620514"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63.260000000000005%" id="mcps1.2.4.1.3"><p id="p4261857720514"><a name="p4261857720514"></a><a name="p4261857720514"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2955271420514"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p4495966820514"><a name="p4495966820514"></a><a name="p4495966820514"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="p1785451920514"><a name="p1785451920514"></a><a name="p1785451920514"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="63.260000000000005%" headers="mcps1.2.4.1.3 "><p id="p3692991420514"><a name="p3692991420514"></a><a name="p3692991420514"></a>Specifies the normal response code for the GET, PUT, and POST operations.</p>
</td>
</tr>
<tr id="row6393377120514"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p1125294520514"><a name="p1125294520514"></a><a name="p1125294520514"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="p3907338920514"><a name="p3907338920514"></a><a name="p3907338920514"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="63.260000000000005%" headers="mcps1.2.4.1.3 "><p id="p1082790820514"><a name="p1082790820514"></a><a name="p1082790820514"></a>Specifies the normal response code for the POST operation of the OpenStack Neutron API.</p>
</td>
</tr>
<tr id="row3034231420514"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p4180839220514"><a name="p4180839220514"></a><a name="p4180839220514"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.2 "><p id="p3103656620514"><a name="p3103656620514"></a><a name="p3103656620514"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="63.260000000000005%" headers="mcps1.2.4.1.3 "><p id="p3093388420514"><a name="p3093388420514"></a><a name="p3093388420514"></a>Specifies the normal response code for the DELETE operation.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Abnormal values

<a name="table1697655195242"></a>
<table><thead align="left"><tr id="row4329637495242"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.2.3.1.1"><p id="p1734541495242"><a name="p1734541495242"></a><a name="p1734541495242"></a><strong id="b8423527069424"><a name="b8423527069424"></a><a name="b8423527069424"></a>Returned Value</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.58%" id="mcps1.2.3.1.2"><p id="p6280127495242"><a name="p6280127495242"></a><a name="p6280127495242"></a><strong id="b1261529474"><a name="b1261529474"></a><a name="b1261529474"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5373842795242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p5784529695242"><a name="p5784529695242"></a><a name="p5784529695242"></a>400 Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p5495737795242"><a name="p5495737795242"></a><a name="p5495737795242"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row2485435295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p6704552895242"><a name="p6704552895242"></a><a name="p6704552895242"></a>401 Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p6197867295242"><a name="p6197867295242"></a><a name="p6197867295242"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row2093713795242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p1818656595242"><a name="p1818656595242"></a><a name="p1818656595242"></a>403 Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p6382566195242"><a name="p6382566195242"></a><a name="p6382566195242"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row3756004295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p2246459695242"><a name="p2246459695242"></a><a name="p2246459695242"></a>404 Not Found</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p769301595242"><a name="p769301595242"></a><a name="p769301595242"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row212827395242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p3817239595242"><a name="p3817239595242"></a><a name="p3817239595242"></a>405 Method Not Allowed</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p495627395242"><a name="p495627395242"></a><a name="p495627395242"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row4460646595242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p5635390995242"><a name="p5635390995242"></a><a name="p5635390995242"></a>406 Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p126394695242"><a name="p126394695242"></a><a name="p126394695242"></a>The response generated by the server could not be accepted by the client.</p>
</td>
</tr>
<tr id="row1137552095242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p4900196195242"><a name="p4900196195242"></a><a name="p4900196195242"></a>407 Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p973591095242"><a name="p973591095242"></a><a name="p973591095242"></a>You must use the proxy server for authentication so that the request can be processed.</p>
</td>
</tr>
<tr id="row2051433295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p5104819595242"><a name="p5104819595242"></a><a name="p5104819595242"></a>408 Request Timeout</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p4126312295242"><a name="p4126312295242"></a><a name="p4126312295242"></a>The request timed out.</p>
</td>
</tr>
<tr id="row3582378595242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p1604544895242"><a name="p1604544895242"></a><a name="p1604544895242"></a>409 Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p2461290095242"><a name="p2461290095242"></a><a name="p2461290095242"></a>The request could not be processed due to a conflict.</p>
</td>
</tr>
<tr id="row2018950895242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p2473741395242"><a name="p2473741395242"></a><a name="p2473741395242"></a>500 Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p5757343195242"><a name="p5757343195242"></a><a name="p5757343195242"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row4839883395242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p2799143995242"><a name="p2799143995242"></a><a name="p2799143995242"></a>501 Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p5271409795242"><a name="p5271409795242"></a><a name="p5271409795242"></a>Failed to complete the request because the server does not support the requested function.</p>
</td>
</tr>
<tr id="row466483295242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p4230707595242"><a name="p4230707595242"></a><a name="p4230707595242"></a>502 Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p432108895242"><a name="p432108895242"></a><a name="p432108895242"></a>Failed to complete the request because the server has received an invalid response.</p>
</td>
</tr>
<tr id="row3888979595242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p6306567195242"><a name="p6306567195242"></a><a name="p6306567195242"></a>503 Service Unavailable</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p804572095242"><a name="p804572095242"></a><a name="p804572095242"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
<tr id="row530261695242"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.3.1.1 "><p id="p2685875895242"><a name="p2685875895242"></a><a name="p2685875895242"></a>504 Gateway Timeout</p>
</td>
<td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.2.3.1.2 "><p id="p2807582995242"><a name="p2807582995242"></a><a name="p2807582995242"></a>A gateway timeout error occurred.</p>
</td>
</tr>
</tbody>
</table>

