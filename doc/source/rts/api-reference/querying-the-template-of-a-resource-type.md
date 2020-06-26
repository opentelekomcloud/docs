# Querying the Template of a Resource Type<a name="EN-US_TOPIC_0084581310"></a>

## Function<a name="en-us_topic_0057973147_section48507965"></a>

This API is used to query the template of a resource type.

>![](/images/icon-note.gif) **NOTE:**   
>The output template parameters of this API are related to the input parameters that you have specified, but the parameters may be different.  

## URI<a name="en-us_topic_0057973147_section33918503"></a>

GET /v1/\{project\_id\}/resource\_types/\{type\_name\}/template

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b171981112105617"><a name="b171981112105617"></a><a name="b171981112105617"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b1075171485615"><a name="b1075171485615"></a><a name="b1075171485615"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b161021818195617"><a name="b161021818195617"></a><a name="b161021818195617"></a>Description</strong></p>
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
<tr id="row205605355223"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5414363327"><a name="p5414363327"></a><a name="p5414363327"></a>type_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p124171268327"><a name="p124171268327"></a><a name="p124171268327"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1342216693211"><a name="p1342216693211"></a><a name="p1342216693211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1642526163220"><a name="p1642526163220"></a><a name="p1642526163220"></a>Specifies the resource type.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973147_section36831075"></a>

<a name="en-us_topic_0057973124_table18628881"></a>
<table><thead align="left"><tr id="en-us_topic_0057973124_row52552023"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b1380833625614"><a name="b1380833625614"></a><a name="b1380833625614"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b338164413560"><a name="b338164413560"></a><a name="b338164413560"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b19868174685612"><a name="b19868174685612"></a><a name="b19868174685612"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b18283134815562"><a name="b18283134815562"></a><a name="b18283134815562"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.56435643564357%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b474185115612"><a name="b474185115612"></a><a name="b474185115612"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1255173115210"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.6.1.1 "><p id="p5352415277"><a name="p5352415277"></a><a name="p5352415277"></a>template_type</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.1.6.1.2 "><p id="p74191615132316"><a name="p74191615132316"></a><a name="p74191615132316"></a>query</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.6.1.3 "><p id="p144192462712"><a name="p144192462712"></a><a name="p144192462712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.6.1.4 "><p id="p3515246279"><a name="p3515246279"></a><a name="p3515246279"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.56435643564357%" headers="mcps1.1.6.1.5 "><p id="p3712418272"><a name="p3712418272"></a><a name="p3712418272"></a>Specifies the resource template type.</p>
<p id="p178453183218"><a name="p178453183218"></a><a name="p178453183218"></a>The valid types are cfn and hot.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973147_section63044227"></a>

<a name="en-us_topic_0057973147_table4089954"></a>
<table><thead align="left"><tr id="en-us_topic_0057973147_row25283375"><th class="cellrowborder" valign="top" width="16.09160916091609%" id="mcps1.1.5.1.1"><p id="p12371421105"><a name="p12371421105"></a><a name="p12371421105"></a><strong id="b1496513185713"><a name="b1496513185713"></a><a name="b1496513185713"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.941494149414941%" id="mcps1.1.5.1.2"><p id="p73741121208"><a name="p73741121208"></a><a name="p73741121208"></a><strong id="b1567111912574"><a name="b1567111912574"></a><a name="b1567111912574"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.09160916091609%" id="mcps1.1.5.1.3"><p id="p73751528013"><a name="p73751528013"></a><a name="p73751528013"></a><strong id="b1428227849"><a name="b1428227849"></a><a name="b1428227849"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="52.87528752875287%" id="mcps1.1.5.1.4"><p id="p43801225012"><a name="p43801225012"></a><a name="p43801225012"></a><strong id="b851142585710"><a name="b851142585710"></a><a name="b851142585710"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973147_row12343988"><td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973147_p60338972"><a name="en-us_topic_0057973147_p60338972"></a><a name="en-us_topic_0057973147_p60338972"></a>outputs</p>
</td>
<td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.1.5.1.2 "><p id="p197301934112315"><a name="p197301934112315"></a><a name="p197301934112315"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973147_p55618577"><a name="en-us_topic_0057973147_p55618577"></a><a name="en-us_topic_0057973147_p55618577"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.87528752875287%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973147_p42592192"><a name="en-us_topic_0057973147_p42592192"></a><a name="en-us_topic_0057973147_p42592192"></a>Includes key-value pairs of the output data.</p>
</td>
</tr>
<tr id="row192984128011"><td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.1 "><p id="p208521633134212"><a name="p208521633134212"></a><a name="p208521633134212"></a>heat_template_version</p>
</td>
<td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.1.5.1.2 "><p id="p7730163462311"><a name="p7730163462311"></a><a name="p7730163462311"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.3 "><p id="p208524335426"><a name="p208524335426"></a><a name="p208524335426"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.87528752875287%" headers="mcps1.1.5.1.4 "><p id="p208521433134214"><a name="p208521433134214"></a><a name="p208521433134214"></a>Specifies the version of the HOT template.</p>
</td>
</tr>
<tr id="row124631810718"><td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.1 "><p id="p846412102114"><a name="p846412102114"></a><a name="p846412102114"></a>HeatTemplateFormatVersion</p>
</td>
<td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.1.5.1.2 "><p id="p1746412103113"><a name="p1746412103113"></a><a name="p1746412103113"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.3 "><p id="p19464210612"><a name="p19464210612"></a><a name="p19464210612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.87528752875287%" headers="mcps1.1.5.1.4 "><p id="p34644101413"><a name="p34644101413"></a><a name="p34644101413"></a>Specifies the version of the CFN template.</p>
</td>
</tr>
<tr id="row133951419904"><td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.1 "><p id="p8742537164212"><a name="p8742537164212"></a><a name="p8742537164212"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.1.5.1.2 "><p id="p16730203462311"><a name="p16730203462311"></a><a name="p16730203462311"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.3 "><p id="p127421137144212"><a name="p127421137144212"></a><a name="p127421137144212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.87528752875287%" headers="mcps1.1.5.1.4 "><p id="p16742153714216"><a name="p16742153714216"></a><a name="p16742153714216"></a>Describes the stack template.</p>
</td>
</tr>
<tr id="en-us_topic_0057973147_row47785409"><td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973147_p45412892"><a name="en-us_topic_0057973147_p45412892"></a><a name="en-us_topic_0057973147_p45412892"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.1.5.1.2 "><p id="p197308342235"><a name="p197308342235"></a><a name="p197308342235"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973147_p54565640"><a name="en-us_topic_0057973147_p54565640"></a><a name="en-us_topic_0057973147_p54565640"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.87528752875287%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973147_p46486449"><a name="en-us_topic_0057973147_p46486449"></a><a name="en-us_topic_0057973147_p46486449"></a>Specifies the key-value pairs of template parameters.</p>
</td>
</tr>
<tr id="en-us_topic_0057973147_row15724863"><td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973147_p65754424"><a name="en-us_topic_0057973147_p65754424"></a><a name="en-us_topic_0057973147_p65754424"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="14.941494149414941%" headers="mcps1.1.5.1.2 "><p id="p173063420232"><a name="p173063420232"></a><a name="p173063420232"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.09160916091609%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973147_p24508133"><a name="en-us_topic_0057973147_p24508133"></a><a name="en-us_topic_0057973147_p24508133"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="52.87528752875287%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973147_p5027197"><a name="en-us_topic_0057973147_p5027197"></a><a name="en-us_topic_0057973147_p5027197"></a>Specifies the template resources.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973147_section30527135"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/resource_types/OS%3A%3AHeat%3A%3ARandomString/template
```

## Response Example<a name="en-us_topic_0057973147_section6308759"></a>

```
{
    "Outputs": {
        "value": {
            "Description": "The random string generated by this resource. This value is also available by referencing the resource.",
            "Value": "{"Fn::GetAtt": ["RandomString", "value"]}"
        },
        "show": {
            "Description": "Detailed information about resource.",
            "Value": "{"Fn::GetAtt": ["RandomString", "show"]}"
        }
    },
    "HeatTemplateFormatVersion": "2012-12-12",
    "Resources": {
        "RandomString": {
            "Type": "OS::Heat::RandomString",
            "Properties": {
                "length": {
                    "Ref": "length"
                },
                "salt": {
                    "Ref": "salt"
                },
                "character_sequences": {
                    "Fn::Split": [
                        ",",
                        {
                            "Ref": "character_sequences"
                        }
                    ]
                },
                "character_classes": {
                    "Fn::Split": [
                        ",",
                        {
                            "Ref": "character_classes"
                        }
                    ]
                },
                "sequence": {
                    "Ref": "sequence"
                }
            }
        }
    },
    "Description": "Initial template of RandomString",
    "Parameters": {
        "length": {
            "Default": 32,
            "Type": "Number",
            "Description": "Length of the string to generate.",
            "MaxValue": 512,
            "MinValue": 1
        },
        "salt": {
            "Type": "String",
            "Description": "Value which can be set or changed on stack update to trigger the resource for replacement with a new random string. The salt value itself is ignored by the random generator."
        },
        "character_sequences": {
            "Type": "CommaDelimitedList",
            "Description": "A list of character sequences and their constraints to generate the random string from."
        },
        "character_classes": {
            "Default": [
                {
                    "class": "lettersdigits",
                    "min": 1
                }
            ],
            "Type": "CommaDelimitedList",
            "Description": "A list of character class and their constraints to generate the random string from."
        },
        "sequence": {
            "Type": "String",
            "Description": "Sequence of characters to build the random string from.",
            "AllowedValues": [
                "lettersdigits",
                "letters",
                "lowercase",
                "uppercase",
                "digits",
                "hexdigits",
                "octdigits"
            ]
        }
    }
}
```

## Return Code<a name="en-us_topic_0057973147_section56778838"></a>

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

<a name="table8571828153012"></a>
<table><thead align="left"><tr id="en-us_topic_0084581294_row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581294_p129561510144"><a name="en-us_topic_0084581294_p129561510144"></a><a name="en-us_topic_0084581294_p129561510144"></a><strong id="en-us_topic_0084581294_b1235759101013"><a name="en-us_topic_0084581294_b1235759101013"></a><a name="en-us_topic_0084581294_b1235759101013"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581294_p4959810444"><a name="en-us_topic_0084581294_p4959810444"></a><a name="en-us_topic_0084581294_p4959810444"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581294_p9959161020418"><a name="en-us_topic_0084581294_p9959161020418"></a><a name="en-us_topic_0084581294_p9959161020418"></a><strong id="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581294_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581294_row179609103411"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p896118101840"><a name="en-us_topic_0084581294_p896118101840"></a><a name="en-us_topic_0084581294_p896118101840"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1296211015416"><a name="en-us_topic_0084581294_p1296211015416"></a><a name="en-us_topic_0084581294_p1296211015416"></a>Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p9963110146"><a name="en-us_topic_0084581294_p9963110146"></a><a name="en-us_topic_0084581294_p9963110146"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_p18134027201912"><a name="en-us_topic_0084581294_p18134027201912"></a><a name="en-us_topic_0084581294_p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p1713419274191"><a name="en-us_topic_0084581294_p1713419274191"></a><a name="en-us_topic_0084581294_p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_p11134162718196"><a name="en-us_topic_0084581294_p11134162718196"></a><a name="en-us_topic_0084581294_p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="en-us_topic_0084581294_row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581294_p125520290312"><a name="en-us_topic_0084581294_p125520290312"></a><a name="en-us_topic_0084581294_p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0084581294_en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
</tbody>
</table>

