# Deleting a Protocol<a name="en-us_topic_0057845559"></a>

## Function Description<a name="section1360442210300"></a>

This interface is used to delete the information about a protocol.

## URI<a name="section5262093810300"></a>

-   URI format

    DELETE /v3/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}


-   URI parameter description

    <a name="table3893247610300"></a>
    <table><thead align="left"><tr id="row2523850510300"><th class="cellrowborder" valign="top" width="21.15%" id="mcps1.1.5.1.1"><p id="p3105303110300"><a name="p3105303110300"></a><a name="p3105303110300"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.83%" id="mcps1.1.5.1.2"><p id="p3226762210300"><a name="p3226762210300"></a><a name="p3226762210300"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.77%" id="mcps1.1.5.1.3"><p id="p6354062210300"><a name="p6354062210300"></a><a name="p6354062210300"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.25%" id="mcps1.1.5.1.4"><p id="p4651674210300"><a name="p4651674210300"></a><a name="p4651674210300"></a><strong id="b842352706114032"><a name="b842352706114032"></a><a name="b842352706114032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row975973410300"><td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.5.1.1 "><p id="p5234099910300"><a name="p5234099910300"></a><a name="p5234099910300"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.2 "><p id="p1176252810300"><a name="p1176252810300"></a><a name="p1176252810300"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77%" headers="mcps1.1.5.1.3 "><p id="p1324074610300"><a name="p1324074610300"></a><a name="p1324074610300"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.25%" headers="mcps1.1.5.1.4 "><p id="p6586753310300"><a name="p6586753310300"></a><a name="p6586753310300"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row5593688710300"><td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.1.5.1.1 "><p id="p3459396910300"><a name="p3459396910300"></a><a name="p3459396910300"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.2 "><p id="p5064808710300"><a name="p5064808710300"></a><a name="p5064808710300"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.77%" headers="mcps1.1.5.1.3 "><p id="p885441910300"><a name="p885441910300"></a><a name="p885441910300"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.25%" headers="mcps1.1.5.1.4 "><p id="p4611930610300"><a name="p4611930610300"></a><a name="p4611930610300"></a>ID of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section4467632610300"></a>

-   Request header parameter description

    <a name="table5697175610300"></a>
    <table><thead align="left"><tr id="row1328480810300"><th class="cellrowborder" valign="top" width="20.97209720972097%" id="mcps1.1.5.1.1"><p id="p232768110300"><a name="p232768110300"></a><a name="p232768110300"></a><strong id="b1902707391713"><a name="b1902707391713"></a><a name="b1902707391713"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.99179917991799%" id="mcps1.1.5.1.2"><p id="p5432444210300"><a name="p5432444210300"></a><a name="p5432444210300"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.92169216921692%" id="mcps1.1.5.1.3"><p id="p3820364310300"><a name="p3820364310300"></a><a name="p3820364310300"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.114411441144114%" id="mcps1.1.5.1.4"><p id="p748737310300"><a name="p748737310300"></a><a name="p748737310300"></a><strong id="b569276191713"><a name="b569276191713"></a><a name="b569276191713"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row249746310300"><td class="cellrowborder" valign="top" width="20.97209720972097%" headers="mcps1.1.5.1.1 "><p id="p96797010300"><a name="p96797010300"></a><a name="p96797010300"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.99179917991799%" headers="mcps1.1.5.1.2 "><p id="p1129675810300"><a name="p1129675810300"></a><a name="p1129675810300"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.3 "><p id="p4262216910300"><a name="p4262216910300"></a><a name="p4262216910300"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.114411441144114%" headers="mcps1.1.5.1.4 "><p id="p2984370210300"><a name="p2984370210300"></a><a name="p2984370210300"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row15786510300"><td class="cellrowborder" valign="top" width="20.97209720972097%" headers="mcps1.1.5.1.1 "><p id="p1278708510300"><a name="p1278708510300"></a><a name="p1278708510300"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.99179917991799%" headers="mcps1.1.5.1.2 "><p id="p2912095810300"><a name="p2912095810300"></a><a name="p2912095810300"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.92169216921692%" headers="mcps1.1.5.1.3 "><p id="p998736310300"><a name="p998736310300"></a><a name="p998736310300"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.114411441144114%" headers="mcps1.1.5.1.4 "><p id="p41791925143832"><a name="p41791925143832"></a><a name="p41791925143832"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X DELETE https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME/protocols/saml
    ```


## Response<a name="section246253135018"></a>

No response body.

## Status Codes<a name="section2883882710300"></a>

<a name="table5424361310300"></a>
<table><thead align="left"><tr id="row5928375610300"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3725493310300"><a name="p3725493310300"></a><a name="p3725493310300"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p6485963110300"><a name="p6485963110300"></a><a name="p6485963110300"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1913878610300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p673781310300"><a name="p673781310300"></a><a name="p673781310300"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p889195210300"><a name="p889195210300"></a><a name="p889195210300"></a>The request is successful.</p>
</td>
</tr>
<tr id="row1291870810300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3978246410300"><a name="p3978246410300"></a><a name="p3978246410300"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p115411910300"><a name="p115411910300"></a><a name="p115411910300"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row1038707710300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3604693110300"><a name="p3604693110300"></a><a name="p3604693110300"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3412027310300"><a name="p3412027310300"></a><a name="p3412027310300"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row3864700110300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4339939510300"><a name="p4339939510300"></a><a name="p4339939510300"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2569009710300"><a name="p2569009710300"></a><a name="p2569009710300"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row2988428510300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p470804510300"><a name="p470804510300"></a><a name="p470804510300"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4580738210300"><a name="p4580738210300"></a><a name="p4580738210300"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row961325510300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4047615110300"><a name="p4047615110300"></a><a name="p4047615110300"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5734277110300"><a name="p5734277110300"></a><a name="p5734277110300"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row4632289810300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6116724410300"><a name="p6116724410300"></a><a name="p6116724410300"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5559975110300"><a name="p5559975110300"></a><a name="p5559975110300"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row3063571610300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6557395510300"><a name="p6557395510300"></a><a name="p6557395510300"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p989013410300"><a name="p989013410300"></a><a name="p989013410300"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row2190234710300"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2925967210300"><a name="p2925967210300"></a><a name="p2925967210300"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2122321310300"><a name="p2122321310300"></a><a name="p2122321310300"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

