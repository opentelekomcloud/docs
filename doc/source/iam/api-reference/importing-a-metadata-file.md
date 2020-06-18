# Importing a Metadata File<a name="en-us_topic_0057845615"></a>

## Function Description<a name="section60756004163916"></a>

Before using the federated identity authentication function, a metadata file must be imported to the IAM system. This interface is used to import a metadata file of a domain.

## URI<a name="section66385700163916"></a>

-   URI format

    POST /v3-ext/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}/metadata


-   URI parameter description

    <a name="table55329861163916"></a>
    <table><thead align="left"><tr id="row25801157163916"><th class="cellrowborder" valign="top" width="20.48795120487951%" id="mcps1.1.5.1.1"><p id="p9518943163916"><a name="p9518943163916"></a><a name="p9518943163916"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.008299170082992%" id="mcps1.1.5.1.2"><p id="p32836901163916"><a name="p32836901163916"></a><a name="p32836901163916"></a><strong id="b842352706112524"><a name="b842352706112524"></a><a name="b842352706112524"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.958204179582044%" id="mcps1.1.5.1.3"><p id="p42543361163916"><a name="p42543361163916"></a><a name="p42543361163916"></a><strong id="b84235270615026"><a name="b84235270615026"></a><a name="b84235270615026"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.54554544545545%" id="mcps1.1.5.1.4"><p id="p23460184163916"><a name="p23460184163916"></a><a name="p23460184163916"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21226772163916"><td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.1.5.1.1 "><p id="p41647005163916"><a name="p41647005163916"></a><a name="p41647005163916"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.008299170082992%" headers="mcps1.1.5.1.2 "><p id="p17964250163916"><a name="p17964250163916"></a><a name="p17964250163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.958204179582044%" headers="mcps1.1.5.1.3 "><p id="p45818164163916"><a name="p45818164163916"></a><a name="p45818164163916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54554544545545%" headers="mcps1.1.5.1.4 "><p id="p20283794163916"><a name="p20283794163916"></a><a name="p20283794163916"></a>Identity provider ID.</p>
    </td>
    </tr>
    <tr id="row48336422163916"><td class="cellrowborder" valign="top" width="20.48795120487951%" headers="mcps1.1.5.1.1 "><p id="p22936134163916"><a name="p22936134163916"></a><a name="p22936134163916"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.008299170082992%" headers="mcps1.1.5.1.2 "><p id="p45887583163916"><a name="p45887583163916"></a><a name="p45887583163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.958204179582044%" headers="mcps1.1.5.1.3 "><p id="p25906712163916"><a name="p25906712163916"></a><a name="p25906712163916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54554544545545%" headers="mcps1.1.5.1.4 "><p id="p18068889163916"><a name="p18068889163916"></a><a name="p18068889163916"></a>Protocol ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section54293899163916"></a>

-   Request header parameter description

    <a name="table8423392163916"></a>
    <table><thead align="left"><tr id="row19381879163916"><th class="cellrowborder" valign="top" width="20.31%" id="mcps1.1.5.1.1"><p id="p26428347163916"><a name="p26428347163916"></a><a name="p26428347163916"></a><strong id="b558954018"><a name="b558954018"></a><a name="b558954018"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.24%" id="mcps1.1.5.1.2"><p id="p60321356163916"><a name="p60321356163916"></a><a name="p60321356163916"></a><strong id="b89752725"><a name="b89752725"></a><a name="b89752725"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.91%" id="mcps1.1.5.1.3"><p id="p54191633163916"><a name="p54191633163916"></a><a name="p54191633163916"></a><strong id="b993916977"><a name="b993916977"></a><a name="b993916977"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.54%" id="mcps1.1.5.1.4"><p id="p27446130163916"><a name="p27446130163916"></a><a name="p27446130163916"></a><strong id="b425685950"><a name="b425685950"></a><a name="b425685950"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8544089163916"><td class="cellrowborder" valign="top" width="20.31%" headers="mcps1.1.5.1.1 "><p id="p20982571163916"><a name="p20982571163916"></a><a name="p20982571163916"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.1.5.1.2 "><p id="p21866706163916"><a name="p21866706163916"></a><a name="p21866706163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p26372790163916"><a name="p26372790163916"></a><a name="p26372790163916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.5.1.4 "><p id="p55821246163916"><a name="p55821246163916"></a><a name="p55821246163916"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row32629171163916"><td class="cellrowborder" valign="top" width="20.31%" headers="mcps1.1.5.1.1 "><p id="p25717229163916"><a name="p25717229163916"></a><a name="p25717229163916"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.1.5.1.2 "><p id="p2720832163916"><a name="p2720832163916"></a><a name="p2720832163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="p19060819163916"><a name="p19060819163916"></a><a name="p19060819163916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.5.1.4 "><p id="p19047553144032"><a name="p19047553144032"></a><a name="p19047553144032"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request body parameter description

    <a name="table20418334163916"></a>
    <table><thead align="left"><tr id="row21228487163916"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.1.5.1.1"><p id="p41785905163916"><a name="p41785905163916"></a><a name="p41785905163916"></a><strong id="b1281725640"><a name="b1281725640"></a><a name="b1281725640"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.82%" id="mcps1.1.5.1.2"><p id="p29215135163916"><a name="p29215135163916"></a><a name="p29215135163916"></a><strong id="b549651640"><a name="b549651640"></a><a name="b549651640"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.26%" id="mcps1.1.5.1.3"><p id="p17615738163916"><a name="p17615738163916"></a><a name="p17615738163916"></a><strong id="b667528820"><a name="b667528820"></a><a name="b667528820"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.37%" id="mcps1.1.5.1.4"><p id="p17588649163916"><a name="p17588649163916"></a><a name="p17588649163916"></a><strong id="b1274587459"><a name="b1274587459"></a><a name="b1274587459"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15394453163916"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.1.5.1.1 "><p id="p38991141163916"><a name="p38991141163916"></a><a name="p38991141163916"></a>xaccount_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.82%" headers="mcps1.1.5.1.2 "><p id="p4165825163916"><a name="p4165825163916"></a><a name="p4165825163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.1.5.1.3 "><p id="p1887570163916"><a name="p1887570163916"></a><a name="p1887570163916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.1.5.1.4 "><p id="p18675520163916"><a name="p18675520163916"></a><a name="p18675520163916"></a>Source of a domain. This field is left blank by default.</p>
    </td>
    </tr>
    <tr id="row33861957163916"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.1.5.1.1 "><p id="p58464009163916"><a name="p58464009163916"></a><a name="p58464009163916"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.82%" headers="mcps1.1.5.1.2 "><p id="p37964252163916"><a name="p37964252163916"></a><a name="p37964252163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.1.5.1.3 "><p id="p55205609163916"><a name="p55205609163916"></a><a name="p55205609163916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.1.5.1.4 "><p id="p42469334163916"><a name="p42469334163916"></a><a name="p42469334163916"></a>Content of the metadata file on the IdP server.</p>
    </td>
    </tr>
    <tr id="row46679688163916"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.1.5.1.1 "><p id="p22958377163916"><a name="p22958377163916"></a><a name="p22958377163916"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.82%" headers="mcps1.1.5.1.2 "><p id="p47689214163916"><a name="p47689214163916"></a><a name="p47689214163916"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.26%" headers="mcps1.1.5.1.3 "><p id="p37621103163916"><a name="p37621103163916"></a><a name="p37621103163916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.1.5.1.4 "><p id="p27410534163916"><a name="p27410534163916"></a><a name="p27410534163916"></a>ID of the domain that a user belongs to.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X POST -d '{"xaccount_type":"","domain_id":"ed7a77d365304f458f7d0a7909c6d889","metadata":"$metadataContent"}' https://10.185.190.118:31943/v3-ext/OS-FEDERATION/identity_providers/ACME/protocols/saml/metadata
    ```


## Response<a name="section62771979163916"></a>

Sample response

```
{ "message": "Import metadata successful"}
```

## Status Codes<a name="section64646211163916"></a>

<a name="table1851743163916"></a>
<table><thead align="left"><tr id="row23259822163916"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p4997463163916"><a name="p4997463163916"></a><a name="p4997463163916"></a><strong id="b842352706104328"><a name="b842352706104328"></a><a name="b842352706104328"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p2141364163916"><a name="p2141364163916"></a><a name="p2141364163916"></a><strong id="b1827689602"><a name="b1827689602"></a><a name="b1827689602"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row39232814163916"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p23741356163916"><a name="p23741356163916"></a><a name="p23741356163916"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p44001687163916"><a name="p44001687163916"></a><a name="p44001687163916"></a>The import is successful.</p>
</td>
</tr>
<tr id="row60470864163916"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p66301833163916"><a name="p66301833163916"></a><a name="p66301833163916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1739362163916"><a name="p1739362163916"></a><a name="p1739362163916"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row15654258163916"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p60035358163916"><a name="p60035358163916"></a><a name="p60035358163916"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p31025855163916"><a name="p31025855163916"></a><a name="p31025855163916"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row10797247163916"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2161834163916"><a name="p2161834163916"></a><a name="p2161834163916"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p40890878163916"><a name="p40890878163916"></a><a name="p40890878163916"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row32473582163916"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p13114481163916"><a name="p13114481163916"></a><a name="p13114481163916"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p55640049163916"><a name="p55640049163916"></a><a name="p55640049163916"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

