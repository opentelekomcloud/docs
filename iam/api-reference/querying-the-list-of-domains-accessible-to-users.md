# Querying the List of Domains Accessible to Users<a name="en-us_topic_0057845574"></a>

## Function Description<a name="section1161918016535"></a>

This interface is used to query the list of domains accessible to users.

## URI<a name="section1466559616535"></a>

URI format

GET /v3/auth/domains

## Request<a name="section3946061516535"></a>

-   Request header parameter description

    <a name="table42709864193734"></a>
    <table><thead align="left"><tr id="row51079856193734"><th class="cellrowborder" valign="top" width="18.4981501849815%" id="mcps1.1.5.1.1"><p id="p49087560193734"><a name="p49087560193734"></a><a name="p49087560193734"></a><strong id="a6f95694edbbb43d8a152536754b86c82_1"><a name="a6f95694edbbb43d8a152536754b86c82_1"></a><a name="a6f95694edbbb43d8a152536754b86c82_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.75812418758124%" id="mcps1.1.5.1.2"><p id="p16669439193734"><a name="p16669439193734"></a><a name="p16669439193734"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.02809719028097%" id="mcps1.1.5.1.3"><p id="p8047347193734"><a name="p8047347193734"></a><a name="p8047347193734"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.71562843715628%" id="mcps1.1.5.1.4"><p id="p47855371193734"><a name="p47855371193734"></a><a name="p47855371193734"></a><strong id="b810139469113029_1"><a name="b810139469113029_1"></a><a name="b810139469113029_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13774939193734"><td class="cellrowborder" valign="top" width="18.4981501849815%" headers="mcps1.1.5.1.1 "><p id="p43827657193734"><a name="p43827657193734"></a><a name="p43827657193734"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.75812418758124%" headers="mcps1.1.5.1.2 "><p id="p60379327193734"><a name="p60379327193734"></a><a name="p60379327193734"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.02809719028097%" headers="mcps1.1.5.1.3 "><p id="p58887289193734"><a name="p58887289193734"></a><a name="p58887289193734"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.71562843715628%" headers="mcps1.1.5.1.4 "><p id="p5141087193734"><a name="p5141087193734"></a><a name="p5141087193734"></a>Authenticated token.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/auth/domains
    ```


## Response<a name="section2806308616535"></a>

-   Response body parameter description

    <a name="table5851746616535"></a>
    <table><thead align="left"><tr id="row4874364216535"><th class="cellrowborder" valign="top" width="18.39%" id="mcps1.1.5.1.1"><p id="p5592089316535"><a name="p5592089316535"></a><a name="p5592089316535"></a><strong id="b57918781164846"><a name="b57918781164846"></a><a name="b57918781164846"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.58%" id="mcps1.1.5.1.2"><p id="p3329852216535"><a name="p3329852216535"></a><a name="p3329852216535"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.03%" id="mcps1.1.5.1.3"><p id="p1282575116535"><a name="p1282575116535"></a><a name="p1282575116535"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.1.5.1.4"><p id="p3225289216535"><a name="p3225289216535"></a><a name="p3225289216535"></a><strong id="b311754837113113"><a name="b311754837113113"></a><a name="b311754837113113"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6234747416535"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.5.1.1 "><p id="p1698064016535"><a name="p1698064016535"></a><a name="p1698064016535"></a>domains</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.58%" headers="mcps1.1.5.1.2 "><p id="p3325463916535"><a name="p3325463916535"></a><a name="p3325463916535"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.03%" headers="mcps1.1.5.1.3 "><p id="p29011544433"><a name="p29011544433"></a><a name="p29011544433"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p1277547116535"><a name="p1277547116535"></a><a name="p1277547116535"></a>List of domains.</p>
    </td>
    </tr>
    <tr id="row4787037616535"><td class="cellrowborder" valign="top" width="18.39%" headers="mcps1.1.5.1.1 "><p id="p5229527616535"><a name="p5229527616535"></a><a name="p5229527616535"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.58%" headers="mcps1.1.5.1.2 "><p id="p805896416535"><a name="p805896416535"></a><a name="p805896416535"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.03%" headers="mcps1.1.5.1.3 "><p id="p6681742833"><a name="p6681742833"></a><a name="p6681742833"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p6019115416535"><a name="p6019115416535"></a><a name="p6019115416535"></a>Resource links of a domain.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description for the domain format

    <a name="table466092157"></a>
    <table><thead align="left"><tr id="row206601826516"><th class="cellrowborder" valign="top" width="18.33%" id="mcps1.1.5.1.1"><p id="p1466015211510"><a name="p1466015211510"></a><a name="p1466015211510"></a><strong id="a6f95694edbbb43d8a152536754b86c82_3"><a name="a6f95694edbbb43d8a152536754b86c82_3"></a><a name="a6f95694edbbb43d8a152536754b86c82_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.65%" id="mcps1.1.5.1.2"><p id="p466011211514"><a name="p466011211514"></a><a name="p466011211514"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.78%" id="mcps1.1.5.1.3"><p id="p15660192453"><a name="p15660192453"></a><a name="p15660192453"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.24%" id="mcps1.1.5.1.4"><p id="p4661021358"><a name="p4661021358"></a><a name="p4661021358"></a><strong id="b810139469113029_3"><a name="b810139469113029_3"></a><a name="b810139469113029_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row166611125517"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.1 "><p id="p15661125513"><a name="p15661125513"></a><a name="p15661125513"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p36611123514"><a name="p36611123514"></a><a name="p36611123514"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.1.5.1.3 "><p id="p16611521653"><a name="p16611521653"></a><a name="p16611521653"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24%" headers="mcps1.1.5.1.4 "><p id="p8661426513"><a name="p8661426513"></a><a name="p8661426513"></a>Whether a domain is enabled. <strong id="b842352706184851"><a name="b842352706184851"></a><a name="b842352706184851"></a>true</strong> indicates that the domain is enabled. <strong id="b842352706184924"><a name="b842352706184924"></a><a name="b842352706184924"></a>false</strong> indicates that the domain is disabled. The default value is <strong id="b602514205184952"><a name="b602514205184952"></a><a name="b602514205184952"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row6661228518"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.1 "><p id="p146611021152"><a name="p146611021152"></a><a name="p146611021152"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p5661726511"><a name="p5661726511"></a><a name="p5661726511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.1.5.1.3 "><p id="p206612023516"><a name="p206612023516"></a><a name="p206612023516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24%" headers="mcps1.1.5.1.4 "><p id="p46611321856"><a name="p46611321856"></a><a name="p46611321856"></a>Domain ID.</p>
    </td>
    </tr>
    <tr id="row106611821556"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.1 "><p id="p86615219518"><a name="p86615219518"></a><a name="p86615219518"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p14661324520"><a name="p14661324520"></a><a name="p14661324520"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.1.5.1.3 "><p id="p86611921650"><a name="p86611921650"></a><a name="p86611921650"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24%" headers="mcps1.1.5.1.4 "><p id="p10661625511"><a name="p10661625511"></a><a name="p10661625511"></a>Domain name.</p>
    </td>
    </tr>
    <tr id="row8661202259"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.1 "><p id="p1566112218518"><a name="p1566112218518"></a><a name="p1566112218518"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p1766118215512"><a name="p1766118215512"></a><a name="p1766118215512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.1.5.1.3 "><p id="p672913371135"><a name="p672913371135"></a><a name="p672913371135"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24%" headers="mcps1.1.5.1.4 "><p id="p7661021352"><a name="p7661021352"></a><a name="p7661021352"></a>Links to a domain resource.</p>
    </td>
    </tr>
    <tr id="row10311535481"><td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.1 "><p id="p1231123510810"><a name="p1231123510810"></a><a name="p1231123510810"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p13117357817"><a name="p13117357817"></a><a name="p13117357817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.78%" headers="mcps1.1.5.1.3 "><p id="p1432035781"><a name="p1432035781"></a><a name="p1432035781"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.24%" headers="mcps1.1.5.1.4 "><p id="p153263511815"><a name="p153263511815"></a><a name="p153263511815"></a>Domain description.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    {
        "domains": [{
            "description": "desc of domain",
            "enabled": true,
            "id": "37ef61",
            "links": {
                "self": "http://example.com/v3/domains/37ef61"
            },
            "name": "my domain"
        }],
        "links": {
            "self": "http://example.com/v3/auth/domains",
            "previous": null,
            "next": null
        }
    }
    ```


## Status Codes<a name="section4586962016535"></a>

<a name="table2445171616535"></a>
<table><thead align="left"><tr id="row220522216535"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p4440527916535"><a name="p4440527916535"></a><a name="p4440527916535"></a><strong id="b842352706183134"><a name="b842352706183134"></a><a name="b842352706183134"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p4005784516535"><a name="p4005784516535"></a><a name="p4005784516535"></a><strong id="b1087815409113153"><a name="b1087815409113153"></a><a name="b1087815409113153"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2345998316535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2121045316535"><a name="p2121045316535"></a><a name="p2121045316535"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4032516916535"><a name="p4032516916535"></a><a name="p4032516916535"></a>The request is successful.</p>
</td>
</tr>
<tr id="row2738220116535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p336583816535"><a name="p336583816535"></a><a name="p336583816535"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p419748416535"><a name="p419748416535"></a><a name="p419748416535"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row3777735716535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4006708216535"><a name="p4006708216535"></a><a name="p4006708216535"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2420822816535"><a name="p2420822816535"></a><a name="p2420822816535"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row1654746316535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6527611816535"><a name="p6527611816535"></a><a name="p6527611816535"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5287423016535"><a name="p5287423016535"></a><a name="p5287423016535"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row610602816535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2482624816535"><a name="p2482624816535"></a><a name="p2482624816535"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6476903216535"><a name="p6476903216535"></a><a name="p6476903216535"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row4605037716535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3909305116535"><a name="p3909305116535"></a><a name="p3909305116535"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1242054916535"><a name="p1242054916535"></a><a name="p1242054916535"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row4467608316535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6199298116535"><a name="p6199298116535"></a><a name="p6199298116535"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5537558816535"><a name="p5537558816535"></a><a name="p5537558816535"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row2861824716535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3637670816535"><a name="p3637670816535"></a><a name="p3637670816535"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6083222516535"><a name="p6083222516535"></a><a name="p6083222516535"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

