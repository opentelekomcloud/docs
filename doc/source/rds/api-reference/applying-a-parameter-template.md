# Applying a Parameter Template<a name="rds_09_0304"></a>

## Function<a name="section34921715163618"></a>

This API is used to apply a parameter template to one or more DB instances.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section152364311313"></a>

-   The following DB engines are supported: MySQL, PostgreSQL, and Microsoft SQL Server.
-   For Microsoft SQL Server, only the following editions are supported: Microsoft SQL Server 2014 SE, 2016 SE, and 2016 EE.

## URI<a name="section349221518369"></a>

-   URI format

    PUT https://\{_Endpoint_\}/v3/\{_project\_id_\}/configurations/\{config\_id\}/apply

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/configurations/463b4b58-d0e8-4e2b-9560-5dea4552fde9/apply

-   Parameter description

    **Table  1**  Parameter description

    <a name="table350771512364"></a>
    <table><thead align="left"><tr id="row178891510369"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p2078801512364"><a name="p2078801512364"></a><a name="p2078801512364"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.610000000000003%" id="mcps1.2.4.1.2"><p id="p1778841553610"><a name="p1778841553610"></a><a name="p1778841553610"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.18%" id="mcps1.2.4.1.3"><p id="p0788171593617"><a name="p0788171593617"></a><a name="p0788171593617"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16788161516363"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p1478816159368"><a name="p1478816159368"></a><a name="p1478816159368"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.4.1.2 "><p id="p77882156369"><a name="p77882156369"></a><a name="p77882156369"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.18%" headers="mcps1.2.4.1.3 "><p id="p107881159368"><a name="p107881159368"></a><a name="p107881159368"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p1955917142067"><a name="p1955917142067"></a><a name="p1955917142067"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row14788171523612"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p107881815193611"><a name="p107881815193611"></a><a name="p107881815193611"></a>config_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.610000000000003%" headers="mcps1.2.4.1.2 "><p id="p157881915113616"><a name="p157881915113616"></a><a name="p157881915113616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.18%" headers="mcps1.2.4.1.3 "><p id="p77882015143610"><a name="p77882015143610"></a><a name="p77882015143610"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section15386150366"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table05381415103619"></a>
    <table><thead align="left"><tr id="row97881015193611"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p778891543617"><a name="p778891543617"></a><a name="p778891543617"></a><strong id="b1501362188"><a name="b1501362188"></a><a name="b1501362188"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p10788141533620"><a name="p10788141533620"></a><a name="p10788141533620"></a><strong>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p167880155368"><a name="p167880155368"></a><a name="p167880155368"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147881915193611"><a name="p147881915193611"></a><a name="p147881915193611"></a><strong id="b314512256"><a name="b314512256"></a><a name="b314512256"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5788121519368"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16788415133610"><a name="p16788415133610"></a><a name="p16788415133610"></a>instance_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p127881615133611"><a name="p127881615133611"></a><a name="p127881615133611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p189001836124616"><a name="p189001836124616"></a><a name="p189001836124616"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1078813155365"><a name="p1078813155365"></a><a name="p1078813155365"></a>Specifies the DB instance ID list object.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

```
{
	"instance_ids": ["73ea2bf70c73497f89ee0ad4ee008aa2in01", "fe5f5a07539c431181fc78220713aebein01"]
}
```

## Response<a name="section8569161515366"></a>

-   Normal response

    **Table  3**  Parameter description

    <a name="table1056917157367"></a>
    <table><thead align="left"><tr id="row97881615113617"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p13788715133620"><a name="p13788715133620"></a><a name="p13788715133620"></a><strong id="b969820788"><a name="b969820788"></a><a name="b969820788"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p978811516362"><a name="p978811516362"></a><a name="p978811516362"></a><strong id="b970759315"><a name="b970759315"></a><a name="b970759315"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p177889156366"><a name="p177889156366"></a><a name="p177889156366"></a><strong id="b2037165250"><a name="b2037165250"></a><a name="b2037165250"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1378819159369"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p17788121516366"><a name="p17788121516366"></a><a name="p17788121516366"></a>configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p7788131520367"><a name="p7788131520367"></a><a name="p7788131520367"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p8788151563617"><a name="p8788151563617"></a><a name="p8788151563617"></a>Specifies the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row178810158365"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p4788101519365"><a name="p4788101519365"></a><a name="p4788101519365"></a>configuration_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p978821573620"><a name="p978821573620"></a><a name="p978821573620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p19788815123616"><a name="p19788815123616"></a><a name="p19788815123616"></a>Specifies the parameter template name.</p>
    </td>
    </tr>
    <tr id="row8788715153611"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p18788131511368"><a name="p18788131511368"></a><a name="p18788131511368"></a>apply_results</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p6301203614332"><a name="p6301203614332"></a><a name="p6301203614332"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p20788181510366"><a name="p20788181510366"></a><a name="p20788181510366"></a>Specifies the result of applying the parameter template.</p>
    <p id="p11498115753016"><a name="p11498115753016"></a><a name="p11498115753016"></a>For details, see <a href="#table19602151563612">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row10788161543616"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p7788111517367"><a name="p7788111517367"></a><a name="p7788111517367"></a>success</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p16788171593618"><a name="p16788171593618"></a><a name="p16788171593618"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p14788181583618"><a name="p14788181583618"></a><a name="p14788181583618"></a>Specifies whether each parameter template is applied to DB instances successfully.</p>
    <a name="ul07881715103618"></a><a name="ul07881715103618"></a><ul id="ul07881715103618"><li><strong id="b842352706174048"><a name="b842352706174048"></a><a name="b842352706174048"></a>true</strong>: Each parameter template is applied to DB instances successfully.</li><li><span class="parmvalue" id="parmvalue8230132315317"><a name="parmvalue8230132315317"></a><a name="parmvalue8230132315317"></a><b>false</b></span>: One or more parameter templates failed to be applied.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  apply\_results field data structure description

    <a name="table19602151563612"></a>
    <table><thead align="left"><tr id="row157887151363"><th class="cellrowborder" valign="top" width="24.942494249424943%" id="mcps1.2.4.1.1"><p id="p9788151517364"><a name="p9788151517364"></a><a name="p9788151517364"></a><strong id="b918271699"><a name="b918271699"></a><a name="b918271699"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.653965396539654%" id="mcps1.2.4.1.2"><p id="p678811533611"><a name="p678811533611"></a><a name="p678811533611"></a><strong id="b1127238380"><a name="b1127238380"></a><a name="b1127238380"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.4035403540354%" id="mcps1.2.4.1.3"><p id="p1580411515361"><a name="p1580411515361"></a><a name="p1580411515361"></a><strong id="b1633770565"><a name="b1633770565"></a><a name="b1633770565"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13804315143614"><td class="cellrowborder" valign="top" width="24.942494249424943%" headers="mcps1.2.4.1.1 "><p id="p18042157360"><a name="p18042157360"></a><a name="p18042157360"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.653965396539654%" headers="mcps1.2.4.1.2 "><p id="p7804615203619"><a name="p7804615203619"></a><a name="p7804615203619"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.4035403540354%" headers="mcps1.2.4.1.3 "><p id="p18804191518362"><a name="p18804191518362"></a><a name="p18804191518362"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row16804161523613"><td class="cellrowborder" valign="top" width="24.942494249424943%" headers="mcps1.2.4.1.1 "><p id="p12804715163614"><a name="p12804715163614"></a><a name="p12804715163614"></a>instance_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.653965396539654%" headers="mcps1.2.4.1.2 "><p id="p6804191513611"><a name="p6804191513611"></a><a name="p6804191513611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.4035403540354%" headers="mcps1.2.4.1.3 "><p id="p1180413153362"><a name="p1180413153362"></a><a name="p1180413153362"></a>Indicates the DB instance name.</p>
    </td>
    </tr>
    <tr id="row3804101543618"><td class="cellrowborder" valign="top" width="24.942494249424943%" headers="mcps1.2.4.1.1 "><p id="p280414153361"><a name="p280414153361"></a><a name="p280414153361"></a>restart_required</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.653965396539654%" headers="mcps1.2.4.1.2 "><p id="p16804181512367"><a name="p16804181512367"></a><a name="p16804181512367"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.4035403540354%" headers="mcps1.2.4.1.3 "><p id="p8804181593615"><a name="p8804181593615"></a><a name="p8804181593615"></a>Indicates whether a reboot is required.</p>
    <a name="ul15804161503611"></a><a name="ul15804161503611"></a><ul id="ul15804161503611"><li><strong id="b842352706174226"><a name="b842352706174226"></a><a name="b842352706174226"></a>true</strong>: A reboot is required.</li><li><strong id="b842352706174241"><a name="b842352706174241"></a><a name="b842352706174241"></a>false</strong>: A reboot is not required.</li></ul>
    </td>
    </tr>
    <tr id="row108041215133614"><td class="cellrowborder" valign="top" width="24.942494249424943%" headers="mcps1.2.4.1.1 "><p id="p15804315103616"><a name="p15804315103616"></a><a name="p15804315103616"></a>success</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.653965396539654%" headers="mcps1.2.4.1.2 "><p id="p880491514363"><a name="p880491514363"></a><a name="p880491514363"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.4035403540354%" headers="mcps1.2.4.1.3 "><p id="p680412152366"><a name="p680412152366"></a><a name="p680412152366"></a>Indicates whether each parameter template is applied to DB instances successfully.</p>
    <a name="ul1680413151367"></a><a name="ul1680413151367"></a><ul id="ul1680413151367"><li><strong id="b1257071618"><a name="b1257071618"></a><a name="b1257071618"></a>true</strong>: The application is successful.</li><li><strong id="b842352706174059"><a name="b842352706174059"></a><a name="b842352706174059"></a>false</strong>: The application failed.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example normal response

    ```
    {
    	"configuration_id": "cf49bbd7d2384878bc3808733c9e9d8bpr01",
    	"configuration_name": "paramsGroup-bcf9",
    	"apply_results": [{
    		"instance_id": "fe5f5a07539c431181fc78220713aebein01",
    		"instance_name": "zyy1",
    		"restart_required": false,
    		"success": false
    	}, {
    		"instance_id": "73ea2bf70c73497f89ee0ad4ee008aa2in01",
    		"instance_name": "zyy2",
    		"restart_required": false,
    		"success": false
    	}],
    	"success": false
    }
    ```

-   Abnormal response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

