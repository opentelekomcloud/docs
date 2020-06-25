# Creating an Identity Provider<a name="en-us_topic_0057845606"></a>

## Function Description<a name="section1156121494041"></a>

This interface is used to create an identity provider.

## URI<a name="section3951742894041"></a>

-   URI format

    PUT /v3/OS-FEDERATION/identity\_providers/\{id\}


-   URI parameter description

    <a name="table5106348094041"></a>
    <table><thead align="left"><tr id="row5126430694041"><th class="cellrowborder" valign="top" width="20.352035203520348%" id="mcps1.1.5.1.1"><p id="p5876810194041"><a name="p5876810194041"></a><a name="p5876810194041"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.301730173017297%" id="mcps1.1.5.1.2"><p id="p6259571294041"><a name="p6259571294041"></a><a name="p6259571294041"></a><strong id="b842352706112524"><a name="b842352706112524"></a><a name="b842352706112524"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23182318231823%" id="mcps1.1.5.1.3"><p id="p3708791694041"><a name="p3708791694041"></a><a name="p3708791694041"></a><strong id="b84235270615026"><a name="b84235270615026"></a><a name="b84235270615026"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.114411441144114%" id="mcps1.1.5.1.4"><p id="p5133121694041"><a name="p5133121694041"></a><a name="p5133121694041"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6418786194041"><td class="cellrowborder" valign="top" width="20.352035203520348%" headers="mcps1.1.5.1.1 "><p id="p3183427594041"><a name="p3183427594041"></a><a name="p3183427594041"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.301730173017297%" headers="mcps1.1.5.1.2 "><p id="p2843945794041"><a name="p2843945794041"></a><a name="p2843945794041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.1.5.1.3 "><p id="p2189464794041"><a name="p2189464794041"></a><a name="p2189464794041"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.114411441144114%" headers="mcps1.1.5.1.4 "><p id="p2863598294041"><a name="p2863598294041"></a><a name="p2863598294041"></a>ID of an identity provider.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3781319794041"></a>

-   Request header parameter description

    <a name="table5802941494041"></a>
    <table><thead align="left"><tr id="row2251960494041"><th class="cellrowborder" valign="top" width="20.34%" id="mcps1.1.5.1.1"><p id="p1214867494041"><a name="p1214867494041"></a><a name="p1214867494041"></a><strong id="b1927227610"><a name="b1927227610"></a><a name="b1927227610"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.34%" id="mcps1.1.5.1.2"><p id="p4451854894041"><a name="p4451854894041"></a><a name="p4451854894041"></a><strong id="b1297398137"><a name="b1297398137"></a><a name="b1297398137"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.94%" id="mcps1.1.5.1.3"><p id="p4923265994041"><a name="p4923265994041"></a><a name="p4923265994041"></a><strong id="b1953663390"><a name="b1953663390"></a><a name="b1953663390"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.379999999999995%" id="mcps1.1.5.1.4"><p id="p2842243894041"><a name="p2842243894041"></a><a name="p2842243894041"></a><strong id="b1774204119"><a name="b1774204119"></a><a name="b1774204119"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2051615094041"><td class="cellrowborder" valign="top" width="20.34%" headers="mcps1.1.5.1.1 "><p id="p5119543494041"><a name="p5119543494041"></a><a name="p5119543494041"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.2 "><p id="p5318948394041"><a name="p5318948394041"></a><a name="p5318948394041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.94%" headers="mcps1.1.5.1.3 "><p id="p1338083294041"><a name="p1338083294041"></a><a name="p1338083294041"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p1010558594041"><a name="p1010558594041"></a><a name="p1010558594041"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row2384140894041"><td class="cellrowborder" valign="top" width="20.34%" headers="mcps1.1.5.1.1 "><p id="p5210592894041"><a name="p5210592894041"></a><a name="p5210592894041"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.2 "><p id="p5983062494041"><a name="p5983062494041"></a><a name="p5983062494041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.94%" headers="mcps1.1.5.1.3 "><p id="p1444235294041"><a name="p1444235294041"></a><a name="p1444235294041"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.379999999999995%" headers="mcps1.1.5.1.4 "><p id="p6357973814242"><a name="p6357973814242"></a><a name="p6357973814242"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table6566837894041"></a>
    <table><thead align="left"><tr id="row316713194041"><th class="cellrowborder" valign="top" width="20.44%" id="mcps1.1.5.1.1"><p id="p5521104194041"><a name="p5521104194041"></a><a name="p5521104194041"></a><strong id="b357297261"><a name="b357297261"></a><a name="b357297261"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.18%" id="mcps1.1.5.1.2"><p id="p4290937394041"><a name="p4290937394041"></a><a name="p4290937394041"></a><strong id="b1759689321"><a name="b1759689321"></a><a name="b1759689321"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.07%" id="mcps1.1.5.1.3"><p id="p5310715694041"><a name="p5310715694041"></a><a name="p5310715694041"></a><strong id="b2005631441"><a name="b2005631441"></a><a name="b2005631441"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.31%" id="mcps1.1.5.1.4"><p id="p671240094041"><a name="p671240094041"></a><a name="p671240094041"></a><strong id="b26931124"><a name="b26931124"></a><a name="b26931124"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row147705523391"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.1.5.1.1 "><p id="p177019521394"><a name="p177019521394"></a><a name="p177019521394"></a>identity_provider</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.1.5.1.2 "><p id="p777016526395"><a name="p777016526395"></a><a name="p777016526395"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p1277075273915"><a name="p1277075273915"></a><a name="p1277075273915"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.31%" headers="mcps1.1.5.1.4 "><p id="p3770852183920"><a name="p3770852183920"></a><a name="p3770852183920"></a>Request body for registering an identity provider.</p>
    </td>
    </tr>
    <tr id="row683356194041"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.1.5.1.1 "><p id="p1664757494041"><a name="p1664757494041"></a><a name="p1664757494041"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.1.5.1.2 "><p id="p627627294041"><a name="p627627294041"></a><a name="p627627294041"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p3861601494041"><a name="p3861601494041"></a><a name="p3861601494041"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.31%" headers="mcps1.1.5.1.4 "><p id="p4088943394041"><a name="p4088943394041"></a><a name="p4088943394041"></a>Identity provider description.</p>
    </td>
    </tr>
    <tr id="row3246057894041"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.1.5.1.1 "><p id="p1206117994041"><a name="p1206117994041"></a><a name="p1206117994041"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.1.5.1.2 "><p id="p3743141294041"><a name="p3743141294041"></a><a name="p3743141294041"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="p1204549394041"><a name="p1204549394041"></a><a name="p1204549394041"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.31%" headers="mcps1.1.5.1.4 "><p id="p2245802394056"><a name="p2245802394056"></a><a name="p2245802394056"></a>Whether an identity provider is enabled.</p>
    <a name="ul203517099419"></a><a name="ul203517099419"></a><ul id="ul203517099419"><li><strong id="b491330209419"><a name="b491330209419"></a><a name="b491330209419"></a>true</strong> indicates that the identity provider is enabled.</li><li><strong id="b395440039419"><a name="b395440039419"></a><a name="b395440039419"></a>false</strong> indicates that the identity provider is disabled.</li></ul>
    <p id="p3616087194041"><a name="p3616087194041"></a><a name="p3616087194041"></a>The default value is <strong id="b89329584593417"><a name="b89329584593417"></a><a name="b89329584593417"></a>false</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PUT -d'{"identity_provider":{"description":"Stores ACME identities.","enabled":true}}' https://10.185.190.118:31943/v3/OS-FEDERATION/identity_providers/ACME
    ```


## Response<a name="section2085259294041"></a>

-   Response body parameter description

    <a name="table4599365094041"></a>
    <table><thead align="left"><tr id="row6084341394041"><th class="cellrowborder" valign="top" width="20.65%" id="mcps1.1.5.1.1"><p id="p2936938394041"><a name="p2936938394041"></a><a name="p2936938394041"></a><strong id="b1708471542"><a name="b1708471542"></a><a name="b1708471542"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.91%" id="mcps1.1.5.1.2"><p id="p3010983894041"><a name="p3010983894041"></a><a name="p3010983894041"></a><strong id="b1748260905"><a name="b1748260905"></a><a name="b1748260905"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.19%" id="mcps1.1.5.1.3"><p id="p2297784294041"><a name="p2297784294041"></a><a name="p2297784294041"></a><strong id="b1073946207"><a name="b1073946207"></a><a name="b1073946207"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.25%" id="mcps1.1.5.1.4"><p id="p4926591494041"><a name="p4926591494041"></a><a name="p4926591494041"></a><strong id="b1410787650"><a name="b1410787650"></a><a name="b1410787650"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3111611194041"><td class="cellrowborder" valign="top" width="20.65%" headers="mcps1.1.5.1.1 "><p id="p3737704894041"><a name="p3737704894041"></a><a name="p3737704894041"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p764204694041"><a name="p764204694041"></a><a name="p764204694041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.19%" headers="mcps1.1.5.1.3 "><p id="p1502596094041"><a name="p1502596094041"></a><a name="p1502596094041"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.25%" headers="mcps1.1.5.1.4 "><p id="p914323094041"><a name="p914323094041"></a><a name="p914323094041"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row1518021494041"><td class="cellrowborder" valign="top" width="20.65%" headers="mcps1.1.5.1.1 "><p id="p2163781894041"><a name="p2163781894041"></a><a name="p2163781894041"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p783286394041"><a name="p783286394041"></a><a name="p783286394041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.19%" headers="mcps1.1.5.1.3 "><p id="p3048218994041"><a name="p3048218994041"></a><a name="p3048218994041"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.25%" headers="mcps1.1.5.1.4 "><p id="p5313821994041"><a name="p5313821994041"></a><a name="p5313821994041"></a>Identity provider description.</p>
    </td>
    </tr>
    <tr id="row848192394041"><td class="cellrowborder" valign="top" width="20.65%" headers="mcps1.1.5.1.1 "><p id="p1594718194041"><a name="p1594718194041"></a><a name="p1594718194041"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p1665327594041"><a name="p1665327594041"></a><a name="p1665327594041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.19%" headers="mcps1.1.5.1.3 "><p id="p673803894041"><a name="p673803894041"></a><a name="p673803894041"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.25%" headers="mcps1.1.5.1.4 "><p id="p891018194041"><a name="p891018194041"></a><a name="p891018194041"></a>Whether an identity provider is enabled.</p>
    </td>
    </tr>
    <tr id="row61413316819"><td class="cellrowborder" valign="top" width="20.65%" headers="mcps1.1.5.1.1 "><p id="p1414173312813"><a name="p1414173312813"></a><a name="p1414173312813"></a>remote_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p014933583"><a name="p014933583"></a><a name="p014933583"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.19%" headers="mcps1.1.5.1.3 "><p id="p414244115131"><a name="p414244115131"></a><a name="p414244115131"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.25%" headers="mcps1.1.5.1.4 "><p id="p111511335811"><a name="p111511335811"></a><a name="p111511335811"></a>Federated user ID list of an identity provider.</p>
    </td>
    </tr>
    <tr id="row1308276894041"><td class="cellrowborder" valign="top" width="20.65%" headers="mcps1.1.5.1.1 "><p id="p5307125794041"><a name="p5307125794041"></a><a name="p5307125794041"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.2 "><p id="p380452294041"><a name="p380452294041"></a><a name="p380452294041"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.19%" headers="mcps1.1.5.1.3 "><p id="p3973086094041"><a name="p3973086094041"></a><a name="p3973086094041"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.25%" headers="mcps1.1.5.1.4 "><p id="p6408307894041"><a name="p6408307894041"></a><a name="p6408307894041"></a>Resource links of an identity provider, including <strong id="b4102052893151"><a name="b4102052893151"></a><a name="b4102052893151"></a>protocols</strong> and <strong id="b84235270695025"><a name="b84235270695025"></a><a name="b84235270695025"></a>self</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "identity_provider": {
            "description": "Stores ACME identities",
            "enabled": true,
            "id": "ACME",
            "remote_ids": [],
            "links": {
                "protocols": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME/protocols",
                "self": "https://example.com/v3/OS-FEDERATION/identity_providers/ACME"
            }
        }
    }
    ```


## Status Codes<a name="section4456313094041"></a>

<a name="table5284375594041"></a>
<table><thead align="left"><tr id="row1009137094041"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1209461894041"><a name="p1209461894041"></a><a name="p1209461894041"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p4014001194041"><a name="p4014001194041"></a><a name="p4014001194041"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3011546094041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2343323094041"><a name="p2343323094041"></a><a name="p2343323094041"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1904350594041"><a name="p1904350594041"></a><a name="p1904350594041"></a>The request is successful.</p>
</td>
</tr>
<tr id="row3717381994041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5828933394041"><a name="p5828933394041"></a><a name="p5828933394041"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2381551594041"><a name="p2381551594041"></a><a name="p2381551594041"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row1301305194041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4742420794041"><a name="p4742420794041"></a><a name="p4742420794041"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1615558894041"><a name="p1615558894041"></a><a name="p1615558894041"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row1118257094041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3337301194041"><a name="p3337301194041"></a><a name="p3337301194041"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1885937694041"><a name="p1885937694041"></a><a name="p1885937694041"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row3551666294041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5827737394041"><a name="p5827737394041"></a><a name="p5827737394041"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2284676494041"><a name="p2284676494041"></a><a name="p2284676494041"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row429429194041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1229326694041"><a name="p1229326694041"></a><a name="p1229326694041"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5623047894041"><a name="p5623047894041"></a><a name="p5623047894041"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row11885125610385"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p888675653816"><a name="p888675653816"></a><a name="p888675653816"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3786276397"><a name="p3786276397"></a><a name="p3786276397"></a>Duplicate identity provider ID.</p>
</td>
</tr>
<tr id="row3631225494041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5561142394041"><a name="p5561142394041"></a><a name="p5561142394041"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p823140994041"><a name="p823140994041"></a><a name="p823140994041"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row697381994041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2800850594041"><a name="p2800850594041"></a><a name="p2800850594041"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5409644394041"><a name="p5409644394041"></a><a name="p5409644394041"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row1710594694041"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4340434994041"><a name="p4340434994041"></a><a name="p4340434994041"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2609141894041"><a name="p2609141894041"></a><a name="p2609141894041"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>

