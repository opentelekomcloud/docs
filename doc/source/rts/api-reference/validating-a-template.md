# Validating a Template<a name="EN-US_TOPIC_0084581309"></a>

## Function<a name="en-us_topic_0057973146_section55668057"></a>

This API is used to check whether the template syntax meets requirements.

## URI<a name="en-us_topic_0057973146_section31250469"></a>

POST /v1/\{project\_id\}/validate

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b395116494294"><a name="b395116494294"></a><a name="b395116494294"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b141618517295"><a name="b141618517295"></a><a name="b141618517295"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b39743512297"><a name="b39743512297"></a><a name="b39743512297"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b20818115202910"><a name="b20818115202910"></a><a name="b20818115202910"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1765464961019"><a name="p1765464961019"></a><a name="p1765464961019"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p0655184916104"><a name="p0655184916104"></a><a name="p0655184916104"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p865694971017"><a name="p865694971017"></a><a name="p865694971017"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p13658144921010"><a name="p13658144921010"></a><a name="p13658144921010"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973146_section12818767"></a>

<a name="en-us_topic_0057973146_table48689546112557"></a>
<table><thead align="left"><tr id="en-us_topic_0057973146_row55759686112557"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b183610173016"><a name="b183610173016"></a><a name="b183610173016"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b16101432306"><a name="b16101432306"></a><a name="b16101432306"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b995053153013"><a name="b995053153013"></a><a name="b995053153013"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b77202420308"><a name="b77202420308"></a><a name="b77202420308"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b1858155123015"><a name="b1858155123015"></a><a name="b1858155123015"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973146_row11737621112557"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973146_p454014411266"><a name="en-us_topic_0057973146_p454014411266"></a><a name="en-us_topic_0057973146_p454014411266"></a>environment</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.2 "><p id="p48311342492"><a name="p48311342492"></a><a name="p48311342492"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973146_p3220736611266"><a name="en-us_topic_0057973146_p3220736611266"></a><a name="en-us_topic_0057973146_p3220736611266"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973146_p5865989011266"><a name="en-us_topic_0057973146_p5865989011266"></a><a name="en-us_topic_0057973146_p5865989011266"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973146_p5383061711266"><a name="en-us_topic_0057973146_p5383061711266"></a><a name="en-us_topic_0057973146_p5383061711266"></a>Specifies information about the environment for creating a stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973146_row12332919112557"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973146_p5094376511266"><a name="en-us_topic_0057973146_p5094376511266"></a><a name="en-us_topic_0057973146_p5094376511266"></a>files</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.2 "><p id="p883114484910"><a name="p883114484910"></a><a name="p883114484910"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973146_p3280427511266"><a name="en-us_topic_0057973146_p3280427511266"></a><a name="en-us_topic_0057973146_p3280427511266"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973146_p3990058511266"><a name="en-us_topic_0057973146_p3990058511266"></a><a name="en-us_topic_0057973146_p3990058511266"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973146_p1072195211266"><a name="en-us_topic_0057973146_p1072195211266"></a><a name="en-us_topic_0057973146_p1072195211266"></a>Specifies the files referenced in the environment.</p>
</td>
</tr>
<tr id="en-us_topic_0057973146_row51273737112557"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973146_p3167507011266"><a name="en-us_topic_0057973146_p3167507011266"></a><a name="en-us_topic_0057973146_p3167507011266"></a>template</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.6.1.2 "><p id="p12831648490"><a name="p12831648490"></a><a name="p12831648490"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973146_p1554385311266"><a name="en-us_topic_0057973146_p1554385311266"></a><a name="en-us_topic_0057973146_p1554385311266"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973146_p5109256911266"><a name="en-us_topic_0057973146_p5109256911266"></a><a name="en-us_topic_0057973146_p5109256911266"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973146_p4485738511266"><a name="en-us_topic_0057973146_p4485738511266"></a><a name="en-us_topic_0057973146_p4485738511266"></a>Specifies the stack template on which operations will be performed.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973146_section14714731132717"></a>

<a name="en-us_topic_0057973146_table62617577"></a>
<table><thead align="left"><tr id="en-us_topic_0057973146_row62584900"><th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.1"><p id="p2085283513568"><a name="p2085283513568"></a><a name="p2085283513568"></a><strong id="b479984903210"><a name="b479984903210"></a><a name="b479984903210"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.2"><p id="p4854835105614"><a name="p4854835105614"></a><a name="p4854835105614"></a><strong id="b59111051133213"><a name="b59111051133213"></a><a name="b59111051133213"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.471647164716472%" id="mcps1.1.5.1.3"><p id="p1856133585614"><a name="p1856133585614"></a><a name="p1856133585614"></a><strong id="b167835319326"><a name="b167835319326"></a><a name="b167835319326"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.945294529452944%" id="mcps1.1.5.1.4"><p id="p188601352562"><a name="p188601352562"></a><a name="p188601352562"></a><strong id="b5392154133211"><a name="b5392154133211"></a><a name="b5392154133211"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973146_row12941756"><td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973146_p41649354"><a name="en-us_topic_0057973146_p41649354"></a><a name="en-us_topic_0057973146_p41649354"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p1847571334916"><a name="p1847571334916"></a><a name="p1847571334916"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973146_p18154524"><a name="en-us_topic_0057973146_p18154524"></a><a name="en-us_topic_0057973146_p18154524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973146_p60712366"><a name="en-us_topic_0057973146_p60712366"></a><a name="en-us_topic_0057973146_p60712366"></a>Describes the template.</p>
</td>
</tr>
<tr id="en-us_topic_0057973146_row9540387"><td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973146_p34573872"><a name="en-us_topic_0057973146_p34573872"></a><a name="en-us_topic_0057973146_p34573872"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p34756139491"><a name="p34756139491"></a><a name="p34756139491"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.471647164716472%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973146_p49020229"><a name="en-us_topic_0057973146_p49020229"></a><a name="en-us_topic_0057973146_p49020229"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.945294529452944%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973146_p36050601"><a name="en-us_topic_0057973146_p36050601"></a><a name="en-us_topic_0057973146_p36050601"></a>Specifies the template parameters.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973146_section48260040"></a>

```
POST /v1/95d02433133a4c0a87ba6967474a2ad3/validate
{
    "template": "heat_template_version: 2014-10-16\ndescription: Create a serious of random string\nparameters:\n  length:\n    type: number\n    default: 4\nresources:\n  random:\n    type: OS::Heat::RandomString\n    properties:\n      length: { get_param: length }",
    "environment": {},
    "files": {}
}
```

## Response Example<a name="en-us_topic_0057973146_section31687177"></a>

```
{
    "Description": "Create a serious of random string",
    "Parameters": {
        "length": {
            "Default": 4,
            "NoEcho": "false",
            "Type": "Number",
            "Description": "",
            "Label": "length"
        }
    }
}
```

## Return Code<a name="en-us_topic_0057973146_section16749139"></a>

**Table  2**  Normal return code

<a name="table01411862119"></a>
<table><thead align="left"><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581285_b14910172512114"><a name="en-us_topic_0084581285_b14910172512114"></a><a name="en-us_topic_0084581285_b14910172512114"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581285_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581285_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p8637307194057"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p28533244194057"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0084581285_en-us_topic_0057973117_p29491459194057"></a>Request was successful.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b1664793453319"><a name="b1664793453319"></a><a name="b1664793453319"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b27301335193317"><a name="b27301335193317"></a><a name="b27301335193317"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b1235113373334"><a name="b1235113373334"></a><a name="b1235113373334"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p896118101840"><a name="p896118101840"></a><a name="p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1296211015416"><a name="p1296211015416"></a><a name="p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p9963110146"><a name="p9963110146"></a><a name="p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row292341875215"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p19789174972712"><a name="p19789174972712"></a><a name="p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p779364918272"><a name="p779364918272"></a><a name="p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p196546319198"><a name="p196546319198"></a><a name="p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

