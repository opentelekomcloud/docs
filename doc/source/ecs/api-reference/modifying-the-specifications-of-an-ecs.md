# Modifying the Specifications of an ECS <a name="EN-US_TOPIC_0020212653"></a>

## Function<a name="section5379216"></a>

ECS specifications can be modified, for example, upgrading the vCPUs and memory, to meet service requirements. This API is used to modify ECS specifications.

An ECS flavor cannot be changed to certain flavors. For details, see  [Querying the Target Flavors to Which an ECS Flavor Can Be Changed](querying-the-target-flavors-to-which-an-ecs-flavor-can-be-changed.md).

## Constraints<a name="section10197106104013"></a>

-   You can modify the ECS specifications only when the ECS is stopped.
-   Before changing a general-purpose \(S1, C1, C2, or M1\) ECS to an H1 ECS, manually install the desired driver on the ECS. Otherwise, the specifications modification will fail. For instructions about how to install a driver, see "Modifying ECS vCPU and Memory Specifications \> Changing a General-Purpose ECS to an H1 ECS" in  _Elastic Cloud Server User Guide_.
-   A Xen ECS can be changed to a KVM ECS, but a KVM ECS cannot be changed to a Xen ECS.
-   Before changing a Xen ECS to a KVM ECS, manually install the desired driver on the ECS. Otherwise, the specifications modification will fail. For instructions about how to install a driver, see "Modifying ECS vCPU and Memory Specifications \> Changing a Xen ECS to a KVM ECS \(Windows\) or Changing a Xen ECS to a KVM ECS \(Linux\) in  _Elastic Cloud Server User Guide_.
-   A Xen ECS with more than 24 VBD disks attached cannot be changed to a KVM ECS.

## URI<a name="section48412952"></a>

POST /v1/\{project\_id\}/cloudservers/\{server\_id\}/resize

[Table 1](#table29396722)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table29396722"></a>
<table><thead align="left"><tr id="row15658103"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p60346796"><a name="p60346796"></a><a name="p60346796"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p56252285"><a name="p56252285"></a><a name="p56252285"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p60141268"><a name="p60141268"></a><a name="p60141268"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39604502"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p53848109"><a name="p53848109"></a><a name="p53848109"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p66729601"><a name="p66729601"></a><a name="p66729601"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row59061958"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p19289328"><a name="p19289328"></a><a name="p19289328"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p18931763"><a name="p18931763"></a><a name="p18931763"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p57077814"><a name="p57077814"></a><a name="p57077814"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section33063388"></a>

[Table 2](#table6742880)  describes the request parameters.

**Table  2**  Request parameters

<a name="table6742880"></a>
<table><thead align="left"><tr id="row13072760"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p52260639"><a name="p52260639"></a><a name="p52260639"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p5253358"><a name="p5253358"></a><a name="p5253358"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.36%" id="mcps1.2.5.1.3"><p id="p22868878"><a name="p22868878"></a><a name="p22868878"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.81%" id="mcps1.2.5.1.4"><p id="p40439847"><a name="p40439847"></a><a name="p40439847"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54402144"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p44497505"><a name="p44497505"></a><a name="p44497505"></a>resize</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p47528147"><a name="p47528147"></a><a name="p47528147"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.2.5.1.3 "><p id="p24574685"><a name="p24574685"></a><a name="p24574685"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.2.5.1.4 "><p id="p63988077"><a name="p63988077"></a><a name="p63988077"></a>Specifies the operation to modify ECS specifications. For details, see <a href="#table7657338">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **resize**  field description

<a name="table7657338"></a>
<table><thead align="left"><tr id="row17725233"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p1733218125569"><a name="p1733218125569"></a><a name="p1733218125569"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p203321912145616"><a name="p203321912145616"></a><a name="p203321912145616"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p1633291212566"><a name="p1633291212566"></a><a name="p1633291212566"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p733241219565"><a name="p733241219565"></a><a name="p733241219565"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40163483"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p32016662"><a name="p32016662"></a><a name="p32016662"></a>flavorRef</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p43212834"><a name="p43212834"></a><a name="p43212834"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p10578662"><a name="p10578662"></a><a name="p10578662"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p61434729"><a name="p61434729"></a><a name="p61434729"></a>Specifies the flavor ID of the ECS after the modification.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section29135036"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section1183192295620"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/resize
```

```
{
"resize": {
        "flavorRef": "c3.15xlarge.2"
    }
}
```

## Example Response<a name="section1923071117499"></a>

None

## Returned Values<a name="section27037160"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

