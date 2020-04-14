# Obtaining the List of Instance Flavors<a name="css_03_0023"></a>

## Function<a name="section162880126447"></a>

This API is used to query and display the IDs of supported instance flavors.

## URI<a name="section1928871264412"></a>

```
GET /v1.0/{project_id}/flavors
```

**Table  1**  Parameter description

<a name="table13042122448"></a>
<table><thead align="left"><tr id="row19460141264413"><th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.1"><p id="p7460181264412"><a name="p7460181264412"></a><a name="p7460181264412"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.740000000000002%" id="mcps1.2.5.1.2"><p id="p2460121274417"><a name="p2460121274417"></a><a name="p2460121274417"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.56%" id="mcps1.2.5.1.3"><p id="p134601612144419"><a name="p134601612144419"></a><a name="p134601612144419"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.4"><p id="p1460712184418"><a name="p1460712184418"></a><a name="p1460712184418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row84601812184412"><td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.1 "><p id="p346041224419"><a name="p346041224419"></a><a name="p346041224419"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p184601712194415"><a name="p184601712194415"></a><a name="p184601712194415"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p194601412174416"><a name="p194601412174416"></a><a name="p194601412174416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.4 "><p id="p1836110010124"><a name="p1836110010124"></a><a name="p1836110010124"></a>Project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section6319121215446"></a>

None

## Response<a name="section2319712124420"></a>

[Table 2](#table347318359446)  describes the response parameters.

**Table  2**  Parameter description

<a name="table347318359446"></a>
<table><thead align="left"><tr id="row7473435194418"><th class="cellrowborder" valign="top" width="22.19221922192219%" id="mcps1.2.4.1.1"><p id="p74739353448"><a name="p74739353448"></a><a name="p74739353448"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.352635263526352%" id="mcps1.2.4.1.2"><p id="p14731535104420"><a name="p14731535104420"></a><a name="p14731535104420"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.45514551455145%" id="mcps1.2.4.1.3"><p id="p11473113513444"><a name="p11473113513444"></a><a name="p11473113513444"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1247323510445"><td class="cellrowborder" valign="top" width="22.19221922192219%" headers="mcps1.2.4.1.1 "><p id="p5571939455"><a name="p5571939455"></a><a name="p5571939455"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="26.352635263526352%" headers="mcps1.2.4.1.2 "><p id="p5575317458"><a name="p5575317458"></a><a name="p5575317458"></a>Array of versions objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.45514551455145%" headers="mcps1.2.4.1.3 "><p id="p5577364514"><a name="p5577364514"></a><a name="p5577364514"></a>List of engine versions. For details, see <a href="#table25411438165118">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **versions**  field description

<a name="table25411438165118"></a>
<table><thead align="left"><tr id="row454143845111"><th class="cellrowborder" valign="top" width="22.81228122812281%" id="mcps1.2.4.1.1"><p id="p18541838105118"><a name="p18541838105118"></a><a name="p18541838105118"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.882688268826882%" id="mcps1.2.4.1.2"><p id="p154133845118"><a name="p154133845118"></a><a name="p154133845118"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.305030503050304%" id="mcps1.2.4.1.3"><p id="p954153825112"><a name="p954153825112"></a><a name="p954153825112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row654183895116"><td class="cellrowborder" valign="top" width="22.81228122812281%" headers="mcps1.2.4.1.1 "><p id="p05416384511"><a name="p05416384511"></a><a name="p05416384511"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="26.882688268826882%" headers="mcps1.2.4.1.2 "><p id="p1854103820518"><a name="p1854103820518"></a><a name="p1854103820518"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.305030503050304%" headers="mcps1.2.4.1.3 "><p id="p18541638115116"><a name="p18541638115116"></a><a name="p18541638115116"></a>Engine version. The default version is 6.2.3.</p>
</td>
</tr>
<tr id="row14541103813513"><td class="cellrowborder" valign="top" width="22.81228122812281%" headers="mcps1.2.4.1.1 "><p id="p175415381511"><a name="p175415381511"></a><a name="p175415381511"></a>flavors</p>
</td>
<td class="cellrowborder" valign="top" width="26.882688268826882%" headers="mcps1.2.4.1.2 "><p id="p05411338165117"><a name="p05411338165117"></a><a name="p05411338165117"></a>Array of flavors objects</p>
</td>
<td class="cellrowborder" valign="top" width="50.305030503050304%" headers="mcps1.2.4.1.3 "><p id="p354113814516"><a name="p354113814516"></a><a name="p354113814516"></a>Flavor list For details, see <a href="#table5319191204412">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **flavors**  field description

<a name="table5319191204412"></a>
<table><thead align="left"><tr id="row174761812154414"><th class="cellrowborder" valign="top" width="24.062406240624064%" id="mcps1.2.4.1.1"><p id="p5476181212444"><a name="p5476181212444"></a><a name="p5476181212444"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.982598259825977%" id="mcps1.2.4.1.2"><p id="p1047616121445"><a name="p1047616121445"></a><a name="p1047616121445"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.95499549954995%" id="mcps1.2.4.1.3"><p id="p13476012154420"><a name="p13476012154420"></a><a name="p13476012154420"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17162174810547"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p916218486541"><a name="p916218486541"></a><a name="p916218486541"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="25.982598259825977%" headers="mcps1.2.4.1.2 "><p id="p31621148125410"><a name="p31621148125410"></a><a name="p31621148125410"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.95499549954995%" headers="mcps1.2.4.1.3 "><p id="p4162194885420"><a name="p4162194885420"></a><a name="p4162194885420"></a>Memory size of an instance.</p>
</td>
</tr>
<tr id="row74749439549"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p114741743145412"><a name="p114741743145412"></a><a name="p114741743145412"></a>cpu</p>
</td>
<td class="cellrowborder" valign="top" width="25.982598259825977%" headers="mcps1.2.4.1.2 "><p id="p147474345414"><a name="p147474345414"></a><a name="p147474345414"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.95499549954995%" headers="mcps1.2.4.1.3 "><p id="p13474124319547"><a name="p13474124319547"></a><a name="p13474124319547"></a>Number of vCPUs of an instance.</p>
</td>
</tr>
<tr id="row16177639165413"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p9177339165420"><a name="p9177339165420"></a><a name="p9177339165420"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25.982598259825977%" headers="mcps1.2.4.1.2 "><p id="p71772039185413"><a name="p71772039185413"></a><a name="p71772039185413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.95499549954995%" headers="mcps1.2.4.1.3 "><p id="p1417713985413"><a name="p1417713985413"></a><a name="p1417713985413"></a>Flavor name.</p>
</td>
</tr>
<tr id="row090371619575"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p1990311645710"><a name="p1990311645710"></a><a name="p1990311645710"></a>region</p>
</td>
<td class="cellrowborder" valign="top" width="25.982598259825977%" headers="mcps1.2.4.1.2 "><p id="p39033166571"><a name="p39033166571"></a><a name="p39033166571"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.95499549954995%" headers="mcps1.2.4.1.3 "><p id="p79039161579"><a name="p79039161579"></a><a name="p79039161579"></a>AZ</p>
</td>
</tr>
<tr id="row2068439175717"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p16684119145711"><a name="p16684119145711"></a><a name="p16684119145711"></a>diskrange</p>
</td>
<td class="cellrowborder" valign="top" width="25.982598259825977%" headers="mcps1.2.4.1.2 "><p id="p196843925717"><a name="p196843925717"></a><a name="p196843925717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.95499549954995%" headers="mcps1.2.4.1.3 "><p id="p10684119125713"><a name="p10684119125713"></a><a name="p10684119125713"></a>Disk capacity range of an instance.</p>
</td>
</tr>
<tr id="row18476111274413"><td class="cellrowborder" valign="top" width="24.062406240624064%" headers="mcps1.2.4.1.1 "><p id="p124764126445"><a name="p124764126445"></a><a name="p124764126445"></a>flavor_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.982598259825977%" headers="mcps1.2.4.1.2 "><p id="p94766127449"><a name="p94766127449"></a><a name="p94766127449"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.95499549954995%" headers="mcps1.2.4.1.3 "><p id="p104761512194419"><a name="p104761512194419"></a><a name="p104761512194419"></a>ID of a flavor.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section1154041616351"></a>

Example request

```
GET /v1.0/6204a5bd270343b5885144cf9c8c158d/flavors
```

Example response

```
{
  "versions": [
    {
      "version": "6.2.3",
      "flavors": [
        {
          "cpu": 1,
          "ram": 8,
          "name": "css.medium.8",
          "region": "eu-de",
          "diskrange": "40,640",
          "flavor_id": "6b6c0bcf-750d-4f8a-b6f5-c45a143f5198"
        },
        {
          "cpu": 2,
          "ram": 16,
          "name": "css.large.8",
          "region": "eu-de",
          "diskrange": "40,1280",
          "flavor_id": "d373e339-3cf4-4c00-9739-2259e9f3ec16"
        },
        {
          "cpu": 4,
          "ram": 32,
          "name": "css.xlarge.8",
          "region": "eu-de",
          "diskrange": "40,2560",
          "flavor_id": "2d8daf1b-873f-4c2e-a7b9-2f9cbcf2f213"
        },
        {
          "cpu": 8,
          "ram": 64,
          "name": "css.2xlarge.8",
          "region": "eu-de",
          "diskrange": "80,5120",
          "flavor_id": "b3d33ec6-d58a-40f0-aa51-4f671ce64b2a"
        },
        {
          "cpu": 16,
          "ram": 128,
          "name": "css.4xlarge.8",
          "region": "eu-de",
          "diskrange": "160,10240",
          "flavor_id": "f74419ca-bc91-4558-b4e2-90eeefb37c6e"
        }
      ]
    }
  ]
}
```

## Status Code<a name="section87962546391"></a>

[Table 5](#table12321369178)  describes the status code.

**Table  5**  Status code

<a name="table12321369178"></a>
<table><thead align="left"><tr id="css_03_0018_row1972183521418"><th class="cellrowborder" valign="top" width="15.939999999999998%" id="mcps1.2.4.1.1"><p id="css_03_0018_p14560134151414"><a name="css_03_0018_p14560134151414"></a><a name="css_03_0018_p14560134151414"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="31.04%" id="mcps1.2.4.1.2"><p id="css_03_0018_p5563194141411"><a name="css_03_0018_p5563194141411"></a><a name="css_03_0018_p5563194141411"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.02%" id="mcps1.2.4.1.3"><p id="css_03_0018_p256616411143"><a name="css_03_0018_p256616411143"></a><a name="css_03_0018_p256616411143"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0018_row129720356144"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p1957004131410"><a name="css_03_0018_p1957004131410"></a><a name="css_03_0018_p1957004131410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p165731141171419"><a name="css_03_0018_p165731141171419"></a><a name="css_03_0018_p165731141171419"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p65778413148"><a name="css_03_0018_p65778413148"></a><a name="css_03_0018_p65778413148"></a>Invalid request.</p>
<p id="css_03_0018_p1557974171415"><a name="css_03_0018_p1557974171415"></a><a name="css_03_0018_p1557974171415"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row8972103517147"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p75841441191410"><a name="css_03_0018_p75841441191410"></a><a name="css_03_0018_p75841441191410"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p258716416142"><a name="css_03_0018_p258716416142"></a><a name="css_03_0018_p258716416142"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p15589154118141"><a name="css_03_0018_p15589154118141"></a><a name="css_03_0018_p15589154118141"></a>The requested resource cannot be found.</p>
<p id="css_03_0018_p14590164151410"><a name="css_03_0018_p14590164151410"></a><a name="css_03_0018_p14590164151410"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row297223511416"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p13595164131416"><a name="css_03_0018_p13595164131416"></a><a name="css_03_0018_p13595164131416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p9598741131416"><a name="css_03_0018_p9598741131416"></a><a name="css_03_0018_p9598741131416"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p659994115146"><a name="css_03_0018_p659994115146"></a><a name="css_03_0018_p659994115146"></a>The request is processed successfully.</p>
</td>
</tr>
</tbody>
</table>

