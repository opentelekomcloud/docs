# Querying Subnet Pools<a name="vpc_subnetpools_0002"></a>

## Function<a name="section47928120"></a>

This API is used to query subnet pools. Pagination query is supported. 

## URI<a name="section28699899"></a>

GET /v2.0/subnetpools

Example:

```
GET https://{Endpoint}/v2.0/subnetpools?fields=id&fields=name&fields=prefixes&fields=default_prefixlen&fields=address_scope_id&fields=is_default
```

Example of querying subnet pools by page

```
GET https://{Endpoint}/v2.0/subnetpools?limit=2&marker=03f761e6-eee0-43fc-a921-8acf64c14988&page_reverse=False
```

## Request Message<a name="section42990474"></a>

None

## Response Message<a name="section51369953"></a>

**Table  1**  Response parameter

<a name="table51277242"></a>
<table><thead align="left"><tr id="row64740644"><th class="cellrowborder" valign="top" width="23.122312231223123%" id="mcps1.2.4.1.1"><p id="p9500791"><a name="p9500791"></a><a name="p9500791"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.552555255525554%" id="mcps1.2.4.1.2"><p id="p31366578"><a name="p31366578"></a><a name="p31366578"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.325132513251326%" id="mcps1.2.4.1.3"><p id="p40344834"><a name="p40344834"></a><a name="p40344834"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46706151"><td class="cellrowborder" valign="top" width="23.122312231223123%" headers="mcps1.2.4.1.1 "><p id="p25101909"><a name="p25101909"></a><a name="p25101909"></a>subnetpools</p>
</td>
<td class="cellrowborder" valign="top" width="25.552555255525554%" headers="mcps1.2.4.1.2 "><p id="p19988723"><a name="p19988723"></a><a name="p19988723"></a>Array of <a href="#table149662441462">subnetpool</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.325132513251326%" headers="mcps1.2.4.1.3 "><p id="p15291872"><a name="p15291872"></a><a name="p15291872"></a>Specifies the subnet pool list. For details, see <a href="#table149662441462">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **subnetpool**  objects

<a name="table149662441462"></a>
<table><thead align="left"><tr id="row496617442612"><th class="cellrowborder" valign="top" width="28.29%" id="mcps1.2.4.1.1"><p id="p1596613445611"><a name="p1596613445611"></a><a name="p1596613445611"></a><strong id="b1869153712285"><a name="b1869153712285"></a><a name="b1869153712285"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.950000000000001%" id="mcps1.2.4.1.2"><p id="p49667449616"><a name="p49667449616"></a><a name="p49667449616"></a><strong id="b19678388280"><a name="b19678388280"></a><a name="b19678388280"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.76%" id="mcps1.2.4.1.3"><p id="p8966144413616"><a name="p8966144413616"></a><a name="p8966144413616"></a><strong id="b127971339152817"><a name="b127971339152817"></a><a name="b127971339152817"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28303131105515"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p2014344105614"><a name="p2014344105614"></a><a name="p2014344105614"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p28944191105614"><a name="p28944191105614"></a><a name="p28944191105614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p53796361105614"><a name="p53796361105614"></a><a name="p53796361105614"></a>Specifies the subnet pool ID.</p>
<p id="p1089535311426"><a name="p1089535311426"></a><a name="p1089535311426"></a>This parameter is not mandatory when you query subnet pools.</p>
</td>
</tr>
<tr id="row1196634410618"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p696615445611"><a name="p696615445611"></a><a name="p696615445611"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p3966104412620"><a name="p3966104412620"></a><a name="p3966104412620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p89666442613"><a name="p89666442613"></a><a name="p89666442613"></a>Specifies the subnet pool name.</p>
</td>
</tr>
<tr id="row9772661105515"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p49939441105624"><a name="p49939441105624"></a><a name="p49939441105624"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p18562940105624"><a name="p18562940105624"></a><a name="p18562940105624"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p682749310257"><a name="p682749310257"></a><a name="p682749310257"></a>Specifies the IP address version.</p>
<p id="p33352482102727"><a name="p33352482102727"></a><a name="p33352482102727"></a>Only IPv4 address is supported.</p>
</td>
</tr>
<tr id="row89665441569"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p79664442613"><a name="p79664442613"></a><a name="p79664442613"></a>default_quota</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p496616449616"><a name="p496616449616"></a><a name="p496616449616"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p7968244361"><a name="p7968244361"></a><a name="p7968244361"></a>Specifies the upper limit of the prefix space that can be allocated from the subnet pool to the subnet. For IPv4 subnet pools, default_quota is measured in units of /32. For IPv6 subnet pools, default_quota is measured in units of /64.</p>
</td>
</tr>
<tr id="row157121839115912"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row2067783695917"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p11508184345913"><a name="p11508184345913"></a><a name="p11508184345913"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p1651534311599"><a name="p1651534311599"></a><a name="p1651534311599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p552334314592"><a name="p552334314592"></a><a name="p552334314592"></a>Specifies the time (UTC) when the subnet pool is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i39934423014"><a name="i39934423014"></a><a name="i39934423014"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1428916334597"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p15531114325914"><a name="p15531114325914"></a><a name="p15531114325914"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p853513432597"><a name="p853513432597"></a><a name="p853513432597"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p1954364325913"><a name="p1954364325913"></a><a name="p1954364325913"></a>Specifies the time (UTC) when the subnet pool rule is updated.</p>
<p id="p21391133101715"><a name="p21391133101715"></a><a name="p21391133101715"></a>Format: <em id="i19384122308"><a name="i19384122308"></a><a name="i19384122308"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1796820448610"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p296834417616"><a name="p296834417616"></a><a name="p296834417616"></a>prefixes</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p187776111514"><a name="p187776111514"></a><a name="p187776111514"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p1496884418618"><a name="p1496884418618"></a><a name="p1496884418618"></a>Specifies a list of subnet prefixes that are assigned to the subnet pool. The adjacent prefixes are merged and treated as a single prefix. Each subnet prefix must be unique.</p>
</td>
</tr>
<tr id="row14968744267"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p199681944763"><a name="p199681944763"></a><a name="p199681944763"></a>min_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p49682044566"><a name="p49682044566"></a><a name="p49682044566"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p397084410616"><a name="p397084410616"></a><a name="p397084410616"></a>Specifies the minimum prefix that can be allocated from the subnet pool.</p>
</td>
</tr>
<tr id="row22360302105653"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p1404384110577"><a name="p1404384110577"></a><a name="p1404384110577"></a>address_scope_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p930111615640"><a name="p930111615640"></a><a name="p930111615640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p2924364410577"><a name="p2924364410577"></a><a name="p2924364410577"></a>Specifies the ID of the address range allocated to the subnet pool.</p>
<p id="p62544866102532"><a name="p62544866102532"></a><a name="p62544866102532"></a>Only the administrator can specify this attribute.</p>
</td>
</tr>
<tr id="row1597013444615"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p19970184415616"><a name="p19970184415616"></a><a name="p19970184415616"></a>shared</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p597044417614"><a name="p597044417614"></a><a name="p597044417614"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p159708444612"><a name="p159708444612"></a><a name="p159708444612"></a>Specifies whether the network can be shared to all projects. </p>
</td>
</tr>
<tr id="row99704441966"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p3970744162"><a name="p3970744162"></a><a name="p3970744162"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p597014415620"><a name="p597014415620"></a><a name="p597014415620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p1612016113323"><a name="p1612016113323"></a><a name="p1612016113323"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row139702441463"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p4970154418614"><a name="p4970154418614"></a><a name="p4970154418614"></a>default_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p397018441063"><a name="p397018441063"></a><a name="p397018441063"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p3970044567"><a name="p3970044567"></a><a name="p3970044567"></a>Specifies the length of the prefix to allocate when the CIDR or prefixlen attributes are omitted when creating a subnet.</p>
</td>
</tr>
<tr id="row197118445620"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p1297110441967"><a name="p1297110441967"></a><a name="p1297110441967"></a>max_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p697184412610"><a name="p697184412610"></a><a name="p697184412610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p497164414613"><a name="p497164414613"></a><a name="p497164414613"></a>Specifies the maximum prefix length that can be allocated from the subnet pool.</p>
</td>
</tr>
<tr id="row1597174413610"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p397114441268"><a name="p397114441268"></a><a name="p397114441268"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p5971104410613"><a name="p5971104410613"></a><a name="p5971104410613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p097164411616"><a name="p097164411616"></a><a name="p097164411616"></a>Provides supplementary information about the subnet pool.</p>
</td>
</tr>
<tr id="row129712441610"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p1971174417613"><a name="p1971174417613"></a><a name="p1971174417613"></a>is_default</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p1597254413618"><a name="p1597254413618"></a><a name="p1597254413618"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p17972114418620"><a name="p17972114418620"></a><a name="p17972114418620"></a>Specifies whether this is the default subnet pool.</p>
</td>
</tr>
<tr id="row129724441264"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p12972144415618"><a name="p12972144415618"></a><a name="p12972144415618"></a>revision_number</p>
</td>
<td class="cellrowborder" valign="top" width="15.950000000000001%" headers="mcps1.2.4.1.2 "><p id="p179721944765"><a name="p179721944765"></a><a name="p179721944765"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.76%" headers="mcps1.2.4.1.3 "><p id="p19724441061"><a name="p19724441061"></a><a name="p19724441061"></a>Specifies the revision number of the subnet pool.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section64320104111236"></a>

Example request

None

Example response

```
{
    "subnetpools": [
        {
            "min_prefixlen": 64,
            "address_scope_id": null,
            "default_prefixlen": 64,
            "id": "03f761e6-eee0-43fc-a921-8acf64c14988",
            "max_prefixlen": 64,
            "name": "my-subnet-pool-ipv6",
            "default_quota": null,
            "is_default": false,
            "project_id": "9fadcee8aa7c40cdb2114fff7d569c08",
            "tenant_id": "9fadcee8aa7c40cdb2114fff7d569c08",
            "prefixes": [
                "2001:db8:0:2::/64",
                "2001:db8::/63"
            ],
            "ip_version": 6,
            "shared": false,
            "description": "",
            "revision_number": 2,
            "created_at": "2018-09-20T02:15:34",
            "updated_at": "2018-09-20T02:15:34"
        },
        {
            "min_prefixlen": 24,
            "address_scope_id": null,
            "default_prefixlen": 25,
            "id": "f49a1319-423a-4ee6-ba54-1d95a4f6cc68",
            "max_prefixlen": 30,
            "name": "my-subnet-pool-ipv4",
            "default_quota": null,
            "is_default": false,
            "project_id": "9fadcee8aa7c40cdb2114fff7d569c08",
            "tenant_id": "9fadcee8aa7c40cdb2114fff7d569c08",
            "prefixes": [
                "10.10.0.0/21",
                "192.168.0.0/16"
            ],
            "ip_version": 4,
            "shared": false,
            "description": "",
            "revision_number": 2,
            "created_at": "2018-09-20T02:15:34",
            "updated_at": "2018-09-20T02:15:34"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

