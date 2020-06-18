# Deleting Permissions of a User Group of a Domain<a name="en-us_topic_0057845560"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to delete permissions of a specified user group of a domain. A role is a set of permissions and represents a group of actions.

## URI<a name="section3019338085013"></a>

-   URI format

    DELETE /v3/domains/\{domain\_id\}/groups/\{group\_id\}/roles/\{role\_id\}

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706113951"><a name="b842352706113951"></a><a name="b842352706113951"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.970000000000002%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="b11323553878"><a name="b11323553878"></a><a name="b11323553878"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.75%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row52260639"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p5253358"><a name="en-us_topic_0032920307_p5253358"></a><a name="en-us_topic_0032920307_p5253358"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p22868878"><a name="en-us_topic_0032920307_p22868878"></a><a name="en-us_topic_0032920307_p22868878"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p40439847"><a name="en-us_topic_0032920307_p40439847"></a><a name="en-us_topic_0032920307_p40439847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.75%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p54402144"><a name="en-us_topic_0032920307_p54402144"></a><a name="en-us_topic_0032920307_p54402144"></a>ID of the domain to which a user group belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row19857248"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p64933228"><a name="en-us_topic_0032920307_p64933228"></a><a name="en-us_topic_0032920307_p64933228"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p25100141"><a name="en-us_topic_0032920307_p25100141"></a><a name="en-us_topic_0032920307_p25100141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p19845579"><a name="en-us_topic_0032920307_p19845579"></a><a name="en-us_topic_0032920307_p19845579"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.75%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p63988077"><a name="en-us_topic_0032920307_p63988077"></a><a name="en-us_topic_0032920307_p63988077"></a>ID of a user group.</p>
    </td>
    </tr>
    <tr id="row27198525143830"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="p43460141143830"><a name="p43460141143830"></a><a name="p43460141143830"></a>role_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.1.5.1.2 "><p id="p30610518143830"><a name="p30610518143830"></a><a name="p30610518143830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p63532892143830"><a name="p63532892143830"></a><a name="p63532892143830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.75%" headers="mcps1.1.5.1.4 "><p id="p45890598143830"><a name="p45890598143830"></a><a name="p45890598143830"></a>ID of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.11191119111911%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.29192919291929%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="b114391561072"><a name="b114391561072"></a><a name="b114391561072"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.77167716771677%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.82448244824482%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.11191119111911%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.29192919291929%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77167716771677%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.82448244824482%" headers="mcps1.1.5.1.4 "><p id="p5164267111831"><a name="p5164267111831"></a><a name="p5164267111831"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X DELETE https://10.22.44.158:31943/v3/domains/d54061ebcb5145dd814f8eb3fe9b7ac0/groups/47d79cabc2cf4c35b13493d919a5bb3d/roles/e62d9ba0d6a544cd878d9e8a4663f6e2
    ```


## **Response**<a name="section1625244161112"></a>

No response body.

## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b4643653491053"><a name="b4643653491053"></a><a name="b4643653491053"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032920307_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p22613965"><a name="en-us_topic_0032920307_p22613965"></a><a name="en-us_topic_0032920307_p22613965"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p19791876"><a name="en-us_topic_0032920307_p19791876"></a><a name="en-us_topic_0032920307_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p66980994"><a name="en-us_topic_0032920307_p66980994"></a><a name="en-us_topic_0032920307_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p56751409"><a name="en-us_topic_0032920307_p56751409"></a><a name="en-us_topic_0032920307_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row460808479497"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p120744399497"><a name="p120744399497"></a><a name="p120744399497"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p385055099497"><a name="p385055099497"></a><a name="p385055099497"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p32717189"><a name="en-us_topic_0032920307_p32717189"></a><a name="en-us_topic_0032920307_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p32846614"><a name="en-us_topic_0032920307_p32846614"></a><a name="en-us_topic_0032920307_p32846614"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row5922032814523"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6322091114523"><a name="p6322091114523"></a><a name="p6322091114523"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2062019914523"><a name="p2062019914523"></a><a name="p2062019914523"></a>The server could not find the requested page.</p>
</td>
</tr>
</tbody>
</table>

