# Querying a Specified SSH Key Pair<a name="EN-US_TOPIC_0020212677"></a>

## Function<a name="section62942996"></a>

This API is used to query a specified SSH key pair based on the SSH key pair name.

## URI<a name="section29616056"></a>

GET /v2/\{project\_id\}/os-keypairs/\{keypair\_name\}

GET /v2.1/\{project\_id\}/os-keypairs/\{keypair\_name\}

[Table 1](#table51931981)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table51931981"></a>
<table><thead align="left"><tr id="row62634432"><th class="cellrowborder" valign="top" width="19.23%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="63.6%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row22724462"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p28742116"><a name="p28742116"></a><a name="p28742116"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p46410096"><a name="p46410096"></a><a name="p46410096"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="63.6%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row10092597"><td class="cellrowborder" valign="top" width="19.23%" headers="mcps1.2.4.1.1 "><p id="p12194051"><a name="p12194051"></a><a name="p12194051"></a>keypair_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p48194049"><a name="p48194049"></a><a name="p48194049"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="63.6%" headers="mcps1.2.4.1.3 "><p id="p11403863"><a name="p11403863"></a><a name="p11403863"></a>Specifies the key pair name.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section65217919"></a>

None

## Response<a name="section50090360"></a>

[Table 2](#table49096623)  describes the response parameters.

**Table  2**  Response parameters

<a name="table49096623"></a>
<table><thead align="left"><tr id="row20553506"><th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.4.1.1"><p id="p52863116"><a name="p52863116"></a><a name="p52863116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.11%" id="mcps1.2.4.1.2"><p id="p16299242"><a name="p16299242"></a><a name="p16299242"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.41%" id="mcps1.2.4.1.3"><p id="p45170224"><a name="p45170224"></a><a name="p45170224"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row31470474"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.4.1.1 "><p id="p66080459"><a name="p66080459"></a><a name="p66080459"></a>keypair</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p30630481"><a name="p30630481"></a><a name="p30630481"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.41%" headers="mcps1.2.4.1.3 "><p id="p49478440"><a name="p49478440"></a><a name="p49478440"></a>Specifies the SSH key pair. For details, see <a href="#table32323009">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **keypair**  field description

<a name="table32323009"></a>
<table><thead align="left"><tr id="row56122340"><th class="cellrowborder" valign="top" width="16.53%" id="mcps1.2.4.1.1"><p id="p3579112043319"><a name="p3579112043319"></a><a name="p3579112043319"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.14%" id="mcps1.2.4.1.2"><p id="p1457914201333"><a name="p1457914201333"></a><a name="p1457914201333"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.33%" id="mcps1.2.4.1.3"><p id="p8579112033320"><a name="p8579112033320"></a><a name="p8579112033320"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1091845"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p21330650"><a name="p21330650"></a><a name="p21330650"></a>public_key</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p28418246"><a name="p28418246"></a><a name="p28418246"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p47371280"><a name="p47371280"></a><a name="p47371280"></a>Specifies information about the public key.</p>
</td>
</tr>
<tr id="row23688339"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p39707298"><a name="p39707298"></a><a name="p39707298"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p2977371"><a name="p2977371"></a><a name="p2977371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p23019892"><a name="p23019892"></a><a name="p23019892"></a>Specifies the key pair name.</p>
</td>
</tr>
<tr id="row19588278171758"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p3411854217180"><a name="p3411854217180"></a><a name="p3411854217180"></a>fingerprint</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p1213855517180"><a name="p1213855517180"></a><a name="p1213855517180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p5774567417180"><a name="p5774567417180"></a><a name="p5774567417180"></a>Specifies fingerprint information about the key pair.</p>
</td>
</tr>
<tr id="row5852437"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p4285383"><a name="p4285383"></a><a name="p4285383"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p64894876"><a name="p64894876"></a><a name="p64894876"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p63724816"><a name="p63724816"></a><a name="p63724816"></a>Specifies the time when the key pair was created.</p>
</td>
</tr>
<tr id="row36652435"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p16057296"><a name="p16057296"></a><a name="p16057296"></a>deleted</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p58113810"><a name="p58113810"></a><a name="p58113810"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p19274797"><a name="p19274797"></a><a name="p19274797"></a>Specifies whether a key pair has been deleted.</p>
<a name="ul1594190135612"></a><a name="ul1594190135612"></a><ul id="ul1594190135612"><li><strong id="b842352706154437"><a name="b842352706154437"></a><a name="b842352706154437"></a>true</strong>: indicates that the key has been deleted.</li><li><strong id="b842352706154455"><a name="b842352706154455"></a><a name="b842352706154455"></a>false</strong>: indicates that the key is not deleted.</li></ul>
</td>
</tr>
<tr id="row39255446"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p25574597"><a name="p25574597"></a><a name="p25574597"></a>deleted_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p22776773"><a name="p22776773"></a><a name="p22776773"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p28378258"><a name="p28378258"></a><a name="p28378258"></a>Specifies the time when the key pair was deleted.</p>
</td>
</tr>
<tr id="row54077734"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p18220335"><a name="p18220335"></a><a name="p18220335"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p22737212"><a name="p22737212"></a><a name="p22737212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p66647176"><a name="p66647176"></a><a name="p66647176"></a>Specifies the key pair ID.</p>
</td>
</tr>
<tr id="row62953674"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p66082838"><a name="p66082838"></a><a name="p66082838"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p46241663"><a name="p46241663"></a><a name="p46241663"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p21523158"><a name="p21523158"></a><a name="p21523158"></a>Specifies the time when the key pair was updated.</p>
</td>
</tr>
<tr id="row59490699"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p54017281"><a name="p54017281"></a><a name="p54017281"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p5473047"><a name="p5473047"></a><a name="p5473047"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p30428869"><a name="p30428869"></a><a name="p30428869"></a>Specifies information about the user to which the key pair belongs.</p>
</td>
</tr>
<tr id="row462920453538"><td class="cellrowborder" valign="top" width="16.53%" headers="mcps1.2.4.1.1 "><p id="p199751011803"><a name="p199751011803"></a><a name="p199751011803"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.14%" headers="mcps1.2.4.1.2 "><p id="p139751111204"><a name="p139751111204"></a><a name="p139751111204"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.33%" headers="mcps1.2.4.1.3 "><p id="p1097512112013"><a name="p1097512112013"></a><a name="p1097512112013"></a>Specifies the key type, which is <strong id="b84235270619443"><a name="b84235270619443"></a><a name="b84235270619443"></a>ssh</strong> by default.</p>
<p id="p144811212011"><a name="p144811212011"></a><a name="p144811212011"></a>This field is supported in microversions later than 2.2.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section4978145455016"></a>

```
GET https://{endpoint}/v2/{project_id}/os-keypairs/{keypair_name}
GET https://{endpoint}/v2.1/{project_id}/os-keypairs/{keypair_name}
```

## Example Response<a name="section13613112651113"></a>

```
{
    "keypair": {
        "created_at": "2014-05-07T12:06:13.681238",
        "deleted": false,
        "deleted_at": null,
        "fingerprint": "9d:00:f4:d7:26:6e:52:06:4c:c1:d3:1d:fd:06:66:01",
        "id": 1,
        "name": "keypair-3582d8b7-e588-4aad-b7f7-f4e76f0e4314",
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDYJrTVpcMwFqQy/oMvtUSRofZdSRHEwrsX8AYkRvn2ZnCXM+b6+GZ2NQuuWj+ocznlnwiGFQDsL/yeE+/kurqcPJFKKp60mToXIMyzioFxW88fJtwEWawHKAclbHWpR1t4fQ4DS+/sIbX/Yd9btlVQ2tpQjodGDbM9Tr9/+/3i6rcR+EoLqmbgCgAiGiVV6VbM2Zx79yUwd+GnQejHX8BlYZoOjCnt3NREsITcmWE9FVFy6TnLmahs3FkEO/QGgWGkaohAJlsgaVvSWGgDn2AujKYwyDokK3dXyeX3m2Vmc3ejiqPa/C4nRrCOlko5nSgV/9IXRx1ERImsqZnE9usB Generated-by-Nova\n",
        "updated_at": null,
        "user_id": "fake"
    }
}
```

## Returned Values<a name="section48160062"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

