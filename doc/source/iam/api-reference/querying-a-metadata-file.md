# Querying a Metadata File<a name="en-us_topic_0057845553"></a>

## Function Description<a name="section46001270164832"></a>

This interface is used to query the content of the metadata file imported by an identity provider to the IAM system.

## URI<a name="section47602695164832"></a>

-   URI format

    GET /v3-ext/OS-FEDERATION/identity\_providers/\{idp\_id\}/protocols/\{protocol\_id\}/metadata


-   URI parameter description

    <a name="table45982210164832"></a>
    <table><thead align="left"><tr id="row34412857164832"><th class="cellrowborder" valign="top" width="20.49%" id="mcps1.1.5.1.1"><p id="p35978026164832"><a name="p35978026164832"></a><a name="p35978026164832"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.09%" id="mcps1.1.5.1.2"><p id="p28538959164832"><a name="p28538959164832"></a><a name="p28538959164832"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.11%" id="mcps1.1.5.1.3"><p id="p29954320164832"><a name="p29954320164832"></a><a name="p29954320164832"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.31%" id="mcps1.1.5.1.4"><p id="p10380887164832"><a name="p10380887164832"></a><a name="p10380887164832"></a><strong id="a76acf34e8e7b48948763ec1b460ad92f"><a name="a76acf34e8e7b48948763ec1b460ad92f"></a><a name="a76acf34e8e7b48948763ec1b460ad92f"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35545481164832"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p60611728164832"><a name="p60611728164832"></a><a name="p60611728164832"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.09%" headers="mcps1.1.5.1.2 "><p id="p10602964164832"><a name="p10602964164832"></a><a name="p10602964164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p53533756164832"><a name="p53533756164832"></a><a name="p53533756164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.31%" headers="mcps1.1.5.1.4 "><p id="p41266993164832"><a name="p41266993164832"></a><a name="p41266993164832"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row35858619164832"><td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.1.5.1.1 "><p id="p18867054164832"><a name="p18867054164832"></a><a name="p18867054164832"></a>protocol _id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.09%" headers="mcps1.1.5.1.2 "><p id="p51836385164832"><a name="p51836385164832"></a><a name="p51836385164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p37997628164832"><a name="p37997628164832"></a><a name="p37997628164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.31%" headers="mcps1.1.5.1.4 "><p id="p57909032164832"><a name="p57909032164832"></a><a name="p57909032164832"></a>ID of a protocol.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section60120012164832"></a>

-   Request header parameter description

    <a name="table48610655164832"></a>
    <table><thead align="left"><tr id="row34035357164832"><th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.5.1.1"><p id="p5400536164832"><a name="p5400536164832"></a><a name="p5400536164832"></a><strong id="b4342783220148"><a name="b4342783220148"></a><a name="b4342783220148"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.46%" id="mcps1.1.5.1.2"><p id="p34790247164832"><a name="p34790247164832"></a><a name="p34790247164832"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.82%" id="mcps1.1.5.1.3"><p id="p66546611164832"><a name="p66546611164832"></a><a name="p66546611164832"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.5%" id="mcps1.1.5.1.4"><p id="p21566371164832"><a name="p21566371164832"></a><a name="p21566371164832"></a><strong id="b2131004320148"><a name="b2131004320148"></a><a name="b2131004320148"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2045599164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p31475856164832"><a name="p31475856164832"></a><a name="p31475856164832"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.46%" headers="mcps1.1.5.1.2 "><p id="p66516446164832"><a name="p66516446164832"></a><a name="p66516446164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.82%" headers="mcps1.1.5.1.3 "><p id="p19123056164832"><a name="p19123056164832"></a><a name="p19123056164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.5%" headers="mcps1.1.5.1.4 "><p id="p5463727164832"><a name="p5463727164832"></a><a name="p5463727164832"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row49173546164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p23634327164832"><a name="p23634327164832"></a><a name="p23634327164832"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.46%" headers="mcps1.1.5.1.2 "><p id="p35332324164832"><a name="p35332324164832"></a><a name="p35332324164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.82%" headers="mcps1.1.5.1.3 "><p id="p43345977164832"><a name="p43345977164832"></a><a name="p43345977164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.5%" headers="mcps1.1.5.1.4 "><p id="p64412052143925"><a name="p64412052143925"></a><a name="p64412052143925"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://10.185.190.118:31943/v3-ext/OS-FEDERATION/identity_providers/ACME/protocols/saml/metadata
    ```


## Response<a name="section34034532164832"></a>

-   Response body parameter description

    <a name="table29374141164832"></a>
    <table><thead align="left"><tr id="row48948992164832"><th class="cellrowborder" valign="top" width="20.22%" id="mcps1.1.5.1.1"><p id="p5445443164832"><a name="p5445443164832"></a><a name="p5445443164832"></a><strong id="b304405620148"><a name="b304405620148"></a><a name="b304405620148"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.5%" id="mcps1.1.5.1.2"><p id="p38427718164832"><a name="p38427718164832"></a><a name="p38427718164832"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.04%" id="mcps1.1.5.1.3"><p id="p25637425164832"><a name="p25637425164832"></a><a name="p25637425164832"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.5.1.4"><p id="p63365549164832"><a name="p63365549164832"></a><a name="p63365549164832"></a><strong id="b6402864920148"><a name="b6402864920148"></a><a name="b6402864920148"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32335841164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p1957494164832"><a name="p1957494164832"></a><a name="p1957494164832"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p24339348164832"><a name="p24339348164832"></a><a name="p24339348164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p25330146164832"><a name="p25330146164832"></a><a name="p25330146164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p38475912164832"><a name="p38475912164832"></a><a name="p38475912164832"></a>ID of a metadata file.</p>
    </td>
    </tr>
    <tr id="row10738892164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p64543914164832"><a name="p64543914164832"></a><a name="p64543914164832"></a>idp_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p60674549164832"><a name="p60674549164832"></a><a name="p60674549164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p15691412164832"><a name="p15691412164832"></a><a name="p15691412164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p63044848164832"><a name="p63044848164832"></a><a name="p63044848164832"></a>ID of an identity provider.</p>
    </td>
    </tr>
    <tr id="row30532720164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p57231217164832"><a name="p57231217164832"></a><a name="p57231217164832"></a>entity_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p5216995164832"><a name="p5216995164832"></a><a name="p5216995164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p19923437164832"><a name="p19923437164832"></a><a name="p19923437164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p3185720164832"><a name="p3185720164832"></a><a name="p3185720164832"></a><strong id="b84235270618164"><a name="b84235270618164"></a><a name="b84235270618164"></a>entityID</strong> field in the metadata file.</p>
    </td>
    </tr>
    <tr id="row28671485164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p40688972164832"><a name="p40688972164832"></a><a name="p40688972164832"></a>protocol_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p7472431164832"><a name="p7472431164832"></a><a name="p7472431164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p1287183164832"><a name="p1287183164832"></a><a name="p1287183164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p37152979164832"><a name="p37152979164832"></a><a name="p37152979164832"></a>ID of a protocol.</p>
    </td>
    </tr>
    <tr id="row65941358164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p39649796164832"><a name="p39649796164832"></a><a name="p39649796164832"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p57516914164832"><a name="p57516914164832"></a><a name="p57516914164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p28358497164832"><a name="p28358497164832"></a><a name="p28358497164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p15336953164832"><a name="p15336953164832"></a><a name="p15336953164832"></a>ID of the domain that a user belongs to.</p>
    </td>
    </tr>
    <tr id="row3814851164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p40567530164832"><a name="p40567530164832"></a><a name="p40567530164832"></a>xaccount_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p64744526164832"><a name="p64744526164832"></a><a name="p64744526164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p9815254164832"><a name="p9815254164832"></a><a name="p9815254164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p56838123164832"><a name="p56838123164832"></a><a name="p56838123164832"></a>Domain source. The value is left empty by default.</p>
    </td>
    </tr>
    <tr id="row41781061164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p28822808164832"><a name="p28822808164832"></a><a name="p28822808164832"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p52946091164832"><a name="p52946091164832"></a><a name="p52946091164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p60774950164832"><a name="p60774950164832"></a><a name="p60774950164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p23823922164832"><a name="p23823922164832"></a><a name="p23823922164832"></a>Time when a metadata file is imported or updated.</p>
    </td>
    </tr>
    <tr id="row13088710164832"><td class="cellrowborder" valign="top" width="20.22%" headers="mcps1.1.5.1.1 "><p id="p53552557164832"><a name="p53552557164832"></a><a name="p53552557164832"></a>data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.5%" headers="mcps1.1.5.1.2 "><p id="p42789881164832"><a name="p42789881164832"></a><a name="p42789881164832"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.1.5.1.3 "><p id="p43428370164832"><a name="p43428370164832"></a><a name="p43428370164832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.5.1.4 "><p id="p28037087164832"><a name="p28037087164832"></a><a name="p28037087164832"></a>Content of a metadata file.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
    "id": "40c174f35ff94e31b8257ad4991bce8b",
    "idp_id": "ACME",
    "entity_id": "https://idp.test.com/idp/shibboleth",
    "protocol_id": "saml",
    "domain_id": "ed7a77d365304f458f7d0a7909c6d889",
    "xaccount_type": "",
    "update_time": "2016-10-26T09:26:23.000000",
    "data": "$data"}
    ```


## Status Codes<a name="section5936311164832"></a>

<a name="table11079186164832"></a>
<table><thead align="left"><tr id="row37659029164832"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p30482470164832"><a name="p30482470164832"></a><a name="p30482470164832"></a><strong id="b842352706104328"><a name="b842352706104328"></a><a name="b842352706104328"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p53161000164832"><a name="p53161000164832"></a><a name="p53161000164832"></a><strong id="b2836313720148"><a name="b2836313720148"></a><a name="b2836313720148"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row11073730164832"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p24556957164832"><a name="p24556957164832"></a><a name="p24556957164832"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p42956513164832"><a name="p42956513164832"></a><a name="p42956513164832"></a>The request is successful.</p>
</td>
</tr>
<tr id="row51064297164832"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p42567388164832"><a name="p42567388164832"></a><a name="p42567388164832"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p25406412164832"><a name="p25406412164832"></a><a name="p25406412164832"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row27331118164832"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p66336931164832"><a name="p66336931164832"></a><a name="p66336931164832"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4582345164832"><a name="p4582345164832"></a><a name="p4582345164832"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row41241110164832"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p52195591164832"><a name="p52195591164832"></a><a name="p52195591164832"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p67093374164832"><a name="p67093374164832"></a><a name="p67093374164832"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row66969454164832"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p55816678164832"><a name="p55816678164832"></a><a name="p55816678164832"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p24857046164832"><a name="p24857046164832"></a><a name="p24857046164832"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

