# Creating a Parameter Template<a name="en-us_topic_0056890263"></a>

## Function<a name="section47791537103033"></a>

This API is used to create a parameter template and configure the name, description, DB engine, and parameter values in the parameter template.

## URI<a name="section10530764103033"></a>

-   URI format

    PATH: /v1.0/\{project\_id\}/configurations

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="table31392003103033"></a>
    <table><thead align="left"><tr id="row22007494103033"><th class="cellrowborder" valign="top" width="20.11%" id="mcps1.2.4.1.1"><p id="p37776629103033"><a name="p37776629103033"></a><a name="p37776629103033"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.270000000000003%" id="mcps1.2.4.1.2"><p id="p40008141103033"><a name="p40008141103033"></a><a name="p40008141103033"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.62%" id="mcps1.2.4.1.3"><p id="p19433973103033"><a name="p19433973103033"></a><a name="p19433973103033"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30647957103033"><td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.4.1.1 "><p id="p3660222814559"><a name="p3660222814559"></a><a name="p3660222814559"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.270000000000003%" headers="mcps1.2.4.1.2 "><p id="p563493414559"><a name="p563493414559"></a><a name="p563493414559"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.4.1.3 "><p id="p4111734614559"><a name="p4111734614559"></a><a name="p4111734614559"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions
    -   The name of the created parameter template is case-insensitive and must be different from the name of an existing or a default parameter template.
    -   Currently, the DB engines MySQL and PostgreSQL support creating parameter templates.
    -   The values of the created parameter template must be within the default value range of the specified database version. For details about the range of parameter values, see section "Editing Parameters in a Parameter Template" in the  _Relational Database Service User Guide_.


## Request<a name="section4755253103033"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table49631178103033"></a>
    <table><thead align="left"><tr id="row8183755103033"><th class="cellrowborder" valign="top" width="22.56%" id="mcps1.2.5.1.1"><p id="p58904447103033"><a name="p58904447103033"></a><a name="p58904447103033"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.380000000000003%" id="mcps1.2.5.1.2"><p id="p6530903103033"><a name="p6530903103033"></a><a name="p6530903103033"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.5.1.3"><p id="p59241148103033"><a name="p59241148103033"></a><a name="p59241148103033"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.82%" id="mcps1.2.5.1.4"><p id="p33803669103033"><a name="p33803669103033"></a><a name="p33803669103033"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53742667103033"><td class="cellrowborder" valign="top" width="22.56%" headers="mcps1.2.5.1.1 "><p id="p58188741103033"><a name="p58188741103033"></a><a name="p58188741103033"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.380000000000003%" headers="mcps1.2.5.1.2 "><p id="p15667563103033"><a name="p15667563103033"></a><a name="p15667563103033"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.5.1.3 "><p id="p61113127103033"><a name="p61113127103033"></a><a name="p61113127103033"></a>Dictionary data structure. For details, see <a href="#table54873338103033">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.4 "><p id="p58292820103033"><a name="p58292820103033"></a><a name="p58292820103033"></a>Specifies the parameter template object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  configuration field data structure description

    <a name="table54873338103033"></a>
    <table><thead align="left"><tr id="row13420685103033"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="p86098651502"><a name="p86098651502"></a><a name="p86098651502"></a><strong id="b84235270691445_7"><a name="b84235270691445_7"></a><a name="b84235270691445_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.69%" id="mcps1.2.5.1.2"><p id="p198997441502"><a name="p198997441502"></a><a name="p198997441502"></a><strong id="b842352706102346_7"><a name="b842352706102346_7"></a><a name="b842352706102346_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.69%" id="mcps1.2.5.1.3"><p id="p43311501502"><a name="p43311501502"></a><a name="p43311501502"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.189999999999998%" id="mcps1.2.5.1.4"><p id="p530109381502"><a name="p530109381502"></a><a name="p530109381502"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46084942103033"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p242582601502"><a name="p242582601502"></a><a name="p242582601502"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p469359981502"><a name="p469359981502"></a><a name="p469359981502"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.69%" headers="mcps1.2.5.1.3 "><p id="p390473891502"><a name="p390473891502"></a><a name="p390473891502"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.5.1.4 "><p id="p655709521502"><a name="p655709521502"></a><a name="p655709521502"></a>Specifies the parameter template name. It contains a maximum of 64 characters and can contain only uppercase letters, lowercase letters, digits, hyphens (-), underscores (_), and periods (.).</p>
    </td>
    </tr>
    <tr id="row27132489103033"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p174608551502"><a name="p174608551502"></a><a name="p174608551502"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p189300281502"><a name="p189300281502"></a><a name="p189300281502"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.69%" headers="mcps1.2.5.1.3 "><p id="p258664601502"><a name="p258664601502"></a><a name="p258664601502"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.5.1.4 "><p id="p51293590111420"><a name="p51293590111420"></a><a name="p51293590111420"></a>Specifies the parameter template description. It contains a maximum of 256 characters and does not support the following special characters: !&lt;&gt;='&amp;"</p>
    </td>
    </tr>
    <tr id="row10643754103033"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p497935221502"><a name="p497935221502"></a><a name="p497935221502"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p322018791502"><a name="p322018791502"></a><a name="p322018791502"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.69%" headers="mcps1.2.5.1.3 "><p id="p28979761502"><a name="p28979761502"></a><a name="p28979761502"></a>Dictionary data structure. For details, see <a href="#table48747964103033">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.5.1.4 "><p id="p348705861502"><a name="p348705861502"></a><a name="p348705861502"></a>Specifies the parameter values defined by users based on the default parameter template.</p>
    </td>
    </tr>
    <tr id="row1855344103033"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p610346061502"><a name="p610346061502"></a><a name="p610346061502"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.69%" headers="mcps1.2.5.1.2 "><p id="p408841221502"><a name="p408841221502"></a><a name="p408841221502"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.69%" headers="mcps1.2.5.1.3 "><p id="p103027201502"><a name="p103027201502"></a><a name="p103027201502"></a>Dictionary data structure. For details, see <a href="#table53696705103033">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.189999999999998%" headers="mcps1.2.5.1.4 "><p id="p58203831502"><a name="p58203831502"></a><a name="p58203831502"></a>Specifies the database object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  values field data structure description

    <a name="table48747964103033"></a>
    <table><thead align="left"><tr id="row52952086103033"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.1"><p id="p5169416415048"><a name="p5169416415048"></a><a name="p5169416415048"></a><strong id="b84235270691445_9"><a name="b84235270691445_9"></a><a name="b84235270691445_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.82%" id="mcps1.2.5.1.2"><p id="p6515656115048"><a name="p6515656115048"></a><a name="p6515656115048"></a><strong id="b842352706102346_9"><a name="b842352706102346_9"></a><a name="b842352706102346_9"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.2.5.1.3"><p id="p2435723015048"><a name="p2435723015048"></a><a name="p2435723015048"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.76%" id="mcps1.2.5.1.4"><p id="p1483289015048"><a name="p1483289015048"></a><a name="p1483289015048"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47756916103033"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p5709850215048"><a name="p5709850215048"></a><a name="p5709850215048"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p5091163415048"><a name="p5091163415048"></a><a name="p5091163415048"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.3 "><p id="p2894160515048"><a name="p2894160515048"></a><a name="p2894160515048"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.5.1.4 "><p id="p16861290151316"><a name="p16861290151316"></a><a name="p16861290151316"></a>Specifies the parameter name. For example, in <strong id="b3367863672350"><a name="b3367863672350"></a><a name="b3367863672350"></a>"max_connections": "10"</strong>, the key is <strong id="b7337336272350"><a name="b7337336272350"></a><a name="b7337336272350"></a>max_connections</strong>.</p>
    </td>
    </tr>
    <tr id="row3200365103033"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.1 "><p id="p4463740915048"><a name="p4463740915048"></a><a name="p4463740915048"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p4281541615048"><a name="p4281541615048"></a><a name="p4281541615048"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.5.1.3 "><p id="p476893415048"><a name="p476893415048"></a><a name="p476893415048"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.5.1.4 "><p id="p45216830151316"><a name="p45216830151316"></a><a name="p45216830151316"></a>Specifies the parameter value. For example, in <strong id="b12548790223511"><a name="b12548790223511"></a><a name="b12548790223511"></a>"max_connections": "10"</strong>, the value is <strong id="b144027762523511"><a name="b144027762523511"></a><a name="b144027762523511"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  datastore field data structure description

    <a name="table53696705103033"></a>
    <table><thead align="left"><tr id="row29729671103033"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p5265129815054"><a name="p5265129815054"></a><a name="p5265129815054"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.18718128187181%" id="mcps1.2.5.1.2"><p id="p2835873515054"><a name="p2835873515054"></a><a name="p2835873515054"></a><strong id="b842352706102346_11"><a name="b842352706102346_11"></a><a name="b842352706102346_11"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.80781921807819%" id="mcps1.2.5.1.3"><p id="p4363548415054"><a name="p4363548415054"></a><a name="p4363548415054"></a><strong id="b842352706164541_7"><a name="b842352706164541_7"></a><a name="b842352706164541_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.577142285771423%" id="mcps1.2.5.1.4"><p id="p1721583215054"><a name="p1721583215054"></a><a name="p1721583215054"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59497879103033"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p6240390815054"><a name="p6240390815054"></a><a name="p6240390815054"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.18718128187181%" headers="mcps1.2.5.1.2 "><p id="p210816015054"><a name="p210816015054"></a><a name="p210816015054"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.80781921807819%" headers="mcps1.2.5.1.3 "><p id="p1545197115054"><a name="p1545197115054"></a><a name="p1545197115054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.577142285771423%" headers="mcps1.2.5.1.4 "><p id="p4213332315054"><a name="p4213332315054"></a><a name="p4213332315054"></a>Specifies the DB engine. Currently, MySQL and PostgreSQL are supported. The value is case-insensitive and can be <strong id="b842352706173632"><a name="b842352706173632"></a><a name="b842352706173632"></a>mysql</strong> or <strong id="b842352706173641"><a name="b842352706173641"></a><a name="b842352706173641"></a>postgresql</strong>.</p>
    </td>
    </tr>
    <tr id="row32955361103033"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p725043915054"><a name="p725043915054"></a><a name="p725043915054"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.18718128187181%" headers="mcps1.2.5.1.2 "><p id="p4179566215054"><a name="p4179566215054"></a><a name="p4179566215054"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.80781921807819%" headers="mcps1.2.5.1.3 "><p id="p3577604415054"><a name="p3577604415054"></a><a name="p3577604415054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.577142285771423%" headers="mcps1.2.5.1.4 "><p id="p58374830113022"><a name="p58374830113022"></a><a name="p58374830113022"></a>Specifies the database version.</p>
    <a name="ul4208889514478"></a><a name="ul4208889514478"></a><ul id="ul4208889514478"><li>For MySQL, the value can be <strong id="b842352706173747"><a name="b842352706173747"></a><a name="b842352706173747"></a>5.6</strong> and <strong id="b842352706173755"><a name="b842352706173755"></a><a name="b842352706173755"></a>5.7</strong>. The value <strong id="b842352706173759"><a name="b842352706173759"></a><a name="b842352706173759"></a>5.6</strong> is supported by default.</li><li>For PostgreSQL, the value can be 9.5, 9.6, 10, and 11. The default value is <strong id="b165162275173835"><a name="b165162275173835"></a><a name="b165162275173835"></a>9.5</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Request example

    ```
    {
      "configuration": {
        "name": "configuration_test",
        "description": "configuration_test",
        "values": {
           "max_connections": "10",
           "autocommit": "OFF"
        },
        "datastore": {
          "type": "mysql",
          "version": "5.6"
        }
      }
    }
    ```


## Normal Response<a name="section38874073103033"></a>

-   Parameter description

    **Table  6**  Parameter description

    <a name="table61792213103033"></a>
    <table><thead align="left"><tr id="row52877597103033"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p55226970103033"><a name="p55226970103033"></a><a name="p55226970103033"></a><strong id="b84235270691445_13"><a name="b84235270691445_13"></a><a name="b84235270691445_13"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.2"><p id="p44199604103033"><a name="p44199604103033"></a><a name="p44199604103033"></a><strong id="b842352706164541_9"><a name="b842352706164541_9"></a><a name="b842352706164541_9"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.67%" id="mcps1.2.4.1.3"><p id="p23398162103033"><a name="p23398162103033"></a><a name="p23398162103033"></a><strong id="b842352706163417_13"><a name="b842352706163417_13"></a><a name="b842352706163417_13"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16202973103033"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p37372412103033"><a name="p37372412103033"></a><a name="p37372412103033"></a>configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.2 "><p id="p7266520103033"><a name="p7266520103033"></a><a name="p7266520103033"></a>Dictionary data structure. For details, see <a href="#table28344292103033">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.67%" headers="mcps1.2.4.1.3 "><p id="p62801689103033"><a name="p62801689103033"></a><a name="p62801689103033"></a>Indicates the parameter template information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  configuration field data structure description

    <a name="table28344292103033"></a>
    <table><thead align="left"><tr id="row36466580103033"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1002967103033"><a name="p1002967103033"></a><a name="p1002967103033"></a><strong id="b84235270691445_15"><a name="b84235270691445_15"></a><a name="b84235270691445_15"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p14131540103033"><a name="p14131540103033"></a><a name="p14131540103033"></a><strong id="b842352706164541_11"><a name="b842352706164541_11"></a><a name="b842352706164541_11"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p3804081103033"><a name="p3804081103033"></a><a name="p3804081103033"></a><strong id="b842352706163417_15"><a name="b842352706163417_15"></a><a name="b842352706163417_15"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39695126103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61188652103033"><a name="p61188652103033"></a><a name="p61188652103033"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p57333786103033"><a name="p57333786103033"></a><a name="p57333786103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13525129103033"><a name="p13525129103033"></a><a name="p13525129103033"></a>Indicates the parameter template ID.</p>
    </td>
    </tr>
    <tr id="row54617305103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61925547103033"><a name="p61925547103033"></a><a name="p61925547103033"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49913426103033"><a name="p49913426103033"></a><a name="p49913426103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16455734103033"><a name="p16455734103033"></a><a name="p16455734103033"></a>Indicates the parameter template name.</p>
    </td>
    </tr>
    <tr id="row13883882103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p50852659103033"><a name="p50852659103033"></a><a name="p50852659103033"></a>datastore_version_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25424749103033"><a name="p25424749103033"></a><a name="p25424749103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46138816103033"><a name="p46138816103033"></a><a name="p46138816103033"></a>Indicates the database version ID.</p>
    </td>
    </tr>
    <tr id="row12596162103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13656172103033"><a name="p13656172103033"></a><a name="p13656172103033"></a>datastore_version_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32408130103033"><a name="p32408130103033"></a><a name="p32408130103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7812910103033"><a name="p7812910103033"></a><a name="p7812910103033"></a>Indicates the database version name.</p>
    </td>
    </tr>
    <tr id="row3207326103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58466883103033"><a name="p58466883103033"></a><a name="p58466883103033"></a>datastore_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p38197105103033"><a name="p38197105103033"></a><a name="p38197105103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6957775103033"><a name="p6957775103033"></a><a name="p6957775103033"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row62619975103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39053233103033"><a name="p39053233103033"></a><a name="p39053233103033"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9195295103033"><a name="p9195295103033"></a><a name="p9195295103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6621434103033"><a name="p6621434103033"></a><a name="p6621434103033"></a>Indicates the parameter template description.</p>
    </td>
    </tr>
    <tr id="row59592907103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p62296180103033"><a name="p62296180103033"></a><a name="p62296180103033"></a>instance_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12825789103033"><a name="p12825789103033"></a><a name="p12825789103033"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32255950103033"><a name="p32255950103033"></a><a name="p32255950103033"></a>Indicates the number of DB instances to which the parameter template applies.</p>
    </td>
    </tr>
    <tr id="row21868097103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26485458103033"><a name="p26485458103033"></a><a name="p26485458103033"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64947392103033"><a name="p64947392103033"></a><a name="p64947392103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26247410103033"><a name="p26247410103033"></a><a name="p26247410103033"></a>Indicates the parameter template creation time in the following format: yyyy-MM-ddTHH:mm:ss.</p>
    </td>
    </tr>
    <tr id="row34900105103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8336220103033"><a name="p8336220103033"></a><a name="p8336220103033"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4145257103033"><a name="p4145257103033"></a><a name="p4145257103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p221526103033"><a name="p221526103033"></a><a name="p221526103033"></a>Indicates the parameter template updated time in the following format: yyyy-MM-ddTHH:mm:ss.</p>
    </td>
    </tr>
    <tr id="row1993736103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27274921103033"><a name="p27274921103033"></a><a name="p27274921103033"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61784958103033"><a name="p61784958103033"></a><a name="p61784958103033"></a>Dictionary data structure. For details, see <a href="#table33572326103033">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11186798103033"><a name="p11186798103033"></a><a name="p11186798103033"></a>Indicates the parameter values defined by users based on the default parameter template. It is displayed only when you specify a custom parameter group. If you use a default parameter group, it is not returned.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  values field data structure description

    <a name="table33572326103033"></a>
    <table><thead align="left"><tr id="row56358927103033"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p1670376103033"><a name="p1670376103033"></a><a name="p1670376103033"></a><strong id="b84235270691445_17"><a name="b84235270691445_17"></a><a name="b84235270691445_17"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1082802103033"><a name="p1082802103033"></a><a name="p1082802103033"></a><strong id="b842352706164541_13"><a name="b842352706164541_13"></a><a name="b842352706164541_13"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p20598165103033"><a name="p20598165103033"></a><a name="p20598165103033"></a><strong id="b842352706163417_17"><a name="b842352706163417_17"></a><a name="b842352706163417_17"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57838648103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54418883103033"><a name="p54418883103033"></a><a name="p54418883103033"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45853407103033"><a name="p45853407103033"></a><a name="p45853407103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34956467202250"><a name="p34956467202250"></a><a name="p34956467202250"></a>Indicates the parameter name. For example, in <strong id="b84235270621563"><a name="b84235270621563"></a><a name="b84235270621563"></a>"max_connections": "10"</strong>, the key is <strong id="b842352706215241"><a name="b842352706215241"></a><a name="b842352706215241"></a>max_connections</strong>.</p>
    </td>
    </tr>
    <tr id="row6919762103033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23629870103033"><a name="p23629870103033"></a><a name="p23629870103033"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34971351103033"><a name="p34971351103033"></a><a name="p34971351103033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49005364202250"><a name="p49005364202250"></a><a name="p49005364202250"></a>Indicates the parameter value. For example, in <strong id="b953814020215624"><a name="b953814020215624"></a><a name="b953814020215624"></a>"max_connections": "10"</strong>, the value is <strong id="b842352706215633"><a name="b842352706215633"></a><a name="b842352706215633"></a>10</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "configuration": {
        "id": "463b4b58-d0e8-4e2b-9560-5dea4552fde9",
        "name": "configuration_test",
        "datastore_version_id": "de90043f-7f29-4a3e-ba82-f8beb5678b46",
        "datastore_version_name": "5.6",
        "datastore_name": "mysql",
        "description": "configuration_test",
        "instance_count": 0,
        "created": "2017-04-09T08:27:56",
        "updated": "2017-04-09T08:27:56",
        "values": {
           "max_connections": "10",
           "autocommit": "OFF"
        }
      }
    }
    ```


## Abnormal Response<a name="section2057086103033"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

