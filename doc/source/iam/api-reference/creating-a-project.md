# Creating a Project<a name="en-us_topic_0066154565"></a>

## Function Description<a name="section14840153773114"></a>

This interface is used to create a project.

## URI<a name="section784163713116"></a>

URI format

POST /v3/projects

## Request<a name="section1984123716317"></a>

-   Request header parameter description

    <a name="table6841837173110"></a>
    <table><thead align="left"><tr id="row58413376318"><th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.5.1.1"><p id="p584143715313"><a name="p584143715313"></a><a name="p584143715313"></a><strong id="b865896518147"><a name="b865896518147"></a><a name="b865896518147"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.709999999999997%" id="mcps1.1.5.1.2"><p id="p58421837173119"><a name="p58421837173119"></a><a name="p58421837173119"></a><strong id="b55396190181415"><a name="b55396190181415"></a><a name="b55396190181415"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.360000000000003%" id="mcps1.1.5.1.3"><p id="p1284203773111"><a name="p1284203773111"></a><a name="p1284203773111"></a><strong id="b29996550181423"><a name="b29996550181423"></a><a name="b29996550181423"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.45%" id="mcps1.1.5.1.4"><p id="p1584293703114"><a name="p1584293703114"></a><a name="p1584293703114"></a><strong id="b19141093181431"><a name="b19141093181431"></a><a name="b19141093181431"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11842637153116"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.1 "><p id="p68421237153116"><a name="p68421237153116"></a><a name="p68421237153116"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.1.5.1.2 "><p id="p198428375319"><a name="p198428375319"></a><a name="p198428375319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.3 "><p id="p158426375311"><a name="p158426375311"></a><a name="p158426375311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.45%" headers="mcps1.1.5.1.4 "><p id="p784213783118"><a name="p784213783118"></a><a name="p784213783118"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row984253713313"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.1 "><p id="p1484219377311"><a name="p1484219377311"></a><a name="p1484219377311"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.709999999999997%" headers="mcps1.1.5.1.2 "><p id="p484223783118"><a name="p484223783118"></a><a name="p484223783118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.3 "><p id="p1884233733118"><a name="p1884233733118"></a><a name="p1884233733118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.45%" headers="mcps1.1.5.1.4 "><p id="p379833091312"><a name="p379833091312"></a><a name="p379833091312"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request body parameter description

    <a name="table1584218378319"></a>
    <table><thead align="left"><tr id="row784312379318"><th class="cellrowborder" valign="top" width="18.35%" id="mcps1.1.5.1.1"><p id="p1084319374318"><a name="p1084319374318"></a><a name="p1084319374318"></a><strong id="b19889620181855"><a name="b19889620181855"></a><a name="b19889620181855"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.09%" id="mcps1.1.5.1.2"><p id="p1584373753111"><a name="p1584373753111"></a><a name="p1584373753111"></a><strong id="b36317923181829"><a name="b36317923181829"></a><a name="b36317923181829"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.490000000000002%" id="mcps1.1.5.1.3"><p id="p188431437173116"><a name="p188431437173116"></a><a name="p188431437173116"></a><strong id="b37271989181838"><a name="b37271989181838"></a><a name="b37271989181838"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.07%" id="mcps1.1.5.1.4"><p id="p2084323733114"><a name="p2084323733114"></a><a name="p2084323733114"></a><strong id="b64170555181845"><a name="b64170555181845"></a><a name="b64170555181845"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row484363763114"><td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.1 "><p id="p10866102274714"><a name="p10866102274714"></a><a name="p10866102274714"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.2 "><p id="p8866182254710"><a name="p8866182254710"></a><a name="p8866182254710"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.490000000000002%" headers="mcps1.1.5.1.3 "><p id="p98661522154710"><a name="p98661522154710"></a><a name="p98661522154710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.07%" headers="mcps1.1.5.1.4 "><p id="p2866922184715"><a name="p2866922184715"></a><a name="p2866922184715"></a>Project name, which must start with <em id="i842352697134716"><a name="i842352697134716"></a><a name="i842352697134716"></a>ID of an existing region</em>_ and be less than or equal to 64 characters.</p>
    <p id="p8866172211473"><a name="p8866172211473"></a><a name="p8866172211473"></a>Example: <em id="i1531907502113130"><a name="i1531907502113130"></a><a name="i1531907502113130"></a>{region_id}</em>_test1</p>
    </td>
    </tr>
    <tr id="row9843637103110"><td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.1 "><p id="p2171222476"><a name="p2171222476"></a><a name="p2171222476"></a>parent_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.2 "><p id="p1216152218474"><a name="p1216152218474"></a><a name="p1216152218474"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.490000000000002%" headers="mcps1.1.5.1.3 "><p id="p615132216471"><a name="p615132216471"></a><a name="p615132216471"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.07%" headers="mcps1.1.5.1.4 "><p id="p1813172216475"><a name="p1813172216475"></a><a name="p1813172216475"></a>Parent project ID to which a project belongs.</p>
    </td>
    </tr>
    <tr id="row11331310194713"><td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.1 "><p id="p10715201514476"><a name="p10715201514476"></a><a name="p10715201514476"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.2 "><p id="p371581515472"><a name="p371581515472"></a><a name="p371581515472"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.490000000000002%" headers="mcps1.1.5.1.3 "><p id="p1171551574715"><a name="p1171551574715"></a><a name="p1171551574715"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.07%" headers="mcps1.1.5.1.4 "><p id="p12715215114715"><a name="p12715215114715"></a><a name="p12715215114715"></a>ID of the domain that a project belongs to.</p>
    </td>
    </tr>
    <tr id="row47961920510"><td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.1 "><p id="p479719754"><a name="p479719754"></a><a name="p479719754"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.09%" headers="mcps1.1.5.1.2 "><p id="p117971296516"><a name="p117971296516"></a><a name="p117971296516"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.490000000000002%" headers="mcps1.1.5.1.3 "><p id="p5324113519"><a name="p5324113519"></a><a name="p5324113519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.07%" headers="mcps1.1.5.1.4 "><p id="p73174114511"><a name="p73174114511"></a><a name="p73174114511"></a>Project description, which can contain a maximum of 255 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X POST –d '{"project":{"domain_id":"acf2ffabba974fae8f30378ffde2cfa6","name":"region_test1"}}' https://10.144.24.54:31943/v3/projects
    ```


## Response<a name="section78443371318"></a>

Sample response

```
{
    "project": {
        "is_domain": false,
        "description": "",
        "links": {
            "self": "10.10.10.10/v3/projects/3de1461665f045ef91ba1efe8121b979"
        },
        "enabled": true,
        "id": "3de1461665f045ef91ba1efe8121b979",
        "parent_id": "d1294857fdf64251994892b344f53e88",
        "domain_id": "d1294857fdf64251994892b344f53e88",
        "name": "region_test1"
    }
}
```

## Status Codes<a name="section584413370311"></a>

<a name="table138451637163117"></a>
<table><thead align="left"><tr id="row3845183773112"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p13845103743114"><a name="p13845103743114"></a><a name="p13845103743114"></a><strong id="b5536438181756"><a name="b5536438181756"></a><a name="b5536438181756"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p11845037143110"><a name="p11845037143110"></a><a name="p11845037143110"></a><strong id="b4379203118184"><a name="b4379203118184"></a><a name="b4379203118184"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4845203710315"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p158454371316"><a name="p158454371316"></a><a name="p158454371316"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1684518374319"><a name="p1684518374319"></a><a name="p1684518374319"></a>The request is successful.</p>
</td>
</tr>
<tr id="row9845133753118"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p48451037173111"><a name="p48451037173111"></a><a name="p48451037173111"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p98451237183119"><a name="p98451237183119"></a><a name="p98451237183119"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row384518375310"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p284583733115"><a name="p284583733115"></a><a name="p284583733115"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p584543743117"><a name="p584543743117"></a><a name="p584543743117"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row1620125915310"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p421115903114"><a name="p421115903114"></a><a name="p421115903114"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p821135963116"><a name="p821135963116"></a><a name="p821135963116"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row118451837143115"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p88458372318"><a name="p88458372318"></a><a name="p88458372318"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p48451637123118"><a name="p48451637123118"></a><a name="p48451637123118"></a>Duplicate project name.</p>
</td>
</tr>
</tbody>
</table>

