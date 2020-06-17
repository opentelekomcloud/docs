# Querying Backup Policy Resource Instances<a name="EN-US_TOPIC_0098635092"></a>

## Function<a name="section29028938"></a>

This API is used to filter instances by specifying tags.

TMS uses this API to filter and list instances of each service by tag. These services must have the query capabilities.

## URI<a name="section59933852"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/csbs\_backup\_policy/resource\_instances/action

-   Request header

    **Table  1**  Request header

    <a name="table54243925"></a>
    <table><thead align="left"><tr id="row52324181"><th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.54455445544555%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15002532"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p7245613"><a name="p7245613"></a><a name="p7245613"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p1627911256416"><a name="p1627911256416"></a><a name="p1627911256416"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p50023786"><a name="p50023786"></a><a name="p50023786"></a>MIME type of the body in the request</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p43719714"><a name="p43719714"></a><a name="p43719714"></a>application/json</p>
    </td>
    </tr>
    <tr id="row57933110"><td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.1 "><p id="p62070358"><a name="p62070358"></a><a name="p62070358"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p1425020251411"><a name="p1425020251411"></a><a name="p1425020251411"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p61643119"><a name="p61643119"></a><a name="p61643119"></a>User token</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.54455445544555%" headers="mcps1.2.5.1.4 "><p id="p42490025"><a name="p42490025"></a><a name="p42490025"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description

    **Table  2**  Parameter description

    <a name="table6835749"></a>
    <table><thead align="left"><tr id="row8975271"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p16705123102410"><a name="p16705123102410"></a><a name="p16705123102410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p970516320249"><a name="p970516320249"></a><a name="p970516320249"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p1770515392418"><a name="p1770515392418"></a><a name="p1770515392418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p7705239247"><a name="p7705239247"></a><a name="p7705239247"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15257210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p27874499"><a name="p27874499"></a><a name="p27874499"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p43241981"><a name="p43241981"></a><a name="p43241981"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p12939600"><a name="p12939600"></a><a name="p12939600"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section2533758"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table61979735"></a>
    <table><thead align="left"><tr id="row56093531"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p81581496248"><a name="p81581496248"></a><a name="p81581496248"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p151581499244"><a name="p151581499244"></a><a name="p151581499244"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p417319142412"><a name="p417319142412"></a><a name="p417319142412"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p18173129172411"><a name="p18173129172411"></a><a name="p18173129172411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25425146"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p46170965"><a name="p46170965"></a><a name="p46170965"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p48860697"><a name="p48860697"></a><a name="p48860697"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p65402348"><a name="p65402348"></a><a name="p65402348"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p15624527153813"><a name="p15624527153813"></a><a name="p15624527153813"></a>List of included tags. Backup resource instances with these tags will be filtered.</p>
    <p id="p0494199183911"><a name="p0494199183911"></a><a name="p0494199183911"></a>This list cannot be an empty list.</p>
    <p id="p646324463913"><a name="p646324463913"></a><a name="p646324463913"></a>The list can contain up to 10 keys.</p>
    <p id="p19401115618394"><a name="p19401115618394"></a><a name="p19401115618394"></a>Keys in this list must be unique.</p>
    <p id="p1771815924015"><a name="p1771815924015"></a><a name="p1771815924015"></a>Keys in this list are in an AND relationship.</p>
    </td>
    </tr>
    <tr id="row62104313520"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p54273555474"><a name="p54273555474"></a><a name="p54273555474"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p842755513476"><a name="p842755513476"></a><a name="p842755513476"></a>No</p>
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
    <tr id="row34517843"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p175677415716"><a name="p175677415716"></a><a name="p175677415716"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p145671340571"><a name="p145671340571"></a><a name="p145671340571"></a>No</p>
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
    <tr id="row65311975"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p02193547116"><a name="p02193547116"></a><a name="p02193547116"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p132193541614"><a name="p132193541614"></a><a name="p132193541614"></a>No</p>
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
    <tr id="row55515744"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p481433"><a name="p481433"></a><a name="p481433"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p38996082"><a name="p38996082"></a><a name="p38996082"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p4566035"><a name="p4566035"></a><a name="p4566035"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p34304549"><a name="p34304549"></a><a name="p34304549"></a>Operation to be performed</p>
    <p id="p64392016184311"><a name="p64392016184311"></a><a name="p64392016184311"></a>Possible values are <strong id="b842352706194826"><a name="b842352706194826"></a><a name="b842352706194826"></a>filter</strong> and <strong id="b842352706194830"><a name="b842352706194830"></a><a name="b842352706194830"></a>count</strong>. </p>
    <p id="p40305487"><a name="p40305487"></a><a name="p40305487"></a><strong id="b45514660820229"><a name="b45514660820229"></a><a name="b45514660820229"></a>filter</strong> indicates pagination query and <strong id="b987992455202243"><a name="b987992455202243"></a><a name="b987992455202243"></a>count</strong> indicates that a specified number of queried records will be returned.</p>
    </td>
    </tr>
    <tr id="row27205071"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p56127162"><a name="p56127162"></a><a name="p56127162"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p50006286"><a name="p50006286"></a><a name="p50006286"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p23977329"><a name="p23977329"></a><a name="p23977329"></a>List&lt;match&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p518016559472"><a name="p518016559472"></a><a name="p518016559472"></a>List of query criteria supported by resources</p>
    <p id="p17555154424814"><a name="p17555154424814"></a><a name="p17555154424814"></a>This list cannot be an empty list.</p>
    <p id="p184835314818"><a name="p184835314818"></a><a name="p184835314818"></a>Keys in this list must be unique.</p>
    </td>
    </tr>
    <tr id="row8643311153"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p37522006"><a name="p37522006"></a><a name="p37522006"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p19383628"><a name="p19383628"></a><a name="p19383628"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p26570072"><a name="p26570072"></a><a name="p26570072"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p09225511219"><a name="p09225511219"></a><a name="p09225511219"></a>Query count (This parameter is not displayed if <strong id="b842352706195922"><a name="b842352706195922"></a><a name="b842352706195922"></a>action</strong> is set to <strong id="b842352706195927"><a name="b842352706195927"></a><a name="b842352706195927"></a>count</strong>.)</p>
    <p id="p4692191"><a name="p4692191"></a><a name="p4692191"></a>If <strong id="b842352706102324"><a name="b842352706102324"></a><a name="b842352706102324"></a>action</strong> is set to <strong id="b842352706102329"><a name="b842352706102329"></a><a name="b842352706102329"></a>filter</strong>, the value defaults to <strong id="b842352706102331"><a name="b842352706102331"></a><a name="b842352706102331"></a>1000</strong>. The value ranges from <strong id="b842352706102340"><a name="b842352706102340"></a><a name="b842352706102340"></a>1</strong> to <strong id="b842352706102344"><a name="b842352706102344"></a><a name="b842352706102344"></a>1000</strong>. If you set a value out of this range, an error will be reported. The number of returned records does not exceed the value of <strong id="b842352706194753"><a name="b842352706194753"></a><a name="b842352706194753"></a>limit</strong>. </p>
    </td>
    </tr>
    <tr id="row156741734171519"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p65164587"><a name="p65164587"></a><a name="p65164587"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p43840169"><a name="p43840169"></a><a name="p43840169"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p61392767"><a name="p61392767"></a><a name="p61392767"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p177411411197"><a name="p177411411197"></a><a name="p177411411197"></a>Query index (This parameter is not displayed if <strong id="b1339191340"><a name="b1339191340"></a><a name="b1339191340"></a>action</strong> is set to <strong id="b1174881592"><a name="b1174881592"></a><a name="b1174881592"></a>count</strong>.)</p>
    <p id="p14508185131920"><a name="p14508185131920"></a><a name="p14508185131920"></a>If <strong id="b200691530720216"><a name="b200691530720216"></a><a name="b200691530720216"></a>action</strong> is set to <strong id="b39257038320216"><a name="b39257038320216"></a><a name="b39257038320216"></a>filter</strong>, the value defaults to <strong id="b163342832120216"><a name="b163342832120216"></a><a name="b163342832120216"></a>0</strong> (minimum value). The first record in the query result is the offset+1 record that meets the query criteria. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **tag**

    **Table  4**  Parameter description of field  **tag**

    <a name="table39330064"></a>
    <table><thead align="left"><tr id="row12811779"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p127211130248"><a name="p127211130248"></a><a name="p127211130248"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p1072113131247"><a name="p1072113131247"></a><a name="p1072113131247"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p372191312245"><a name="p372191312245"></a><a name="p372191312245"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p167211113112413"><a name="p167211113112413"></a><a name="p167211113112413"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57097117"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61463750"><a name="p61463750"></a><a name="p61463750"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p12507852"><a name="p12507852"></a><a name="p12507852"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p6503062"><a name="p6503062"></a><a name="p6503062"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p321161514239"><a name="p321161514239"></a><a name="p321161514239"></a>Tag key</p>
    <p id="p10460518142315"><a name="p10460518142315"></a><a name="p10460518142315"></a>A tag key consists of up to 127 characters.</p>
    <p id="p1448142852310"><a name="p1448142852310"></a><a name="p1448142852310"></a>A tag key cannot be an empty string.</p>
    <p id="p18211830102310"><a name="p18211830102310"></a><a name="p18211830102310"></a>Spaces before and after a key will be deprecated.</p>
    </td>
    </tr>
    <tr id="row43111924"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2404952"><a name="p2404952"></a><a name="p2404952"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p60583453"><a name="p60583453"></a><a name="p60583453"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p8312683"><a name="p8312683"></a><a name="p8312683"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p6635160"><a name="p6635160"></a><a name="p6635160"></a>List of tag values</p>
    <p id="p2523131132416"><a name="p2523131132416"></a><a name="p2523131132416"></a>The list can contain up to 10 values.</p>
    <p id="p991663534711"><a name="p991663534711"></a><a name="p991663534711"></a>A tag value consists of up to 255 characters.</p>
    <p id="p19191952142520"><a name="p19191952142520"></a><a name="p19191952142520"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p1054662113481"><a name="p1054662113481"></a><a name="p1054662113481"></a>Values in this list must be unique.</p>
    <p id="p1539561418287"><a name="p1539561418287"></a><a name="p1539561418287"></a>Values in this list are in an OR relationship.</p>
    <p id="p261532134815"><a name="p261532134815"></a><a name="p261532134815"></a>This list can be empty and each value can be an empty character string.</p>
    <p id="p1630812219279"><a name="p1630812219279"></a><a name="p1630812219279"></a>If this list is left blank, it indicates that all values are included.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **match**

    **Table  5**  Parameter description of field  **match**

    <a name="table55470665"></a>
    <table><thead align="left"><tr id="row49592727"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p0126131752410"><a name="p0126131752410"></a><a name="p0126131752410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p2126317112415"><a name="p2126317112415"></a><a name="p2126317112415"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p20126117112416"><a name="p20126117112416"></a><a name="p20126117112416"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p20126141713249"><a name="p20126141713249"></a><a name="p20126141713249"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31671811"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p15279862"><a name="p15279862"></a><a name="p15279862"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p29709347"><a name="p29709347"></a><a name="p29709347"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p57646896"><a name="p57646896"></a><a name="p57646896"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p38886981"><a name="p38886981"></a><a name="p38886981"></a>Tag key</p>
    <p id="p75017351392"><a name="p75017351392"></a><a name="p75017351392"></a>Possible values are:</p>
    <p id="p10450046113913"><a name="p10450046113913"></a><a name="p10450046113913"></a><strong id="b842352706202849"><a name="b842352706202849"></a><a name="b842352706202849"></a>resource_name</strong>: indicates the resource name.</p>
    </td>
    </tr>
    <tr id="row14438515"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p28669032"><a name="p28669032"></a><a name="p28669032"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p40490233"><a name="p40490233"></a><a name="p40490233"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p58483472"><a name="p58483472"></a><a name="p58483472"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p1843451574214"><a name="p1843451574214"></a><a name="p1843451574214"></a>Tag value</p>
    <p id="p1830782015424"><a name="p1830782015424"></a><a name="p1830782015424"></a>A tag value consists of up to 255 characters.</p>
    <p id="p32618093"><a name="p32618093"></a><a name="p32618093"></a>If <strong id="b842352706203053"><a name="b842352706203053"></a><a name="b842352706203053"></a>key</strong> is set to <strong id="b842352706203057"><a name="b842352706203057"></a><a name="b842352706203057"></a>resource_name</strong>, an empty character string indicates exact matching and any non-empty string indicates fuzzy matching. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/csbs_backup_policy/resource_instances/action
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


## Response<a name="section22803825"></a>

-   Parameter description

    **Table  6**  Parameter description

    <a name="table61958854"></a>
    <table><thead align="left"><tr id="row41454307"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p659652316249"><a name="p659652316249"></a><a name="p659652316249"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p10611523162414"><a name="p10611523162414"></a><a name="p10611523162414"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p176111723192417"><a name="p176111723192417"></a><a name="p176111723192417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13864738"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p49301983"><a name="p49301983"></a><a name="p49301983"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p34037668"><a name="p34037668"></a><a name="p34037668"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p2384185575515"><a name="p2384185575515"></a><a name="p2384185575515"></a>List of matched resources (This parameter is not displayed if <strong id="b767907442"><a name="b767907442"></a><a name="b767907442"></a>action</strong> is set to <strong id="b2001782822"><a name="b2001782822"></a><a name="b2001782822"></a>count</strong>.)</p>
    </td>
    </tr>
    <tr id="row50289647"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p46929584"><a name="p46929584"></a><a name="p46929584"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p43199991"><a name="p43199991"></a><a name="p43199991"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.2.4.1.3 "><p id="p9538345"><a name="p9538345"></a><a name="p9538345"></a>Total number of matched resources</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Parameter description of field  **resource**

    **Table  7**  Parameter description of field  **resource**

    <a name="table12686464"></a>
    <table><thead align="left"><tr id="row15160332"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p1670573119241"><a name="p1670573119241"></a><a name="p1670573119241"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p872083182414"><a name="p872083182414"></a><a name="p872083182414"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p14720163142419"><a name="p14720163142419"></a><a name="p14720163142419"></a>Description</p>
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
    <p id="p1734411441237"><a name="p1734411441237"></a><a name="p1734411441237"></a>The returned value is an empty dictionary.</p>
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

-   Parameter description of field  **resource\_tag**

    **Table  8**  Parameter description of field  **resource\_tag**

    <a name="table55256281"></a>
    <table><thead align="left"><tr id="row23988764"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p6784194112249"><a name="p6784194112249"></a><a name="p6784194112249"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p17981441142419"><a name="p17981441142419"></a><a name="p17981441142419"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.33%" id="mcps1.2.4.1.3"><p id="p1179884116241"><a name="p1179884116241"></a><a name="p1179884116241"></a>Description</p>
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
    <p id="p92562414333"><a name="p92562414333"></a><a name="p92562414333"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    When  **action**  is set to  **filter**:

    ```
    {
        "resources": [
            {
                "resource_detail": {}, 
                "resource_id": "cdfs_cefs_wesas_12_dsad", 
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

    When  **action**  is set to  **count**:

    ```
    {
           "total_count": 1000
    }
    ```


## Status Codes<a name="section3907839"></a>

-   Normal

    <a name="table15889527"></a>
    <table><thead align="left"><tr id="row11673575"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p6035484"><a name="p6035484"></a><a name="p6035484"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p19112173"><a name="p19112173"></a><a name="p19112173"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4582212"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p35614854"><a name="p35614854"></a><a name="p35614854"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p66230941"><a name="p66230941"></a><a name="p66230941"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table63106033"></a>
    <table><thead align="left"><tr id="row61389792"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p6517283"><a name="p6517283"></a><a name="p6517283"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p58137894"><a name="p58137894"></a><a name="p58137894"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11548945"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p63049357"><a name="p63049357"></a><a name="p63049357"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p6724289"><a name="p6724289"></a><a name="p6724289"></a>Invalid parameters.</p>
    </td>
    </tr>
    <tr id="row60518608"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p3060236"><a name="p3060236"></a><a name="p3060236"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p46552597"><a name="p46552597"></a><a name="p46552597"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row16320194"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p46867304"><a name="p46867304"></a><a name="p46867304"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p38155279"><a name="p38155279"></a><a name="p38155279"></a>You do not have permission to perform this operation.</p>
    </td>
    </tr>
    <tr id="row7853194"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p32128981"><a name="p32128981"></a><a name="p32128981"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p52310644"><a name="p52310644"></a><a name="p52310644"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1033751"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p16624976"><a name="p16624976"></a><a name="p16624976"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p4445777"><a name="p4445777"></a><a name="p4445777"></a>A system exception occurs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

