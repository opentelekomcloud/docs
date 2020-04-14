# Querying a Stack Template<a name="EN-US_TOPIC_0084581308"></a>

## Function<a name="en-us_topic_0057973145_section59686491"></a>

This API is used to query a stack template. 

## URI<a name="en-us_topic_0057973145_section307511"></a>

GET /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}/template

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API supports redirection. During the calling, you can specify only  **stack\_name**  or  **stack\_id**.  

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b20668932105317"><a name="b20668932105317"></a><a name="b20668932105317"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b36374335532"><a name="b36374335532"></a><a name="b36374335532"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b18459113410535"><a name="b18459113410535"></a><a name="b18459113410535"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b33472353538"><a name="b33472353538"></a><a name="b33472353538"></a>Description</strong></p>
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
<tr id="row161097438473"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10658144911017"><a name="p10658144911017"></a><a name="p10658144911017"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1166014498107"><a name="p1166014498107"></a><a name="p1166014498107"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p666214493103"><a name="p666214493103"></a><a name="p666214493103"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p76631349181010"><a name="p76631349181010"></a><a name="p76631349181010"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="row131851844124918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p146651349161017"><a name="p146651349161017"></a><a name="p146651349161017"></a>stack_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1666614912100"><a name="p1666614912100"></a><a name="p1666614912100"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p106671249191011"><a name="p106671249191011"></a><a name="p106671249191011"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p6668124912103"><a name="p6668124912103"></a><a name="p6668124912103"></a>Specifies the stack UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973145_section2767599"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973145_section24908398"></a>

<a name="en-us_topic_0057973145_table22004215"></a>
<table><thead align="left"><tr id="en-us_topic_0057973145_row57369096"><th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b143155317531"><a name="b143155317531"></a><a name="b143155317531"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.478452154784522%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b1390295314534"><a name="b1390295314534"></a><a name="b1390295314534"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.66833316668333%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b1686465415532"><a name="b1686465415532"></a><a name="b1686465415532"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.374762523747634%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b3761145515316"><a name="b3761145515316"></a><a name="b3761145515316"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19475211125716"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p12920101455612"><a name="p12920101455612"></a><a name="p12920101455612"></a>heat_template_version</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p176411511191917"><a name="p176411511191917"></a><a name="p176411511191917"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p692021420560"><a name="p692021420560"></a><a name="p692021420560"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.374762523747634%" headers="mcps1.1.5.1.4 "><p id="p12920714125613"><a name="p12920714125613"></a><a name="p12920714125613"></a>Specifies the version of the HOT template.</p>
</td>
</tr>
<tr id="en-us_topic_0057973145_row712884"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973145_p57743657"><a name="en-us_topic_0057973145_p57743657"></a><a name="en-us_topic_0057973145_p57743657"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p136411911141915"><a name="p136411911141915"></a><a name="p136411911141915"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973145_p46724626"><a name="en-us_topic_0057973145_p46724626"></a><a name="en-us_topic_0057973145_p46724626"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.374762523747634%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973145_p6983522"><a name="en-us_topic_0057973145_p6983522"></a><a name="en-us_topic_0057973145_p6983522"></a>Includes key-value pairs of the output data.</p>
</td>
</tr>
<tr id="en-us_topic_0057973145_row62851700"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973145_p57822944"><a name="en-us_topic_0057973145_p57822944"></a><a name="en-us_topic_0057973145_p57822944"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p1641311161918"><a name="p1641311161918"></a><a name="p1641311161918"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973145_p53146884"><a name="en-us_topic_0057973145_p53146884"></a><a name="en-us_topic_0057973145_p53146884"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.374762523747634%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973145_p66163095"><a name="en-us_topic_0057973145_p66163095"></a><a name="en-us_topic_0057973145_p66163095"></a>Specifies the key-value pairs of template parameters.</p>
</td>
</tr>
<tr id="row3334913144419"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="p7208173102111"><a name="p7208173102111"></a><a name="p7208173102111"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p1064191116196"><a name="p1064191116196"></a><a name="p1064191116196"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="p17208531202115"><a name="p17208531202115"></a><a name="p17208531202115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.374762523747634%" headers="mcps1.1.5.1.4 "><p id="p102088312216"><a name="p102088312216"></a><a name="p102088312216"></a>Describes the stack template.</p>
</td>
</tr>
<tr id="en-us_topic_0057973145_row58596944"><td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973145_p48732029"><a name="en-us_topic_0057973145_p48732029"></a><a name="en-us_topic_0057973145_p48732029"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="15.478452154784522%" headers="mcps1.1.5.1.2 "><p id="p2641181113193"><a name="p2641181113193"></a><a name="p2641181113193"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.66833316668333%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973145_p54980295"><a name="en-us_topic_0057973145_p54980295"></a><a name="en-us_topic_0057973145_p54980295"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.374762523747634%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973145_p15573968"><a name="en-us_topic_0057973145_p15573968"></a><a name="en-us_topic_0057973145_p15573968"></a>Specifies the template resources.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973145_section22848996"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/template
```

## Response Example<a name="en-us_topic_0057973145_section4314378"></a>

```
{
    "description": "Hello world HOT template that just defines a single server. Contains just base features to verify base HOT support.\n",
    "heat_template_version": "2013-05-23",
    "outputs": {
        "foo": {
            "description": "Show foo parameter value",
            "value": {
                "get_param": "foo"
            }
        }
    },
    "parameters": {
        "foo": {
            "default": "secret",
            "description": "Name of an existing key pair to use for the server",
            "hidden": true,
            "type": "string"
        }
    },
    "resources": {
        "random_key_name": {
            "properties": {
                "length": 8
            },
            "type": "OS::Heat::RandomString"
        }
    }
}
```

## Return Code<a name="en-us_topic_0057973145_section14779329217"></a>

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

<a name="table1927576173211"></a>
<table><thead align="left"><tr id="en-us_topic_0084581290_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581290_p129561510144"><a name="en-us_topic_0084581290_p129561510144"></a><a name="en-us_topic_0084581290_p129561510144"></a><strong id="en-us_topic_0084581290_b1552942884813"><a name="en-us_topic_0084581290_b1552942884813"></a><a name="en-us_topic_0084581290_b1552942884813"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581290_p4959810444"><a name="en-us_topic_0084581290_p4959810444"></a><a name="en-us_topic_0084581290_p4959810444"></a><strong id="en-us_topic_0084581290_b956007905"><a name="en-us_topic_0084581290_b956007905"></a><a name="en-us_topic_0084581290_b956007905"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581290_p9959161020418"><a name="en-us_topic_0084581290_p9959161020418"></a><a name="en-us_topic_0084581290_p9959161020418"></a><strong id="en-us_topic_0084581290_b359171417"><a name="en-us_topic_0084581290_b359171417"></a><a name="en-us_topic_0084581290_b359171417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581290_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p896118101840"><a name="en-us_topic_0084581290_p896118101840"></a><a name="en-us_topic_0084581290_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1296211015416"><a name="en-us_topic_0084581290_p1296211015416"></a><a name="en-us_topic_0084581290_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p9963110146"><a name="en-us_topic_0084581290_p9963110146"></a><a name="en-us_topic_0084581290_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p18134027201912"><a name="en-us_topic_0084581290_p18134027201912"></a><a name="en-us_topic_0084581290_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p1713419274191"><a name="en-us_topic_0084581290_p1713419274191"></a><a name="en-us_topic_0084581290_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p11134162718196"><a name="en-us_topic_0084581290_p11134162718196"></a><a name="en-us_topic_0084581290_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p125520290312"><a name="en-us_topic_0084581290_p125520290312"></a><a name="en-us_topic_0084581290_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581290_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row196097477276"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p19789174972712"><a name="en-us_topic_0084581290_p19789174972712"></a><a name="en-us_topic_0084581290_p19789174972712"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p779364918272"><a name="en-us_topic_0084581290_p779364918272"></a><a name="en-us_topic_0084581290_p779364918272"></a>Internal Server Error</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p196546319198"><a name="en-us_topic_0084581290_p196546319198"></a><a name="en-us_topic_0084581290_p196546319198"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

