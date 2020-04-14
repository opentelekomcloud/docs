# Querying Resources by Tag<a name="smn_api_56001"></a>

## Description<a name="section34083598194741"></a>

-   API name

    GetResourceInstances


-   Function

    Query SMN resources by tag.


## URI<a name="section16663308194741"></a>

-   URI format

    POST /v2/\{project\_id\}/\{resource\_type\}/resource\_instances/action


-   Parameter description

    <a name="table692210424914"></a>
    <table><thead align="left"><tr id="row199531142096"><th class="cellrowborder" valign="top" width="21.84%" id="mcps1.1.5.1.1"><p id="p18953142091"><a name="p18953142091"></a><a name="p18953142091"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26.44%" id="mcps1.1.5.1.2"><p id="p189530421394"><a name="p189530421394"></a><a name="p189530421394"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.24%" id="mcps1.1.5.1.3"><p id="p129538421390"><a name="p129538421390"></a><a name="p129538421390"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.48%" id="mcps1.1.5.1.4"><p id="p9953194213916"><a name="p9953194213916"></a><a name="p9953194213916"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row129533421894"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.5.1.1 "><p id="p15953144211913"><a name="p15953144211913"></a><a name="p15953144211913"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.44%" headers="mcps1.1.5.1.2 "><p id="p59531421199"><a name="p59531421199"></a><a name="p59531421199"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.1.5.1.3 "><p id="p1095317425913"><a name="p1095317425913"></a><a name="p1095317425913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.48%" headers="mcps1.1.5.1.4 "><p id="p995315422920"><a name="p995315422920"></a><a name="p995315422920"></a>Project ID</p>
    <p id="p118812918506"><a name="p118812918506"></a><a name="p118812918506"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row99537424915"><td class="cellrowborder" valign="top" width="21.84%" headers="mcps1.1.5.1.1 "><p id="p99531421797"><a name="p99531421797"></a><a name="p99531421797"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.44%" headers="mcps1.1.5.1.2 "><p id="p1495310421799"><a name="p1495310421799"></a><a name="p1495310421799"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.24%" headers="mcps1.1.5.1.3 "><p id="p149531342296"><a name="p149531342296"></a><a name="p149531342296"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.48%" headers="mcps1.1.5.1.4 "><p id="p52661238184213"><a name="p52661238184213"></a><a name="p52661238184213"></a>Resource type</p>
    <p id="p16612591087"><a name="p16612591087"></a><a name="p16612591087"></a>The value can be the following:</p>
    <p id="p14550953686"><a name="p14550953686"></a><a name="p14550953686"></a><strong id="b8638141823218"><a name="b8638141823218"></a><a name="b8638141823218"></a>smn_topic</strong>: topic</p>
    <p id="p8682201993"><a name="p8682201993"></a><a name="p8682201993"></a></p>
    <p id="p278251314214"><a name="p278251314214"></a><a name="p278251314214"></a></p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1142871194741"></a>

-   Parameter description

    <a name="table163121742121118"></a>
    <table><thead align="left"><tr id="row154221042181113"><th class="cellrowborder" valign="top" width="16.87168716871687%" id="mcps1.1.5.1.1"><p id="p1442284241113"><a name="p1442284241113"></a><a name="p1442284241113"></a><strong id="b463974686"><a name="b463974686"></a><a name="b463974686"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.562256225622562%" id="mcps1.1.5.1.2"><p id="p184221942111116"><a name="p184221942111116"></a><a name="p184221942111116"></a><strong id="b379454164"><a name="b379454164"></a><a name="b379454164"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.94239423942394%" id="mcps1.1.5.1.3"><p id="p11422242101116"><a name="p11422242101116"></a><a name="p11422242101116"></a><strong id="b1730330645"><a name="b1730330645"></a><a name="b1730330645"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.62366236623662%" id="mcps1.1.5.1.4"><p id="p172161339171313"><a name="p172161339171313"></a><a name="p172161339171313"></a><strong id="b2020663370"><a name="b2020663370"></a><a name="b2020663370"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row144221542181111"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p164228426114"><a name="p164228426114"></a><a name="p164228426114"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p4422542161112"><a name="p4422542161112"></a><a name="p4422542161112"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p13422124291118"><a name="p13422124291118"></a><a name="p13422124291118"></a>Tags structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p132727111254"><a name="p132727111254"></a><a name="p132727111254"></a>Includes specified tags. For details, see <a href="#table12385184281216">Table 1</a>.</p>
    <div class="note" id="note156841029125418"><a name="note156841029125418"></a><a name="note156841029125418"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p86841296546"><a name="p86841296546"></a><a name="p86841296546"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. Each tag key can have up to 10 tag values. Each tag key and tag values of one key must be unique. Resources identified by different keys are in AND relationship.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row17422114231115"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p74221442111112"><a name="p74221442111112"></a><a name="p74221442111112"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p10422942171111"><a name="p10422942171111"></a><a name="p10422942171111"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p204221142151112"><a name="p204221142151112"></a><a name="p204221142151112"></a>Tags structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p11216103951310"><a name="p11216103951310"></a><a name="p11216103951310"></a>Includes any of the specified tags. For details, see <a href="#table12385184281216">Table 1</a>.</p>
    <div class="note" id="note431014399542"><a name="note431014399542"></a><a name="note431014399542"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6310203955413"><a name="p6310203955413"></a><a name="p6310203955413"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. Each tag key can have up to 10 tag values. Each tag key and tag values of one key must be unique. Resources identified by different keys are in OR relationship.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row13422164220114"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p11422174261116"><a name="p11422174261116"></a><a name="p11422174261116"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p20422442141118"><a name="p20422442141118"></a><a name="p20422442141118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p1866963145215"><a name="p1866963145215"></a><a name="p1866963145215"></a>Tags structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p82165399139"><a name="p82165399139"></a><a name="p82165399139"></a>Excludes specified tags. For details, see <a href="#table12385184281216">Table 1</a>.</p>
    <div class="note" id="note2715124713543"><a name="note2715124713543"></a><a name="note2715124713543"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6715184718544"><a name="p6715184718544"></a><a name="p6715184718544"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. Each tag key can have up to 10 tag values. Each tag key and tag values of one key must be unique. Resources identified by different keys are in NAND relationship.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row0422194219118"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p9422042101110"><a name="p9422042101110"></a><a name="p9422042101110"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p1342216420115"><a name="p1342216420115"></a><a name="p1342216420115"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p64221742121116"><a name="p64221742121116"></a><a name="p64221742121116"></a>Tags structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p12160393138"><a name="p12160393138"></a><a name="p12160393138"></a>Excludes any of the specified tags. For details, see <a href="#table12385184281216">Table 1</a>.</p>
    <div class="note" id="note121691756185412"><a name="note121691756185412"></a><a name="note121691756185412"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1493371445514"><a name="p1493371445514"></a><a name="p1493371445514"></a>The structure body is mandatory. A maximum of 10 tag keys are allowed in each query operation. The tag key cannot be left blank or set to the empty string. Each tag key can have up to 10 tag values. Each tag key and tag values of one key must be unique. Resources identified by different keys are in NOR relationship.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row15422042151113"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p174221442151111"><a name="p174221442151111"></a><a name="p174221442151111"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p342213429119"><a name="p342213429119"></a><a name="p342213429119"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p8422442161119"><a name="p8422442161119"></a><a name="p8422442161119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p5699151414544"><a name="p5699151414544"></a><a name="p5699151414544"></a>Maximum number of resources to be queried</p>
    <a name="ul2162893714"></a><a name="ul2162893714"></a><ul id="ul2162893714"><li>If <strong id="b842352706152943"><a name="b842352706152943"></a><a name="b842352706152943"></a>action</strong> is set to <strong id="b842352706152951"><a name="b842352706152951"></a><a name="b842352706152951"></a>count</strong>, this parameter does not take effect.</li><li>If <strong id="b84235270692122"><a name="b84235270692122"></a><a name="b84235270692122"></a>action</strong> is set to <strong id="b84235270692134"><a name="b84235270692134"></a><a name="b84235270692134"></a>filter</strong>, this parameter takes effect. Its value ranges from 1 to 1000 (default).</li></ul>
    </td>
    </tr>
    <tr id="row5422142171118"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p8437842141117"><a name="p8437842141117"></a><a name="p8437842141117"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p9437174281113"><a name="p9437174281113"></a><a name="p9437174281113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p1343724215117"><a name="p1343724215117"></a><a name="p1343724215117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p138117139135"><a name="p138117139135"></a><a name="p138117139135"></a>Start location of pagination query. The query starts from the next resource of the specified location. You do not need to specify this parameter when querying resources on the first page. When you query resources on subsequent pages, set this parameter to the location returned in the response body for the previous query.</p>
    <a name="ul1279161261617"></a><a name="ul1279161261617"></a><ul id="ul1279161261617"><li>If <strong id="b1088205526"><a name="b1088205526"></a><a name="b1088205526"></a>action</strong> is set to <strong id="b1514275001"><a name="b1514275001"></a><a name="b1514275001"></a>count</strong>, this parameter does not take effect.</li><li>If <strong id="b84235270692726"><a name="b84235270692726"></a><a name="b84235270692726"></a>action</strong> is set to <strong id="b84235270692731"><a name="b84235270692731"></a><a name="b84235270692731"></a>filter</strong>, this parameter takes effect. Its value can be 0 (default) or a positive integer.</li></ul>
    </td>
    </tr>
    <tr id="row54371642161115"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p4437164210116"><a name="p4437164210116"></a><a name="p4437164210116"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p44377426118"><a name="p44377426118"></a><a name="p44377426118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p10437742171119"><a name="p10437742171119"></a><a name="p10437742171119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p277291081511"><a name="p277291081511"></a><a name="p277291081511"></a>Operation to be performed. The value can be <strong id="b84235270616546"><a name="b84235270616546"></a><a name="b84235270616546"></a>filter</strong> or <strong id="b84235270616552"><a name="b84235270616552"></a><a name="b84235270616552"></a>count</strong> (case-sensitive).</p>
    <p id="p1061044516952"><a name="p1061044516952"></a><a name="p1061044516952"></a><strong id="b1749576416952"><a name="b1749576416952"></a><a name="b1749576416952"></a>filter</strong>: queries resources in pages based on filter conditions.</p>
    <p id="p4081382911230"><a name="p4081382911230"></a><a name="p4081382911230"></a><strong id="b84235270620460"><a name="b84235270620460"></a><a name="b84235270620460"></a>count</strong>: queries the total number of resources meeting filter conditions.</p>
    </td>
    </tr>
    <tr id="row543716422116"><td class="cellrowborder" valign="top" width="16.87168716871687%" headers="mcps1.1.5.1.1 "><p id="p13437164216113"><a name="p13437164216113"></a><a name="p13437164216113"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.562256225622562%" headers="mcps1.1.5.1.2 "><p id="p14437184241113"><a name="p14437184241113"></a><a name="p14437184241113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94239423942394%" headers="mcps1.1.5.1.3 "><p id="p11437114217112"><a name="p11437114217112"></a><a name="p11437114217112"></a>Match condition structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.62366236623662%" headers="mcps1.1.5.1.4 "><p id="p2991175121517"><a name="p2991175121517"></a><a name="p2991175121517"></a>Key-value pair to be matched</p>
    <p id="p8184185775619"><a name="p8184185775619"></a><a name="p8184185775619"></a>The key can only be <strong id="b842352706161550"><a name="b842352706161550"></a><a name="b842352706161550"></a>resource_name</strong>.</p>
    <p id="p11842575562"><a name="p11842575562"></a><a name="p11842575562"></a>The value will be exactly matched.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Tags structure

    <a name="table12385184281216"></a>
    <table><thead align="left"><tr id="row12526442141213"><th class="cellrowborder" valign="top" width="18.16%" id="mcps1.2.6.1.1"><p id="p1252612428129"><a name="p1252612428129"></a><a name="p1252612428129"></a><strong id="b47901755163415"><a name="b47901755163415"></a><a name="b47901755163415"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.030000000000001%" id="mcps1.2.6.1.2"><p id="p852612421125"><a name="p852612421125"></a><a name="p852612421125"></a><strong id="b895256445"><a name="b895256445"></a><a name="b895256445"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.81%" id="mcps1.2.6.1.3"><p id="p14526542121214"><a name="p14526542121214"></a><a name="p14526542121214"></a><strong id="b2041287441"><a name="b2041287441"></a><a name="b2041287441"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.65%" id="mcps1.2.6.1.4"><p id="p17526124281215"><a name="p17526124281215"></a><a name="p17526124281215"></a><strong id="b63411457103415"><a name="b63411457103415"></a><a name="b63411457103415"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.35%" id="mcps1.2.6.1.5"><p id="p12294162622414"><a name="p12294162622414"></a><a name="p12294162622414"></a><strong id="b167841358163418"><a name="b167841358163418"></a><a name="b167841358163418"></a>Constraint</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1526194218129"><td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.2.6.1.1 "><p id="p65262427126"><a name="p65262427126"></a><a name="p65262427126"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.2.6.1.2 "><p id="p4526154211123"><a name="p4526154211123"></a><a name="p4526154211123"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.81%" headers="mcps1.2.6.1.3 "><p id="p35261242171216"><a name="p35261242171216"></a><a name="p35261242171216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.2.6.1.4 "><p id="p552604213129"><a name="p552604213129"></a><a name="p552604213129"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.35%" headers="mcps1.2.6.1.5 "><p id="p6294172612244"><a name="p6294172612244"></a><a name="p6294172612244"></a>A key contains 127 Unicode characters and cannot be blank.</p>
    </td>
    </tr>
    <tr id="row55261142141216"><td class="cellrowborder" valign="top" width="18.16%" headers="mcps1.2.6.1.1 "><p id="p1852614219127"><a name="p1852614219127"></a><a name="p1852614219127"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.030000000000001%" headers="mcps1.2.6.1.2 "><p id="p11526104271211"><a name="p11526104271211"></a><a name="p11526104271211"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.81%" headers="mcps1.2.6.1.3 "><p id="p45262426129"><a name="p45262426129"></a><a name="p45262426129"></a>String list</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.2.6.1.4 "><p id="p152694220126"><a name="p152694220126"></a><a name="p152694220126"></a>Value list</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.35%" headers="mcps1.2.6.1.5 "><p id="p18294152612244"><a name="p18294152612244"></a><a name="p18294152612244"></a>Each value contains a maximum of 255 Unicode characters. If the value starts with an asterisk (*), the character string following the asterisk is fuzzy-matched. The <strong id="b18353175912112"><a name="b18353175912112"></a><a name="b18353175912112"></a>values</strong> field cannot be missing, but can be an empty list. If it is empty, any value will be matched. The values are in OR relationship.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    POST https://{SMN_Endpoint}/v2/{project_id}/{resource_type}/resource_instances/action
    ```

    -   Request body when  **action**  is set to  **filter**

        ```
        {
          "offset": "100", 
          "limit": "100", 
          "action": "filter", 
          "matches":[
               {
                "key": "resource_name", 
                "value": "resource1"
               }
           ], 
           "not_tags": [
               {
                "key": "key1", 
                "values": ["*value1","value2"]
               },
               {
                "key": "key2", 
                "values": ["*value21","value22"]
               }
           ], 
           "tags": [
            {
              "key": "key1", 
              "values": ["*value1","value2"]
              }
             ], 
           "tags_any": [
            {
              "key": "key1", 
              "values": ["value1", "value2"]
            }
          ],
           "not_tags_any": [
            {
              "key": "key1", 
              "values": ["value1", "value2"]
            }
          ]
        }
        ```

    -   Request body when  **action**  is set to  **count**

        ```
        {
          "action": "count", 
          "not_tags": [
            {
              "key": "key1", 
              "values": ["value1", "*value2"]
            }
          ], 
          "tags": [
            {
              "key": "key1", 
              "values": ["value1", "value2"]
            }
          ], 
          "tags_any": [
            {
              "key": "key1", 
              "values": [ "value1", "value2"]
            }
          ],
          "not_tags_any": [
            {
              "key": "key1", 
              "values": ["value1", "value2"]
            }
           ],
           "matches":[
           {
                "key": "resource_name", 
                "value": "resouurce"
           }
          ]
        }
        ```



## Response<a name="section13775125191714"></a>

-   Parameter description

    <a name="table479165191720"></a>
    <table><thead align="left"><tr id="row17931135116172"><th class="cellrowborder" valign="top" width="20.65%" id="mcps1.1.5.1.1"><p id="p15931551181711"><a name="p15931551181711"></a><a name="p15931551181711"></a><strong id="b553634246"><a name="b553634246"></a><a name="b553634246"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.57%" id="mcps1.1.5.1.2"><p id="p8931185119173"><a name="p8931185119173"></a><a name="p8931185119173"></a><strong id="b305302294"><a name="b305302294"></a><a name="b305302294"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.169999999999998%" id="mcps1.1.5.1.3"><p id="p1293118514171"><a name="p1293118514171"></a><a name="p1293118514171"></a><strong id="b1528776683"><a name="b1528776683"></a><a name="b1528776683"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.61%" id="mcps1.1.5.1.4"><p id="p1493155131717"><a name="p1493155131717"></a><a name="p1493155131717"></a><strong id="b255500611"><a name="b255500611"></a><a name="b255500611"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row189311551101713"><td class="cellrowborder" valign="top" width="20.65%" headers="mcps1.1.5.1.1 "><p id="p093165181714"><a name="p093165181714"></a><a name="p093165181714"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.57%" headers="mcps1.1.5.1.2 "><p id="p11931145115176"><a name="p11931145115176"></a><a name="p11931145115176"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.169999999999998%" headers="mcps1.1.5.1.3 "><p id="p19931165111175"><a name="p19931165111175"></a><a name="p19931165111175"></a>Resource structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.61%" headers="mcps1.1.5.1.4 "><p id="p0482182011216"><a name="p0482182011216"></a><a name="p0482182011216"></a>For details, see <a href="#table97917514177">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row1393115111174"><td class="cellrowborder" valign="top" width="20.65%" headers="mcps1.1.5.1.1 "><p id="p9931195191717"><a name="p9931195191717"></a><a name="p9931195191717"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.57%" headers="mcps1.1.5.1.2 "><p id="p14931651161717"><a name="p14931651161717"></a><a name="p14931651161717"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.169999999999998%" headers="mcps1.1.5.1.3 "><p id="p89313512179"><a name="p89313512179"></a><a name="p89313512179"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.61%" headers="mcps1.1.5.1.4 "><p id="p7931251111720"><a name="p7931251111720"></a><a name="p7931251111720"></a>Total number of resources</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Resource structure

    <a name="table97917514177"></a>
    <table><thead align="left"><tr id="row20931851161717"><th class="cellrowborder" valign="top" width="19.73%" id="mcps1.2.5.1.1"><p id="p169312051161713"><a name="p169312051161713"></a><a name="p169312051161713"></a><strong id="b520919401466"><a name="b520919401466"></a><a name="b520919401466"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.2"><p id="p6931195111719"><a name="p6931195111719"></a><a name="p6931195111719"></a><strong id="b1593427990"><a name="b1593427990"></a><a name="b1593427990"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.53%" id="mcps1.2.5.1.3"><p id="p093195116179"><a name="p093195116179"></a><a name="p093195116179"></a><strong id="b419849882"><a name="b419849882"></a><a name="b419849882"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32.15%" id="mcps1.2.5.1.4"><p id="p59319515179"><a name="p59319515179"></a><a name="p59319515179"></a><strong id="b13369124134610"><a name="b13369124134610"></a><a name="b13369124134610"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row393195119172"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p1793165110171"><a name="p1793165110171"></a><a name="p1793165110171"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.2 "><p id="p6931185117179"><a name="p6931185117179"></a><a name="p6931185117179"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.53%" headers="mcps1.2.5.1.3 "><p id="p69311951191710"><a name="p69311951191710"></a><a name="p69311951191710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.15%" headers="mcps1.2.5.1.4 "><p id="p1931175111170"><a name="p1931175111170"></a><a name="p1931175111170"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row493125112176"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p2931165110176"><a name="p2931165110176"></a><a name="p2931165110176"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.2 "><p id="p6931105151716"><a name="p6931105151716"></a><a name="p6931105151716"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.53%" headers="mcps1.2.5.1.3 "><p id="p293145151713"><a name="p293145151713"></a><a name="p293145151713"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.15%" headers="mcps1.2.5.1.4 "><p id="p1793113514176"><a name="p1793113514176"></a><a name="p1793113514176"></a>Resource details. Resource object used for extension. The value is left blank by default.</p>
    <p id="p826215381712"><a name="p826215381712"></a><a name="p826215381712"></a>For topic resources, the value of this field is <strong id="b842352706143216"><a name="b842352706143216"></a><a name="b842352706143216"></a>{"topic_urn":"${TopicUrn}","display_name":"display name"}</strong>.</p>
    <p id="p1226217381177"><a name="p1226217381177"></a><a name="p1226217381177"></a>For other resources, the value is <strong id="b82963378259"><a name="b82963378259"></a><a name="b82963378259"></a>null</strong>.</p>
    </td>
    </tr>
    <tr id="row8931195121716"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p29311851181715"><a name="p29311851181715"></a><a name="p29311851181715"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.2 "><p id="p10931155119177"><a name="p10931155119177"></a><a name="p10931155119177"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.53%" headers="mcps1.2.5.1.3 "><p id="p69311851201711"><a name="p69311851201711"></a><a name="p69311851201711"></a>Resource_tag structure array</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.15%" headers="mcps1.2.5.1.4 "><p id="p20931135117174"><a name="p20931135117174"></a><a name="p20931135117174"></a>List of queried tags. If no tag is matched, an empty array is returned. For details, see <a href="#table178221351151717">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row493125112175"><td class="cellrowborder" valign="top" width="19.73%" headers="mcps1.2.5.1.1 "><p id="p9931135131716"><a name="p9931135131716"></a><a name="p9931135131716"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.2 "><p id="p29311512174"><a name="p29311512174"></a><a name="p29311512174"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.53%" headers="mcps1.2.5.1.3 "><p id="p99312519176"><a name="p99312519176"></a><a name="p99312519176"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.15%" headers="mcps1.2.5.1.4 "><p id="p893175191714"><a name="p893175191714"></a><a name="p893175191714"></a>Resource name</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Resource\_tag structure

    <a name="table178221351151717"></a>
    <table><thead align="left"><tr id="row139311651171713"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.6.1.1"><p id="p993135161718"><a name="p993135161718"></a><a name="p993135161718"></a><strong id="b6377153915111"><a name="b6377153915111"></a><a name="b6377153915111"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.6.1.2"><p id="p19311451131719"><a name="p19311451131719"></a><a name="p19311451131719"></a><strong id="b553769561"><a name="b553769561"></a><a name="b553769561"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.6.1.3"><p id="p13931451141710"><a name="p13931451141710"></a><a name="p13931451141710"></a><strong id="b1343797695"><a name="b1343797695"></a><a name="b1343797695"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.6.1.4"><p id="p393125141712"><a name="p393125141712"></a><a name="p393125141712"></a><strong id="b36311841175120"><a name="b36311841175120"></a><a name="b36311841175120"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.633663366336634%" id="mcps1.2.6.1.5"><p id="p1715443212610"><a name="p1715443212610"></a><a name="p1715443212610"></a><strong id="b134437429517"><a name="b134437429517"></a><a name="b134437429517"></a>Constraint</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3931105113173"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.1 "><p id="p17931145131711"><a name="p17931145131711"></a><a name="p17931145131711"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.2 "><p id="p9931145120179"><a name="p9931145120179"></a><a name="p9931145120179"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.3 "><p id="p16931751111714"><a name="p16931751111714"></a><a name="p16931751111714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.6.1.4 "><p id="p393175116171"><a name="p393175116171"></a><a name="p393175116171"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.2.6.1.5 "><p id="p171314419267"><a name="p171314419267"></a><a name="p171314419267"></a>The key contains 36 Unicode characters at most and cannot be blank or an empty string. It can contain only digits, letters, hyphens (-), and underscores (_) and must not start or end with a space.</p>
    </td>
    </tr>
    <tr id="row39312515173"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.6.1.1 "><p id="p09311651171711"><a name="p09311651171711"></a><a name="p09311651171711"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.2 "><p id="p1693155113179"><a name="p1693155113179"></a><a name="p1693155113179"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.6.1.3 "><p id="p14931751141720"><a name="p14931751141720"></a><a name="p14931751141720"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.6.1.4 "><p id="p159313515179"><a name="p159313515179"></a><a name="p159313515179"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.633663366336634%" headers="mcps1.2.6.1.5 "><p id="p344164632615"><a name="p344164632615"></a><a name="p344164632615"></a>Each value contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_) and must not start or end with a space.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    Response body when  **action**  is set to  **filter**

    ```
    { 
          "resources": [
             {
                "resource_detail": {
                     "topic_urn":"urn:smn:regionId:f96188c7ccaf4ffba0c9aa149ab2bd57:resouece1",
                     "display_name":"testtest"
                 },
                "resource_id": "cffe4fc4c9a54219b60dbaf7b586e132", 
                "resource_name": "resouece1", 
                "tags": [
                    {
                       "key": "key1",
                       "value": "value1"
                    }
                 ]
             }
           ], 
          "total_count": 1000
    }
    ```

    Response body when  **action**  is set to  **count**

    ```
    {
           "total_count": 1000
    }
    ```


## Returned Value<a name="section104011733101818"></a>

See section  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See section  [Error Code](error-code.md).

