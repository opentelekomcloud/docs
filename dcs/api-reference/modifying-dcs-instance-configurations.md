# Modifying DCS Instance Configurations<a name="EN-US_TOPIC_0237964364"></a>

## Function<a name="section46805556"></a>

This API is used to modify the configuration parameters of a DCS instance.

## URI<a name="section18596821"></a>

-   URI format:

    PUT /v1.0/\{project\_id\}/instances/\{instance\_id\}/configs

-   Parameter description:

[Table 1](#table48735027)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="table48735027"></a>
<table><thead align="left"><tr id="row4485854"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p27809855"><a name="p27809855"></a><a name="p27809855"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p38005777"><a name="p38005777"></a><a name="p38005777"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p58569083"><a name="p58569083"></a><a name="p58569083"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p46475302"><a name="p46475302"></a><a name="p46475302"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6403130"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p48891485"><a name="p48891485"></a><a name="p48891485"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p787386"><a name="p787386"></a><a name="p787386"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p63778295"><a name="p63778295"></a><a name="p63778295"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p65768252"><a name="p65768252"></a><a name="p65768252"></a>Project ID.</p>
</td>
</tr>
<tr id="row55043362"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p29327303"><a name="p29327303"></a><a name="p29327303"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p26701320"><a name="p26701320"></a><a name="p26701320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p15323343"><a name="p15323343"></a><a name="p15323343"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p33231233"><a name="p33231233"></a><a name="p33231233"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section33153663"></a>

-   Request parameter:

    [Table 2](#table21768161)  describes request parameters.


**Table  2**  Parameter description

<a name="table21768161"></a>
<table><thead align="left"><tr id="row61365090"><th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.5.1.1"><p id="p4516376"><a name="p4516376"></a><a name="p4516376"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.5.1.2"><p id="p30282212"><a name="p30282212"></a><a name="p30282212"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.3"><p id="p36940075"><a name="p36940075"></a><a name="p36940075"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.4"><p id="p39356119"><a name="p39356119"></a><a name="p39356119"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33729104"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.1 "><p id="p47702909"><a name="p47702909"></a><a name="p47702909"></a>redis_config</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.5.1.2 "><p id="p38730439"><a name="p38730439"></a><a name="p38730439"></a>Array.</p>
<p id="p13029634"><a name="p13029634"></a><a name="p13029634"></a>For details, see <a href="#ref478570460">Table 3</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.3 "><p id="p36253648"><a name="p36253648"></a><a name="p36253648"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.4 "><p id="p50864351"><a name="p50864351"></a><a name="p50864351"></a>Array of configurations items of the DCS instance.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the redis\_config array

<a name="ref478570460"></a>
<table><thead align="left"><tr id="row16012368"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p21933451"><a name="p21933451"></a><a name="p21933451"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p31779119"><a name="p31779119"></a><a name="p31779119"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p23971810"><a name="p23971810"></a><a name="p23971810"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p62668495"><a name="p62668495"></a><a name="p62668495"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42983324"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p59097201"><a name="p59097201"></a><a name="p59097201"></a>param_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p22143991"><a name="p22143991"></a><a name="p22143991"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p48832853"><a name="p48832853"></a><a name="p48832853"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p63147060"><a name="p63147060"></a><a name="p63147060"></a>Parameter ID.</p>
</td>
</tr>
<tr id="row31452636"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p64635550"><a name="p64635550"></a><a name="p64635550"></a>param_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p988213"><a name="p988213"></a><a name="p988213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p12936457"><a name="p12936457"></a><a name="p12936457"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p41220097"><a name="p41220097"></a><a name="p41220097"></a>Parameter name.</p>
</td>
</tr>
<tr id="row35436558"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p51788984"><a name="p51788984"></a><a name="p51788984"></a>param_value</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p34158203"><a name="p34158203"></a><a name="p34158203"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p15351038"><a name="p15351038"></a><a name="p15351038"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p35474537"><a name="p35474537"></a><a name="p35474537"></a>Value to which the parameter is modified.</p>
</td>
</tr>
</tbody>
</table>

For possible values of parameters in  [Table 3](#ref478570460), see  [Querying DCS Instance Configurations](querying-dcs-instance-configurations.md).

-   Example request:

    ```
    { 
     "redis_config": [ 
            { 
                "param_id": "1", 
                "param_name": "timeout", 
                "param_value": "100" 
            } 
     ] 
    }
    ```


## Response<a name="section29947515"></a>

-   Status code:

    If status code "204 No content" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    None.

-   Example response:

    None.


