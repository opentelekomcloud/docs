# Updating a Stack<a name="EN-US_TOPIC_0084581291"></a>

## Function<a name="en-us_topic_0057973126_section15690402"></a>

This API is used to update a stack.

## URI<a name="en-us_topic_0057973126_section6995890"></a>

PUT /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b57101528194910"><a name="b57101528194910"></a><a name="b57101528194910"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b1277816319491"><a name="b1277816319491"></a><a name="b1277816319491"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b19749163464916"><a name="b19749163464916"></a><a name="b19749163464916"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b43241037144917"><a name="b43241037144917"></a><a name="b43241037144917"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p95831413718"><a name="p95831413718"></a><a name="p95831413718"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p15861811371"><a name="p15861811371"></a><a name="p15861811371"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1059001471"><a name="p1059001471"></a><a name="p1059001471"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1459421871"><a name="p1459421871"></a><a name="p1459421871"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row161097438473"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8597416710"><a name="p8597416710"></a><a name="p8597416710"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p8600512716"><a name="p8600512716"></a><a name="p8600512716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p146021114718"><a name="p146021114718"></a><a name="p146021114718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p176041611277"><a name="p176041611277"></a><a name="p176041611277"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="row131851844124918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7611121874"><a name="p7611121874"></a><a name="p7611121874"></a>stack_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p26131311373"><a name="p26131311373"></a><a name="p26131311373"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p176151011178"><a name="p176151011178"></a><a name="p176151011178"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p11617111473"><a name="p11617111473"></a><a name="p11617111473"></a>Specifies the stack UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973126_section62963013"></a>

<a name="en-us_topic_0057973126_table957285211738"></a>
<table><thead align="left"><tr id="en-us_topic_0057973126_row1651674711738"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b1257115425016"><a name="b1257115425016"></a><a name="b1257115425016"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b94717713504"><a name="b94717713504"></a><a name="b94717713504"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b102511110125018"><a name="b102511110125018"></a><a name="b102511110125018"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.4"><p id="p18709155145010"><a name="p18709155145010"></a><a name="p18709155145010"></a><strong id="b352212115505"><a name="b352212115505"></a><a name="b352212115505"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.1.6.1.5"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b66852015175019"><a name="b66852015175019"></a><a name="b66852015175019"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973126_row1114067011738"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973126_p5986384711823"><a name="en-us_topic_0057973126_p5986384711823"></a><a name="en-us_topic_0057973126_p5986384711823"></a>template</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p20423174193918"><a name="p20423174193918"></a><a name="p20423174193918"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973126_p1713343911823"><a name="en-us_topic_0057973126_p1713343911823"></a><a name="en-us_topic_0057973126_p1713343911823"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973126_p4563133211823"><a name="en-us_topic_0057973126_p4563133211823"></a><a name="en-us_topic_0057973126_p4563133211823"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973126_p17724747115641"><a name="en-us_topic_0057973126_p17724747115641"></a><a name="en-us_topic_0057973126_p17724747115641"></a>Specifies the template. The template content must use the YAML syntax.</p>
</td>
</tr>
<tr id="en-us_topic_0057973126_row1298961811738"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973126_p6365223611823"><a name="en-us_topic_0057973126_p6365223611823"></a><a name="en-us_topic_0057973126_p6365223611823"></a>template_url</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p1423124112393"><a name="p1423124112393"></a><a name="p1423124112393"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973126_p5555746311823"><a name="en-us_topic_0057973126_p5555746311823"></a><a name="en-us_topic_0057973126_p5555746311823"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973126_p3030570111823"><a name="en-us_topic_0057973126_p3030570111823"></a><a name="en-us_topic_0057973126_p3030570111823"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973126_p386065911823"><a name="en-us_topic_0057973126_p386065911823"></a><a name="en-us_topic_0057973126_p386065911823"></a>Specifies the template URL. You cannot select a template using the URL temporarily.</p>
</td>
</tr>
<tr id="en-us_topic_0057973126_row4482092111738"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973126_p6295731811823"><a name="en-us_topic_0057973126_p6295731811823"></a><a name="en-us_topic_0057973126_p6295731811823"></a>environment</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p8423184117391"><a name="p8423184117391"></a><a name="p8423184117391"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973126_p6637801811823"><a name="en-us_topic_0057973126_p6637801811823"></a><a name="en-us_topic_0057973126_p6637801811823"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973126_p791041111823"><a name="en-us_topic_0057973126_p791041111823"></a><a name="en-us_topic_0057973126_p791041111823"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973126_p3676356011823"><a name="en-us_topic_0057973126_p3676356011823"></a><a name="en-us_topic_0057973126_p3676356011823"></a>Specifies information about the environment for creating a stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973126_row4718075611738"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973126_p2419902911823"><a name="en-us_topic_0057973126_p2419902911823"></a><a name="en-us_topic_0057973126_p2419902911823"></a>files</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p104231641123917"><a name="p104231641123917"></a><a name="p104231641123917"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973126_p1396432411823"><a name="en-us_topic_0057973126_p1396432411823"></a><a name="en-us_topic_0057973126_p1396432411823"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973126_p5736848411823"><a name="en-us_topic_0057973126_p5736848411823"></a><a name="en-us_topic_0057973126_p5736848411823"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973126_p1633564511823"><a name="en-us_topic_0057973126_p1633564511823"></a><a name="en-us_topic_0057973126_p1633564511823"></a>Specifies the files referenced in the environment.</p>
</td>
</tr>
<tr id="en-us_topic_0057973126_row99502011738"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973126_p3041635811823"><a name="en-us_topic_0057973126_p3041635811823"></a><a name="en-us_topic_0057973126_p3041635811823"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p442311417393"><a name="p442311417393"></a><a name="p442311417393"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973126_p4780590611823"><a name="en-us_topic_0057973126_p4780590611823"></a><a name="en-us_topic_0057973126_p4780590611823"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973126_p4707320311823"><a name="en-us_topic_0057973126_p4707320311823"></a><a name="en-us_topic_0057973126_p4707320311823"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973126_p5483313711823"><a name="en-us_topic_0057973126_p5483313711823"></a><a name="en-us_topic_0057973126_p5483313711823"></a>Specifies parameter information of the stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973126_row5970737811738"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973126_p4358325011823"><a name="en-us_topic_0057973126_p4358325011823"></a><a name="en-us_topic_0057973126_p4358325011823"></a>timeout_mins</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p15423241203910"><a name="p15423241203910"></a><a name="p15423241203910"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973126_p4058232511823"><a name="en-us_topic_0057973126_p4058232511823"></a><a name="en-us_topic_0057973126_p4058232511823"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973126_p6594293011823"><a name="en-us_topic_0057973126_p6594293011823"></a><a name="en-us_topic_0057973126_p6594293011823"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973126_p3977710311823"><a name="en-us_topic_0057973126_p3977710311823"></a><a name="en-us_topic_0057973126_p3977710311823"></a>Specifies the timeout duration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973126_row164156811738"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973126_p647903411823"><a name="en-us_topic_0057973126_p647903411823"></a><a name="en-us_topic_0057973126_p647903411823"></a>disable_rollback</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.2 "><p id="p1842334115398"><a name="p1842334115398"></a><a name="p1842334115398"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973126_p5503971111823"><a name="en-us_topic_0057973126_p5503971111823"></a><a name="en-us_topic_0057973126_p5503971111823"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973126_p2903158411823"><a name="en-us_topic_0057973126_p2903158411823"></a><a name="en-us_topic_0057973126_p2903158411823"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973126_p274813511823"><a name="en-us_topic_0057973126_p274813511823"></a><a name="en-us_topic_0057973126_p274813511823"></a>Specifies whether to perform a rollback when a stack update fails.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973126_section29796213"></a>

N/A

## Request Example<a name="en-us_topic_0057973126_section66839330"></a>

```
PUT /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306
{
    "template": {
        "heat_template_version": "2013-05-23",
        "description": "Create a simple stack",
        "parameters": {
            "flavor": {
                "default": "m1.tiny",
                "type": "string"
            }
        },
        "resources": {
            "hello_world": {
                "type": "OS::Nova::Server",
                "properties": {
                    "key_name": "heat_key",
                    "flavor": {
                        "get_param": "flavor"
                    },
                    "image": "40be8d1a-3eb9-40de-8abd-43237517384f",
                    "user_data": "#!/bin/bash -xv\necho \"hello world\" > /root/hello-world.txt\n"
                }
            }
        }
    },
    "parameters": {
        "flavor": "m1.small"
    }
}
```

## Response Example<a name="en-us_topic_0057973126_section64683061"></a>

None

## Return Code<a name="en-us_topic_0057973126_section45276639"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0057973117_p13413377194057"></a>Return Code</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0057973117_p25449701194057"></a><strong id="b2124121085318"><a name="b2124121085318"></a><a name="b2124121085318"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973126_p40181483194449"><a name="en-us_topic_0057973126_p40181483194449"></a><a name="en-us_topic_0057973126_p40181483194449"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973126_p33474668194449"><a name="en-us_topic_0057973126_p33474668194449"></a><a name="en-us_topic_0057973126_p33474668194449"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973126_p27093619194449"><a name="en-us_topic_0057973126_p27093619194449"></a><a name="en-us_topic_0057973126_p27093619194449"></a>The request has been accepted, but the processing is not complete.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
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

