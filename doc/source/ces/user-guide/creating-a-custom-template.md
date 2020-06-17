# Creating a Custom Template<a name="EN-US_TOPIC_0084572337"></a>

1.  On the  **Alarm Templates**  page, click  **Create Custom Template**.
2.  In the  **Select Template**  step, configure parameters based on  [Table 1](#table1956141511220).

    **Table  1**  Parameters

    <a name="table1956141511220"></a>
    <table><thead align="left"><tr id="row17562201515222"><th class="cellrowborder" valign="top" width="27.93%" id="mcps1.2.3.1.1"><p id="p9562171592217"><a name="p9562171592217"></a><a name="p9562171592217"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72.07000000000001%" id="mcps1.2.3.1.2"><p id="p105621415112212"><a name="p105621415112212"></a><a name="p105621415112212"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19564181512228"><td class="cellrowborder" valign="top" width="27.93%" headers="mcps1.2.3.1.1 "><p id="p16497122695118"><a name="p16497122695118"></a><a name="p16497122695118"></a>Resource Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.07000000000001%" headers="mcps1.2.3.1.2 "><p id="p1156471519223"><a name="p1156471519223"></a><a name="p1156471519223"></a>Specifies the name of the service for which the alarm rule is configured.</p>
    <p id="p113726155384"><a name="p113726155384"></a><a name="p113726155384"></a>Example value: <strong id="b1259616854316"><a name="b1259616854316"></a><a name="b1259616854316"></a>Elastic Cloud Server</strong></p>
    </td>
    </tr>
    <tr id="row956421512227"><td class="cellrowborder" valign="top" width="27.93%" headers="mcps1.2.3.1.1 "><p id="p1256441511220"><a name="p1256441511220"></a><a name="p1256441511220"></a>Dimension</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.07000000000001%" headers="mcps1.2.3.1.2 "><p id="p6564161512216"><a name="p6564161512216"></a><a name="p6564161512216"></a>Specifies the metric dimension of the selected cloud resource.</p>
    <p id="p127271425203813"><a name="p127271425203813"></a><a name="p127271425203813"></a>Example value: <strong id="b1160384561515"><a name="b1160384561515"></a><a name="b1160384561515"></a>ECS</strong></p>
    </td>
    </tr>
    <tr id="row9565191518227"><td class="cellrowborder" valign="top" width="27.93%" headers="mcps1.2.3.1.1 "><p id="p156513153221"><a name="p156513153221"></a><a name="p156513153221"></a>Import</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.07000000000001%" headers="mcps1.2.3.1.2 "><a name="ul14566181502211"></a><a name="ul14566181502211"></a><ul id="ul14566181502211"><li>Yes<p id="p20556165544715"><a name="p20556165544715"></a><a name="p20556165544715"></a>Select an existing template.</p>
    </li><li>No</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **Next**. In the  **Add Alarm Rule**  step, configure parameters based on  [Table 2](#table691022118227).

    **Table  2**  Parameters

    <a name="table691022118227"></a>
    <table><thead align="left"><tr id="row891192162214"><th class="cellrowborder" valign="top" width="26.939999999999998%" id="mcps1.2.3.1.1"><p id="p59115213229"><a name="p59115213229"></a><a name="p59115213229"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="73.06%" id="mcps1.2.3.1.2"><p id="p79121621172218"><a name="p79121621172218"></a><a name="p79121621172218"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9914182112229"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.3.1.1 "><p id="p14915132112229"><a name="p14915132112229"></a><a name="p14915132112229"></a>Metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.06%" headers="mcps1.2.3.1.2 "><p id="p1915421162216"><a name="p1915421162216"></a><a name="p1915421162216"></a>For example:</p>
    <a name="ul691572111221"></a><a name="ul691572111221"></a><ul id="ul691572111221"><li>CPU Usage<p id="p99165216228"><a name="p99165216228"></a><a name="p99165216228"></a>Indicates the CPU usage of the monitored object. The unit is percent.</p>
    </li></ul>
    <a name="ul20916182142211"></a><a name="ul20916182142211"></a><ul id="ul20916182142211"><li>Memory Usage<p id="p4916192113224"><a name="p4916192113224"></a><a name="p4916192113224"></a>Indicates the percentage of memory currently in use. The unit is percent.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="row95813546476"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.3.1.1 "><p id="p9435204373719"><a name="p9435204373719"></a><a name="p9435204373719"></a>Alarm Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.06%" headers="mcps1.2.3.1.2 "><p id="p2043584343715"><a name="p2043584343715"></a><a name="p2043584343715"></a>Specifies the policy that triggers an alarm.</p>
    <p id="p043712111488"><a name="p043712111488"></a><a name="p043712111488"></a>For example, an alarm is triggered if the metric average data is 80% or more for three consecutive periods of 5 minutes.</p>
    </td>
    </tr>
    <tr id="row1639201161214"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.3.1.1 "><p id="p1195420845111"><a name="p1195420845111"></a><a name="p1195420845111"></a>Alarm Severity</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.06%" headers="mcps1.2.3.1.2 "><p id="p17956884516"><a name="p17956884516"></a><a name="p17956884516"></a>Specifies the severity of the alarm. Valid values are <strong id="b842352706182313"><a name="b842352706182313"></a><a name="b842352706182313"></a>Critical</strong>, <strong id="b842352706182316"><a name="b842352706182316"></a><a name="b842352706182316"></a>Major</strong>, <strong id="b842352706182320"><a name="b842352706182320"></a><a name="b842352706182320"></a>Minor</strong>, and <strong id="b842352706182324"><a name="b842352706182324"></a><a name="b842352706182324"></a>Informational</strong>.</p>
    </td>
    </tr>
    <tr id="row1791811213223"><td class="cellrowborder" valign="top" width="26.939999999999998%" headers="mcps1.2.3.1.1 "><p id="p1691842115227"><a name="p1691842115227"></a><a name="p1691842115227"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="73.06%" headers="mcps1.2.3.1.2 "><p id="p291852122210"><a name="p291852122210"></a><a name="p291852122210"></a>When the number of the custom metrics is two or more than two, you can delete custom metrics.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Next**. In the  **Specify Template Name**  step, configure parameters based on  [Table 3](#table722215293225).

    **Table  3**  Parameters

    <a name="table722215293225"></a>
    <table><thead align="left"><tr id="row222382918227"><th class="cellrowborder" valign="top" width="23.830000000000002%" id="mcps1.2.3.1.1"><p id="p1722316294221"><a name="p1722316294221"></a><a name="p1722316294221"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76.17%" id="mcps1.2.3.1.2"><p id="p1223142918226"><a name="p1223142918226"></a><a name="p1223142918226"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1224132902213"><td class="cellrowborder" valign="top" width="23.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p3224192912228"><a name="p3224192912228"></a><a name="p3224192912228"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.17%" headers="mcps1.2.3.1.2 "><p id="p1422519296221"><a name="p1422519296221"></a><a name="p1422519296221"></a>Specifies the custom template name. The system generates a name randomly but you can change it.</p>
    <p id="p1597716527386"><a name="p1597716527386"></a><a name="p1597716527386"></a>Example value: <strong id="b1876910260157"><a name="b1876910260157"></a><a name="b1876910260157"></a>alarmTemplate-ku0x</strong></p>
    </td>
    </tr>
    <tr id="row202252298225"><td class="cellrowborder" valign="top" width="23.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p8225152911226"><a name="p8225152911226"></a><a name="p8225152911226"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.17%" headers="mcps1.2.3.1.2 "><p id="p8225132992214"><a name="p8225132992214"></a><a name="p8225132992214"></a>Provides supplementary information about the alarm template. This parameter is optional.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Finish**.

