# Modifying Project Data<a name="en-us_topic_0066154566"></a>

## Function Description<a name="section136583151330"></a>

This interface is used to modify project information.

## URI<a name="section9658161518332"></a>

-   URI format

    PATCH /v3/projects/\{project\_id\}


-   URI parameter description

    <a name="table1765831514339"></a>
    <table><thead align="left"><tr id="row136591215133314"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.1.5.1.1"><p id="p66598151330"><a name="p66598151330"></a><a name="p66598151330"></a><strong id="b53311302182144"><a name="b53311302182144"></a><a name="b53311302182144"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.2"><p id="p1565991583314"><a name="p1565991583314"></a><a name="p1565991583314"></a><strong id="b13290795182156_1"><a name="b13290795182156_1"></a><a name="b13290795182156_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.41%" id="mcps1.1.5.1.3"><p id="p9659315143313"><a name="p9659315143313"></a><a name="p9659315143313"></a><strong id="b1400565718225_1"><a name="b1400565718225_1"></a><a name="b1400565718225_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.330000000000005%" id="mcps1.1.5.1.4"><p id="p4659131573319"><a name="p4659131573319"></a><a name="p4659131573319"></a><strong id="b15483672182216"><a name="b15483672182216"></a><a name="b15483672182216"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row365911520332"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.1.5.1.1 "><p id="p37620953151130"><a name="p37620953151130"></a><a name="p37620953151130"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.2 "><p id="p20659171513317"><a name="p20659171513317"></a><a name="p20659171513317"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.41%" headers="mcps1.1.5.1.3 "><p id="p5659191514336"><a name="p5659191514336"></a><a name="p5659191514336"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.330000000000005%" headers="mcps1.1.5.1.4 "><p id="p56591315203314"><a name="p56591315203314"></a><a name="p56591315203314"></a>Project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section4659131517333"></a>

-   Request header parameter description

    <a name="table9659111593317"></a>
    <table><thead align="left"><tr id="row76601115103317"><th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.1.5.1.1"><p id="p15660215143314"><a name="p15660215143314"></a><a name="p15660215143314"></a><strong id="b51854391182410"><a name="b51854391182410"></a><a name="b51854391182410"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.85811418858114%" id="mcps1.1.5.1.2"><p id="p1366016151333"><a name="p1366016151333"></a><a name="p1366016151333"></a><strong id="b13290795182156_3"><a name="b13290795182156_3"></a><a name="b13290795182156_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.238176182381764%" id="mcps1.1.5.1.3"><p id="p12660141523316"><a name="p12660141523316"></a><a name="p12660141523316"></a><strong id="b1400565718225_3"><a name="b1400565718225_3"></a><a name="b1400565718225_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.535546445355465%" id="mcps1.1.5.1.4"><p id="p366041510334"><a name="p366041510334"></a><a name="p366041510334"></a><strong id="b4654987182428"><a name="b4654987182428"></a><a name="b4654987182428"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16601915183311"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.1.5.1.1 "><p id="p066081553317"><a name="p066081553317"></a><a name="p066081553317"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.85811418858114%" headers="mcps1.1.5.1.2 "><p id="p18660191533319"><a name="p18660191533319"></a><a name="p18660191533319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.238176182381764%" headers="mcps1.1.5.1.3 "><p id="p13660141512331"><a name="p13660141512331"></a><a name="p13660141512331"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.535546445355465%" headers="mcps1.1.5.1.4 "><p id="p1066031573318"><a name="p1066031573318"></a><a name="p1066031573318"></a>Text type and encoding mode.</p>
    <p id="p5660181593311"><a name="p5660181593311"></a><a name="p5660181593311"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row6660191533312"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.1.5.1.1 "><p id="p11660915173320"><a name="p11660915173320"></a><a name="p11660915173320"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.85811418858114%" headers="mcps1.1.5.1.2 "><p id="p146607157336"><a name="p146607157336"></a><a name="p146607157336"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.238176182381764%" headers="mcps1.1.5.1.3 "><p id="p966071513313"><a name="p966071513313"></a><a name="p966071513313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.535546445355465%" headers="mcps1.1.5.1.4 "><p id="p2219223591414"><a name="p2219223591414"></a><a name="p2219223591414"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request body parameter description

    <a name="table46601915113311"></a>
    <table><thead align="left"><tr id="row126611515123310"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.1.5.1.1"><p id="p196611915173316"><a name="p196611915173316"></a><a name="p196611915173316"></a><strong id="b12756667182446"><a name="b12756667182446"></a><a name="b12756667182446"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.72%" id="mcps1.1.5.1.2"><p id="p1966141515334"><a name="p1966141515334"></a><a name="p1966141515334"></a><strong id="b2980390182457"><a name="b2980390182457"></a><a name="b2980390182457"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.1.5.1.3"><p id="p866110159333"><a name="p866110159333"></a><a name="p866110159333"></a><strong id="b1400565718225_5"><a name="b1400565718225_5"></a><a name="b1400565718225_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.54%" id="mcps1.1.5.1.4"><p id="p66619159336"><a name="p66619159336"></a><a name="p66619159336"></a><strong id="b9907860182436"><a name="b9907860182436"></a><a name="b9907860182436"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10661141573316"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.1.5.1.1 "><p id="p46611015103314"><a name="p46611015103314"></a><a name="p46611015103314"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.1.5.1.2 "><p id="p366191510336"><a name="p366191510336"></a><a name="p366191510336"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.1.5.1.3 "><p id="p26611515103318"><a name="p26611515103318"></a><a name="p26611515103318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.5.1.4 "><p id="p066131553314"><a name="p066131553314"></a><a name="p066131553314"></a>Project name, which must start with <em id="i842352697134716"><a name="i842352697134716"></a><a name="i842352697134716"></a>ID of an existing region</em>_ and be less than or equal to 64 characters.</p>
    <p id="p646762814348"><a name="p646762814348"></a><a name="p646762814348"></a>Example: <em id="i842352697134816"><a name="i842352697134816"></a><a name="i842352697134816"></a>region</em>_test2</p>
    </td>
    </tr>
    <tr id="row1661101514336"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.1.5.1.1 "><p id="p1766110156335"><a name="p1766110156335"></a><a name="p1766110156335"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.72%" headers="mcps1.1.5.1.2 "><p id="p1466116158331"><a name="p1466116158331"></a><a name="p1466116158331"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.1.5.1.3 "><p id="p1566181512332"><a name="p1566181512332"></a><a name="p1566181512332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.54%" headers="mcps1.1.5.1.4 "><p id="p186611215103311"><a name="p186611215103311"></a><a name="p186611215103311"></a>Project description, which can contain a maximum of 255 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X PATCH -d '{"project":{"name":"region_test2","description":"test_project_desc"}}' https://10.144.24.54:31943/v3/projects/23da5961c8214f5caf701c27d9703959
    ```


## Response<a name="section116611315193312"></a>

Sample response

```
{
    "project": {
        "is_domain": false,
        "description": "test_project_desc",
        "links": {
            "self": "10.10.10.10/v3/projects/23da5961c8214f5caf701c27d9703959"
        },
        "enabled": true,
        "id": "23da5961c8214f5caf701c27d9703959",
        "parent_id": "d1294857fdf64251994892b344f53e88",
        "domain_id": "d1294857fdf64251994892b344f53e88",
        "name": "region_test2"
    }
}
```

## Status Codes<a name="section36611815103319"></a>

<a name="table156611415193318"></a>
<table><thead align="left"><tr id="row2066121533319"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p46611151332"><a name="p46611151332"></a><a name="p46611151332"></a><strong id="b25940534182714"><a name="b25940534182714"></a><a name="b25940534182714"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p566114154334"><a name="p566114154334"></a><a name="p566114154334"></a><strong id="b37731373182726"><a name="b37731373182726"></a><a name="b37731373182726"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1166116156330"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6661181583317"><a name="p6661181583317"></a><a name="p6661181583317"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p196611715173319"><a name="p196611715173319"></a><a name="p196611715173319"></a>The request is successful.</p>
</td>
</tr>
<tr id="row12661131516333"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p17661121514334"><a name="p17661121514334"></a><a name="p17661121514334"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p666114154335"><a name="p666114154335"></a><a name="p666114154335"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row3661115103315"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p16661191593311"><a name="p16661191593311"></a><a name="p16661191593311"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p26611915193313"><a name="p26611915193313"></a><a name="p26611915193313"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row156611915163319"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1366191518335"><a name="p1366191518335"></a><a name="p1366191518335"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p666191513317"><a name="p666191513317"></a><a name="p666191513317"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row18867124011346"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p14867104033419"><a name="p14867104033419"></a><a name="p14867104033419"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3867204073419"><a name="p3867204073419"></a><a name="p3867204073419"></a>Duplicate project name.</p>
</td>
</tr>
</tbody>
</table>

