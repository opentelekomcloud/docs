# Deleting an Identity Provider<a name="en-us_topic_0057845570"></a>

## Function Description<a name="section6240520694241"></a>

This interface is used to delete the information about an identity provider.

## URI<a name="section6069442994241"></a>

-   URI format

    DELETE /v3/OS-FEDERATION/identity\_providers/\{id\}


-   URI parameter description

    <a name="table5171140094241"></a>
    <table><thead align="left"><tr id="row1006611394241"><th class="cellrowborder" valign="top" width="19.958004199580042%" id="mcps1.1.5.1.1"><p id="p1004882694241"><a name="p1004882694241"></a><a name="p1004882694241"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.098190180981902%" id="mcps1.1.5.1.2"><p id="p864861294241"><a name="p864861294241"></a><a name="p864861294241"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.2982701729827%" id="mcps1.1.5.1.3"><p id="p2944899994241"><a name="p2944899994241"></a><a name="p2944899994241"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.645535446455355%" id="mcps1.1.5.1.4"><p id="p3655869894241"><a name="p3655869894241"></a><a name="p3655869894241"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row846453394241"><td class="cellrowborder" valign="top" width="19.958004199580042%" headers="mcps1.1.5.1.1 "><p id="p1453857794241"><a name="p1453857794241"></a><a name="p1453857794241"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.098190180981902%" headers="mcps1.1.5.1.2 "><p id="p3677408594241"><a name="p3677408594241"></a><a name="p3677408594241"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.2982701729827%" headers="mcps1.1.5.1.3 "><p id="p2591093894241"><a name="p2591093894241"></a><a name="p2591093894241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.645535446455355%" headers="mcps1.1.5.1.4 "><p id="p1841125694241"><a name="p1841125694241"></a><a name="p1841125694241"></a>ID of an identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1491674294241"></a>

-   Request header parameter description

    <a name="table2402107594241"></a>
    <table><thead align="left"><tr id="row605976494241"><th class="cellrowborder" valign="top" width="19.79%" id="mcps1.1.5.1.1"><p id="p2107883694241"><a name="p2107883694241"></a><a name="p2107883694241"></a><strong id="b2383801391651"><a name="b2383801391651"></a><a name="b2383801391651"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.97%" id="mcps1.1.5.1.2"><p id="p2966412894241"><a name="p2966412894241"></a><a name="p2966412894241"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.78%" id="mcps1.1.5.1.3"><p id="p5398419394241"><a name="p5398419394241"></a><a name="p5398419394241"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.46%" id="mcps1.1.5.1.4"><p id="p1064355194241"><a name="p1064355194241"></a><a name="p1064355194241"></a><strong id="b433235991651"><a name="b433235991651"></a><a name="b433235991651"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5682131394241"><td class="cellrowborder" valign="top" width="19.79%" headers="mcps1.1.5.1.1 "><p id="p3912366494241"><a name="p3912366494241"></a><a name="p3912366494241"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.5.1.2 "><p id="p1490021194241"><a name="p1490021194241"></a><a name="p1490021194241"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.1.5.1.3 "><p id="p6606645194241"><a name="p6606645194241"></a><a name="p6606645194241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.46%" headers="mcps1.1.5.1.4 "><p id="p4978229594241"><a name="p4978229594241"></a><a name="p4978229594241"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row4538747494241"><td class="cellrowborder" valign="top" width="19.79%" headers="mcps1.1.5.1.1 "><p id="p5250679294241"><a name="p5250679294241"></a><a name="p5250679294241"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.97%" headers="mcps1.1.5.1.2 "><p id="p2519176694241"><a name="p2519176694241"></a><a name="p2519176694241"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.1.5.1.3 "><p id="p2726720594241"><a name="p2726720594241"></a><a name="p2726720594241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.46%" headers="mcps1.1.5.1.4 "><p id="p44909934142634"><a name="p44909934142634"></a><a name="p44909934142634"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X DELETE https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME
    ```


## Response<a name="section8554205141216"></a>

No response body.

## Status Codes<a name="section5501530194241"></a>

<a name="table2705437394241"></a>
<table><thead align="left"><tr id="row719985594241"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p4631736894241"><a name="p4631736894241"></a><a name="p4631736894241"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p6071932694241"><a name="p6071932694241"></a><a name="p6071932694241"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1931834494241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2128201494241"><a name="p2128201494241"></a><a name="p2128201494241"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4612161094241"><a name="p4612161094241"></a><a name="p4612161094241"></a>The request is successful.</p>
</td>
</tr>
<tr id="row1244130694241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p111289594241"><a name="p111289594241"></a><a name="p111289594241"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2303569394241"><a name="p2303569394241"></a><a name="p2303569394241"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row599464694241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1580432394241"><a name="p1580432394241"></a><a name="p1580432394241"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p508180594241"><a name="p508180594241"></a><a name="p508180594241"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row4573624894241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1364859994241"><a name="p1364859994241"></a><a name="p1364859994241"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3179475994241"><a name="p3179475994241"></a><a name="p3179475994241"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row1771738194241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2582174594241"><a name="p2582174594241"></a><a name="p2582174594241"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1118656194241"><a name="p1118656194241"></a><a name="p1118656194241"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row3357018694241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3483054094241"><a name="p3483054094241"></a><a name="p3483054094241"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p270147894241"><a name="p270147894241"></a><a name="p270147894241"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row2431330894241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2322094294241"><a name="p2322094294241"></a><a name="p2322094294241"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p184817394241"><a name="p184817394241"></a><a name="p184817394241"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row1663356094241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p514115794241"><a name="p514115794241"></a><a name="p514115794241"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1378056294241"><a name="p1378056294241"></a><a name="p1378056294241"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row5691619694241"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4680915794241"><a name="p4680915794241"></a><a name="p4680915794241"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3344533894241"><a name="p3344533894241"></a><a name="p3344533894241"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

