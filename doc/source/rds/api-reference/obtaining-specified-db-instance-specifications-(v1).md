# Obtaining Specified DB Instance Specifications<a name="en-us_topic_0056890256"></a>

## Function<a name="section44230431101549"></a>

This API is used to obtain DB instance specifications of a specified specification ID.

## URI<a name="section31729879101549"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/flavors/\{flavorId\}

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table23140016101549"></a>
    <table><thead align="left"><tr id="row27795795101549"><th class="cellrowborder" valign="top" width="21.25%" id="mcps1.2.4.1.1"><p id="p36866898101549"><a name="p36866898101549"></a><a name="p36866898101549"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.38%" id="mcps1.2.4.1.2"><p id="p33428750101549"><a name="p33428750101549"></a><a name="p33428750101549"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.370000000000005%" id="mcps1.2.4.1.3"><p id="p23374190101549"><a name="p23374190101549"></a><a name="p23374190101549"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14261210101549"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p14307387101549"><a name="p14307387101549"></a><a name="p14307387101549"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.38%" headers="mcps1.2.4.1.2 "><p id="p18047737101549"><a name="p18047737101549"></a><a name="p18047737101549"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.370000000000005%" headers="mcps1.2.4.1.3 "><p id="p52580603101549"><a name="p52580603101549"></a><a name="p52580603101549"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row556889316231"><td class="cellrowborder" valign="top" width="21.25%" headers="mcps1.2.4.1.1 "><p id="p6457320716239"><a name="p6457320716239"></a><a name="p6457320716239"></a>flavorId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.38%" headers="mcps1.2.4.1.2 "><p id="p6304726516239"><a name="p6304726516239"></a><a name="p6304726516239"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.370000000000005%" headers="mcps1.2.4.1.3 "><p id="p417079116231"><a name="p417079116231"></a><a name="p417079116231"></a>Specifies the specification ID.</p>
    <p id="p64139204162316"><a name="p64139204162316"></a><a name="p64139204162316"></a>When this parameter is empty, the URLs of all DB instance specifications are obtained. For details, see <span class="parmname" id="parmname1015220599105"><a name="parmname1015220599105"></a><a name="parmname1015220599105"></a><b>str_id</b></span> in <span class="parmname" id="parmname47834231116"><a name="parmname47834231116"></a><a name="parmname47834231116"></a><b>flavors</b></span> in section <a href="obtaining-all-db-instance-specifications-18.md">Obtaining All DB Instance Specifications</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Currently, only the DB engines MySQL and PostgreSQL are supported by the API.


## Request<a name="section28070818101549"></a>

None

## Normal Response<a name="section62531952101549"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table37458421101549"></a>
    <table><thead align="left"><tr id="row57880533101549"><th class="cellrowborder" valign="top" width="21.64%" id="mcps1.2.4.1.1"><p id="p57811625101549"><a name="p57811625101549"></a><a name="p57811625101549"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.25%" id="mcps1.2.4.1.2"><p id="p52230049101549"><a name="p52230049101549"></a><a name="p52230049101549"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.11%" id="mcps1.2.4.1.3"><p id="p2775590101549"><a name="p2775590101549"></a><a name="p2775590101549"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63972357101549"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p14378425101549"><a name="p14378425101549"></a><a name="p14378425101549"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p23801806101549"><a name="p23801806101549"></a><a name="p23801806101549"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p48898156101549"><a name="p48898156101549"></a><a name="p48898156101549"></a>Indicates the memory specifications in GB.</p>
    </td>
    </tr>
    <tr id="row37430221101549"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p11949066101549"><a name="p11949066101549"></a><a name="p11949066101549"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p28350308101549"><a name="p28350308101549"></a><a name="p28350308101549"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p14673602101549"><a name="p14673602101549"></a><a name="p14673602101549"></a>Indicates the specification ID (Int type). Its default value is <strong id="b842352706114710"><a name="b842352706114710"></a><a name="b842352706114710"></a>1</strong> because RDS uses UUID to store the specification ID and cannot convert it to the Int type.</p>
    </td>
    </tr>
    <tr id="row64953558101549"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p26746870101549"><a name="p26746870101549"></a><a name="p26746870101549"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p19012879101549"><a name="p19012879101549"></a><a name="p19012879101549"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p63648200101549"><a name="p63648200101549"></a><a name="p63648200101549"></a>Indicates the link address.</p>
    </td>
    </tr>
    <tr id="row55230537101549"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p44488507101549"><a name="p44488507101549"></a><a name="p44488507101549"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p46799301101549"><a name="p46799301101549"></a><a name="p46799301101549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p32647056101549"><a name="p32647056101549"></a><a name="p32647056101549"></a>Indicates the specification item name.</p>
    </td>
    </tr>
    <tr id="row4160090011234"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p6120435811252"><a name="p6120435811252"></a><a name="p6120435811252"></a>str_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p5860598511252"><a name="p5860598511252"></a><a name="p5860598511252"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p4946435711252"><a name="p4946435711252"></a><a name="p4946435711252"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    <tr id="row47070999145632"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p36569660145641"><a name="p36569660145641"></a><a name="p36569660145641"></a>flavor_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p64947236145632"><a name="p64947236145632"></a><a name="p64947236145632"></a>List data structure. For details, see <a href="#table6215887215014">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p26234743145632"><a name="p26234743145632"></a><a name="p26234743145632"></a>Indicates the specification information.</p>
    </td>
    </tr>
    <tr id="row60274269145636"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p50377617145636"><a name="p50377617145636"></a><a name="p50377617145636"></a>price_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p54055206145636"><a name="p54055206145636"></a><a name="p54055206145636"></a>List data structure. For details, see <a href="#table6260788515016">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p16395588145636"><a name="p16395588145636"></a><a name="p16395588145636"></a>Indicates the price information.</p>
    </td>
    </tr>
    <tr id="row3177911615837"><td class="cellrowborder" valign="top" width="21.64%" headers="mcps1.2.4.1.1 "><p id="p2397160015837"><a name="p2397160015837"></a><a name="p2397160015837"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.25%" headers="mcps1.2.4.1.2 "><p id="p6265147715837"><a name="p6265147715837"></a><a name="p6265147715837"></a>Dictionary data structure. For details, see <a href="#table497927581596">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.11%" headers="mcps1.2.4.1.3 "><p id="p4160489915837"><a name="p4160489915837"></a><a name="p4160489915837"></a>Indicates the embedded specification information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  links field data structure description

    <a name="table25388053101549"></a>
    <table><thead align="left"><tr id="row6032865101549"><th class="cellrowborder" valign="top" width="22.009999999999998%" id="mcps1.2.4.1.1"><p id="p18900038101549"><a name="p18900038101549"></a><a name="p18900038101549"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.110000000000003%" id="mcps1.2.4.1.2"><p id="p54508124101549"><a name="p54508124101549"></a><a name="p54508124101549"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.88%" id="mcps1.2.4.1.3"><p id="p53081930101549"><a name="p53081930101549"></a><a name="p53081930101549"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7679206101549"><td class="cellrowborder" valign="top" width="22.009999999999998%" headers="mcps1.2.4.1.1 "><p id="p18035950101549"><a name="p18035950101549"></a><a name="p18035950101549"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p51625859101549"><a name="p51625859101549"></a><a name="p51625859101549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.88%" headers="mcps1.2.4.1.3 "><p id="p20945036101549"><a name="p20945036101549"></a><a name="p20945036101549"></a>Indicates the link property.</p>
    </td>
    </tr>
    <tr id="row703888311359"><td class="cellrowborder" valign="top" width="22.009999999999998%" headers="mcps1.2.4.1.1 "><p id="p4425720211426"><a name="p4425720211426"></a><a name="p4425720211426"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.110000000000003%" headers="mcps1.2.4.1.2 "><p id="p2806364211426"><a name="p2806364211426"></a><a name="p2806364211426"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.88%" headers="mcps1.2.4.1.3 "><p id="p5856251411426"><a name="p5856251411426"></a><a name="p5856251411426"></a>Indicates the API link. Its value is <strong id="b842352706182645"><a name="b842352706182645"></a><a name="b842352706182645"></a>""</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  flavor\_detail field data structure description

    <a name="table6215887215014"></a>
    <table><thead align="left"><tr id="row1683573215014"><th class="cellrowborder" valign="top" width="21.447855214478555%" id="mcps1.2.4.1.1"><p id="p2151706915014"><a name="p2151706915014"></a><a name="p2151706915014"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.2970702929707%" id="mcps1.2.4.1.2"><p id="p6516099815014"><a name="p6516099815014"></a><a name="p6516099815014"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.25507449255074%" id="mcps1.2.4.1.3"><p id="p4354944715014"><a name="p4354944715014"></a><a name="p4354944715014"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3784431315014"><td class="cellrowborder" valign="top" width="21.447855214478555%" headers="mcps1.2.4.1.1 "><p id="p4549049915014"><a name="p4549049915014"></a><a name="p4549049915014"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2970702929707%" headers="mcps1.2.4.1.2 "><p id="p6085182215014"><a name="p6085182215014"></a><a name="p6085182215014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.25507449255074%" headers="mcps1.2.4.1.3 "><p id="p3005056215014"><a name="p3005056215014"></a><a name="p3005056215014"></a>Indicates the specification name, such a cpu or mem.</p>
    </td>
    </tr>
    <tr id="row201960215014"><td class="cellrowborder" valign="top" width="21.447855214478555%" headers="mcps1.2.4.1.1 "><p id="p2937006915014"><a name="p2937006915014"></a><a name="p2937006915014"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.2970702929707%" headers="mcps1.2.4.1.2 "><p id="p3016539715014"><a name="p3016539715014"></a><a name="p3016539715014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.25507449255074%" headers="mcps1.2.4.1.3 "><p id="p2747807315014"><a name="p2747807315014"></a><a name="p2747807315014"></a>Indicates the specification item value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  price\_detail field data structure description

    <a name="table6260788515016"></a>
    <table><thead align="left"><tr id="row1153918115016"><th class="cellrowborder" valign="top" width="21.46%" id="mcps1.2.4.1.1"><p id="p6225848115016"><a name="p6225848115016"></a><a name="p6225848115016"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.220000000000002%" id="mcps1.2.4.1.2"><p id="p977216415016"><a name="p977216415016"></a><a name="p977216415016"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.32%" id="mcps1.2.4.1.3"><p id="p5334785715016"><a name="p5334785715016"></a><a name="p5334785715016"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2620915015016"><td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.4.1.1 "><p id="p4256638715016"><a name="p4256638715016"></a><a name="p4256638715016"></a>timeUnit</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p2532533715016"><a name="p2532533715016"></a><a name="p2532533715016"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.2.4.1.3 "><p id="p3808642315016"><a name="p3808642315016"></a><a name="p3808642315016"></a>Indicates the pricing unit.</p>
    </td>
    </tr>
    <tr id="row723349515016"><td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.4.1.1 "><p id="p4904225415016"><a name="p4904225415016"></a><a name="p4904225415016"></a>price</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1299960015016"><a name="p1299960015016"></a><a name="p1299960015016"></a>Float</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.2.4.1.3 "><p id="p4633469515016"><a name="p4633469515016"></a><a name="p4633469515016"></a>Indicates the unit price.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  flavor field data structure description

    <a name="table497927581596"></a>
    <table><thead align="left"><tr id="row78856391596"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.2.4.1.1"><p id="p347570181596"><a name="p347570181596"></a><a name="p347570181596"></a><strong id="b84235270691445_13"><a name="b84235270691445_13"></a><a name="b84235270691445_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.06%" id="mcps1.2.4.1.2"><p id="p638550821596"><a name="p638550821596"></a><a name="p638550821596"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.760000000000005%" id="mcps1.2.4.1.3"><p id="p48791341596"><a name="p48791341596"></a><a name="p48791341596"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row596337561596"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.2.4.1.1 "><p id="p55464813151015"><a name="p55464813151015"></a><a name="p55464813151015"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.06%" headers="mcps1.2.4.1.2 "><p id="p63464887151015"><a name="p63464887151015"></a><a name="p63464887151015"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.760000000000005%" headers="mcps1.2.4.1.3 "><p id="p40382213151015"><a name="p40382213151015"></a><a name="p40382213151015"></a>Indicates the memory specifications in GB.</p>
    </td>
    </tr>
    <tr id="row3991536315958"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.2.4.1.1 "><p id="p44951233151015"><a name="p44951233151015"></a><a name="p44951233151015"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.06%" headers="mcps1.2.4.1.2 "><p id="p17171274151015"><a name="p17171274151015"></a><a name="p17171274151015"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.760000000000005%" headers="mcps1.2.4.1.3 "><p id="p48695923151015"><a name="p48695923151015"></a><a name="p48695923151015"></a>Indicates the specification ID (Int type). Its default value is <strong id="b23746938191548"><a name="b23746938191548"></a><a name="b23746938191548"></a>1</strong> because RDS uses UUID to store the specification ID and cannot convert it to the Int type.</p>
    </td>
    </tr>
    <tr id="row21332647151021"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.2.4.1.1 "><p id="p8108001151023"><a name="p8108001151023"></a><a name="p8108001151023"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.06%" headers="mcps1.2.4.1.2 "><p id="p52768370151023"><a name="p52768370151023"></a><a name="p52768370151023"></a>List data structure. For details, see <a href="#table25388053101549">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.760000000000005%" headers="mcps1.2.4.1.3 "><p id="p46379616151023"><a name="p46379616151023"></a><a name="p46379616151023"></a>Indicates the link address.</p>
    </td>
    </tr>
    <tr id="row5033941196"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.2.4.1.1 "><p id="p5196942811914"><a name="p5196942811914"></a><a name="p5196942811914"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.06%" headers="mcps1.2.4.1.2 "><p id="p4877410911914"><a name="p4877410911914"></a><a name="p4877410911914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.760000000000005%" headers="mcps1.2.4.1.3 "><p id="p5838871811914"><a name="p5838871811914"></a><a name="p5838871811914"></a>Indicates the specification item name.</p>
    </td>
    </tr>
    <tr id="row3989126411837"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.2.4.1.1 "><p id="p5641325211849"><a name="p5641325211849"></a><a name="p5641325211849"></a>str_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.06%" headers="mcps1.2.4.1.2 "><p id="p607072411849"><a name="p607072411849"></a><a name="p607072411849"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.760000000000005%" headers="mcps1.2.4.1.3 "><p id="p2196665311849"><a name="p2196665311849"></a><a name="p2196665311849"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "ram": 2,
        "id": 1,
        "links": null,
        "name": "rds.pg.c2.medium",
        "str_id": "9ff2a3a5-c859-bbc0-67f7-86ce59432b1d",
        "flavor_detail": [
          {
            "name": "cpu",
            "value": "1"
          },
          {
            "name": "mem",
            "value": "2"
          },
          {
            "name": "flavor",
            "value": "normal1"
          },
          {
            "name": "dbType",
            "value": "MySQL"
          },
          {
            "name": "serverType",
            "value": "XEN"
          }
        ],
        "price_detail": [],
        "flavor": {
          "ram": 2048,
          "id": 1,
          "links": [
            {
              "rel": "self",
              "href": ""
            },
            {
              "rel": "bookmark",
              "href": ""
            }
          ],
          "name": "rds.pg.c2.medium",
          "str_id": "9ff2a3a5-c859-bbc0-67f7-86ce59432b1d"
        }
    }
    ```


## Abnormal Response<a name="section26140549101733"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

