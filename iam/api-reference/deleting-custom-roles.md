# Deleting Custom Roles<a name="EN-US_TOPIC_0147658938"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to delete a custom role.

## URI<a name="section3019338085013"></a>

-   URI format

    DELETE /v3.0/OS-ROLE/roles/\{role\_id\}

-   URI parameter description

    <a name="table98401658191411"></a>
    <table><thead align="left"><tr id="row2847958191412"><th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.1.5.1.1"><p id="p1584916584149"><a name="p1584916584149"></a><a name="p1584916584149"></a><strong id="b842352706115348"><a name="b842352706115348"></a><a name="b842352706115348"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.1.5.1.2"><p id="p88521458131414"><a name="p88521458131414"></a><a name="p88521458131414"></a><strong id="b7930731103215"><a name="b7930731103215"></a><a name="b7930731103215"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.3"><p id="p38544583144"><a name="p38544583144"></a><a name="p38544583144"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.97%" id="mcps1.1.5.1.4"><p id="p1855135811145"><a name="p1855135811145"></a><a name="p1855135811145"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10857175812142"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.1 "><p id="p11858195810145"><a name="p11858195810145"></a><a name="p11858195810145"></a>role_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.2 "><p id="p78604589143"><a name="p78604589143"></a><a name="p78604589143"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.3 "><p id="p178621558171415"><a name="p178621558171415"></a><a name="p178621558171415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.97%" headers="mcps1.1.5.1.4 "><p id="p986535814143"><a name="p986535814143"></a><a name="p986535814143"></a>ID of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="b13634202633213_1"><a name="b13634202633213_1"></a><a name="b13634202633213_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.57%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.080000000000005%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p4276535113040"><a name="p4276535113040"></a><a name="p4276535113040"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    <tr id="row0289192254015"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p756284913314"><a name="p756284913314"></a><a name="p756284913314"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p1656219494334"><a name="p1656219494334"></a><a name="p1656219494334"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.1.5.1.3 "><p id="p86097153416"><a name="p86097153416"></a><a name="p86097153416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p95620493339"><a name="p95620493339"></a><a name="p95620493339"></a>Fill <strong id="b1230634495415"><a name="b1230634495415"></a><a name="b1230634495415"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X DELETE https://10.22.44.158:31943/v3.0/OS-ROLE/roles/9698542758bc422088c0c3eabfc30d12
    ```


## **Response**<a name="section422798898594"></a>

-   Error response body parameter description

    <a name="table11369132715418"></a>
    <table><thead align="left"><tr id="row1937712715414"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="p1237819270542"><a name="p1237819270542"></a><a name="p1237819270542"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.2"><p id="p338319273549"><a name="p338319273549"></a><a name="p338319273549"></a><strong id="b651434731"><a name="b651434731"></a><a name="b651434731"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.06%" id="mcps1.1.5.1.3"><p id="p15386152755413"><a name="p15386152755413"></a><a name="p15386152755413"></a><strong id="b2077277291"><a name="b2077277291"></a><a name="b2077277291"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.940000000000005%" id="mcps1.1.5.1.4"><p id="p538916276547"><a name="p538916276547"></a><a name="p538916276547"></a><strong id="b393398730"><a name="b393398730"></a><a name="b393398730"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row93911227135417"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p339310274543"><a name="p339310274543"></a><a name="p339310274543"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p16394152716546"><a name="p16394152716546"></a><a name="p16394152716546"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p1339662755417"><a name="p1339662755417"></a><a name="p1339662755417"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p1397172725415"><a name="p1397172725415"></a><a name="p1397172725415"></a>Response failed</p>
    </td>
    </tr>
    <tr id="row18399927115419"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p1024473095615"><a name="p1024473095615"></a><a name="p1024473095615"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p1740352725417"><a name="p1740352725417"></a><a name="p1740352725417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p84051327155415"><a name="p84051327155415"></a><a name="p84051327155415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p154064276547"><a name="p154064276547"></a><a name="p154064276547"></a>Error details</p>
    </td>
    </tr>
    <tr id="row372143818575"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p157237386575"><a name="p157237386575"></a><a name="p157237386575"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p1723193895712"><a name="p1723193895712"></a><a name="p1723193895712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p472318381579"><a name="p472318381579"></a><a name="p472318381579"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p1172313855711"><a name="p1172313855711"></a><a name="p1172313855711"></a>Status code</p>
    </td>
    </tr>
    <tr id="row12320192018583"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p1132012017585"><a name="p1132012017585"></a><a name="p1132012017585"></a>title</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p9320122095810"><a name="p9320122095810"></a><a name="p9320122095810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p2032082014581"><a name="p2032082014581"></a><a name="p2032082014581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p681134632"><a name="p681134632"></a><a name="p681134632"></a>Error type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response \(failed response\)

```
{
  "error": {
    "message": "Authentication failed",
    "code": 401,
    "title": "Unauthorized"
  }
}
```

## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b23486412155652"><a name="b23486412155652"></a><a name="b23486412155652"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b20601766145329_9"><a name="b20601766145329_9"></a><a name="b20601766145329_9"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032920307_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p22613965"><a name="en-us_topic_0032920307_p22613965"></a><a name="en-us_topic_0032920307_p22613965"></a>200</p>
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
<tr id="row19866120144214"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p18866420104215"><a name="p18866420104215"></a><a name="p18866420104215"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p18661820124213"><a name="p18661820124213"></a><a name="p18661820124213"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row52593584174147"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p64430038174149"><a name="p64430038174149"></a><a name="p64430038174149"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p51450627174149"><a name="p51450627174149"></a><a name="p51450627174149"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

