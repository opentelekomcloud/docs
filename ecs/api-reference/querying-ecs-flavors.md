# Querying ECS Flavors<a name="EN-US_TOPIC_0065817705"></a>

## Function<a name="en-us_topic_0057973030_section20360452"></a>

This API is used to query available ECS flavors. After receiving the request, Nova uses nova-api to view the flavors from the database.

## URI<a name="en-us_topic_0057973030_section49026344"></a>

GET /v2/\{project\_id\}/flavors\{?minDisk,minRam,sort\_key,sort\_dir\}

GET /v2.1/\{project\_id\}/flavors\{?minDisk,minRam,sort\_key,sort\_dir\}

[Table 1](#en-us_topic_0057973030_table32475667)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="en-us_topic_0057973030_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973030_row44937496"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.29%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973030_row1664874"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973030_p637140"><a name="en-us_topic_0057973030_p637140"></a><a name="en-us_topic_0057973030_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973030_p51608407"><a name="en-us_topic_0057973030_p51608407"></a><a name="en-us_topic_0057973030_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

Parameters in the following table can be used as URI parameters to filter query results. Usage: /v2/\{project\_id\}/flavors?minDisk=\{minDisk\}&minRam=\{minRam\}

[Table 2](#en-us_topic_0057973030_table714692)  describes the query parameters.

**Table  2**  Query parameters

<a name="en-us_topic_0057973030_table714692"></a>
<table><thead align="left"><tr id="en-us_topic_0057973030_row26530596"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973030_p1494644"><a name="en-us_topic_0057973030_p1494644"></a><a name="en-us_topic_0057973030_p1494644"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.51%" id="mcps1.2.5.1.2"><p id="p07066410411"><a name="p07066410411"></a><a name="p07066410411"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.13%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973030_p53957349"><a name="en-us_topic_0057973030_p53957349"></a><a name="en-us_topic_0057973030_p53957349"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.44%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973030_p14912584"><a name="en-us_topic_0057973030_p14912584"></a><a name="en-us_topic_0057973030_p14912584"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973030_row67068683"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973030_p63854222"><a name="en-us_topic_0057973030_p63854222"></a><a name="en-us_topic_0057973030_p63854222"></a>minDisk</p>
</td>
<td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.2.5.1.2 "><p id="p2070684134111"><a name="p2070684134111"></a><a name="p2070684134111"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973030_p4809465"><a name="en-us_topic_0057973030_p4809465"></a><a name="en-us_topic_0057973030_p4809465"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973030_p13737385"><a name="en-us_topic_0057973030_p13737385"></a><a name="en-us_topic_0057973030_p13737385"></a>Specifies the minimum disk specification in the unit of GB. Only the ECSs with the disk specification greater than or equal to the minimum specification can be queried.</p>
</td>
</tr>
<tr id="en-us_topic_0057973030_row56527608"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973030_p15333556"><a name="en-us_topic_0057973030_p15333556"></a><a name="en-us_topic_0057973030_p15333556"></a>minRam</p>
</td>
<td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.2.5.1.2 "><p id="p197071941144111"><a name="p197071941144111"></a><a name="p197071941144111"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973030_p34058557"><a name="en-us_topic_0057973030_p34058557"></a><a name="en-us_topic_0057973030_p34058557"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973030_p52787924"><a name="en-us_topic_0057973030_p52787924"></a><a name="en-us_topic_0057973030_p52787924"></a>Specifies the minimum RAM in the unit of MB. Only the ECSs with the RAM specification greater than or equal to the minimum specification can be queried.</p>
</td>
</tr>
<tr id="en-us_topic_0057973030_row35021432"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973030_p18163716"><a name="en-us_topic_0057973030_p18163716"></a><a name="en-us_topic_0057973030_p18163716"></a>sort_key</p>
</td>
<td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.2.5.1.2 "><p id="p157074413412"><a name="p157074413412"></a><a name="p157074413412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973030_p61974917"><a name="en-us_topic_0057973030_p61974917"></a><a name="en-us_topic_0057973030_p61974917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.5.1.4 "><p id="p1085012527405"><a name="p1085012527405"></a><a name="p1085012527405"></a>Indicates a sorting field, the default value of which is <strong id="b842352706101459"><a name="b842352706101459"></a><a name="b842352706101459"></a>flavorid</strong>.</p>
<p id="en-us_topic_0057973030_p4829829"><a name="en-us_topic_0057973030_p4829829"></a><a name="en-us_topic_0057973030_p4829829"></a>The value of this parameter can also be <strong id="b842352706101549"><a name="b842352706101549"></a><a name="b842352706101549"></a>name</strong>, <strong id="b842352706101555"><a name="b842352706101555"></a><a name="b842352706101555"></a>memory_mb</strong>, <strong id="b842352706101622"><a name="b842352706101622"></a><a name="b842352706101622"></a>vcpus</strong>, <strong id="b842352706101625"><a name="b842352706101625"></a><a name="b842352706101625"></a>root_gb</strong>, or <strong id="b842352706144441"><a name="b842352706144441"></a><a name="b842352706144441"></a>flavorid</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973030_row43468468"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973030_p31284983"><a name="en-us_topic_0057973030_p31284983"></a><a name="en-us_topic_0057973030_p31284983"></a>sort_dir</p>
</td>
<td class="cellrowborder" valign="top" width="17.51%" headers="mcps1.2.5.1.2 "><p id="p1270710419411"><a name="p1270710419411"></a><a name="p1270710419411"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973030_p51055732"><a name="en-us_topic_0057973030_p51055732"></a><a name="en-us_topic_0057973030_p51055732"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973030_p36319798"><a name="en-us_topic_0057973030_p36319798"></a><a name="en-us_topic_0057973030_p36319798"></a>Specifies the ascending (<strong id="b740796858102558"><a name="b740796858102558"></a><a name="b740796858102558"></a>asc</strong>) or descending (<strong id="b67906925910263"><a name="b67906925910263"></a><a name="b67906925910263"></a>desc</strong>) sorting. The default value is <strong id="b274442023102145"><a name="b274442023102145"></a><a name="b274442023102145"></a>asc</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section16555112313153"></a>

None

## Response<a name="en-us_topic_0057973030_section9063995"></a>

[Table 4](#en-us_topic_0057973030_table56222540)  describes the response parameters.

**Table  3**  Response parameters

<a name="table23477058"></a>
<table><thead align="left"><tr id="row2792905"><th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.1"><p id="p14248253101715"><a name="p14248253101715"></a><a name="p14248253101715"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.659999999999998%" id="mcps1.2.4.1.2"><p id="p224810537176"><a name="p224810537176"></a><a name="p224810537176"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.61%" id="mcps1.2.4.1.3"><p id="p17248653121717"><a name="p17248653121717"></a><a name="p17248653121717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9994955"><td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.1 "><p id="p4284989"><a name="p4284989"></a><a name="p4284989"></a>flavors</p>
</td>
<td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.2.4.1.2 "><p id="p62312200"><a name="p62312200"></a><a name="p62312200"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.61%" headers="mcps1.2.4.1.3 "><p id="p127029403320"><a name="p127029403320"></a><a name="p127029403320"></a>Specifies ECS flavors. For details, see <a href="#en-us_topic_0057973030_table56222540">Table 4</a>.</p>
</td>
</tr>
<tr id="row19878185610436"><td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.1 "><p id="p187945610434"><a name="p187945610434"></a><a name="p187945610434"></a>flavors_links</p>
</td>
<td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.2.4.1.2 "><p id="p0953191316483"><a name="p0953191316483"></a><a name="p0953191316483"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.61%" headers="mcps1.2.4.1.3 "><p id="p5483191813483"><a name="p5483191813483"></a><a name="p5483191813483"></a>Specifies data links for querying the next pages in pagination query. For details, see <a href="#en-us_topic_0057973030_table15913898194628">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **flavors**  field description

<a name="en-us_topic_0057973030_table56222540"></a>
<table><thead align="left"><tr id="en-us_topic_0057973030_row14829771"><th class="cellrowborder" valign="top" width="17.7%" id="mcps1.2.4.1.1"><p id="p110452114597"><a name="p110452114597"></a><a name="p110452114597"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.58%" id="mcps1.2.4.1.2"><p id="p71044217595"><a name="p71044217595"></a><a name="p71044217595"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.72%" id="mcps1.2.4.1.3"><p id="p15104102175910"><a name="p15104102175910"></a><a name="p15104102175910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973030_row37642492"><td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973030_p29143010"><a name="en-us_topic_0057973030_p29143010"></a><a name="en-us_topic_0057973030_p29143010"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.58%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973030_p11773580"><a name="en-us_topic_0057973030_p11773580"></a><a name="en-us_topic_0057973030_p11773580"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973030_p4157774"><a name="en-us_topic_0057973030_p4157774"></a><a name="en-us_topic_0057973030_p4157774"></a>Specifies the flavor ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973030_row37419966"><td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973030_p11118435"><a name="en-us_topic_0057973030_p11118435"></a><a name="en-us_topic_0057973030_p11118435"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="15.58%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973030_p28178065"><a name="en-us_topic_0057973030_p28178065"></a><a name="en-us_topic_0057973030_p28178065"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973030_p58474149"><a name="en-us_topic_0057973030_p58474149"></a><a name="en-us_topic_0057973030_p58474149"></a>Specifies the shortcut link of the ECS flavor.</p>
<p id="en-us_topic_0057973030_p191091358102214"><a name="en-us_topic_0057973030_p191091358102214"></a><a name="en-us_topic_0057973030_p191091358102214"></a>For details, see <a href="#en-us_topic_0057973030_table15913898194628">Table 5</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973030_row56505297"><td class="cellrowborder" valign="top" width="17.7%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973030_p13526335"><a name="en-us_topic_0057973030_p13526335"></a><a name="en-us_topic_0057973030_p13526335"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.58%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973030_p21891354"><a name="en-us_topic_0057973030_p21891354"></a><a name="en-us_topic_0057973030_p21891354"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973030_p16205877"><a name="en-us_topic_0057973030_p16205877"></a><a name="en-us_topic_0057973030_p16205877"></a>Specifies the flavor name.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **links**  field description

<a name="en-us_topic_0057973030_table15913898194628"></a>
<table><thead align="left"><tr id="en-us_topic_0057973030_row37608132194628"><th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.4.1.1"><p id="p4900154420113"><a name="p4900154420113"></a><a name="p4900154420113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.72%" id="mcps1.2.4.1.2"><p id="p29006449111"><a name="p29006449111"></a><a name="p29006449111"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.67%" id="mcps1.2.4.1.3"><p id="p139153449113"><a name="p139153449113"></a><a name="p139153449113"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973030_row17692319194628"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973030_p23791739194628"><a name="en-us_topic_0057973030_p23791739194628"></a><a name="en-us_topic_0057973030_p23791739194628"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="15.72%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973030_p48082703194628"><a name="en-us_topic_0057973030_p48082703194628"></a><a name="en-us_topic_0057973030_p48082703194628"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973030_p2384900194628"><a name="en-us_topic_0057973030_p2384900194628"></a><a name="en-us_topic_0057973030_p2384900194628"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973030_row21464106194628"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973030_p60871059194628"><a name="en-us_topic_0057973030_p60871059194628"></a><a name="en-us_topic_0057973030_p60871059194628"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="15.72%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973030_p31608752194628"><a name="en-us_topic_0057973030_p31608752194628"></a><a name="en-us_topic_0057973030_p31608752194628"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973030_p10172138194628"><a name="en-us_topic_0057973030_p10172138194628"></a><a name="en-us_topic_0057973030_p10172138194628"></a>Specifies the shortcut link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973030_section14467097"></a>

```
GET https://{endpoint}/v2/743b4c0428d94531b9f2add666642e6b/flavors
GET https://{endpoint}/v2.1/743b4c0428d94531b9f2add666642e6b/flavors
```

## Example Response<a name="section945413916318"></a>

```
{
    "flavors": [
        {
            "id": "c2.medium",
            "links": [
                {
                    "href": "https://compute.region.xxx.com/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/c2.medium",
                    "rel": "self"
                },
                {
                    "href": "https://compute.region.xxx.com/743b4c0428d94531b9f2add666642e6b/flavors/c2.medium",
                    "rel": "bookmark"
                }
            ],
            "name": "c2.medium"
        },
        {
            "id": "c2.xlarge",
            "links": [
                {
                    "href": "https://compute.region.xxx.com/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/c2.xlarge",
                    "rel": "self"
                },
                {
                    "href": "https://compute.region.x.com/743b4c0428d94531b9f2add666642e6b/flavors/c2.xlarge",
                    "rel": "bookmark"
                }
            ],
            "name": "c2.xlarge"
        }
    ]
}     
```

## Returned Values<a name="en-us_topic_0057973030_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

