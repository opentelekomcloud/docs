# Creating a Stack<a name="EN-US_TOPIC_0084581286"></a>

## Function<a name="en-us_topic_0057973121_section35971064"></a>

This API is used to create a stack. Heat verifies a request body and parses the template. After that, Heat invokes the API of the target component based on resource dependencies to create a resource.

## URI<a name="en-us_topic_0057973121_section55304127"></a>

POST /v1/\{project\_id\}/stacks

For details about the parameters, see  [Table 1](#table1759528275).

**Table  1**  Parameter description

<a name="table1759528275"></a>
<table><thead align="left"><tr id="row26011272716"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p43085863"><a name="p43085863"></a><a name="p43085863"></a><strong id="b866332313557"><a name="b866332313557"></a><a name="b866332313557"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p12821133562718"><a name="p12821133562718"></a><a name="p12821133562718"></a><strong id="b572942705517"><a name="b572942705517"></a><a name="b572942705517"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p294000"><a name="p294000"></a><a name="p294000"></a><strong id="b290022835514"><a name="b290022835514"></a><a name="b290022835514"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p23814038"><a name="p23814038"></a><a name="p23814038"></a><strong id="b1042131095612"><a name="b1042131095612"></a><a name="b1042131095612"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10601725277"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14468758"><a name="p14468758"></a><a name="p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1581811351277"><a name="p1581811351277"></a><a name="p1581811351277"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p31118786"><a name="p31118786"></a><a name="p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Parameter<a name="en-us_topic_0057973121_section27975100"></a>

<a name="en-us_topic_0057973121_table66651251"></a>
<table><thead align="left"><tr id="en-us_topic_0057973121_row6890438"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.6.1.1"><p id="en-us_topic_0057973121_p21254616"><a name="en-us_topic_0057973121_p21254616"></a><a name="en-us_topic_0057973121_p21254616"></a><strong id="b19783623205610"><a name="b19783623205610"></a><a name="b19783623205610"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.2"><p id="p14932214133918"><a name="p14932214133918"></a><a name="p14932214133918"></a><strong id="b1955010276567"><a name="b1955010276567"></a><a name="b1955010276567"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.3"><p id="en-us_topic_0057973121_p43902359"><a name="en-us_topic_0057973121_p43902359"></a><a name="en-us_topic_0057973121_p43902359"></a><strong id="b1499813017561"><a name="b1499813017561"></a><a name="b1499813017561"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.4"><p id="en-us_topic_0057973121_p66430186"><a name="en-us_topic_0057973121_p66430186"></a><a name="en-us_topic_0057973121_p66430186"></a><strong id="b595213155613"><a name="b595213155613"></a><a name="b595213155613"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.6.1.5"><p id="en-us_topic_0057973121_p12135994"><a name="en-us_topic_0057973121_p12135994"></a><a name="en-us_topic_0057973121_p12135994"></a><strong id="b11431183655615"><a name="b11431183655615"></a><a name="b11431183655615"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973121_row43491438"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p33145583"><a name="en-us_topic_0057973121_p33145583"></a><a name="en-us_topic_0057973121_p33145583"></a>stack_name</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p192324314345"><a name="p192324314345"></a><a name="p192324314345"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p437668"><a name="en-us_topic_0057973121_p437668"></a><a name="en-us_topic_0057973121_p437668"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p35451125"><a name="en-us_topic_0057973121_p35451125"></a><a name="en-us_topic_0057973121_p35451125"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973121_p52968908"><a name="en-us_topic_0057973121_p52968908"></a><a name="en-us_topic_0057973121_p52968908"></a>Specifies the stack name.</p>
<a name="ul45291469124"></a><a name="ul45291469124"></a><ul id="ul45291469124"><li>The value can contain only uppercase letters, lowercase letters, digits, hyphens (-), periods (.), and underscores (_).</li><li>The value must start with an uppercase letter or a lowercase letter.</li><li>The value can contain 1 to 255 characters.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0057973121_row6958124"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p26737156"><a name="en-us_topic_0057973121_p26737156"></a><a name="en-us_topic_0057973121_p26737156"></a>template</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1123143193418"><a name="p1123143193418"></a><a name="p1123143193418"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p18226004"><a name="en-us_topic_0057973121_p18226004"></a><a name="en-us_topic_0057973121_p18226004"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p67020229"><a name="en-us_topic_0057973121_p67020229"></a><a name="en-us_topic_0057973121_p67020229"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="p2684529103115"><a name="p2684529103115"></a><a name="p2684529103115"></a>Specifies the template. The template uses the YAML syntax for content orchestration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973121_row2494326"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p713839"><a name="en-us_topic_0057973121_p713839"></a><a name="en-us_topic_0057973121_p713839"></a>template_url</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1223144318346"><a name="p1223144318346"></a><a name="p1223144318346"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p57820997"><a name="en-us_topic_0057973121_p57820997"></a><a name="en-us_topic_0057973121_p57820997"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p65609144115231"><a name="en-us_topic_0057973121_p65609144115231"></a><a name="en-us_topic_0057973121_p65609144115231"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973121_p52989151"><a name="en-us_topic_0057973121_p52989151"></a><a name="en-us_topic_0057973121_p52989151"></a>Specifies the template URL. You cannot select a template using the URL temporarily.</p>
</td>
</tr>
<tr id="en-us_topic_0057973121_row7140313"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p41494485"><a name="en-us_topic_0057973121_p41494485"></a><a name="en-us_topic_0057973121_p41494485"></a>environment</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p1523443163412"><a name="p1523443163412"></a><a name="p1523443163412"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p5610121"><a name="en-us_topic_0057973121_p5610121"></a><a name="en-us_topic_0057973121_p5610121"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p51766686"><a name="en-us_topic_0057973121_p51766686"></a><a name="en-us_topic_0057973121_p51766686"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973121_p32352060"><a name="en-us_topic_0057973121_p32352060"></a><a name="en-us_topic_0057973121_p32352060"></a>Specifies the environment information for creating a stack. </p>
</td>
</tr>
<tr id="en-us_topic_0057973121_row22733085"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p29440602"><a name="en-us_topic_0057973121_p29440602"></a><a name="en-us_topic_0057973121_p29440602"></a>files</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p15231432346"><a name="p15231432346"></a><a name="p15231432346"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p35878580"><a name="en-us_topic_0057973121_p35878580"></a><a name="en-us_topic_0057973121_p35878580"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p20483858"><a name="en-us_topic_0057973121_p20483858"></a><a name="en-us_topic_0057973121_p20483858"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973121_p48579805"><a name="en-us_topic_0057973121_p48579805"></a><a name="en-us_topic_0057973121_p48579805"></a>Specifies the files referenced in the environment. </p>
</td>
</tr>
<tr id="en-us_topic_0057973121_row34565062"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p48306655"><a name="en-us_topic_0057973121_p48306655"></a><a name="en-us_topic_0057973121_p48306655"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p172313432345"><a name="p172313432345"></a><a name="p172313432345"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p20524952"><a name="en-us_topic_0057973121_p20524952"></a><a name="en-us_topic_0057973121_p20524952"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p51908377"><a name="en-us_topic_0057973121_p51908377"></a><a name="en-us_topic_0057973121_p51908377"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973121_p43829003"><a name="en-us_topic_0057973121_p43829003"></a><a name="en-us_topic_0057973121_p43829003"></a>Specifies parameter information of the stack.</p>
</td>
</tr>
<tr id="en-us_topic_0057973121_row58916709"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p7524163"><a name="en-us_topic_0057973121_p7524163"></a><a name="en-us_topic_0057973121_p7524163"></a>timeout_mins</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p192384318341"><a name="p192384318341"></a><a name="p192384318341"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p5477477"><a name="en-us_topic_0057973121_p5477477"></a><a name="en-us_topic_0057973121_p5477477"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p41022516"><a name="en-us_topic_0057973121_p41022516"></a><a name="en-us_topic_0057973121_p41022516"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973121_p34489495"><a name="en-us_topic_0057973121_p34489495"></a><a name="en-us_topic_0057973121_p34489495"></a>Specifies the timeout duration.</p>
</td>
</tr>
<tr id="en-us_topic_0057973121_row41970004"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.6.1.1 "><p id="en-us_topic_0057973121_p44127153"><a name="en-us_topic_0057973121_p44127153"></a><a name="en-us_topic_0057973121_p44127153"></a>disable_rollback</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.2 "><p id="p623743163416"><a name="p623743163416"></a><a name="p623743163416"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="en-us_topic_0057973121_p17529622"><a name="en-us_topic_0057973121_p17529622"></a><a name="en-us_topic_0057973121_p17529622"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.4 "><p id="en-us_topic_0057973121_p10613292"><a name="en-us_topic_0057973121_p10613292"></a><a name="en-us_topic_0057973121_p10613292"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.6.1.5 "><p id="en-us_topic_0057973121_p54370330"><a name="en-us_topic_0057973121_p54370330"></a><a name="en-us_topic_0057973121_p54370330"></a>Specifies whether to perform a rollback when stack creation fails.</p>
</td>
</tr>
</tbody>
</table>

**environment**  structure information

<a name="table25216525290"></a>
<table><thead align="left"><tr id="row7522852162919"><th class="cellrowborder" valign="top" width="18.23182318231823%" id="mcps1.1.6.1.1"><p id="p193675374306"><a name="p193675374306"></a><a name="p193675374306"></a><strong id="b1734912215412"><a name="b1734912215412"></a><a name="b1734912215412"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.271227122712272%" id="mcps1.1.6.1.2"><p id="p9370113711305"><a name="p9370113711305"></a><a name="p9370113711305"></a><strong id="b23265261742"><a name="b23265261742"></a><a name="b23265261742"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.181618161816182%" id="mcps1.1.6.1.3"><p id="p1337414375304"><a name="p1337414375304"></a><a name="p1337414375304"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.42174217421742%" id="mcps1.1.6.1.4"><p id="p53772037203013"><a name="p53772037203013"></a><a name="p53772037203013"></a><strong id="b1730113301248"><a name="b1730113301248"></a><a name="b1730113301248"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="35.8935893589359%" id="mcps1.1.6.1.5"><p id="p8379173713302"><a name="p8379173713302"></a><a name="p8379173713302"></a><strong id="b158881434346"><a name="b158881434346"></a><a name="b158881434346"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1752245262915"><td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.1.6.1.1 "><p id="p1224425913011"><a name="p1224425913011"></a><a name="p1224425913011"></a>parameters</p>
</td>
<td class="cellrowborder" valign="top" width="12.271227122712272%" headers="mcps1.1.6.1.2 "><p id="p124585920302"><a name="p124585920302"></a><a name="p124585920302"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.181618161816182%" headers="mcps1.1.6.1.3 "><p id="p1245459183017"><a name="p1245459183017"></a><a name="p1245459183017"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="17.42174217421742%" headers="mcps1.1.6.1.4 "><p id="p1424585920308"><a name="p1424585920308"></a><a name="p1424585920308"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="35.8935893589359%" headers="mcps1.1.6.1.5 "><p id="p8245195918304"><a name="p8245195918304"></a><a name="p8245195918304"></a>Specifies the parameters and their values.</p>
</td>
</tr>
<tr id="row45221052142919"><td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.1.6.1.1 "><p id="p1524512597307"><a name="p1524512597307"></a><a name="p1524512597307"></a>parameters_defaults</p>
</td>
<td class="cellrowborder" valign="top" width="12.271227122712272%" headers="mcps1.1.6.1.2 "><p id="p32454595300"><a name="p32454595300"></a><a name="p32454595300"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.181618161816182%" headers="mcps1.1.6.1.3 "><p id="p8245105963010"><a name="p8245105963010"></a><a name="p8245105963010"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="17.42174217421742%" headers="mcps1.1.6.1.4 "><p id="p72451659163011"><a name="p72451659163011"></a><a name="p72451659163011"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="35.8935893589359%" headers="mcps1.1.6.1.5 "><p id="p02451059153015"><a name="p02451059153015"></a><a name="p02451059153015"></a>Specifies the parameters and their default values.</p>
</td>
</tr>
<tr id="row0522175217296"><td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.1.6.1.1 "><p id="p7714116153118"><a name="p7714116153118"></a><a name="p7714116153118"></a>resource_registry</p>
</td>
<td class="cellrowborder" valign="top" width="12.271227122712272%" headers="mcps1.1.6.1.2 "><p id="p77141964318"><a name="p77141964318"></a><a name="p77141964318"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="16.181618161816182%" headers="mcps1.1.6.1.3 "><p id="p1671419653110"><a name="p1671419653110"></a><a name="p1671419653110"></a>Json</p>
</td>
<td class="cellrowborder" valign="top" width="17.42174217421742%" headers="mcps1.1.6.1.4 "><p id="p87141762313"><a name="p87141762313"></a><a name="p87141762313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="35.8935893589359%" headers="mcps1.1.6.1.5 "><p id="p14714461315"><a name="p14714461315"></a><a name="p14714461315"></a>Specifies the custom resource information.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="en-us_topic_0057973121_section50449312"></a>

<a name="table999210913192"></a>
<table><thead align="left"><tr id="row29979919195"><th class="cellrowborder" valign="top" width="18.3%" id="mcps1.1.5.1.1"><p id="p17493122142817"><a name="p17493122142817"></a><a name="p17493122142817"></a><strong id="b24725868162658"><a name="b24725868162658"></a><a name="b24725868162658"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.719999999999999%" id="mcps1.1.5.1.2"><p id="p1887419221879"><a name="p1887419221879"></a><a name="p1887419221879"></a><strong id="b37315868"><a name="b37315868"></a><a name="b37315868"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.98%" id="mcps1.1.5.1.3"><p id="p16493922112813"><a name="p16493922112813"></a><a name="p16493922112813"></a><strong id="b33311119165"><a name="b33311119165"></a><a name="b33311119165"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p1549342213284"><a name="p1549342213284"></a><a name="p1549342213284"></a><strong id="b153228227611"><a name="b153228227611"></a><a name="b153228227611"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row57151015196"><td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.1.5.1.1 "><p id="p5810107190"><a name="p5810107190"></a><a name="p5810107190"></a>stack</p>
</td>
<td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.1.5.1.2 "><p id="p153612459398"><a name="p153612459398"></a><a name="p153612459398"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.1.5.1.3 "><p id="p3101310141920"><a name="p3101310141920"></a><a name="p3101310141920"></a>Dict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p813141001915"><a name="p813141001915"></a><a name="p813141001915"></a>Specifies the stack object.</p>
</td>
</tr>
</tbody>
</table>

**stack**  structure information

<a name="en-us_topic_0057973121_table41920649"></a>
<table><thead align="left"><tr id="en-us_topic_0057973121_row56500278"><th class="cellrowborder" valign="top" width="16.28%" id="mcps1.1.5.1.1"><p id="p393155220405"><a name="p393155220405"></a><a name="p393155220405"></a><strong id="b6834646561"><a name="b6834646561"></a><a name="b6834646561"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.1.5.1.2"><p id="p593355215405"><a name="p593355215405"></a><a name="p593355215405"></a><strong id="b157161251568"><a name="b157161251568"></a><a name="b157161251568"></a>In</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.6%" id="mcps1.1.5.1.3"><p id="p11937155264012"><a name="p11937155264012"></a><a name="p11937155264012"></a><strong id="b50175516610"><a name="b50175516610"></a><a name="b50175516610"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p1494315210407"><a name="p1494315210407"></a><a name="p1494315210407"></a><strong id="b492317581261"><a name="b492317581261"></a><a name="b492317581261"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973121_row12576876"><td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973121_p12094018"><a name="en-us_topic_0057973121_p12094018"></a><a name="en-us_topic_0057973121_p12094018"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p155318616402"><a name="p155318616402"></a><a name="p155318616402"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973121_p40091438"><a name="en-us_topic_0057973121_p40091438"></a><a name="en-us_topic_0057973121_p40091438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973121_p40287329"><a name="en-us_topic_0057973121_p40287329"></a><a name="en-us_topic_0057973121_p40287329"></a>Specifies the stack UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973121_row27041649"><td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057973121_p42889935"><a name="en-us_topic_0057973121_p42889935"></a><a name="en-us_topic_0057973121_p42889935"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.1.5.1.2 "><p id="p2536614013"><a name="p2536614013"></a><a name="p2536614013"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="18.6%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057973121_p51532677"><a name="en-us_topic_0057973121_p51532677"></a><a name="en-us_topic_0057973121_p51532677"></a>List &lt;dict&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057973121_p11440155"><a name="en-us_topic_0057973121_p11440155"></a><a name="en-us_topic_0057973121_p11440155"></a>Specifies the stack URL list.</p>
</td>
</tr>
</tbody>
</table>

## Request Example<a name="en-us_topic_0057973121_section51390628"></a>

```
POST /v1/95d02433133a4c0a87ba6967474a2ad3/stacks
{
    "files": {},
    "disable_rollback": true,
    "parameters": {
        "flavor": "m1.heat"
    },
    "environment": {
        "parameters": {
            "flavor": "m1.heat"
        },
        "parameter_defaults": {
            "flavor": "m1.heat"
        },
        "resource_registry": {
            "OS::Networking::FloatingIP": "OS::Nova::FloatingIP"
        }
    },
    "stack_name": "teststack",
    "template": {
        "heat_template_version": "2013-05-23",
        "description": "Simple template to test heat commands",
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
                    "user_data": "#!/bin/bash -xv\necho \"hello world\" &gt; /root/hello-world.txt\n"
                }
            }
        }
    },
    "timeout_mins": 60
}
```

## Response Example<a name="en-us_topic_0057973121_section59862473"></a>

```
{
    "stack": {
        "id": "c89c4bb3-96cb-4a55-aafa-076a7939a306",
        "links": [
            {
                "href":  "http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306",
                "rel": "self"
            }
        ]
    }
}
```

## Return Code<a name="en-us_topic_0057973121_section1891353"></a>

**Table  2**  Normal return code

<a name="en-us_topic_0057973117_table40445519194057"></a>
<table><thead align="left"><tr id="en-us_topic_0057973117_row42419326194057"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973117_p13413377194057"><a name="en-us_topic_0057973117_p13413377194057"></a><a name="en-us_topic_0057973117_p13413377194057"></a><strong id="b952465016317"><a name="b952465016317"></a><a name="b952465016317"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973117_p12741761194057"><a name="en-us_topic_0057973117_p12741761194057"></a><a name="en-us_topic_0057973117_p12741761194057"></a><strong id="en-us_topic_0057973140_b84235270615814_1"><a name="en-us_topic_0057973140_b84235270615814_1"></a><a name="en-us_topic_0057973140_b84235270615814_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973117_p25449701194057"><a name="en-us_topic_0057973117_p25449701194057"></a><a name="en-us_topic_0057973117_p25449701194057"></a><strong id="en-us_topic_0057973140_b842352706193020"><a name="en-us_topic_0057973140_b842352706193020"></a><a name="en-us_topic_0057973140_b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973117_row48159894194057"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973117_p8637307194057"><a name="en-us_topic_0057973117_p8637307194057"></a><a name="en-us_topic_0057973117_p8637307194057"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973117_p28533244194057"><a name="en-us_topic_0057973117_p28533244194057"></a><a name="en-us_topic_0057973117_p28533244194057"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973117_p29491459194057"><a name="en-us_topic_0057973117_p29491459194057"></a><a name="en-us_topic_0057973117_p29491459194057"></a>The resource has been created and is ready for use.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error return code

<a name="table19512103414"></a>
<table><thead align="left"><tr id="row16955110342"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p129561510144"><a name="p129561510144"></a><a name="p129561510144"></a><strong id="b107291410588"><a name="b107291410588"></a><a name="b107291410588"></a>Return Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p4959810444"><a name="p4959810444"></a><a name="p4959810444"></a><strong id="b2065991605"><a name="b2065991605"></a><a name="b2065991605"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p9959161020418"><a name="p9959161020418"></a><a name="p9959161020418"></a><strong id="b957735195"><a name="b957735195"></a><a name="b957735195"></a>Description</strong></p>
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
<tr id="row16531631121913"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p156541031121913"><a name="p156541031121913"></a><a name="p156541031121913"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p12654183112194"><a name="p12654183112194"></a><a name="p12654183112194"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p1253585513244"><a name="p1253585513244"></a><a name="p1253585513244"></a>The request could not be processed due to a conflict.</p>
</td>
</tr>
</tbody>
</table>

