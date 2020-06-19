# Querying an Alarm Rule<a name="EN-US_TOPIC_0171212601"></a>

## Function<a name="section66578044"></a>

This API is used to query an alarm rule based on the alarm rule ID.

## URI<a name="section62331491"></a>

GET /V1.0/\{project\_id\}/alarms/\{alarm\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table31681753175455"></a>
    <table><thead align="left"><tr id="row39882175175455"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="p9230722175455"><a name="p9230722175455"></a><a name="p9230722175455"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.2"><p id="p9490989175455"><a name="p9490989175455"></a><a name="p9490989175455"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.08%" id="mcps1.2.4.1.3"><p id="p30572649175455"><a name="p30572649175455"></a><a name="p30572649175455"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60465501175455"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p65867442175455"><a name="p65867442175455"></a><a name="p65867442175455"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p33662608175455"><a name="p33662608175455"></a><a name="p33662608175455"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.08%" headers="mcps1.2.4.1.3 "><p id="p42316702175455"><a name="p42316702175455"></a><a name="p42316702175455"></a>Specifies the project ID.</p>
    <p id="p1624720191068"><a name="p1624720191068"></a><a name="p1624720191068"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row53812216202217"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p63822203202217"><a name="p63822203202217"></a><a name="p63822203202217"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p2215992202217"><a name="p2215992202217"></a><a name="p2215992202217"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.08%" headers="mcps1.2.4.1.3 "><p id="p45277653202217"><a name="p45277653202217"></a><a name="p45277653202217"></a>Specifies the alarm rule ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/alarms/al1441967036681YkazZ0deN
    ```


## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

-   Response parameters

    <a name="table42286344152742"></a>
    <table><thead align="left"><tr id="row38095364152742"><th class="cellrowborder" valign="top" width="20.7020702070207%" id="mcps1.1.4.1.1"><p id="p65825661152742"><a name="p65825661152742"></a><a name="p65825661152742"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.39163916391639%" id="mcps1.1.4.1.2"><p id="p36622711152742"><a name="p36622711152742"></a><a name="p36622711152742"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.90629062906291%" id="mcps1.1.4.1.3"><p id="p13649609152742"><a name="p13649609152742"></a><a name="p13649609152742"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48913836152742"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.1.4.1.1 "><p id="p2597784152742"><a name="p2597784152742"></a><a name="p2597784152742"></a>metric_alarms</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.1.4.1.2 "><p id="p65521217152742"><a name="p65521217152742"></a><a name="p65521217152742"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.1.4.1.3 "><p id="p5618383152742"><a name="p5618383152742"></a><a name="p5618383152742"></a>Specifies the list of alarm objects.</p>
    <p id="p118152512355"><a name="p118152512355"></a><a name="p118152512355"></a>For details, see <a href="#table1358574011306">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **metric\_alarms**  field data structure description

    <a name="table1358574011306"></a>
    <table><thead align="left"><tr id="row9573140143015"><th class="cellrowborder" valign="top" width="20.7020702070207%" id="mcps1.2.4.1.1"><p id="p1557384013300"><a name="p1557384013300"></a><a name="p1557384013300"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.39163916391639%" id="mcps1.2.4.1.2"><p id="p5573440153014"><a name="p5573440153014"></a><a name="p5573440153014"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.90629062906291%" id="mcps1.2.4.1.3"><p id="p195730403301"><a name="p195730403301"></a><a name="p195730403301"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row205738405308"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p1157364016307"><a name="p1157364016307"></a><a name="p1157364016307"></a>alarm_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p12573104011303"><a name="p12573104011303"></a><a name="p12573104011303"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p4573440163019"><a name="p4573440163019"></a><a name="p4573440163019"></a>Specifies the name of the alarm.</p>
    </td>
    </tr>
    <tr id="row25741540133013"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p16573184014306"><a name="p16573184014306"></a><a name="p16573184014306"></a>alarm_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p17574124023016"><a name="p17574124023016"></a><a name="p17574124023016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p1857413406305"><a name="p1857413406305"></a><a name="p1857413406305"></a>Provides supplementary information about the alarm.</p>
    </td>
    </tr>
    <tr id="row155741140143015"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p16574640163019"><a name="p16574640163019"></a><a name="p16574640163019"></a>metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p15613193451220"><a name="p15613193451220"></a><a name="p15613193451220"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p1574114053012"><a name="p1574114053012"></a><a name="p1574114053012"></a>Specifies the alarm metric.</p>
    <p id="p649212419352"><a name="p649212419352"></a><a name="p649212419352"></a>For details, see <a href="#table1358724013016">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row45761840113018"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p13575114083012"><a name="p13575114083012"></a><a name="p13575114083012"></a>condition</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p95751540103013"><a name="p95751540103013"></a><a name="p95751540103013"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p135768405307"><a name="p135768405307"></a><a name="p135768405307"></a>Specifies the alarm triggering condition.</p>
    <p id="p14454145463510"><a name="p14454145463510"></a><a name="p14454145463510"></a>For details, see <a href="#table159417407300">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row0582174003015"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p65822040133017"><a name="p65822040133017"></a><a name="p65822040133017"></a>alarm_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p8582194016301"><a name="p8582194016301"></a><a name="p8582194016301"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p18582940193011"><a name="p18582940193011"></a><a name="p18582940193011"></a>Specifies whether to enable the alarm rule.</p>
    </td>
    </tr>
    <tr id="row3583174083016"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p185821840133017"><a name="p185821840133017"></a><a name="p185821840133017"></a>alarm_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p115820402307"><a name="p115820402307"></a><a name="p115820402307"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p19582740193010"><a name="p19582740193010"></a><a name="p19582740193010"></a>Specifies the alarm severity. The value can be <strong id="b84235270610925"><a name="b84235270610925"></a><a name="b84235270610925"></a>1</strong>, <strong id="b84235270610928"><a name="b84235270610928"></a><a name="b84235270610928"></a>2</strong>, <strong id="b84235270610931"><a name="b84235270610931"></a><a name="b84235270610931"></a>3</strong> or <strong id="b84235270610934"><a name="b84235270610934"></a><a name="b84235270610934"></a>4</strong>, which indicates critical, major, minor, and informational, respectively.</p>
    </td>
    </tr>
    <tr id="row05831440103013"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p6583340143018"><a name="p6583340143018"></a><a name="p6583340143018"></a>alarm_action_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p1583194013014"><a name="p1583194013014"></a><a name="p1583194013014"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p65831640133018"><a name="p65831640133018"></a><a name="p65831640133018"></a>Specifies whether to enable the action to be triggered by an alarm.</p>
    </td>
    </tr>
    <tr id="row157678553312"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p557864016306"><a name="p557864016306"></a><a name="p557864016306"></a>alarm_actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p1578124013018"><a name="p1578124013018"></a><a name="p1578124013018"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p757814409303"><a name="p757814409303"></a><a name="p757814409303"></a>Specifies the action triggered by an alarm.</p>
    <p id="p657904083018"><a name="p657904083018"></a><a name="p657904083018"></a>For details, see <a href="#table359064073020">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row37641510123312"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p15579140163017"><a name="p15579140163017"></a><a name="p15579140163017"></a>ok_actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p7581840133019"><a name="p7581840133019"></a><a name="p7581840133019"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p1854123711153"><a name="p1854123711153"></a><a name="p1854123711153"></a>Specifies the action triggered by clearing an alarm.</p>
    <p id="p2551537141517"><a name="p2551537141517"></a><a name="p2551537141517"></a>For details, see <a href="#table1859144073012">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row75845404301"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p17584440173011"><a name="p17584440173011"></a><a name="p17584440173011"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p1458484012308"><a name="p1458484012308"></a><a name="p1458484012308"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p115848409301"><a name="p115848409301"></a><a name="p115848409301"></a>Specifies the alarm rule ID.</p>
    </td>
    </tr>
    <tr id="row20584124023017"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p1658444017304"><a name="p1658444017304"></a><a name="p1658444017304"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p4833115211216"><a name="p4833115211216"></a><a name="p4833115211216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p558414407303"><a name="p558414407303"></a><a name="p558414407303"></a>Specifies the time when the alarm status changed. The value is a UNIX timestamp and the unit is ms.</p>
    </td>
    </tr>
    <tr id="row16585144011306"><td class="cellrowborder" valign="top" width="20.7020702070207%" headers="mcps1.2.4.1.1 "><p id="p175847405306"><a name="p175847405306"></a><a name="p175847405306"></a>alarm_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.4.1.2 "><p id="p23811055141215"><a name="p23811055141215"></a><a name="p23811055141215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.90629062906291%" headers="mcps1.2.4.1.3 "><p id="p2584134043014"><a name="p2584134043014"></a><a name="p2584134043014"></a>Specifies the alarm status. The value can be:</p>
    <a name="ul19585640123011"></a><a name="ul19585640123011"></a><ul id="ul19585640123011"><li><strong id="b334613954411"><a name="b334613954411"></a><a name="b334613954411"></a>ok</strong>: The alarm status is normal.</li><li><strong id="b51598041151512"><a name="b51598041151512"></a><a name="b51598041151512"></a>alarm</strong>: An alarm is generated.</li><li><strong id="b1251114017444"><a name="b1251114017444"></a><a name="b1251114017444"></a>insufficient_data</strong>: The required data is insufficient.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Field  **metric**  data structure description

    <a name="table1358724013016"></a>
    <table><thead align="left"><tr id="row9586104013016"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p1858674016307"><a name="p1858674016307"></a><a name="p1858674016307"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p1958684013306"><a name="p1958684013306"></a><a name="p1958684013306"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p16586840173017"><a name="p16586840173017"></a><a name="p16586840173017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row058694020301"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p1458611403306"><a name="p1458611403306"></a><a name="p1458611403306"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p19586174017307"><a name="p19586174017307"></a><a name="p19586174017307"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p12933146104119"><a name="p12933146104119"></a><a name="p12933146104119"></a>Query the namespace of a service. For example, see <a href="ecs-metrics.md#en-us_topic_0022067719_section24282572112133">Namespace</a> for ECS namespace.</p>
    </td>
    </tr>
    <tr id="row35879403303"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p75865406307"><a name="p75865406307"></a><a name="p75865406307"></a>dimensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p19586164043017"><a name="p19586164043017"></a><a name="p19586164043017"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p55861740143019"><a name="p55861740143019"></a><a name="p55861740143019"></a>Specifies the list of the metric dimensions.</p>
    <p id="p9586154053018"><a name="p9586154053018"></a><a name="p9586154053018"></a>For details, see <a href="#table15589124016303">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row96438865716"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p13623999153639"><a name="p13623999153639"></a><a name="p13623999153639"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p136841954153011"><a name="p136841954153011"></a><a name="p136841954153011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p686919215492"><a name="p686919215492"></a><a name="p686919215492"></a>Specifies the metric ID. For example, if the <a href="ecs-metrics.md">monitoring metric</a> of an ECS is CPU usage, <strong id="b267242123518"><a name="b267242123518"></a><a name="b267242123518"></a>metric_name</strong> is <strong id="b66735217351"><a name="b66735217351"></a><a name="b66735217351"></a>cpu_util</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **dimensions**  field data structure description

    <a name="table15589124016303"></a>
    <table><thead align="left"><tr id="row95871840183019"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p155871640123019"><a name="p155871640123019"></a><a name="p155871640123019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p758714013304"><a name="p758714013304"></a><a name="p758714013304"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p1958714018307"><a name="p1958714018307"></a><a name="p1958714018307"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3588194053014"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p9588164019308"><a name="p9588164019308"></a><a name="p9588164019308"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p858811407301"><a name="p858811407301"></a><a name="p858811407301"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p132891013125316"><a name="p132891013125316"></a><a name="p132891013125316"></a>Specifies the monitoring dimension. For example, the monitoring dimension of an ECS is <strong id="b1199338173615"><a name="b1199338173615"></a><a name="b1199338173615"></a>instance_id</strong>, which is listed in the <strong id="b179931814367"><a name="b179931814367"></a><a name="b179931814367"></a>key</strong> column in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    </td>
    </tr>
    <tr id="row6589124015301"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p19588184023011"><a name="p19588184023011"></a><a name="p19588184023011"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1588154012306"><a name="p1588154012306"></a><a name="p1588154012306"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p11371113251615"><a name="p11371113251615"></a><a name="p11371113251615"></a>Specifies the dimension value, for example, an ECS ID.</p>
    <p id="p18588194043020"><a name="p18588194043020"></a><a name="p18588194043020"></a>The value is a string of 1 to 256 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **alarm\_actions**  field data structure description

    <a name="table359064073020"></a>
    <table><thead align="left"><tr id="row1258924033017"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p135896407302"><a name="p135896407302"></a><a name="p135896407302"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p6589194012309"><a name="p6589194012309"></a><a name="p6589194012309"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p7589340173016"><a name="p7589340173016"></a><a name="p7589340173016"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18590840153020"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p4589154053013"><a name="p4589154053013"></a><a name="p4589154053013"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1258919407308"><a name="p1258919407308"></a><a name="p1258919407308"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><div class="p" id="p2059034043019"><a name="p2059034043019"></a><a name="p2059034043019"></a>Specifies the alarm notification type.<a name="ul10590940153014"></a><a name="ul10590940153014"></a><ul id="ul10590940153014"><li><strong id="b792212361457"><a name="b792212361457"></a><a name="b792212361457"></a>notification</strong>: indicates that a notification will be sent to the user.</li><li><strong id="b15532143744518"><a name="b15532143744518"></a><a name="b15532143744518"></a>autoscaling</strong>: indicates that a scaling action will be triggered.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1859074017305"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p1459014406307"><a name="p1459014406307"></a><a name="p1459014406307"></a>notificationList</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p189944518163"><a name="p189944518163"></a><a name="p189944518163"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p35901840113013"><a name="p35901840113013"></a><a name="p35901840113013"></a>Specifies the list of objects to be notified if the alarm status changes.</p>
    <div class="note" id="note1578161452512"><a name="note1578161452512"></a><a name="note1578161452512"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19791914112518"><a name="p19791914112518"></a><a name="p19791914112518"></a>The IDs in the list are character strings.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **ok\_actions**  field data structure description

    <a name="table1859144073012"></a>
    <table><thead align="left"><tr id="row1159014401302"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p659084020309"><a name="p659084020309"></a><a name="p659084020309"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p13590144073018"><a name="p13590144073018"></a><a name="p13590144073018"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p559024053012"><a name="p559024053012"></a><a name="p559024053012"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1259134016305"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p1659024013014"><a name="p1659024013014"></a><a name="p1659024013014"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p15911940183012"><a name="p15911940183012"></a><a name="p15911940183012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><div class="p" id="p165918407306"><a name="p165918407306"></a><a name="p165918407306"></a>Specifies the notification type when an alarm is triggered.<a name="ul10591184093013"></a><a name="ul10591184093013"></a><ul id="ul10591184093013"><li><strong id="b3574342194513"><a name="b3574342194513"></a><a name="b3574342194513"></a>notification</strong>: indicates that a notification will be sent to the user.</li><li><strong id="b91617439459"><a name="b91617439459"></a><a name="b91617439459"></a>autoscaling</strong>: indicates that a scaling action will be triggered.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row195911940183017"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p115912405301"><a name="p115912405301"></a><a name="p115912405301"></a>notificationList</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p9548141017165"><a name="p9548141017165"></a><a name="p9548141017165"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p20591840103012"><a name="p20591840103012"></a><a name="p20591840103012"></a>Specifies the list of objects to be notified if the alarm status changes.</p>
    <div class="note" id="note187241341152520"><a name="note187241341152520"></a><a name="note187241341152520"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p672444172514"><a name="p672444172514"></a><a name="p672444172514"></a>The IDs in the list are character strings.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **condition**  field data structure description

    <a name="table159417407300"></a>
    <table><thead align="left"><tr id="row175923401303"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p8592184020306"><a name="p8592184020306"></a><a name="p8592184020306"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p759220403308"><a name="p759220403308"></a><a name="p759220403308"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p1592124010305"><a name="p1592124010305"></a><a name="p1592124010305"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row859212406308"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p14592164013013"><a name="p14592164013013"></a><a name="p14592164013013"></a>period</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1592540163016"><a name="p1592540163016"></a><a name="p1592540163016"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p9592124016302"><a name="p9592124016302"></a><a name="p9592124016302"></a>Specifies the interval (seconds) for checking whether the configured alarm rules are met.</p>
    </td>
    </tr>
    <tr id="row12593134013307"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p75931140123014"><a name="p75931140123014"></a><a name="p75931140123014"></a>filter</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1859312409302"><a name="p1859312409302"></a><a name="p1859312409302"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p2735918404"><a name="p2735918404"></a><a name="p2735918404"></a>Specifies the data rollup method. The following methods are supported:</p>
    <a name="en-us_topic_0046434864_ul7891893153925"></a><a name="en-us_topic_0046434864_ul7891893153925"></a><ul id="en-us_topic_0046434864_ul7891893153925"><li>If <strong id="b193931533173"><a name="b193931533173"></a><a name="b193931533173"></a>Avg.</strong> is selected for <strong id="b33942033579"><a name="b33942033579"></a><a name="b33942033579"></a>Statistic</strong>, Cloud Eye calculates the average value of metric data within a rollup period.</li><li>If <strong id="b5331193415719"><a name="b5331193415719"></a><a name="b5331193415719"></a>Max.</strong> is selected for <strong id="b123314343712"><a name="b123314343712"></a><a name="b123314343712"></a>Statistic</strong>, Cloud Eye calculates the maximum value of metric data within a rollup period.</li><li>If <strong id="b161007353720"><a name="b161007353720"></a><a name="b161007353720"></a>Min.</strong> is selected for <strong id="b1310017351078"><a name="b1310017351078"></a><a name="b1310017351078"></a>Statistic</strong>, Cloud Eye calculates the minimum value of metric data within a rollup period.</li><li>If <strong id="b151153612711"><a name="b151153612711"></a><a name="b151153612711"></a>Sum</strong> is selected for <strong id="b151120361979"><a name="b151120361979"></a><a name="b151120361979"></a>Statistic</strong>, Cloud Eye calculates the sum of metric data within a rollup period.</li><li>If <strong id="b13511372076"><a name="b13511372076"></a><a name="b13511372076"></a>Variance</strong> is selected for <strong id="b851337977"><a name="b851337977"></a><a name="b851337977"></a>Statistic</strong>, Cloud Eye calculates the variance value of metric data within a rollup period.</li></ul>
    </td>
    </tr>
    <tr id="row11593174014301"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p15593194018309"><a name="p15593194018309"></a><a name="p15593194018309"></a>comparison_operator</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p5593340113012"><a name="p5593340113012"></a><a name="p5593340113012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p135931040103011"><a name="p135931040103011"></a><a name="p135931040103011"></a>Specifies the comparison condition of alarm thresholds. The value can be <strong id="b1719894944515"><a name="b1719894944515"></a><a name="b1719894944515"></a>&gt;</strong>, <strong id="b21997498455"><a name="b21997498455"></a><a name="b21997498455"></a>=</strong>, <strong id="b319934913459"><a name="b319934913459"></a><a name="b319934913459"></a>&lt;</strong>, <strong id="b22001849114516"><a name="b22001849114516"></a><a name="b22001849114516"></a>≥</strong>, or <strong id="b17200184934518"><a name="b17200184934518"></a><a name="b17200184934518"></a>≤</strong>.</p>
    </td>
    </tr>
    <tr id="row1593040153018"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p759394033014"><a name="p759394033014"></a><a name="p759394033014"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p559324053017"><a name="p559324053017"></a><a name="p559324053017"></a>Integer or Float</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p105933404305"><a name="p105933404305"></a><a name="p105933404305"></a>Specifies the alarm threshold.</p>
    </td>
    </tr>
    <tr id="row25941440173013"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p105931440173016"><a name="p105931440173016"></a><a name="p105931440173016"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p059394018301"><a name="p059394018301"></a><a name="p059394018301"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p9594240113019"><a name="p9594240113019"></a><a name="p9594240113019"></a>Specifies the data unit.</p>
    </td>
    </tr>
    <tr id="row35945402309"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p20594124010304"><a name="p20594124010304"></a><a name="p20594124010304"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p75941740143016"><a name="p75941740143016"></a><a name="p75941740143016"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p145946405309"><a name="p145946405309"></a><a name="p145946405309"></a>Specifies the number of consecutive times that an alarm is triggered.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
    "metric_alarms":
      [
       {
        "alarm_name":"alarm-ipwx",
        "alarm_description":"",
        "metric":
         {
          "namespace":"SYS.ELB",
          "dimensions":
          [
           {
            "name":"lb_instance_id",
            "value":"44d06d10-bce0-4237-86b9-7b4d1e7d5621"
           }
          ],
          "metric_name":"m8_out_Bps"
          },
        "condition":
         {
          "period":300,
          "filter":"sum",
          "comparison_operator":">=",
          "value":0,
          "unit":"",
          "count":1
          },
        "alarm_enabled":true,
        "alarm_level": 2,
        "alarm_action_enabled":true,
        "alarm_actions":
         [
          {
           "type":"notification",
           "notificationList":["urn:smn:region:68438a86d98e427e907e0097b7e35d48:sd"]
          }
         ],
        "ok_actions":
         [
          {
           "type":"notification",
           "notificationList":["urn:smn:region:68438a86d98e427e907e0097b7e35d48:sd"]
          }
         ],
        "alarm_id":"al1498096535573r8DNy7Gyk",
        "update_time":1498100100000,
        "alarm_state":"alarm"
       }
      ]
    }
    ```


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.3.1.1"><p id="p9886408"><a name="p9886408"></a><a name="p9886408"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="71.43%" id="mcps1.1.3.1.2"><p id="p62601592"><a name="p62601592"></a><a name="p62601592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.3.1.1 "><p id="p5034751391559"><a name="p5034751391559"></a><a name="p5034751391559"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="71.43%" headers="mcps1.1.3.1.2 "><p id="p5161672091559"><a name="p5161672091559"></a><a name="p5161672091559"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.3.1.1 "><p id="p4762558891559"><a name="p4762558891559"></a><a name="p4762558891559"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="71.43%" headers="mcps1.1.3.1.2 "><p id="p3246739491559"><a name="p3246739491559"></a><a name="p3246739491559"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.3.1.1 "><p id="p4641015691559"><a name="p4641015691559"></a><a name="p4641015691559"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="71.43%" headers="mcps1.1.3.1.2 "><p id="p112628291559"><a name="p112628291559"></a><a name="p112628291559"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.3.1.1 "><p id="p1575359891559"><a name="p1575359891559"></a><a name="p1575359891559"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="71.43%" headers="mcps1.1.3.1.2 "><p id="p97307991559"><a name="p97307991559"></a><a name="p97307991559"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.3.1.1 "><p id="p3828603291559"><a name="p3828603291559"></a><a name="p3828603291559"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="71.43%" headers="mcps1.1.3.1.2 "><p id="p1416086091559"><a name="p1416086091559"></a><a name="p1416086091559"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.3.1.1 "><p id="p5561134191559"><a name="p5561134191559"></a><a name="p5561134191559"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="71.43%" headers="mcps1.1.3.1.2 "><p id="p822479291559"><a name="p822479291559"></a><a name="p822479291559"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.3.1.1 "><p id="p2318494091559"><a name="p2318494091559"></a><a name="p2318494091559"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="71.43%" headers="mcps1.1.3.1.2 "><p id="p6604084791559"><a name="p6604084791559"></a><a name="p6604084791559"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1343182834618"></a>

For details, see  [Error Codes](error-codes.md).

