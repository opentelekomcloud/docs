# Querying the List of Domain Names<a name="EN-US_TOPIC_0193631139"></a>

## Function Description<a name="section60785565"></a>

This API is used to query the list of domain names.

## URI<a name="section10199180"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/instance?offset=\{offset\}&limit=\{limit\}&hostname=\{hostname\}&policyname=\{policyname\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table4196369"></a>
    <table><thead align="left"><tr id="row49735522"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p2045483"><a name="p2045483"></a><a name="p2045483"></a><strong id="b5335940165013"><a name="b5335940165013"></a><a name="b5335940165013"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.77852214778522%" id="mcps1.2.5.1.2"><p id="p31466469"><a name="p31466469"></a><a name="p31466469"></a><strong id="b1397574125013"><a name="b1397574125013"></a><a name="b1397574125013"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.918008199180083%" id="mcps1.2.5.1.3"><p id="p65756088"><a name="p65756088"></a><a name="p65756088"></a><strong id="b9819114475017"><a name="b9819114475017"></a><a name="b9819114475017"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p24642891"><a name="p24642891"></a><a name="p24642891"></a><strong id="b93061509508"><a name="b93061509508"></a><a name="b93061509508"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49917126"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16755410"><a name="p16755410"></a><a name="p16755410"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77852214778522%" headers="mcps1.2.5.1.2 "><p id="p15010966"><a name="p15010966"></a><a name="p15010966"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.5.1.3 "><p id="p7928763"><a name="p7928763"></a><a name="p7928763"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p38250089"><a name="p38250089"></a><a name="p38250089"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row8706482"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16851416219"><a name="p16851416219"></a><a name="p16851416219"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77852214778522%" headers="mcps1.2.5.1.2 "><p id="p13588841"><a name="p13588841"></a><a name="p13588841"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.5.1.3 "><p id="p26954327"><a name="p26954327"></a><a name="p26954327"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p21617533"><a name="p21617533"></a><a name="p21617533"></a>Specifies the number of returned pages. Its value ranges from <strong id="b2584046145217"><a name="b2584046145217"></a><a name="b2584046145217"></a>0</strong> to <strong id="b195841146155214"><a name="b195841146155214"></a><a name="b195841146155214"></a>65535</strong>. The default value is <strong id="b158412465528"><a name="b158412465528"></a><a name="b158412465528"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row53916483"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p5159020"><a name="p5159020"></a><a name="p5159020"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77852214778522%" headers="mcps1.2.5.1.2 "><p id="p15227445"><a name="p15227445"></a><a name="p15227445"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.5.1.3 "><p id="p25463494"><a name="p25463494"></a><a name="p25463494"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p25357967"><a name="p25357967"></a><a name="p25357967"></a>Specifies the maximum number of records displayed on each page. Its value ranges from <strong id="b153401042123216"><a name="b153401042123216"></a><a name="b153401042123216"></a>0</strong> to <strong id="b163495425326"><a name="b163495425326"></a><a name="b163495425326"></a>50</strong>. The default value is <strong id="b15349134253217"><a name="b15349134253217"></a><a name="b15349134253217"></a>10</strong>. If <strong id="b1768216012454"><a name="b1768216012454"></a><a name="b1768216012454"></a>limit</strong> is <strong id="b1868290194520"><a name="b1868290194520"></a><a name="b1868290194520"></a>-1</strong>, one page with 65535 records is displayed.</p>
    </td>
    </tr>
    <tr id="row40840970"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p19784312"><a name="p19784312"></a><a name="p19784312"></a>hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77852214778522%" headers="mcps1.2.5.1.2 "><p id="p59025450"><a name="p59025450"></a><a name="p59025450"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.5.1.3 "><p id="p16332169"><a name="p16332169"></a><a name="p16332169"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p47837308"><a name="p47837308"></a><a name="p47837308"></a>Specifies the domain name.</p>
    </td>
    </tr>
    <tr id="row27882593"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p43897550"><a name="p43897550"></a><a name="p43897550"></a>policyname</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77852214778522%" headers="mcps1.2.5.1.2 "><p id="p66040643"><a name="p66040643"></a><a name="p66040643"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.5.1.3 "><p id="p47691881"><a name="p47691881"></a><a name="p47691881"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p37837159"><a name="p37837159"></a><a name="p37837159"></a>Specifies the policy name.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section24683756"></a>

Request parameters

None

## Response<a name="section20827215"></a>

Response parameters

**Table  2**  Parameter description

<a name="table53675654"></a>
<table><thead align="left"><tr id="row15396832"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p39183914"><a name="p39183914"></a><a name="p39183914"></a><strong id="b8187243135212"><a name="b8187243135212"></a><a name="b8187243135212"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p19780493"><a name="p19780493"></a><a name="p19780493"></a><strong id="b2398114455216"><a name="b2398114455216"></a><a name="b2398114455216"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p58716080"><a name="p58716080"></a><a name="p58716080"></a><strong id="b10233134514526"><a name="b10233134514526"></a><a name="b10233134514526"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row58682673"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p55676055"><a name="p55676055"></a><a name="p55676055"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p13466643"><a name="p13466643"></a><a name="p13466643"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p17056266"><a name="p17056266"></a><a name="p17056266"></a>Specifies the total number of domain names.</p>
</td>
</tr>
<tr id="row19288672"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p18878622"><a name="p18878622"></a><a name="p18878622"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p52773388"><a name="p52773388"></a><a name="p52773388"></a><a href="#table1272813819259">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p46786002"><a name="p46786002"></a><a name="p46786002"></a>Specifies the domain objects.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table1272813819259"></a>
<table><thead align="left"><tr id="row14733082258"><th class="cellrowborder" valign="top" width="25.247475252474754%" id="mcps1.2.4.1.1"><p id="p873817812512"><a name="p873817812512"></a><a name="p873817812512"></a><strong id="b178810741311"><a name="b178810741311"></a><a name="b178810741311"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.797420257974203%" id="mcps1.2.4.1.2"><p id="p137404817256"><a name="p137404817256"></a><a name="p137404817256"></a><strong id="b1703084272"><a name="b1703084272"></a><a name="b1703084272"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.95510448955104%" id="mcps1.2.4.1.3"><p id="p6742198152512"><a name="p6742198152512"></a><a name="p6742198152512"></a><strong id="b0452310191317"><a name="b0452310191317"></a><a name="b0452310191317"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1426410531637"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p1369552737"><a name="p1369552737"></a><a name="p1369552737"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p0711152337"><a name="p0711152337"></a><a name="p0711152337"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p2751752432"><a name="p2751752432"></a><a name="p2751752432"></a>Specifies the domain ID.</p>
</td>
</tr>
<tr id="row8264105312312"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p147919521435"><a name="p147919521435"></a><a name="p147919521435"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p7815521638"><a name="p7815521638"></a><a name="p7815521638"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p38415210312"><a name="p38415210312"></a><a name="p38415210312"></a>Specifies the returned domain name.</p>
</td>
</tr>
<tr id="row3264115315318"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p1796052839"><a name="p1796052839"></a><a name="p1796052839"></a>cname</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p0999524315"><a name="p0999524315"></a><a name="p0999524315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p510119526315"><a name="p510119526315"></a><a name="p510119526315"></a>Specifies the CNAME value.</p>
<p id="p91023521538"><a name="p91023521538"></a><a name="p91023521538"></a>For example, <strong id="b3437134725611"><a name="b3437134725611"></a><a name="b3437134725611"></a>efec1196267b41c399f2980ea4048517.waf.cloud.com</strong>.</p>
</td>
</tr>
<tr id="row52643531035"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p31074525318"><a name="p31074525318"></a><a name="p31074525318"></a>txt_code</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p1410914520313"><a name="p1410914520313"></a><a name="p1410914520313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p111112529312"><a name="p111112529312"></a><a name="p111112529312"></a>Specifies the TXT record. This parameter is returned only when <strong id="b3466131411515"><a name="b3466131411515"></a><a name="b3466131411515"></a>proxy</strong> is set to <strong id="b746681491519"><a name="b746681491519"></a><a name="b746681491519"></a>true</strong>.</p>
</td>
</tr>
<tr id="row62649531339"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p1111825213310"><a name="p1111825213310"></a><a name="p1111825213310"></a>sub_domain</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p161201552938"><a name="p161201552938"></a><a name="p161201552938"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p16122145214312"><a name="p16122145214312"></a><a name="p16122145214312"></a>Specifies the subdomain name. This parameter is returned only when <strong id="b837213240155"><a name="b837213240155"></a><a name="b837213240155"></a>proxy</strong> is set to <strong id="b7372102421512"><a name="b7372102421512"></a><a name="b7372102421512"></a>true</strong>.</p>
</td>
</tr>
<tr id="row226214539310"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p2012895215320"><a name="p2012895215320"></a><a name="p2012895215320"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p13130752838"><a name="p13130752838"></a><a name="p13130752838"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p513210521431"><a name="p513210521431"></a><a name="p513210521431"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row626216532033"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p413555219313"><a name="p413555219313"></a><a name="p413555219313"></a>protect_status</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p81381552331"><a name="p81381552331"></a><a name="p81381552331"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p114014521439"><a name="p114014521439"></a><a name="p114014521439"></a>Specifies the WAF mode.</p>
<a name="ul121411752134"></a><a name="ul121411752134"></a><ul id="ul121411752134"><li><span class="parmvalue" id="parmvalue6295174817531"><a name="parmvalue6295174817531"></a><a name="parmvalue6295174817531"></a><b>-1</b></span>: bypassed.</li><li><strong id="b1439174121611"><a name="b1439174121611"></a><a name="b1439174121611"></a>0</strong>: disabled.</li><li><strong id="b86264128168"><a name="b86264128168"></a><a name="b86264128168"></a>1</strong>: enabled.</li></ul>
</td>
</tr>
<tr id="row15262105318311"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p14150452034"><a name="p14150452034"></a><a name="p14150452034"></a>access_status</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p01506521136"><a name="p01506521136"></a><a name="p01506521136"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p171523521737"><a name="p171523521737"></a><a name="p171523521737"></a>Specifies whether a domain name is connected to WAF.</p>
<a name="ul111531252836"></a><a name="ul111531252836"></a><ul id="ul111531252836"><li><strong id="b7397116062"><a name="b7397116062"></a><a name="b7397116062"></a>0</strong>: The domain name is not connected to WAF.</li><li><strong id="b1181119914610"><a name="b1181119914610"></a><a name="b1181119914610"></a>1</strong>: The domain name is connected to WAF.</li></ul>
</td>
</tr>
<tr id="row726215531833"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p1021910521839"><a name="p1021910521839"></a><a name="p1021910521839"></a>proxy</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p16221155210314"><a name="p16221155210314"></a><a name="p16221155210314"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p4222185216320"><a name="p4222185216320"></a><a name="p4222185216320"></a>Specifies whether a proxy is configured.</p>
<a name="ul1222313528312"></a><a name="ul1222313528312"></a><ul id="ul1222313528312"><li><strong id="b41261645151720"><a name="b41261645151720"></a><a name="b41261645151720"></a>true</strong>: A proxy is configured.</li><li><strong id="b181681101818"><a name="b181681101818"></a><a name="b181681101818"></a>false</strong>: No proxy is configured.</li></ul>
</td>
</tr>
<tr id="row6262353438"><td class="cellrowborder" valign="top" width="25.247475252474754%" headers="mcps1.2.4.1.1 "><p id="p1423216523317"><a name="p1423216523317"></a><a name="p1423216523317"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="25.797420257974203%" headers="mcps1.2.4.1.2 "><p id="p123411522313"><a name="p123411522313"></a><a name="p123411522313"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="48.95510448955104%" headers="mcps1.2.4.1.3 "><p id="p17235165213314"><a name="p17235165213314"></a><a name="p17235165213314"></a>Specifies the time when a domain name is created.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1677820363290"></a>

**total**  with a value of  **2**  is used as an example.

Response example

```
{
    "total": 2,
    "items": [
        {
          "id": "388a7789d55b41d1918b3088a8f1e7f3",
          "hostname": "www.a.com",
          "cname": "3249d21e5eb34d21be12fdc817fcb67d.waf.cloud.com",
          "txt_code": "3249d21e5eb34d21be12fdc817fcb67d",
          "sub_domain": "3249d21e5eb34d21be12fdc817fcb67d.www.a.com",
          "policy_id": "xxxxxxxxxxxxxx",
          "protect_status": 0,
          "access_status": 0,
          "proxy": true,
          "timestamp": 1499817600
        }, 
       {
          "id": "296a7710d55b41d1918b3036a8f1e7e5",
          "hostname": "www.b.com",
          "cname": "efec1196267b41c399f2980ea4048517.waf.cloud.com",
          "policy_id": "xxxxxxxxxxxxxx",
          "protect_status": 1,
          "access_status": 1,
          "proxy": false,
          "timestamp": 1499817612
        }
     ]
}

```

## Status Code<a name="section53227215"></a>

[Table 4](#t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  4**  Status code

<a name="t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="af3c4073076f24eca88d94e3fa1effdc6"><a name="af3c4073076f24eca88d94e3fa1effdc6"></a><a name="af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="ada185614bba24140995b8123b3e9faa8"><a name="ada185614bba24140995b8123b3e9faa8"></a><a name="ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="a93f3895d44bb4226934cc626ac50e37b"><a name="a93f3895d44bb4226934cc626ac50e37b"></a><a name="a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

