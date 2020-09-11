# Querying Backup Resource Instances<a name="EN-US_TOPIC_0098635086"></a>

## Function<a name="section35899943"></a>

This API is used to filter instances by specifying tags.

Tag Management Service \(TMS\) uses this API to filter and list instances of each service by tag. These services must have the query capabilities.

## URI<a name="section54664039"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup/resource\_instances/action

-   Request header

    **Table  1**  Request header

    <a name="table20432162"></a>
    <table><thead align="left"><tr id="row57818045"><th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row546286"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p44249235"><a name="p44249235"></a><a name="p44249235"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p1349835311518"><a name="p1349835311518"></a><a name="p1349835311518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p27418305"><a name="p27418305"></a><a name="p27418305"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p39744725"><a name="p39744725"></a><a name="p39744725"></a>application/json</p>
    </td>
    </tr>
    <tr id="row22158209"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p49984495"><a name="p49984495"></a><a name="p49984495"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p15496653358"><a name="p15496653358"></a><a name="p15496653358"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p22212298"><a name="p22212298"></a><a name="p22212298"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p41544677"><a name="p41544677"></a><a name="p41544677"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table45529105"></a>
    <table><thead align="left"><tr id="row64560089"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.5.1.1"><p id="p13599171761216"><a name="p13599171761216"></a><a name="p13599171761216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.2"><p id="p196152178123"><a name="p196152178123"></a><a name="p196152178123"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p19615717141216"><a name="p19615717141216"></a><a name="p19615717141216"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p1761571718127"><a name="p1761571718127"></a><a name="p1761571718127"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43823951"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p60079171"><a name="p60079171"></a><a name="p60079171"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.2 "><p id="p34574683"><a name="p34574683"></a><a name="p34574683"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p49085952"><a name="p49085952"></a><a name="p49085952"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section22214308"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table40155382"></a>
    <table><thead align="left"><tr id="row3231228"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p499032320129"><a name="p499032320129"></a><a name="p499032320129"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p52120247121"><a name="p52120247121"></a><a name="p52120247121"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p12192413121"><a name="p12192413121"></a><a name="p12192413121"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p143782415121"><a name="p143782415121"></a><a name="p143782415121"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44521582"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p49478415"><a name="p49478415"></a><a name="p49478415"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p48328717"><a name="p48328717"></a><a name="p48328717"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p22312015"><a name="p22312015"></a><a name="p22312015"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p15624527153813"><a name="p15624527153813"></a><a name="p15624527153813"></a>List of included tags. Backups with these tags will be filtered.</p>
    <p id="p0494199183911"><a name="p0494199183911"></a><a name="p0494199183911"></a>This list cannot be an empty list.</p>
    <p id="p646324463913"><a name="p646324463913"></a><a name="p646324463913"></a>The list can contain up to 10 keys.</p>
    <p id="p19401115618394"><a name="p19401115618394"></a><a name="p19401115618394"></a>Keys in this list must be unique.</p>
    <p id="p1771815924015"><a name="p1771815924015"></a><a name="p1771815924015"></a>Keys in this list are in an AND relationship.</p>
    <p id="p164965117535"><a name="p164965117535"></a><a name="p164965117535"></a>The response returns resources containing all tags in this list. Keys in this list are in an AND relationship while values in each key-value structure is in an OR relationship.</p>
    </td>
    </tr>
    <tr id="row15427175544720"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p54273555474"><a name="p54273555474"></a><a name="p54273555474"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p842755513476"><a name="p842755513476"></a><a name="p842755513476"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p142795514710"><a name="p142795514710"></a><a name="p142795514710"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p1842725544712"><a name="p1842725544712"></a><a name="p1842725544712"></a>List of tags. Backups with any tags in this list will be filtered.</p>
    <p id="p158584245013"><a name="p158584245013"></a><a name="p158584245013"></a>This list cannot be an empty list.</p>
    <p id="p16591114214506"><a name="p16591114214506"></a><a name="p16591114214506"></a>The list can contain up to 10 keys.</p>
    <p id="p459817429501"><a name="p459817429501"></a><a name="p459817429501"></a>Keys in this list must be unique.</p>
    <p id="p765214147556"><a name="p765214147556"></a><a name="p765214147556"></a>The response returns resources containing any tags in this list. Keys in this list are in an OR relationship while values in each key-value structure is in an OR relationship.</p>
    </td>
    </tr>
    <tr id="row195677435718"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p175677415716"><a name="p175677415716"></a><a name="p175677415716"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p145671340571"><a name="p145671340571"></a><a name="p145671340571"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p85673413570"><a name="p85673413570"></a><a name="p85673413570"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p115672419576"><a name="p115672419576"></a><a name="p115672419576"></a>List of excluded tags. Backups without these tags will be filtered.</p>
    <p id="p1199314506578"><a name="p1199314506578"></a><a name="p1199314506578"></a>This list cannot be an empty list.</p>
    <p id="p62165145715"><a name="p62165145715"></a><a name="p62165145715"></a>The list can contain up to 10 keys.</p>
    <p id="p0111751105713"><a name="p0111751105713"></a><a name="p0111751105713"></a>Keys in this list must be unique.</p>
    <p id="p17588613201"><a name="p17588613201"></a><a name="p17588613201"></a>The response returns resources containing no tags in this list. Keys in this list are in an AND relationship while values in each key-value structure is in an OR relationship.</p>
    </td>
    </tr>
    <tr id="row12196548112"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p02193547116"><a name="p02193547116"></a><a name="p02193547116"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p132193541614"><a name="p132193541614"></a><a name="p132193541614"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p62191954011"><a name="p62191954011"></a><a name="p62191954011"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p192791022229"><a name="p192791022229"></a><a name="p192791022229"></a>List of tags. Backups without any tags in this list will be filtered.</p>
    <p id="p428532217220"><a name="p428532217220"></a><a name="p428532217220"></a>This list cannot be an empty list.</p>
    <p id="p1229319221525"><a name="p1229319221525"></a><a name="p1229319221525"></a>The list can contain up to 10 keys.</p>
    <p id="p1529610224214"><a name="p1529610224214"></a><a name="p1529610224214"></a>Keys in this list must be unique.</p>
    <p id="p43845237217"><a name="p43845237217"></a><a name="p43845237217"></a>The response returns resources without any tags in this list. Keys in this list are in an OR relationship while values in each key-value structure is in an OR relationship.</p>
    </td>
    </tr>
    <tr id="row2948748"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p37522006"><a name="p37522006"></a><a name="p37522006"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p19383628"><a name="p19383628"></a><a name="p19383628"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p3210845577"><a name="p3210845577"></a><a name="p3210845577"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p09225511219"><a name="p09225511219"></a><a name="p09225511219"></a>Query count (This parameter is not displayed if <strong id="b842352706195922"><a name="b842352706195922"></a><a name="b842352706195922"></a>action</strong> is set to <strong id="b842352706195927"><a name="b842352706195927"></a><a name="b842352706195927"></a>count</strong>.)</p>
    <p id="p4692191"><a name="p4692191"></a><a name="p4692191"></a>If <strong id="b842352706102324"><a name="b842352706102324"></a><a name="b842352706102324"></a>action</strong> is set to <strong id="b842352706102329"><a name="b842352706102329"></a><a name="b842352706102329"></a>filter</strong>, the value defaults to <strong id="b842352706102331"><a name="b842352706102331"></a><a name="b842352706102331"></a>1000</strong>. The value ranges from <strong id="b842352706102340"><a name="b842352706102340"></a><a name="b842352706102340"></a>1</strong> to <strong id="b842352706102344"><a name="b842352706102344"></a><a name="b842352706102344"></a>1000</strong>. If you set a value out of this range, an error will be reported. The number of returned records does not exceed the value of <strong id="b842352706194753"><a name="b842352706194753"></a><a name="b842352706194753"></a>limit</strong>. </p>
    </td>
    </tr>
    <tr id="row42229725"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p65164587"><a name="p65164587"></a><a name="p65164587"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p43840169"><a name="p43840169"></a><a name="p43840169"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p9429145905611"><a name="p9429145905611"></a><a name="p9429145905611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p177411411197"><a name="p177411411197"></a><a name="p177411411197"></a>Query index (This parameter is not displayed if <strong id="b1191904758"><a name="b1191904758"></a><a name="b1191904758"></a>action</strong> is set to <strong id="b1067591997"><a name="b1067591997"></a><a name="b1067591997"></a>count</strong>.)</p>
    <p id="p14508185131920"><a name="p14508185131920"></a><a name="p14508185131920"></a>If <strong id="b200691530720216"><a name="b200691530720216"></a><a name="b200691530720216"></a>action</strong> is set to <strong id="b39257038320216"><a name="b39257038320216"></a><a name="b39257038320216"></a>filter</strong>, the value defaults to <strong id="b163342832120216"><a name="b163342832120216"></a><a name="b163342832120216"></a>0</strong> (minimum value). The first record in the query result is the offset+1 record that meets the query criteria. </p>
    </td>
    </tr>
    <tr id="row60824073"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p27802884"><a name="p27802884"></a><a name="p27802884"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p37441107"><a name="p37441107"></a><a name="p37441107"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p12830815"><a name="p12830815"></a><a name="p12830815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p34304549"><a name="p34304549"></a><a name="p34304549"></a>Operation to be performed</p>
    <p id="p64392016184311"><a name="p64392016184311"></a><a name="p64392016184311"></a>Possible values are <strong id="b842352706194826"><a name="b842352706194826"></a><a name="b842352706194826"></a>filter</strong> and <strong id="b842352706194830"><a name="b842352706194830"></a><a name="b842352706194830"></a>count</strong>. </p>
    <p id="p40305487"><a name="p40305487"></a><a name="p40305487"></a><strong id="b45514660820229"><a name="b45514660820229"></a><a name="b45514660820229"></a>filter</strong> indicates pagination query and <strong id="b987992455202243"><a name="b987992455202243"></a><a name="b987992455202243"></a>count</strong> indicates that a specified number of queried records will be returned.</p>
    </td>
    </tr>
    <tr id="row28461771"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p23702140"><a name="p23702140"></a><a name="p23702140"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p40825226"><a name="p40825226"></a><a name="p40825226"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p18509020"><a name="p18509020"></a><a name="p18509020"></a>List&lt;match&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p518016559472"><a name="p518016559472"></a><a name="p518016559472"></a>List of query criteria supported by resources</p>
    <p id="p17555154424814"><a name="p17555154424814"></a><a name="p17555154424814"></a>This list cannot be an empty list.</p>
    <p id="p184835314818"><a name="p184835314818"></a><a name="p184835314818"></a>Keys in this list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **tag**

    **Table  4**  Parameter description of field  **tag**

    <a name="table37882110"></a>
    <table><thead align="left"><tr id="row59354473"><th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.1"><p id="p9646132818126"><a name="p9646132818126"></a><a name="p9646132818126"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p2646152801210"><a name="p2646152801210"></a><a name="p2646152801210"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p17661152820124"><a name="p17661152820124"></a><a name="p17661152820124"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p966162861210"><a name="p966162861210"></a><a name="p966162861210"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20316329"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p35009954"><a name="p35009954"></a><a name="p35009954"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p17234060"><a name="p17234060"></a><a name="p17234060"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p53781647"><a name="p53781647"></a><a name="p53781647"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p321161514239"><a name="p321161514239"></a><a name="p321161514239"></a>Tag key</p>
    <p id="p10460518142315"><a name="p10460518142315"></a><a name="p10460518142315"></a>A tag key consists of up to 127 characters.</p>
    <p id="p1448142852310"><a name="p1448142852310"></a><a name="p1448142852310"></a>A tag key cannot be an empty string.</p>
    <p id="p18211830102310"><a name="p18211830102310"></a><a name="p18211830102310"></a>Spaces before and after a key will be deprecated.</p>
    </td>
    </tr>
    <tr id="row15244259"><td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.1 "><p id="p26825449"><a name="p26825449"></a><a name="p26825449"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p25377797"><a name="p25377797"></a><a name="p25377797"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p42335644"><a name="p42335644"></a><a name="p42335644"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p6635160"><a name="p6635160"></a><a name="p6635160"></a>List of tag values</p>
    <p id="p2523131132416"><a name="p2523131132416"></a><a name="p2523131132416"></a>The list can contain up to 10 values.</p>
    <p id="p991663534711"><a name="p991663534711"></a><a name="p991663534711"></a>A tag value consists of up to 255 characters.</p>
    <p id="p19191952142520"><a name="p19191952142520"></a><a name="p19191952142520"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p1054662113481"><a name="p1054662113481"></a><a name="p1054662113481"></a>Values in this list must be unique.</p>
    <p id="p261532134815"><a name="p261532134815"></a><a name="p261532134815"></a>Values in this list are in an OR relationship.</p>
    <p id="p1058913346263"><a name="p1058913346263"></a><a name="p1058913346263"></a>This list can be empty and each value can be an empty character string.</p>
    <p id="p423705915480"><a name="p423705915480"></a><a name="p423705915480"></a>If this list is left blank, it indicates that all values are included.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **match**

    **Table  5**  Parameter description of field  **match**

    <a name="table18068436"></a>
    <table><thead align="left"><tr id="row56908160"><th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.5.1.1"><p id="p143491832181216"><a name="p143491832181216"></a><a name="p143491832181216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p1436510326125"><a name="p1436510326125"></a><a name="p1436510326125"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.3"><p id="p136523211121"><a name="p136523211121"></a><a name="p136523211121"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p4380132141214"><a name="p4380132141214"></a><a name="p4380132141214"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52430087"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p18978665"><a name="p18978665"></a><a name="p18978665"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p60876920"><a name="p60876920"></a><a name="p60876920"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p32083483"><a name="p32083483"></a><a name="p32083483"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p10967192418392"><a name="p10967192418392"></a><a name="p10967192418392"></a>Tag key</p>
    <p id="p75017351392"><a name="p75017351392"></a><a name="p75017351392"></a>Possible values are:</p>
    <p id="p10450046113913"><a name="p10450046113913"></a><a name="p10450046113913"></a><strong id="b842352706202849"><a name="b842352706202849"></a><a name="b842352706202849"></a>resource_name</strong>: indicates the resource name.</p>
    </td>
    </tr>
    <tr id="row34974869"><td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.1 "><p id="p14392122"><a name="p14392122"></a><a name="p14392122"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p24911248"><a name="p24911248"></a><a name="p24911248"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.3 "><p id="p4545214"><a name="p4545214"></a><a name="p4545214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p1843451574214"><a name="p1843451574214"></a><a name="p1843451574214"></a>Tag value</p>
    <p id="p1830782015424"><a name="p1830782015424"></a><a name="p1830782015424"></a>A tag value consists of up to 255 characters.</p>
    <p id="p32618093"><a name="p32618093"></a><a name="p32618093"></a>If <strong id="b842352706203053"><a name="b842352706203053"></a><a name="b842352706203053"></a>key</strong> is set to <strong id="b842352706203057"><a name="b842352706203057"></a><a name="b842352706203057"></a>resource_name</strong>, an empty character string indicates exact matching and any non-empty string indicates fuzzy matching. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/csbs_backup/resource_instances/action
    ```


-   When  **action**  is set to  **filter**:

    ```
    {
        "offset": "100",
        "limit": "100",
        "action": "filter",
        "matches": [{
                "key": "resource_name",
                "value": "resource1"
            }
        ],
        "not_tags": [{
                "key": "key1",
                "values": [
                    "*value1",
                    "value2"
                ]
            }
        ],
        "tags": [{
                "key": "key1",
                "values": [
                    "*value1",
                    "value2"
                ]
            }
        ],
        "tags_any": [{
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                ]
            }
        ],
        "not_tags_any": [{
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                ]
            }
        ]
    }
    ```


-   When  **action**  is set to  **count**:

    ```
    {
        "action": "count",
        "not_tags": [{
                "key": "key1",
                "values": [
                    "value1",
                    "*value2"
                ]
            }
        ],
        "tags": [{
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                ]
            }
        ],
        "tags_any": [{
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                ]
            }
        ],
        "not_tags_any": [{
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                ]
            }
        ],
        "matches": [{
                "key": "resource_name",
                "value": "resource1"
            }
        ]
    }
    ```


## Response<a name="section65711047"></a>

-   Parameter description

    **Table  6**  Parameter description

    <a name="table61958854"></a>
    <table><thead align="left"><tr id="row41454307"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p1630103911127"><a name="p1630103911127"></a><a name="p1630103911127"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p564516393128"><a name="p564516393128"></a><a name="p564516393128"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p464593901215"><a name="p464593901215"></a><a name="p464593901215"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13864738"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p49301983"><a name="p49301983"></a><a name="p49301983"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p34037668"><a name="p34037668"></a><a name="p34037668"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p5587738"><a name="p5587738"></a><a name="p5587738"></a>List of matched resources (This parameter is not displayed if <strong id="b1759243687"><a name="b1759243687"></a><a name="b1759243687"></a>action</strong> is set to <strong id="b161621166"><a name="b161621166"></a><a name="b161621166"></a>count</strong>.)</p>
    </td>
    </tr>
    <tr id="row50289647"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p46929584"><a name="p46929584"></a><a name="p46929584"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p43199991"><a name="p43199991"></a><a name="p43199991"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p19183631135514"><a name="p19183631135514"></a><a name="p19183631135514"></a>Total number of matched resources</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description of field  **resource**

    **Table  7**  Parameter description of field  **resource**

    <a name="table12686464"></a>
    <table><thead align="left"><tr id="row15160332"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p25184812122"><a name="p25184812122"></a><a name="p25184812122"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p17201748121216"><a name="p17201748121216"></a><a name="p17201748121216"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p22084818120"><a name="p22084818120"></a><a name="p22084818120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22103973"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p45591407"><a name="p45591407"></a><a name="p45591407"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1916477"><a name="p1916477"></a><a name="p1916477"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p21016952"><a name="p21016952"></a><a name="p21016952"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row54934841"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p20537154"><a name="p20537154"></a><a name="p20537154"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p52896747"><a name="p52896747"></a><a name="p52896747"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p56778076"><a name="p56778076"></a><a name="p56778076"></a>Resource details</p>
    <p id="p17874425294"><a name="p17874425294"></a><a name="p17874425294"></a>Backup details, including <strong id="b842352706203428"><a name="b842352706203428"></a><a name="b842352706203428"></a>tags</strong></p>
    </td>
    </tr>
    <tr id="row41240639"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p52157488"><a name="p52157488"></a><a name="p52157488"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p64007038"><a name="p64007038"></a><a name="p64007038"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p17187600"><a name="p17187600"></a><a name="p17187600"></a>Tag list</p>
    </td>
    </tr>
    <tr id="row20470679"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p47512266"><a name="p47512266"></a><a name="p47512266"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p23288375"><a name="p23288375"></a><a name="p23288375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p7310212"><a name="p7310212"></a><a name="p7310212"></a>Resource name</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_detail**

    **Table  8**  Parameter description of field  **resource\_detail**

    <a name="table31284045"></a>
    <table><thead align="left"><tr id="row64126600"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1367713113139"><a name="p1367713113139"></a><a name="p1367713113139"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p156936118131"><a name="p156936118131"></a><a name="p156936118131"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p196935111131"><a name="p196935111131"></a><a name="p196935111131"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26325568"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51996302"><a name="p51996302"></a><a name="p51996302"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p33385823"><a name="p33385823"></a><a name="p33385823"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19897138"><a name="p19897138"></a><a name="p19897138"></a>Backup record ID</p>
    </td>
    </tr>
    <tr id="row44856519"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9499412"><a name="p9499412"></a><a name="p9499412"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48618095"><a name="p48618095"></a><a name="p48618095"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45751629"><a name="p45751629"></a><a name="p45751629"></a>Creation time, for example, <strong id="b136843365254"><a name="b136843365254"></a><a name="b136843365254"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row9111485"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66941716"><a name="p66941716"></a><a name="p66941716"></a>extend_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44192877"><a name="p44192877"></a><a name="p44192877"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22853313"><a name="p22853313"></a><a name="p22853313"></a>Extension information</p>
    </td>
    </tr>
    <tr id="row4353229"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17067270"><a name="p17067270"></a><a name="p17067270"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40779379"><a name="p40779379"></a><a name="p40779379"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14795382"><a name="p14795382"></a><a name="p14795382"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row66049575"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48415341"><a name="p48415341"></a><a name="p48415341"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26805152"><a name="p26805152"></a><a name="p26805152"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23733724"><a name="p23733724"></a><a name="p23733724"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row12276932"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54907410"><a name="p54907410"></a><a name="p54907410"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7135583"><a name="p7135583"></a><a name="p7135583"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p41111342"><a name="p41111342"></a><a name="p41111342"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row34457765"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39615556"><a name="p39615556"></a><a name="p39615556"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5034912"><a name="p5034912"></a><a name="p5034912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5174700"><a name="p5174700"></a><a name="p5174700"></a>Backup status. Possible values are <strong id="b842352706203645"><a name="b842352706203645"></a><a name="b842352706203645"></a>deleted</strong>, <strong id="b842352706203643"><a name="b842352706203643"></a><a name="b842352706203643"></a>waiting_protect</strong>, <strong id="b842352706203651"><a name="b842352706203651"></a><a name="b842352706203651"></a>protecting</strong>, <strong id="b842352706203654"><a name="b842352706203654"></a><a name="b842352706203654"></a>available</strong>, <strong id="b842352706203659"><a name="b842352706203659"></a><a name="b842352706203659"></a>waiting_restore</strong>, <strong id="b84235270620372"><a name="b84235270620372"></a><a name="b84235270620372"></a>restoring</strong>, <strong id="b84235270620378"><a name="b84235270620378"></a><a name="b84235270620378"></a>error</strong>, <strong id="b842352706203714"><a name="b842352706203714"></a><a name="b842352706203714"></a>waiting_delete</strong>, and <strong id="b842352706203716"><a name="b842352706203716"></a><a name="b842352706203716"></a>deleting</strong>.</p>
    <p id="p199923219255"><a name="p199923219255"></a><a name="p199923219255"></a>Enum:[ waiting_protect, protecting, available, waiting_restore, restoring, error, waiting_delete, deleting,deleted]</p>
    </td>
    </tr>
    <tr id="row16497581"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p61235723"><a name="p61235723"></a><a name="p61235723"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p53922812"><a name="p53922812"></a><a name="p53922812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5671647"><a name="p5671647"></a><a name="p5671647"></a>Modification time, for example, <strong id="b1344123872518"><a name="b1344123872518"></a><a name="b1344123872518"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row51044828"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40990393"><a name="p40990393"></a><a name="p40990393"></a>backup_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p32752180"><a name="p32752180"></a><a name="p32752180"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35680930"><a name="p35680930"></a><a name="p35680930"></a>VM metadata</p>
    </td>
    </tr>
    <tr id="row7523923353"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2052319231152"><a name="p2052319231152"></a><a name="p2052319231152"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25231123550"><a name="p25231123550"></a><a name="p25231123550"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1452312318520"><a name="p1452312318520"></a><a name="p1452312318520"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row1483112381346"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p583173853411"><a name="p583173853411"></a><a name="p583173853411"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12831193833415"><a name="p12831193833415"></a><a name="p12831193833415"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p7831173883410"><a name="p7831173883410"></a><a name="p7831173883410"></a>Tag list</p>
    </td>
    </tr>
    <tr id="row186965413101"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1430747161018"><a name="p1430747161018"></a><a name="p1430747161018"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p133205712103"><a name="p133205712103"></a><a name="p133205712103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p83271175104"><a name="p83271175104"></a><a name="p83271175104"></a>Resource type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **extend\_info**

    **Table  9**  Parameter description of field  **extend\_info**

    <a name="table4474257"></a>
    <table><thead align="left"><tr id="row25374974"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p861741315132"><a name="p861741315132"></a><a name="p861741315132"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p66337137131"><a name="p66337137131"></a><a name="p66337137131"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p106491113161315"><a name="p106491113161315"></a><a name="p106491113161315"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35881396"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20711946"><a name="p20711946"></a><a name="p20711946"></a>auto_trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62743133"><a name="p62743133"></a><a name="p62743133"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p49029033"><a name="p49029033"></a><a name="p49029033"></a>Whether automatic trigger is enabled</p>
    </td>
    </tr>
    <tr id="row38608121"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40250071"><a name="p40250071"></a><a name="p40250071"></a>average_speed</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7336516"><a name="p7336516"></a><a name="p7336516"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57386915"><a name="p57386915"></a><a name="p57386915"></a>Average speed</p>
    </td>
    </tr>
    <tr id="row46720194"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26239345"><a name="p26239345"></a><a name="p26239345"></a>copy_from</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p22108653"><a name="p22108653"></a><a name="p22108653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45970441"><a name="p45970441"></a><a name="p45970441"></a>This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row11080792"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25128946"><a name="p25128946"></a><a name="p25128946"></a>copy_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51649553"><a name="p51649553"></a><a name="p51649553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p112911849103111"><a name="p112911849103111"></a><a name="p112911849103111"></a>This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row40063217"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23895134"><a name="p23895134"></a><a name="p23895134"></a>fail_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9669625"><a name="p9669625"></a><a name="p9669625"></a>fail_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45042167"><a name="p45042167"></a><a name="p45042167"></a>Error code</p>
    </td>
    </tr>
    <tr id="row2726327"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19505966"><a name="p19505966"></a><a name="p19505966"></a>fail_op</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2039495"><a name="p2039495"></a><a name="p2039495"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30981435"><a name="p30981435"></a><a name="p30981435"></a>Type of the failed operation</p>
    <p id="p10397463"><a name="p10397463"></a><a name="p10397463"></a>Enum: [backup, restore, delete, verify, copy]</p>
    </td>
    </tr>
    <tr id="row26468307"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63558136"><a name="p63558136"></a><a name="p63558136"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p57560327"><a name="p57560327"></a><a name="p57560327"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p31874881"><a name="p31874881"></a><a name="p31874881"></a>Description of the failure cause</p>
    </td>
    </tr>
    <tr id="row18438475"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17121511"><a name="p17121511"></a><a name="p17121511"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61107184"><a name="p61107184"></a><a name="p61107184"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50734894"><a name="p50734894"></a><a name="p50734894"></a>Backup type</p>
    </td>
    </tr>
    <tr id="row53960863"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p8753788"><a name="p8753788"></a><a name="p8753788"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55529076"><a name="p55529076"></a><a name="p55529076"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1561311"><a name="p1561311"></a><a name="p1561311"></a>Whether incremental backup is used</p>
    </td>
    </tr>
    <tr id="row14051800"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p64454033"><a name="p64454033"></a><a name="p64454033"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29959179"><a name="p29959179"></a><a name="p29959179"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p10774429"><a name="p10774429"></a><a name="p10774429"></a>Backup progress. The value is an integer ranging from 0 to 100.</p>
    </td>
    </tr>
    <tr id="row29860999"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2821893"><a name="p2821893"></a><a name="p2821893"></a>resource_az</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p59506486"><a name="p59506486"></a><a name="p59506486"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55296057"><a name="p55296057"></a><a name="p55296057"></a>AZ to which the backup resource belongs</p>
    </td>
    </tr>
    <tr id="row27902470"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45507587"><a name="p45507587"></a><a name="p45507587"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7944126"><a name="p7944126"></a><a name="p7944126"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39494476"><a name="p39494476"></a><a name="p39494476"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row611222610436"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p149812204222"><a name="p149812204222"></a><a name="p149812204222"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p998142020221"><a name="p998142020221"></a><a name="p998142020221"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p09822022216"><a name="p09822022216"></a><a name="p09822022216"></a>Backup object type</p>
    </td>
    </tr>
    <tr id="row19905972"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1771067"><a name="p1771067"></a><a name="p1771067"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10137332"><a name="p10137332"></a><a name="p10137332"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15817592"><a name="p15817592"></a><a name="p15817592"></a>Backup capacity</p>
    </td>
    </tr>
    <tr id="row8140604"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p55409189"><a name="p55409189"></a><a name="p55409189"></a>space_saving_ratio</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10978802"><a name="p10978802"></a><a name="p10978802"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p16867749"><a name="p16867749"></a><a name="p16867749"></a>Space saving rate</p>
    </td>
    </tr>
    <tr id="row17592014"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p15667012"><a name="p15667012"></a><a name="p15667012"></a>volume_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p47601111"><a name="p47601111"></a><a name="p47601111"></a>List&lt;volume_backup&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30484803"><a name="p30484803"></a><a name="p30484803"></a>Volume backup list</p>
    </td>
    </tr>
    <tr id="row5927779"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10388065"><a name="p10388065"></a><a name="p10388065"></a>finished_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40598030"><a name="p40598030"></a><a name="p40598030"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p106125"><a name="p106125"></a><a name="p106125"></a>Backup completion time, for example, <strong id="b14715204514256"><a name="b14715204514256"></a><a name="b14715204514256"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row1878614674719"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14691120181216"><a name="p14691120181216"></a><a name="p14691120181216"></a>supported_restore_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p204691920121214"><a name="p204691920121214"></a><a name="p204691920121214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18728201715"><a name="p18728201715"></a><a name="p18728201715"></a>Restoration mode. Possible values are <strong id="b87075192210935"><a name="b87075192210935"></a><a name="b87075192210935"></a>na</strong>, <strong id="b84235270610734"><a name="b84235270610734"></a><a name="b84235270610734"></a>snapshot</strong>, and <strong id="b84235270610737"><a name="b84235270610737"></a><a name="b84235270610737"></a>backup</strong>.</p>
    <p id="p55391555134115"><a name="p55391555134115"></a><a name="p55391555134115"></a><strong id="b84235270610750"><a name="b84235270610750"></a><a name="b84235270610750"></a>snapshot</strong>: Data is restored from snapshots of the EVS disks of the ECS.</p>
    <p id="p8166816173"><a name="p8166816173"></a><a name="p8166816173"></a><strong id="b84235270610831"><a name="b84235270610831"></a><a name="b84235270610831"></a>backup</strong>: Data is restored from backups of the EVS disks of the server.</p>
    <p id="p11211554424"><a name="p11211554424"></a><a name="p11211554424"></a><strong id="b84235270610912"><a name="b84235270610912"></a><a name="b84235270610912"></a>na</strong>: Restoration is not supported.</p>
    </td>
    </tr>
    <tr id="row73401142174616"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p334014284610"><a name="p334014284610"></a><a name="p334014284610"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5340242114618"><a name="p5340242114618"></a><a name="p5340242114618"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p193409421466"><a name="p193409421466"></a><a name="p193409421466"></a>Tag list</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **backup\_data**

    **Table  10**  Parameter description of field  **backup\_data**

    <a name="table8596189"></a>
    <table><thead align="left"><tr id="row56714947"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p653923551315"><a name="p653923551315"></a><a name="p653923551315"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p135392358133"><a name="p135392358133"></a><a name="p135392358133"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p15555193519135"><a name="p15555193519135"></a><a name="p15555193519135"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63047142"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6544886"><a name="p6544886"></a><a name="p6544886"></a>__openstack_region_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58434603"><a name="p58434603"></a><a name="p58434603"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35582368"><a name="p35582368"></a><a name="p35582368"></a>Name of the AZ where the ECS resides</p>
    </td>
    </tr>
    <tr id="row51805857"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p35524928"><a name="p35524928"></a><a name="p35524928"></a>cloudservicetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9973792"><a name="p9973792"></a><a name="p9973792"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2570800"><a name="p2570800"></a><a name="p2570800"></a>ECS type</p>
    </td>
    </tr>
    <tr id="row23137205"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62174317"><a name="p62174317"></a><a name="p62174317"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p38022763"><a name="p38022763"></a><a name="p38022763"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59944961"><a name="p59944961"></a><a name="p59944961"></a>System disk size corresponding to the ECS specifications</p>
    </td>
    </tr>
    <tr id="row2633738"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12006197"><a name="p12006197"></a><a name="p12006197"></a>imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p53964645"><a name="p53964645"></a><a name="p53964645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9060154"><a name="p9060154"></a><a name="p9060154"></a>Image type. Possible values are <strong id="b842352706102151"><a name="b842352706102151"></a><a name="b842352706102151"></a>gold</strong> (public image), <strong id="b842352706102251"><a name="b842352706102251"></a><a name="b842352706102251"></a>private</strong> (private image), and <strong id="b842352706102254"><a name="b842352706102254"></a><a name="b842352706102254"></a>market</strong> (market image).</p>
    <p id="p14432528"><a name="p14432528"></a><a name="p14432528"></a>Enum: [gold, private, market]</p>
    </td>
    </tr>
    <tr id="row62783896"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52330790"><a name="p52330790"></a><a name="p52330790"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p13365491"><a name="p13365491"></a><a name="p13365491"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8862978"><a name="p8862978"></a><a name="p8862978"></a>Memory size of the ECS, in MB</p>
    </td>
    </tr>
    <tr id="row12657945"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p18660600"><a name="p18660600"></a><a name="p18660600"></a>vcpus</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25630932"><a name="p25630932"></a><a name="p25630932"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p62839584"><a name="p62839584"></a><a name="p62839584"></a>CPU cores corresponding to the ECS</p>
    </td>
    </tr>
    <tr id="row28685351"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41812081"><a name="p41812081"></a><a name="p41812081"></a>eip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55141104"><a name="p55141104"></a><a name="p55141104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37244403"><a name="p37244403"></a><a name="p37244403"></a>Elastic IP address of the ECS</p>
    </td>
    </tr>
    <tr id="row66764179"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39189427"><a name="p39189427"></a><a name="p39189427"></a>private_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27774216"><a name="p27774216"></a><a name="p27774216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35118989"><a name="p35118989"></a><a name="p35118989"></a>Internal IP address of the ECS</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **image\_data**

    **Table  11**  Parameter description of field  **image\_data**

    <a name="table17665422205719"></a>
    <table><thead align="left"><tr id="row156851122175719"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p16899174711310"><a name="p16899174711310"></a><a name="p16899174711310"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p7914347191316"><a name="p7914347191316"></a><a name="p7914347191316"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p15914647141320"><a name="p15914647141320"></a><a name="p15914647141320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6718112212576"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11724172211573"><a name="p11724172211573"></a><a name="p11724172211573"></a>image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p173310227573"><a name="p173310227573"></a><a name="p173310227573"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p3739112205719"><a name="p3739112205719"></a><a name="p3739112205719"></a>Image ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **fail\_code**

    **Table  12**  Parameter description of field  **fail\_code**

    <a name="table13384103111117"></a>
    <table><thead align="left"><tr id="row173845314115"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1486956201313"><a name="p1486956201313"></a><a name="p1486956201313"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p15102145612135"><a name="p15102145612135"></a><a name="p15102145612135"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p111171056121320"><a name="p111171056121320"></a><a name="p111171056121320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1838415319115"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14384103120115"><a name="p14384103120115"></a><a name="p14384103120115"></a>Code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p13384113115116"><a name="p13384113115116"></a><a name="p13384113115116"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23846311716"><a name="p23846311716"></a><a name="p23846311716"></a>Error code</p>
    </td>
    </tr>
    <tr id="row20384231212"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p838433113119"><a name="p838433113119"></a><a name="p838433113119"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p23849318116"><a name="p23849318116"></a><a name="p23849318116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p163844311713"><a name="p163844311713"></a><a name="p163844311713"></a>Error description</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field** volume\_backup**

    **Table  13**  Parameter description of field** volume\_backup**

    <a name="table26065838"></a>
    <table><thead align="left"><tr id="row3231685"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p12141246141"><a name="p12141246141"></a><a name="p12141246141"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p9158145145"><a name="p9158145145"></a><a name="p9158145145"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p191735431413"><a name="p191735431413"></a><a name="p191735431413"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8986735"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p56836906"><a name="p56836906"></a><a name="p56836906"></a>average_speed</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50095482"><a name="p50095482"></a><a name="p50095482"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p31202271"><a name="p31202271"></a><a name="p31202271"></a>Average speed</p>
    </td>
    </tr>
    <tr id="row12384989"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63660086"><a name="p63660086"></a><a name="p63660086"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55367277"><a name="p55367277"></a><a name="p55367277"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55564443"><a name="p55564443"></a><a name="p55564443"></a>Whether the disk is bootable</p>
    </td>
    </tr>
    <tr id="row30317943"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39834343"><a name="p39834343"></a><a name="p39834343"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31212633"><a name="p31212633"></a><a name="p31212633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45195306"><a name="p45195306"></a><a name="p45195306"></a>Cinder backup ID</p>
    </td>
    </tr>
    <tr id="row4104573"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p64035022"><a name="p64035022"></a><a name="p64035022"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p32297070"><a name="p32297070"></a><a name="p32297070"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p65925901"><a name="p65925901"></a><a name="p65925901"></a>Backup set type: backup</p>
    <p id="p56462200"><a name="p56462200"></a><a name="p56462200"></a>Enum:[ backup]</p>
    </td>
    </tr>
    <tr id="row38397760"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23210864"><a name="p23210864"></a><a name="p23210864"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16467941"><a name="p16467941"></a><a name="p16467941"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p58834810"><a name="p58834810"></a><a name="p58834810"></a>Whether incremental backup is used</p>
    </td>
    </tr>
    <tr id="row59751243"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p8012554"><a name="p8012554"></a><a name="p8012554"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24132138"><a name="p24132138"></a><a name="p24132138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8546138"><a name="p8546138"></a><a name="p8546138"></a>EVS disk backup name</p>
    </td>
    </tr>
    <tr id="row9806383"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p56119559"><a name="p56119559"></a><a name="p56119559"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p41203013"><a name="p41203013"></a><a name="p41203013"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p49109755"><a name="p49109755"></a><a name="p49109755"></a>Accumulated size (MB) of backups</p>
    </td>
    </tr>
    <tr id="row39334612"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p31986975"><a name="p31986975"></a><a name="p31986975"></a>source_volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p17128847"><a name="p17128847"></a><a name="p17128847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45259396"><a name="p45259396"></a><a name="p45259396"></a>Source disk ID</p>
    </td>
    </tr>
    <tr id="row4681386"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43648019"><a name="p43648019"></a><a name="p43648019"></a>source_volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p21133674"><a name="p21133674"></a><a name="p21133674"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34106024"><a name="p34106024"></a><a name="p34106024"></a>Source volume size in GB</p>
    </td>
    </tr>
    <tr id="row38518764"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33012204"><a name="p33012204"></a><a name="p33012204"></a>space_saving_ratio</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p32770942"><a name="p32770942"></a><a name="p32770942"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37200607"><a name="p37200607"></a><a name="p37200607"></a>Space saving rate</p>
    </td>
    </tr>
    <tr id="row66370010"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7261755"><a name="p7261755"></a><a name="p7261755"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64196347"><a name="p64196347"></a><a name="p64196347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p32521642"><a name="p32521642"></a><a name="p32521642"></a>Status</p>
    </td>
    </tr>
    <tr id="row24259325"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p18848346"><a name="p18848346"></a><a name="p18848346"></a>source_volume_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49472988"><a name="p49472988"></a><a name="p49472988"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p47889106"><a name="p47889106"></a><a name="p47889106"></a>Source volume name</p>
    </td>
    </tr>
    <tr id="row0397855134916"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p18739530979"><a name="p18739530979"></a><a name="p18739530979"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p773917301975"><a name="p773917301975"></a><a name="p773917301975"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p3739143011716"><a name="p3739143011716"></a><a name="p3739143011716"></a>ID of the snapshot from which the backup is generated</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  14**  Parameter description of field  **resource\_tag**

    <a name="table55256281"></a>
    <table><thead align="left"><tr id="row23988764"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p11798111317143"><a name="p11798111317143"></a><a name="p11798111317143"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p381413139144"><a name="p381413139144"></a><a name="p381413139144"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p5814131318142"><a name="p5814131318142"></a><a name="p5814131318142"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24665405"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p51740790"><a name="p51740790"></a><a name="p51740790"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p30254496"><a name="p30254496"></a><a name="p30254496"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p13925135105714"><a name="p13925135105714"></a><a name="p13925135105714"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row43820797"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p59823639"><a name="p59823639"></a><a name="p59823639"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p13876573"><a name="p13876573"></a><a name="p13876573"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p1966153512589"><a name="p1966153512589"></a><a name="p1966153512589"></a>Tag value</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p139758212811"><a name="p139758212811"></a><a name="p139758212811"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    <p id="p49692801"><a name="p49692801"></a><a name="p49692801"></a></p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    When  **action**  is set to  **filter**:

    ```
    {
        "status":"aviable",
        "backup_data":{
            "eip":"",
            "cloudservicetype":"QEMU",
            "ram":1024,
            "__openstack_region_name":"",
            "vcpus":1,
            "private_ip":"",
            "disk":0,
            "imagetype":"gold"
        },
        "periodic_type":null,
        "name":"manualbk_ea67",
        "resource_id":"58482e0b-a357-4125-bdad-102f796b0e0c",
        "created_at":"2020-02-11T06:34:43.897750",
        "checkpoint_id":"ee45c782-71f8-4265-8392-e31fc701836c",
        "replication_records":[
     
        ],
        "updated_at":"2020-02-11T06:38:29.765609",
        "protected_at":"2020-02-11T06:30:26.000000",
        "tags":[
     
        ],
        "extend_info":{
            "auto_trigger":false,
            "finished_at":"2020-02-11T06:38:29.748932",
            "volume_backups":[
     
            ],
            "incremental":true,
            "copy_from":null,
            "dec_size":0,
            "size":0,
            "resource_az":"br-iaas-odin1b",
            "copy_status":"na",
            "image_type":"backup",
            "average_speed":0,
            "taskid":"e9c97c75-59fa-4b99-8b4b-1dd991dbba33",
            "progress":8,
            "resource_type":"OS::Nova::Server"
        },
        "progress":null,
        "expired_at":null,
        "id":"a6d04e0e-0121-41d1-8371-eaeab14482f8",
        "resource_type":"OS::Nova::Server",
        "description":"--"
    }
    ```

    When  **action**  is set to  **count**:

    ```
    {
        total_count": 1000
    }
    ```


## Status Codes<a name="section54528513"></a>

-   Normal

    <a name="table9107180"></a>
    <table><thead align="left"><tr id="row26570537"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p4729870"><a name="p4729870"></a><a name="p4729870"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p47575204"><a name="p47575204"></a><a name="p47575204"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28386322"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p17590785"><a name="p17590785"></a><a name="p17590785"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15567513"><a name="p15567513"></a><a name="p15567513"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table53009025"></a>
    <table><thead align="left"><tr id="row38294646"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p14858635"><a name="p14858635"></a><a name="p14858635"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p62698772"><a name="p62698772"></a><a name="p62698772"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45435770"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p56418724"><a name="p56418724"></a><a name="p56418724"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p6513914"><a name="p6513914"></a><a name="p6513914"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row58625234"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p51023510"><a name="p51023510"></a><a name="p51023510"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p39263675"><a name="p39263675"></a><a name="p39263675"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row17828761"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p34843570"><a name="p34843570"></a><a name="p34843570"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p3756927"><a name="p3756927"></a><a name="p3756927"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row33812349"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p54445748"><a name="p54445748"></a><a name="p54445748"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p48029459"><a name="p48029459"></a><a name="p48029459"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row29611954"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p49758049"><a name="p49758049"></a><a name="p49758049"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p3870157"><a name="p3870157"></a><a name="p3870157"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

