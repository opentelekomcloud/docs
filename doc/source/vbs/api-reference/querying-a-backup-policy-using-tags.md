# Querying a Backup Policy Using Tags<a name="EN-US_TOPIC_0067142133"></a>

## Function<a name="section63962185"></a>

This interface is used to query a backup policy using tags.

## URI<a name="section38788755"></a>

-   URI format

    POST /v2/\{project\_id\}/backuppolicy/resource\_instances/action

-   Parameter description

    <a name="table60344938"></a>
    <table><thead align="left"><tr id="row59011071"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p15167431"><a name="p15167431"></a><a name="p15167431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p20602375"><a name="p20602375"></a><a name="p20602375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p58179688"><a name="p58179688"></a><a name="p58179688"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14934289"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1717931"><a name="p1717931"></a><a name="p1717931"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4934750"><a name="p4934750"></a><a name="p4934750"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13554483"></a>

-   Parameter description

    <a name="table55298598184810"></a>
    <table><thead align="left"><tr id="row13717697184810"><th class="cellrowborder" valign="top" width="20.3%" id="mcps1.1.5.1.1"><p id="p1431817452527"><a name="p1431817452527"></a><a name="p1431817452527"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.900000000000002%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.32%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row669026184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p54191158184810"><a name="p54191158184810"></a><a name="p54191158184810"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p27407641184810"><a name="p27407641184810"></a><a name="p27407641184810"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p5426486184810"><a name="p5426486184810"></a><a name="p5426486184810"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p36892211184810"><a name="p36892211184810"></a><a name="p36892211184810"></a>List of tags. Backup policies with these tags will be filtered. This list can have a maximum of 10 tags.</p>
    </td>
    </tr>
    <tr id="row63594445184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p50876414184810"><a name="p50876414184810"></a><a name="p50876414184810"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p27348835184810"><a name="p27348835184810"></a><a name="p27348835184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p663140184810"><a name="p663140184810"></a><a name="p663140184810"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p53714411184810"><a name="p53714411184810"></a><a name="p53714411184810"></a>Tag key. Tag keys must be unique.</p>
    </td>
    </tr>
    <tr id="row13667651184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p33337931184810"><a name="p33337931184810"></a><a name="p33337931184810"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p16017867184810"><a name="p16017867184810"></a><a name="p16017867184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p22378860184810"><a name="p22378860184810"></a><a name="p22378860184810"></a>list&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p748373184810"><a name="p748373184810"></a><a name="p748373184810"></a>List of tag values. This list can have a maximum of 10 tag values and these values must be unique.</p>
    </td>
    </tr>
    <tr id="row6735365184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p8693678184810"><a name="p8693678184810"></a><a name="p8693678184810"></a>tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p33099316184810"><a name="p33099316184810"></a><a name="p33099316184810"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p63798910184810"><a name="p63798910184810"></a><a name="p63798910184810"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p1842725544712"><a name="p1842725544712"></a><a name="p1842725544712"></a>List of tags. Backups with any tags in this list will be filtered.</p>
    <p id="p158584245013"><a name="p158584245013"></a><a name="p158584245013"></a>This list cannot be an empty list.</p>
    <p id="p16591114214506"><a name="p16591114214506"></a><a name="p16591114214506"></a>The list can contain up to 10 keys.</p>
    <p id="p459817429501"><a name="p459817429501"></a><a name="p459817429501"></a>Keys in this list must be unique.</p>
    <p id="p765214147556"><a name="p765214147556"></a><a name="p765214147556"></a>The response returns resources containing any tags in this list. Keys in this list are in an OR relationship while values in each key-value structure is in an OR relationship.</p>
    </td>
    </tr>
    <tr id="row2962844184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p38663808184810"><a name="p38663808184810"></a><a name="p38663808184810"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p44760773184810"><a name="p44760773184810"></a><a name="p44760773184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p1744019184810"><a name="p1744019184810"></a><a name="p1744019184810"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p7047825184810"><a name="p7047825184810"></a><a name="p7047825184810"></a>Tag key</p>
    </td>
    </tr>
    <tr id="row63430425184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p37590819184810"><a name="p37590819184810"></a><a name="p37590819184810"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p24957489184810"><a name="p24957489184810"></a><a name="p24957489184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p8290732184810"><a name="p8290732184810"></a><a name="p8290732184810"></a>list&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p460667184810"><a name="p460667184810"></a><a name="p460667184810"></a>List of tag values</p>
    </td>
    </tr>
    <tr id="row4146006184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p282175184810"><a name="p282175184810"></a><a name="p282175184810"></a>not_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p22856176184810"><a name="p22856176184810"></a><a name="p22856176184810"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p39410962184810"><a name="p39410962184810"></a><a name="p39410962184810"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p115672419576"><a name="p115672419576"></a><a name="p115672419576"></a>List of excluded tags. Backups without these tags will be filtered.</p>
    <p id="p1199314506578"><a name="p1199314506578"></a><a name="p1199314506578"></a>This list cannot be an empty list.</p>
    <p id="p62165145715"><a name="p62165145715"></a><a name="p62165145715"></a>The list can contain up to 10 keys.</p>
    <p id="p0111751105713"><a name="p0111751105713"></a><a name="p0111751105713"></a>Keys in this list must be unique.</p>
    <p id="p17588613201"><a name="p17588613201"></a><a name="p17588613201"></a>The response returns resources containing no tags in this list. Keys in this list are in an AND relationship while values in each key-value structure is in an OR relationship.</p>
    </td>
    </tr>
    <tr id="row7997746184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p43837700184810"><a name="p43837700184810"></a><a name="p43837700184810"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p61192835184810"><a name="p61192835184810"></a><a name="p61192835184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p57672598184810"><a name="p57672598184810"></a><a name="p57672598184810"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p40968870184810"><a name="p40968870184810"></a><a name="p40968870184810"></a>Tag key</p>
    </td>
    </tr>
    <tr id="row33175512184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p2861933184810"><a name="p2861933184810"></a><a name="p2861933184810"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p30490035184810"><a name="p30490035184810"></a><a name="p30490035184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p53773777184810"><a name="p53773777184810"></a><a name="p53773777184810"></a>list&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p60708720184810"><a name="p60708720184810"></a><a name="p60708720184810"></a>List of tag values</p>
    </td>
    </tr>
    <tr id="row9507576184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p31916154184810"><a name="p31916154184810"></a><a name="p31916154184810"></a>not_tags_any</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p35071697184810"><a name="p35071697184810"></a><a name="p35071697184810"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p22235237184810"><a name="p22235237184810"></a><a name="p22235237184810"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p192791022229"><a name="p192791022229"></a><a name="p192791022229"></a>List of tags. Backups without any tags in this list will be filtered.</p>
    <p id="p428532217220"><a name="p428532217220"></a><a name="p428532217220"></a>This list cannot be an empty list.</p>
    <p id="p1229319221525"><a name="p1229319221525"></a><a name="p1229319221525"></a>The list can contain up to 10 keys.</p>
    <p id="p1529610224214"><a name="p1529610224214"></a><a name="p1529610224214"></a>Keys in this list must be unique.</p>
    <p id="p43845237217"><a name="p43845237217"></a><a name="p43845237217"></a>The response returns resources without any tags in this list. Keys in this list are in an OR relationship while values in each key-value structure is in an OR relationship.</p>
    </td>
    </tr>
    <tr id="row36251914184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p50723956184810"><a name="p50723956184810"></a><a name="p50723956184810"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p14999799184810"><a name="p14999799184810"></a><a name="p14999799184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p7024186184810"><a name="p7024186184810"></a><a name="p7024186184810"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p32088165184810"><a name="p32088165184810"></a><a name="p32088165184810"></a>Tag key</p>
    </td>
    </tr>
    <tr id="row20358033184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p38388013184810"><a name="p38388013184810"></a><a name="p38388013184810"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p22421316184810"><a name="p22421316184810"></a><a name="p22421316184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p4187328184810"><a name="p4187328184810"></a><a name="p4187328184810"></a>list&lt;string&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p3629321184810"><a name="p3629321184810"></a><a name="p3629321184810"></a>List of tag values</p>
    </td>
    </tr>
    <tr id="row167381757124916"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p37381157144913"><a name="p37381157144913"></a><a name="p37381157144913"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p187404571492"><a name="p187404571492"></a><a name="p187404571492"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p1074065794912"><a name="p1074065794912"></a><a name="p1074065794912"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p1474095717493"><a name="p1474095717493"></a><a name="p1474095717493"></a>Search criteria. Fuzzy search is supported.</p>
    </td>
    </tr>
    <tr id="row125614719512"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p1136183975111"><a name="p1136183975111"></a><a name="p1136183975111"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p1214363925116"><a name="p1214363925116"></a><a name="p1214363925116"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p714883985119"><a name="p714883985119"></a><a name="p714883985119"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p715314395514"><a name="p715314395514"></a><a name="p715314395514"></a>Field for searching. Currently, only <strong id="b842352706204544"><a name="b842352706204544"></a><a name="b842352706204544"></a>resource_name</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row1656171119519"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p121621039155115"><a name="p121621039155115"></a><a name="p121621039155115"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p2165163925112"><a name="p2165163925112"></a><a name="p2165163925112"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p14354174815112"><a name="p14354174815112"></a><a name="p14354174815112"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p1817253914511"><a name="p1817253914511"></a><a name="p1817253914511"></a>Search value</p>
    </td>
    </tr>
    <tr id="row32663894184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p28529724184810"><a name="p28529724184810"></a><a name="p28529724184810"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p29206307184810"><a name="p29206307184810"></a><a name="p29206307184810"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p16900658184810"><a name="p16900658184810"></a><a name="p16900658184810"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p26776082184810"><a name="p26776082184810"></a><a name="p26776082184810"></a>Number of queried records. This parameter is not displayed if <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> if <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The value must be an integer ranging from <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>.</p>
    </td>
    </tr>
    <tr id="row16150121114710"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p171509114472"><a name="p171509114472"></a><a name="p171509114472"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p19150011204719"><a name="p19150011204719"></a><a name="p19150011204719"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p5150141174711"><a name="p5150141174711"></a><a name="p5150141174711"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p1315016118479"><a name="p1315016118479"></a><a name="p1315016118479"></a>Query index. (This parameter is not displayed if <strong id="b842352706162146"><a name="b842352706162146"></a><a name="b842352706162146"></a>action</strong> is set to <strong id="b842352706162149"><a name="b842352706162149"></a><a name="b842352706162149"></a>count</strong>.) The query starts from the next piece of data indexed by this parameter. If <strong id="b655888473162315"><a name="b655888473162315"></a><a name="b655888473162315"></a>action</strong> is set to <strong id="b969534961162315"><a name="b969534961162315"></a><a name="b969534961162315"></a>filter</strong>, the default value is <strong id="b842352706162352"><a name="b842352706162352"></a><a name="b842352706162352"></a>0</strong> which indicates the query starts from the first piece of data. The value must be a non-negative integer.</p>
    </td>
    </tr>
    <tr id="row37990305184810"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.1.5.1.1 "><p id="p57315884184810"><a name="p57315884184810"></a><a name="p57315884184810"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.900000000000002%" headers="mcps1.1.5.1.2 "><p id="p12075040184810"><a name="p12075040184810"></a><a name="p12075040184810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p38554147184810"><a name="p38554147184810"></a><a name="p38554147184810"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.32%" headers="mcps1.1.5.1.4 "><p id="p35878240184810"><a name="p35878240184810"></a><a name="p35878240184810"></a>Operator. Possible values are:</p>
    <p id="p139614811480"><a name="p139614811480"></a><a name="p139614811480"></a><strong id="b842352706103947"><a name="b842352706103947"></a><a name="b842352706103947"></a>filter</strong>: queries backup policies by specifying filtering conditions.</p>
    <p id="p429424014910"><a name="p429424014910"></a><a name="p429424014910"></a><strong id="b842352706104030"><a name="b842352706104030"></a><a name="b842352706104030"></a>count</strong>: queries backup policies by specifying the total number.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
      "limit": "10",
      "offset": "0",
      "tags":
          [
            {
               "key": "Tag001",
               "values":["Value001","Value002"]
             }
           ],
      "action":"filter"
    }
    ```


## Response<a name="section54881489"></a>

-   Parameter description

    <a name="table2553741120254"></a>
    <table><thead align="left"><tr id="row84520220254"><th class="cellrowborder" valign="top" width="24.94%" id="mcps1.1.4.1.1"><p id="p1851311191196"><a name="p1851311191196"></a><a name="p1851311191196"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.1.4.1.2"><p id="p752919191999"><a name="p752919191999"></a><a name="p752919191999"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.07%" id="mcps1.1.4.1.3"><p id="p1052919191691"><a name="p1052919191691"></a><a name="p1052919191691"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row894248020254"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p34048608151944"><a name="p34048608151944"></a><a name="p34048608151944"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p4563373217131"><a name="p4563373217131"></a><a name="p4563373217131"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p1948402220254"><a name="p1948402220254"></a><a name="p1948402220254"></a>Total number of resources</p>
    </td>
    </tr>
    <tr id="row49142966153315"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p38366875153340"><a name="p38366875153340"></a><a name="p38366875153340"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p66829450153340"><a name="p66829450153340"></a><a name="p66829450153340"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p3760433518513"><a name="p3760433518513"></a><a name="p3760433518513"></a>List of resources</p>
    </td>
    </tr>
    <tr id="row37005886153318"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p9704892153340"><a name="p9704892153340"></a><a name="p9704892153340"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p54594377153340"><a name="p54594377153340"></a><a name="p54594377153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p60068455153340"><a name="p60068455153340"></a><a name="p60068455153340"></a>Resource ID</p>
    </td>
    </tr>
    <tr id="row27429961153321"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p2606949118530"><a name="p2606949118530"></a><a name="p2606949118530"></a>resouce_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p32108888153340"><a name="p32108888153340"></a><a name="p32108888153340"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p50683125153340"><a name="p50683125153340"></a><a name="p50683125153340"></a>Resource details, used for extension</p>
    </td>
    </tr>
    <tr id="row59676584153324"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p38123120153340"><a name="p38123120153340"></a><a name="p38123120153340"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p11054614153340"><a name="p11054614153340"></a><a name="p11054614153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p23008573153340"><a name="p23008573153340"></a><a name="p23008573153340"></a>Resource name</p>
    </td>
    </tr>
    <tr id="row3032128414342"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p4010493014342"><a name="p4010493014342"></a><a name="p4010493014342"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p6170234814342"><a name="p6170234814342"></a><a name="p6170234814342"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p3183428014342"><a name="p3183428014342"></a><a name="p3183428014342"></a>List of tags</p>
    </td>
    </tr>
    <tr id="row17757769153327"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p63142605153340"><a name="p63142605153340"></a><a name="p63142605153340"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p15615278153340"><a name="p15615278153340"></a><a name="p15615278153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p45645767143341"><a name="p45645767143341"></a><a name="p45645767143341"></a>Tag key</p>
    </td>
    </tr>
    <tr id="row55800042153331"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p63777303153340"><a name="p63777303153340"></a><a name="p63777303153340"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p19118878153340"><a name="p19118878153340"></a><a name="p19118878153340"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p46173942143351"><a name="p46173942143351"></a><a name="p46173942143351"></a>Tag value</p>
    </td>
    </tr>
    <tr id="row4113847020254"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p4388173520254"><a name="p4388173520254"></a><a name="p4388173520254"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p534483917131"><a name="p534483917131"></a><a name="p534483917131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p1103955520254"><a name="p1103955520254"></a><a name="p1103955520254"></a>Error message returned after an error occurs</p>
    </td>
    </tr>
    <tr id="row3224713720254"><td class="cellrowborder" valign="top" width="24.94%" headers="mcps1.1.4.1.1 "><p id="p6188131520254"><a name="p6188131520254"></a><a name="p6188131520254"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.4.1.2 "><p id="p3027879417131"><a name="p3027879417131"></a><a name="p3027879417131"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.07%" headers="mcps1.1.4.1.3 "><p id="p6179451720254"><a name="p6179451720254"></a><a name="p6179451720254"></a>Error code returned after an error occurs</p>
    <p id="p1927974620254"><a name="p1927974620254"></a><a name="p1927974620254"></a>For details about error codes, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "total_count":10,
      "resources":[
        {
          "resource_name": "name",
          "resource_id": "0781095c-b8ab-4ce5-99f3-4c5f6ff75319",
          "resource_detail": null,
          "tags": [{
              "key":"key",
              "value":"value"
           }]
        }
      ]
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX",
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section24171358"></a>

-   Normal

    200

-   Abnormal

    <a name="table51230787"></a>
    <table><thead align="left"><tr id="row60503138"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p1807185"><a name="p1807185"></a><a name="p1807185"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p12164329"><a name="p12164329"></a><a name="p12164329"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45786577"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17725233"><a name="p17725233"></a><a name="p17725233"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p26457778"><a name="p26457778"></a><a name="p26457778"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row36793414"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p27476571"><a name="p27476571"></a><a name="p27476571"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11009764"><a name="p11009764"></a><a name="p11009764"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row31979016"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p40163483"><a name="p40163483"></a><a name="p40163483"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p32016662"><a name="p32016662"></a><a name="p32016662"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row4499052116376"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2035357816376"><a name="p2035357816376"></a><a name="p2035357816376"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3802708716376"><a name="p3802708716376"></a><a name="p3802708716376"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row8462523163725"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14375766163725"><a name="p14375766163725"></a><a name="p14375766163725"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p23586373163725"><a name="p23586373163725"></a><a name="p23586373163725"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row60343628163758"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p55995701163758"><a name="p55995701163758"></a><a name="p55995701163758"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p39357967163758"><a name="p39357967163758"></a><a name="p39357967163758"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row32079544163754"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p48306260163754"><a name="p48306260163754"></a><a name="p48306260163754"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20492948163754"><a name="p20492948163754"></a><a name="p20492948163754"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row28680770163738"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p41441040163738"><a name="p41441040163738"></a><a name="p41441040163738"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1281119163738"><a name="p1281119163738"></a><a name="p1281119163738"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row65552906164354"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8185203164354"><a name="p8185203164354"></a><a name="p8185203164354"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p59021712164354"><a name="p59021712164354"></a><a name="p59021712164354"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row19714506"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p53371190"><a name="p53371190"></a><a name="p53371190"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p28099101"><a name="p28099101"></a><a name="p28099101"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row32688750164938"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p30543097164938"><a name="p30543097164938"></a><a name="p30543097164938"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p58071768164938"><a name="p58071768164938"></a><a name="p58071768164938"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row11809518164943"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17046908164943"><a name="p17046908164943"></a><a name="p17046908164943"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38622347164943"><a name="p38622347164943"></a><a name="p38622347164943"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row38399341164956"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p23338889164956"><a name="p23338889164956"></a><a name="p23338889164956"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p11401882164956"><a name="p11401882164956"></a><a name="p11401882164956"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row51565323"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p16041657"><a name="p16041657"></a><a name="p16041657"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p24305815"><a name="p24305815"></a><a name="p24305815"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

