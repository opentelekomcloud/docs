# Querying Resources of a Stack<a name="EN-US_TOPIC_0084581294"></a>

## Function<a name="en-us_topic_0057973129_section12517393"></a>

This API is used to query resources of a stack.

## URI<a name="en-us_topic_0057973129_section45547679"></a>

GET /v1/\{project\_id\}/stacks/\{stack\_name\}/\{stack\_id\}/resources

>![](/images/icon-note.gif) **NOTE:**   
>This API supports redirection. During the calling, you can specify only  **stack\_name**  or  **stack\_id**.  

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17762534144716"><a name="p17762534144716"></a><a name="p17762534144716"></a><strong id="b1243712261272"><a name="b1243712261272"></a><a name="b1243712261272"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p376433420478"><a name="p376433420478"></a><a name="p376433420478"></a><strong id="b1313132810718"><a name="b1313132810718"></a><a name="b1313132810718"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p15766123474714"><a name="p15766123474714"></a><a name="p15766123474714"></a><strong id="b4101102914715"><a name="b4101102914715"></a><a name="b4101102914715"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p147683349474"><a name="p147683349474"></a><a name="p147683349474"></a><strong id="b1599216321479"><a name="b1599216321479"></a><a name="b1599216321479"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p136901966819"><a name="p136901966819"></a><a name="p136901966819"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1693146782"><a name="p1693146782"></a><a name="p1693146782"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p13695562812"><a name="p13695562812"></a><a name="p13695562812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p26975615811"><a name="p26975615811"></a><a name="p26975615811"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row161097438473"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p7700061689"><a name="p7700061689"></a><a name="p7700061689"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p670219612818"><a name="p670219612818"></a><a name="p670219612818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1570446784"><a name="p1570446784"></a><a name="p1570446784"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p670616613812"><a name="p670616613812"></a><a name="p670616613812"></a>Specifies the stack name.</p>
</td>
</tr>
<tr id="row131851844124918"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p570917616819"><a name="p570917616819"></a><a name="p570917616819"></a>stack_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p157103613818"><a name="p157103613818"></a><a name="p157103613818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p177131365812"><a name="p177131365812"></a><a name="p177131365812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1371519616817"><a name="p1371519616817"></a><a name="p1371519616817"></a>Specifies the stack UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973129_section7275928"></a>

N/A

## Response Parameter<a name="en-us_topic_0057973129_section65483359"></a>

<a name="en-us_topic_0057973129_table65554707"></a>
<table><thead align="left"><tr id="en-us_topic_0057973129_row29979494"><th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.1"><p id="p13701251185014"><a name="p13701251185014"></a><a name="p13701251185014"></a><strong id="b18531915810"><a name="b18531915810"></a><a name="b18531915810"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.291529152915292%" id="mcps1.1.5.1.2"><p id="p13704145119507"><a name="p13704145119507"></a><a name="p13704145119507"></a><strong id="b198185381"><a name="b198185381"></a><a name="b198185381"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.65176517651765%" id="mcps1.1.5.1.3"><p id="p3705151185017"><a name="p3705151185017"></a><a name="p3705151185017"></a><strong id="b5118166185"><a name="b5118166185"></a><a name="b5118166185"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.76517651765175%" id="mcps1.1.5.1.4"><p id="p1371214511507"><a name="p1371214511507"></a><a name="p1371214511507"></a><strong id="b154401491086"><a name="b154401491086"></a><a name="b154401491086"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973129_row51026446"><td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p39501455"><a name="en-us_topic_0057973129_p39501455"></a><a name="en-us_topic_0057973129_p39501455"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="15.291529152915292%" headers="mcps1.1.5.1.2 "><p id="p926164151013"><a name="p926164151013"></a><a name="p926164151013"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.65176517651765%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p45501252"><a name="en-us_topic_0057973129_p45501252"></a><a name="en-us_topic_0057973129_p45501252"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.76517651765175%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p33488748"><a name="en-us_topic_0057973129_p33488748"></a><a name="en-us_topic_0057973129_p33488748"></a>Specifies resource information of the stack.</p>
</td>
</tr>
</tbody>
</table>

**resources**  structure information

<a name="en-us_topic_0057973129_table50475349111050"></a>
<table><thead align="left"><tr id="en-us_topic_0057973129_row41175655111050"><th class="cellrowborder" valign="top" width="15.659999999999998%" id="mcps1.1.5.1.1"><p id="p1085195995314"><a name="p1085195995314"></a><a name="p1085195995314"></a><strong id="b282612201483"><a name="b282612201483"></a><a name="b282612201483"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.46%" id="mcps1.1.5.1.2"><p id="p19854125911535"><a name="p19854125911535"></a><a name="p19854125911535"></a><strong id="b1774215275810"><a name="b1774215275810"></a><a name="b1774215275810"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.07%" id="mcps1.1.5.1.3"><p id="p11855165911536"><a name="p11855165911536"></a><a name="p11855165911536"></a><strong id="b792112301385"><a name="b792112301385"></a><a name="b792112301385"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51.81%" id="mcps1.1.5.1.4"><p id="p13859125935317"><a name="p13859125935317"></a><a name="p13859125935317"></a><strong id="b7941143320816"><a name="b7941143320816"></a><a name="b7941143320816"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973129_row42901509111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p759129411110"><a name="en-us_topic_0057973129_p759129411110"></a><a name="en-us_topic_0057973129_p759129411110"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p582591420911"><a name="p582591420911"></a><a name="p582591420911"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p1091505411110"><a name="en-us_topic_0057973129_p1091505411110"></a><a name="en-us_topic_0057973129_p1091505411110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p1170419111110"><a name="en-us_topic_0057973129_p1170419111110"></a><a name="en-us_topic_0057973129_p1170419111110"></a>Specifies the resource name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row32859638111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p952988811110"><a name="en-us_topic_0057973129_p952988811110"></a><a name="en-us_topic_0057973129_p952988811110"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p1082571414911"><a name="p1082571414911"></a><a name="p1082571414911"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p3372344911110"><a name="en-us_topic_0057973129_p3372344911110"></a><a name="en-us_topic_0057973129_p3372344911110"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p4724484711110"><a name="en-us_topic_0057973129_p4724484711110"></a><a name="en-us_topic_0057973129_p4724484711110"></a>Specifies the resource URL list.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row22674562111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p1464632311110"><a name="en-us_topic_0057973129_p1464632311110"></a><a name="en-us_topic_0057973129_p1464632311110"></a>logical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p882518141893"><a name="p882518141893"></a><a name="p882518141893"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p4550151911110"><a name="en-us_topic_0057973129_p4550151911110"></a><a name="en-us_topic_0057973129_p4550151911110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p6174441911110"><a name="en-us_topic_0057973129_p6174441911110"></a><a name="en-us_topic_0057973129_p6174441911110"></a>Specifies the logical resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row48186560111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p4874319811110"><a name="en-us_topic_0057973129_p4874319811110"></a><a name="en-us_topic_0057973129_p4874319811110"></a>physical_resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p2825141412919"><a name="p2825141412919"></a><a name="p2825141412919"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p5588499911110"><a name="en-us_topic_0057973129_p5588499911110"></a><a name="en-us_topic_0057973129_p5588499911110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p3039107611110"><a name="en-us_topic_0057973129_p3039107611110"></a><a name="en-us_topic_0057973129_p3039107611110"></a>Specifies the physical resource ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row36384656111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p916980911110"><a name="en-us_topic_0057973129_p916980911110"></a><a name="en-us_topic_0057973129_p916980911110"></a>resource_type</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p58250144910"><a name="p58250144910"></a><a name="p58250144910"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p455705611110"><a name="en-us_topic_0057973129_p455705611110"></a><a name="en-us_topic_0057973129_p455705611110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p3357728011110"><a name="en-us_topic_0057973129_p3357728011110"></a><a name="en-us_topic_0057973129_p3357728011110"></a>Specifies the resource type.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row42941271111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p5021113811110"><a name="en-us_topic_0057973129_p5021113811110"></a><a name="en-us_topic_0057973129_p5021113811110"></a>resource_status</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p168252141695"><a name="p168252141695"></a><a name="p168252141695"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p4057033811110"><a name="en-us_topic_0057973129_p4057033811110"></a><a name="en-us_topic_0057973129_p4057033811110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p6497191811110"><a name="en-us_topic_0057973129_p6497191811110"></a><a name="en-us_topic_0057973129_p6497191811110"></a>Specifies the resource status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row24585157111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p5277969511110"><a name="en-us_topic_0057973129_p5277969511110"></a><a name="en-us_topic_0057973129_p5277969511110"></a>resource_status_reason</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p1082521411918"><a name="p1082521411918"></a><a name="p1082521411918"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p4729692211110"><a name="en-us_topic_0057973129_p4729692211110"></a><a name="en-us_topic_0057973129_p4729692211110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p584548611110"><a name="en-us_topic_0057973129_p584548611110"></a><a name="en-us_topic_0057973129_p584548611110"></a>Specifies the resource operation reason.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row17511314111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p3350089711110"><a name="en-us_topic_0057973129_p3350089711110"></a><a name="en-us_topic_0057973129_p3350089711110"></a>updated_time</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p1982531417919"><a name="p1982531417919"></a><a name="p1982531417919"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p2921814511110"><a name="en-us_topic_0057973129_p2921814511110"></a><a name="en-us_topic_0057973129_p2921814511110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p1785952511110"><a name="en-us_topic_0057973129_p1785952511110"></a><a name="en-us_topic_0057973129_p1785952511110"></a>Specifies the time when the resource was updated.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row57290023115723"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p41410601115723"><a name="en-us_topic_0057973129_p41410601115723"></a><a name="en-us_topic_0057973129_p41410601115723"></a>creation_time</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p128254141098"><a name="p128254141098"></a><a name="p128254141098"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p57743576115723"><a name="en-us_topic_0057973129_p57743576115723"></a><a name="en-us_topic_0057973129_p57743576115723"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p12535162115723"><a name="en-us_topic_0057973129_p12535162115723"></a><a name="en-us_topic_0057973129_p12535162115723"></a>Specifies the time when the resource was created.</p>
</td>
</tr>
<tr id="en-us_topic_0057973129_row51390524111050"><td class="cellrowborder" valign="top" width="15.659999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973129_p47440611110"><a name="en-us_topic_0057973129_p47440611110"></a><a name="en-us_topic_0057973129_p47440611110"></a>required_by</p>
</td>
<td class="cellrowborder" valign="top" width="14.46%" headers="mcps1.1.5.1.2 "><p id="p4826171411910"><a name="p4826171411910"></a><a name="p4826171411910"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.07%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973129_p3842693211110"><a name="en-us_topic_0057973129_p3842693211110"></a><a name="en-us_topic_0057973129_p3842693211110"></a>List &lt;str&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="51.81%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973129_p2557382711110"><a name="en-us_topic_0057973129_p2557382711110"></a><a name="en-us_topic_0057973129_p2557382711110"></a>Specifies the resource dependency.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973129_section52479324"></a>

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources
```

## Response Example<a name="en-us_topic_0057973129_section2551872"></a>

```
{
    "resources": [
        {
            "resource_name": "instacne_port",
            "links": [
                {
                    "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources/instacne_port",
                    "rel": "self"
                 },
                {
                    "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306",
                    "rel": "stack"
                 }
            ],
            "logical_resource_id": "instacne_port",
            "resource_status_reason": "state changed",
            "updated_time": "2014-01-27T16:28:03Z",
            "required_by": ["my_instance"],
            "resource_status": "RESUME_COMPLETE",
            "physical_resource_id": "202307c7-d10e-4bcf-af85-6253f5d6b022",
            "resource_type": "OS::Neutron::Port"
        },
        {
            "resource_name": "my_instance",
            "links": [
                {
                    "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306/resources/my_instance",
                    "rel": "self"
                 },
                {
                    "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306",
                    "rel": "stack"
                 }
            ],
            "logical_resource_id": "my_instance",
            "resource_status_reason": "state changed",
            "updated_time": "2014-01-27T16:28:06Z",
            "required_by": [],
            "resource_status": "RESUME_COMPLETE",
            "physical_resource_id": "e722ad16-ff09-4622-aa5c-0466ae4ef8d8",
            "resource_type": "OS::Nova::Server"
        }
    ]
}
```

## Return Code<a name="en-us_topic_0057973129_section22966852"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0084581290_en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0084581290_en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0084581290_en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0084581290_en-us_topic_0057973117_p13413377194057"></a><strong id="en-us_topic_0084581290_b731785218616"><a name="en-us_topic_0084581290_b731785218616"></a><a name="en-us_topic_0084581290_b731785218616"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0084581290_en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0084581290_en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0084581290_en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0084581290_en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0084581290_en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0084581290_en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0084581290_en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0084581290_en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0084581290_en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0084581290_en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0084581290_en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0084581290_en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0084581290_en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_en-us_topic_0057973124_p9904457194351"><a name="en-us_topic_0084581290_en-us_topic_0057973124_p9904457194351"></a><a name="en-us_topic_0084581290_en-us_topic_0057973124_p9904457194351"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_en-us_topic_0057973124_p64063566194351"><a name="en-us_topic_0084581290_en-us_topic_0057973124_p64063566194351"></a><a name="en-us_topic_0084581290_en-us_topic_0057973124_p64063566194351"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_en-us_topic_0057973124_p21766343194351"><a name="en-us_topic_0084581290_en-us_topic_0057973124_p21766343194351"></a><a name="en-us_topic_0084581290_en-us_topic_0057973124_p21766343194351"></a>Request was successful.</p>
</td>
</tr>
<tr id="en-us_topic_0084581290_row18143162895914"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0084581290_p52068209206"><a name="en-us_topic_0084581290_p52068209206"></a><a name="en-us_topic_0084581290_p52068209206"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0084581290_p52061120172014"><a name="en-us_topic_0084581290_p52061120172014"></a><a name="en-us_topic_0084581290_p52061120172014"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0084581290_p620662018205"><a name="en-us_topic_0084581290_p620662018205"></a><a name="en-us_topic_0084581290_p620662018205"></a>The response is about redirection. The response header usually contains a location value that allows you to track the real location of the resource.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b1235759101013"><a name="b1235759101013"></a><a name="b1235759101013"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
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
<tr id="row181330274199"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p18134027201912"><a name="p18134027201912"></a><a name="p18134027201912"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p1713419274191"><a name="p1713419274191"></a><a name="p1713419274191"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p11134162718196"><a name="p11134162718196"></a><a name="p11134162718196"></a>Authorization failed.</p>
</td>
</tr>
<tr id="row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973122_p5338333194217"><a name="en-us_topic_0057973122_p5338333194217"></a><a name="en-us_topic_0057973122_p5338333194217"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p125520290312"><a name="p125520290312"></a><a name="p125520290312"></a>Not found</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973122_p29751790194217"><a name="en-us_topic_0057973122_p29751790194217"></a><a name="en-us_topic_0057973122_p29751790194217"></a>The requested resources are not found.</p>
</td>
</tr>
</tbody>
</table>

