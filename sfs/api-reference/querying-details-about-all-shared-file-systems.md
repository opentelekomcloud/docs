# Querying Details About All Shared File Systems<a name="sfs_02_0023"></a>

## Function<a name="s87111b996cfb415597f182c407abd8aa"></a>

This API is used to query the details about all shared file systems.

## URI<a name="s34bf80d06f774e58ab8a5e8cb5e62406"></a>

-   GET /v2/\{project\_id\}/shares/detail?all\_tenants=\{all\_tenants\}&project\_id=\{project\_id\}&status=\{status\}&limit=\{limit\}&offset=\{offset\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}&is\_public=\{is\_public\}&metadata=\{metadata\}& export\_location\_id=\{export\_location\_id\}& export\_location\_path=\{export\_location\_path\}& name\~=\{name\}& description\~=\{description\}& with\_count=\{with\_count\}
-   Parameter description

    <a name="t615ef424f0d84673a031c9706de13485"></a>
    <table><thead align="left"><tr id="rdd09b24c551244499ca9198c0d64ca39"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rb823b7ad28654a5e8cef86526598a1aa"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="aaad083a44f6544d1b60e951c6d60dd83"><a name="aaad083a44f6544d1b60e951c6d60dd83"></a><a name="aaad083a44f6544d1b60e951c6d60dd83"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="ad3c5828e7122461788f34d3a9e183309"><a name="ad3c5828e7122461788f34d3a9e183309"></a><a name="ad3c5828e7122461788f34d3a9e183309"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="a44681b00405a4900b71337efb5638781"><a name="a44681b00405a4900b71337efb5638781"></a><a name="a44681b00405a4900b71337efb5638781"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="ac49305b5a17847b4b8291b0ce7fe0617"><a name="ac49305b5a17847b4b8291b0ce7fe0617"></a><a name="ac49305b5a17847b4b8291b0ce7fe0617"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    <tr id="r171525a5ce674cbab69a9a60adb51843"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="ae5666fd5d9594ca3ada9813d824aec12"><a name="ae5666fd5d9594ca3ada9813d824aec12"></a><a name="ae5666fd5d9594ca3ada9813d824aec12"></a>all_tenants</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="a039ea6c45efc4a80a6b00df52910138b"><a name="a039ea6c45efc4a80a6b00df52910138b"></a><a name="a039ea6c45efc4a80a6b00df52910138b"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="aa6c380efa230412ebdb30eeb7873c609"><a name="aa6c380efa230412ebdb30eeb7873c609"></a><a name="aa6c380efa230412ebdb30eeb7873c609"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="a914944ab0eac4b1692f2ba464c778bda"><a name="a914944ab0eac4b1692f2ba464c778bda"></a><a name="a914944ab0eac4b1692f2ba464c778bda"></a>(Administrators only) Specifies whether to list shared file systems of all tenants. To list shared file systems of all tenants, set it to <strong id="b183877260211126"><a name="b183877260211126"></a><a name="b183877260211126"></a>1</strong>. To list shared file systems only of the current tenant, set it to <strong id="b140429609111125"><a name="b140429609111125"></a><a name="b140429609111125"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="re2256914fe8449ff96fb63102a287500"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="a400854e98e9e493baa86ea69d231589d"><a name="a400854e98e9e493baa86ea69d231589d"></a><a name="a400854e98e9e493baa86ea69d231589d"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="a121f417dce594199aee895fcc2bf1ea7"><a name="a121f417dce594199aee895fcc2bf1ea7"></a><a name="a121f417dce594199aee895fcc2bf1ea7"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="af03cee547a2e4a7a80cccae445e5a469"><a name="af03cee547a2e4a7a80cccae445e5a469"></a><a name="af03cee547a2e4a7a80cccae445e5a469"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="a90ffdd8edfe14c3b9832acbb5397a482"><a name="a90ffdd8edfe14c3b9832acbb5397a482"></a><a name="a90ffdd8edfe14c3b9832acbb5397a482"></a>Specifies the UUID of the tenant who creates the shared file system. This parameter is used together with <strong id="a555615ad5d1b4794ac506bd8b9fa2673"><a name="a555615ad5d1b4794ac506bd8b9fa2673"></a><a name="a555615ad5d1b4794ac506bd8b9fa2673"></a>all_tenants</strong>.</p>
    </td>
    </tr>
    <tr id="r0ee6109ca4f24b4bb9d92910dc19a93e"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="a39e5d3a857184f2f86f63b2307e50665"><a name="a39e5d3a857184f2f86f63b2307e50665"></a><a name="a39e5d3a857184f2f86f63b2307e50665"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="a97b1834ea163435198f9a524de2e560f"><a name="a97b1834ea163435198f9a524de2e560f"></a><a name="a97b1834ea163435198f9a524de2e560f"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="a0439b8314708490d8709ebeef90ce8b8"><a name="a0439b8314708490d8709ebeef90ce8b8"></a><a name="a0439b8314708490d8709ebeef90ce8b8"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="afbe00d65e78f4bbaa1852f479b7db917"><a name="afbe00d65e78f4bbaa1852f479b7db917"></a><a name="afbe00d65e78f4bbaa1852f479b7db917"></a>Filters shared file systems by status. Possible values are <strong id="a0cb461c95ffe4dc89e4f4dba74adca62"><a name="a0cb461c95ffe4dc89e4f4dba74adca62"></a><a name="a0cb461c95ffe4dc89e4f4dba74adca62"></a>creating</strong>, <strong id="a3d0bea3c84164fbe9d83d73b9cb96ca8"><a name="a3d0bea3c84164fbe9d83d73b9cb96ca8"></a><a name="a3d0bea3c84164fbe9d83d73b9cb96ca8"></a>error</strong>, <strong id="addc6ec94868247e08f2563e7c9d177b9"><a name="addc6ec94868247e08f2563e7c9d177b9"></a><a name="addc6ec94868247e08f2563e7c9d177b9"></a>available</strong>, <strong id="a1c7321f123c14cdaae38d64cf3c782f1"><a name="a1c7321f123c14cdaae38d64cf3c782f1"></a><a name="a1c7321f123c14cdaae38d64cf3c782f1"></a>deleting</strong>, <strong id="afd39d686059a4befbf06a2a0d4946f8d"><a name="afd39d686059a4befbf06a2a0d4946f8d"></a><a name="afd39d686059a4befbf06a2a0d4946f8d"></a>error_deleting</strong>, <strong id="a9f4f68bd7e914824b953e01dd3345327"><a name="a9f4f68bd7e914824b953e01dd3345327"></a><a name="a9f4f68bd7e914824b953e01dd3345327"></a>manage_starting</strong>, <strong id="a5f08a15292f44a35aa5a8f9ff0fb618d"><a name="a5f08a15292f44a35aa5a8f9ff0fb618d"></a><a name="a5f08a15292f44a35aa5a8f9ff0fb618d"></a>manage_error</strong>, <strong id="a8b4726877a074ccfa741ab2100d1552b"><a name="a8b4726877a074ccfa741ab2100d1552b"></a><a name="a8b4726877a074ccfa741ab2100d1552b"></a>unmanage_starting</strong>, <strong id="a42295fa447be405a87a24bd3300285b0"><a name="a42295fa447be405a87a24bd3300285b0"></a><a name="a42295fa447be405a87a24bd3300285b0"></a>unmanage_error</strong>, <strong id="a903c2f089a5d4a91b8cec757aed0de05"><a name="a903c2f089a5d4a91b8cec757aed0de05"></a><a name="a903c2f089a5d4a91b8cec757aed0de05"></a>unmanaged</strong>, <strong id="a70cf791d5b534a1888c1f749b48ea43e"><a name="a70cf791d5b534a1888c1f749b48ea43e"></a><a name="a70cf791d5b534a1888c1f749b48ea43e"></a>extending</strong>, <strong id="aa62f4b575be749e5b86a355330722dec"><a name="aa62f4b575be749e5b86a355330722dec"></a><a name="aa62f4b575be749e5b86a355330722dec"></a>extending_error</strong>, <strong id="a689fb39e49284c5e9284b702da769259"><a name="a689fb39e49284c5e9284b702da769259"></a><a name="a689fb39e49284c5e9284b702da769259"></a>shrinking</strong>, <strong id="a3e88472b66ad4d6bb2729011cb49137f"><a name="a3e88472b66ad4d6bb2729011cb49137f"></a><a name="a3e88472b66ad4d6bb2729011cb49137f"></a>shrinking_error</strong>, and <strong id="ac218120fa964488fb6e4bbf1bd3f1492"><a name="ac218120fa964488fb6e4bbf1bd3f1492"></a><a name="ac218120fa964488fb6e4bbf1bd3f1492"></a>shrinking_possible_data_loss_error</strong>.</p>
    </td>
    </tr>
    <tr id="r262dd006119a4f04bc3cbeb1fc21ae56"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="ae607935c51cc4593b852bd62ceea2594"><a name="ae607935c51cc4593b852bd62ceea2594"></a><a name="ae607935c51cc4593b852bd62ceea2594"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="ab964f3cc9ca3400486bae9f55724af8f"><a name="ab964f3cc9ca3400486bae9f55724af8f"></a><a name="ab964f3cc9ca3400486bae9f55724af8f"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="a4786f5c3d92041149f430b518dc09c37"><a name="a4786f5c3d92041149f430b518dc09c37"></a><a name="a4786f5c3d92041149f430b518dc09c37"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="a16fe5d6c36c64f2989213b6f417d4b23"><a name="a16fe5d6c36c64f2989213b6f417d4b23"></a><a name="a16fe5d6c36c64f2989213b6f417d4b23"></a>Specifies the maximum number of shared file systems that can be returned.</p>
    </td>
    </tr>
    <tr id="r216bd0b576114a0a8c764aede6da732f"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="a3a867532610642dab7b2e23935044422"><a name="a3a867532610642dab7b2e23935044422"></a><a name="a3a867532610642dab7b2e23935044422"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="af8bee002cfe342858116eb35e6ef6b96"><a name="af8bee002cfe342858116eb35e6ef6b96"></a><a name="af8bee002cfe342858116eb35e6ef6b96"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="a4b143e869b1a44cca71a063000eec9ed"><a name="a4b143e869b1a44cca71a063000eec9ed"></a><a name="a4b143e869b1a44cca71a063000eec9ed"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="a10feefd7d2ad43a0af53cd75681cee22"><a name="a10feefd7d2ad43a0af53cd75681cee22"></a><a name="a10feefd7d2ad43a0af53cd75681cee22"></a>Specifies the offset to define the start point of shared file system listing.</p>
    </td>
    </tr>
    <tr id="r4240b547cf6c41968c8cc250c778d5cf"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="a706e2205cbfe46c388645e7acdfc5c2b"><a name="a706e2205cbfe46c388645e7acdfc5c2b"></a><a name="a706e2205cbfe46c388645e7acdfc5c2b"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="a8540ce6d3b554dfaa138d60a1bfce1ff"><a name="a8540ce6d3b554dfaa138d60a1bfce1ff"></a><a name="a8540ce6d3b554dfaa138d60a1bfce1ff"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="aa4432c058dc64c90a518f5dca672492a"><a name="aa4432c058dc64c90a518f5dca672492a"></a><a name="aa4432c058dc64c90a518f5dca672492a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="adf12fee4a5ea4156982468995e72e062"><a name="adf12fee4a5ea4156982468995e72e062"></a><a name="adf12fee4a5ea4156982468995e72e062"></a>Specifies the keyword for sorting the queried shared file systems. Possible values are <strong id="b5673134515362"><a name="b5673134515362"></a><a name="b5673134515362"></a>id</strong>, <strong id="b46731145193611"><a name="b46731145193611"></a><a name="b46731145193611"></a>status</strong>, <strong id="b18674174514365"><a name="b18674174514365"></a><a name="b18674174514365"></a>size</strong>, <strong id="b467494512369"><a name="b467494512369"></a><a name="b467494512369"></a>host</strong>, <strong id="b1467574553620"><a name="b1467574553620"></a><a name="b1467574553620"></a>share_proto</strong>, <strong id="b56751454360"><a name="b56751454360"></a><a name="b56751454360"></a>availability_zone_id</strong>, <strong id="b1167584518367"><a name="b1167584518367"></a><a name="b1167584518367"></a>user_id</strong>, <strong id="b1967617459361"><a name="b1967617459361"></a><a name="b1967617459361"></a>project_id</strong>, <strong id="b86761245103612"><a name="b86761245103612"></a><a name="b86761245103612"></a>created_at</strong>, <strong id="b567714454364"><a name="b567714454364"></a><a name="b567714454364"></a>updated_at</strong>, <strong id="b1967744553610"><a name="b1967744553610"></a><a name="b1967744553610"></a>display_name</strong>, <strong id="b16678145193616"><a name="b16678145193616"></a><a name="b16678145193616"></a>name</strong>, <strong id="b7678114513614"><a name="b7678114513614"></a><a name="b7678114513614"></a>share_type_id</strong>, <strong id="b46790456368"><a name="b46790456368"></a><a name="b46790456368"></a>share_network_id</strong>, and <strong id="b1967924513369"><a name="b1967924513369"></a><a name="b1967924513369"></a>snapshot_id</strong>.</p>
    </td>
    </tr>
    <tr id="r683b17a7eb5b471b951b7dfbccdc243d"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="ad78c4374d9a94dcfa93ce9fc2a24a717"><a name="ad78c4374d9a94dcfa93ce9fc2a24a717"></a><a name="ad78c4374d9a94dcfa93ce9fc2a24a717"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="a752331297fde411da59e207f8369b829"><a name="a752331297fde411da59e207f8369b829"></a><a name="a752331297fde411da59e207f8369b829"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="a375bfdd05ea74185ab24ef24b18cc832"><a name="a375bfdd05ea74185ab24ef24b18cc832"></a><a name="a375bfdd05ea74185ab24ef24b18cc832"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="ab77f64fe275d4e5fbf78a0f84b742ef5"><a name="ab77f64fe275d4e5fbf78a0f84b742ef5"></a><a name="ab77f64fe275d4e5fbf78a0f84b742ef5"></a>Specifies the direction to sort shared file systems. Possible values are <strong id="ae2272847b34e414e81f383252ce2fdf1"><a name="ae2272847b34e414e81f383252ce2fdf1"></a><a name="ae2272847b34e414e81f383252ce2fdf1"></a>asc</strong> (ascending) and <strong id="a866a3e586e12435bac3d18aae907a8a7"><a name="a866a3e586e12435bac3d18aae907a8a7"></a><a name="a866a3e586e12435bac3d18aae907a8a7"></a>desc</strong> (descending).</p>
    </td>
    </tr>
    <tr id="row61194181213339"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p17850409213344"><a name="p17850409213344"></a><a name="p17850409213344"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="p36597059213344"><a name="p36597059213344"></a><a name="p36597059213344"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p11571830213344"><a name="p11571830213344"></a><a name="p11571830213344"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p64903017213344"><a name="p64903017213344"></a><a name="p64903017213344"></a>When this parameter is set to <strong id="b5475407522328"><a name="b5475407522328"></a><a name="b5475407522328"></a>true</strong>, the current tenant can query all its own shared file systems and other tenants' shared file systems whose <strong id="b842352706111345"><a name="b842352706111345"></a><a name="b842352706111345"></a>is_public</strong> is set to <strong id="b589508122328"><a name="b589508122328"></a><a name="b589508122328"></a>true</strong>. When this parameter is set to <strong id="b773955622328"><a name="b773955622328"></a><a name="b773955622328"></a>false</strong>, the current tenant can query only the shared file systems owned by the tenant.</p>
    </td>
    </tr>
    <tr id="row1688941914411"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p9417141194110"><a name="p9417141194110"></a><a name="p9417141194110"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="p24171441114110"><a name="p24171441114110"></a><a name="p24171441114110"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p15417124118412"><a name="p15417124118412"></a><a name="p15417124118412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p1740010383379"><a name="p1740010383379"></a><a name="p1740010383379"></a>Specifies the metadata information used to query the shared file systems. The value consists of one or more key and value pairs organized as a dictionary of strings. </p>
    </td>
    </tr>
    <tr id="row96611325144120"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p941714120415"><a name="p941714120415"></a><a name="p941714120415"></a>export_location_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="p041754117412"><a name="p041754117412"></a><a name="p041754117412"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p134171541194111"><a name="p134171541194111"></a><a name="p134171541194111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p94173413410"><a name="p94173413410"></a><a name="p94173413410"></a>Specifies the field used for filtering based on the UUID of the mount path. This field is supported by API v2.35 and later versions.</p>
    </td>
    </tr>
    <tr id="row576213309417"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p6417341104120"><a name="p6417341104120"></a><a name="p6417341104120"></a>export_location_path</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="p9417104113410"><a name="p9417104113410"></a><a name="p9417104113410"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p1341734144111"><a name="p1341734144111"></a><a name="p1341734144111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p124171041194115"><a name="p124171041194115"></a><a name="p124171041194115"></a>Specifies the field used for filtering based on the mount path. This field is supported by API v2.35 and later versions.</p>
    </td>
    </tr>
    <tr id="row94763335415"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p16417104124112"><a name="p16417104124112"></a><a name="p16417104124112"></a>name~</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="p04171441134118"><a name="p04171441134118"></a><a name="p04171441134118"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p1541719418417"><a name="p1541719418417"></a><a name="p1541719418417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p1141794119412"><a name="p1141794119412"></a><a name="p1141794119412"></a>Specifies the field used for fuzzy filtering based on the name of a shared file system. This field is supported by API v2.36 and later versions.</p>
    </td>
    </tr>
    <tr id="row4250122814411"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p241754134115"><a name="p241754134115"></a><a name="p241754134115"></a>description~</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="p1441704174111"><a name="p1441704174111"></a><a name="p1441704174111"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p54171412417"><a name="p54171412417"></a><a name="p54171412417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p1941719417414"><a name="p1941719417414"></a><a name="p1941719417414"></a>Specifies the field used for fuzzy filtering based on the description of a shared file system. This field is supported by API v2.36 and later versions.</p>
    </td>
    </tr>
    <tr id="row159151022174120"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.1 "><p id="p2041714116417"><a name="p2041714116417"></a><a name="p2041714116417"></a>with_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.2 "><p id="p10417241174110"><a name="p10417241174110"></a><a name="p10417241174110"></a>No (query parameter)</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p164178415412"><a name="p164178415412"></a><a name="p164178415412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.5.1.4 "><p id="p441719412416"><a name="p441719412416"></a><a name="p441719412416"></a>Specifies whether the number of queried shared file systems is returned. This field is supported by API v2.42 and later versions.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s7ca7d63b6f534ad492fa92ae779d0c24"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="s552e52b0bcb64dc78d5f1a628b076e23"></a>

-   Parameter description

    <a name="t87fd1aa9dd04472facc8679378961670"></a>
    <table><thead align="left"><tr id="r454ffc4daf2f4ef984e6e1813e9f07e8"><th class="cellrowborder" valign="top" width="22.86%" id="mcps1.1.4.1.1"><p id="p36281553105316"><a name="p36281553105316"></a><a name="p36281553105316"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.41%" id="mcps1.1.4.1.2"><p id="p176446533531"><a name="p176446533531"></a><a name="p176446533531"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.73%" id="mcps1.1.4.1.3"><p id="p126441153165312"><a name="p126441153165312"></a><a name="p126441153165312"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rd59c444142dc4b33852485b096741e97"><td class="cellrowborder" valign="top" width="22.86%" headers="mcps1.1.4.1.1 "><p id="af69f7adb2e1f4125b1caeb5209e9a599"><a name="af69f7adb2e1f4125b1caeb5209e9a599"></a><a name="af69f7adb2e1f4125b1caeb5209e9a599"></a>shares</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.41%" headers="mcps1.1.4.1.2 "><p id="af6c3a2d4632e415bb356e574253886c9"><a name="af6c3a2d4632e415bb356e574253886c9"></a><a name="af6c3a2d4632e415bb356e574253886c9"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.73%" headers="mcps1.1.4.1.3 "><p id="a37a170ecda034a09bb936c456ca84cf2"><a name="a37a170ecda034a09bb936c456ca84cf2"></a><a name="a37a170ecda034a09bb936c456ca84cf2"></a>Specifies the list of share objects.</p>
    </td>
    </tr>
    <tr id="row760532754418"><td class="cellrowborder" valign="top" width="22.86%" headers="mcps1.1.4.1.1 "><p id="p176191628154417"><a name="p176191628154417"></a><a name="p176191628154417"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.41%" headers="mcps1.1.4.1.2 "><p id="p1063532864411"><a name="p1063532864411"></a><a name="p1063532864411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.73%" headers="mcps1.1.4.1.3 "><p id="p2063572811447"><a name="p2063572811447"></a><a name="p2063572811447"></a>Specifies the number of returned shared file systems.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **share**  field

    <a name="table797579194010"></a>
    <table><thead align="left"><tr id="row12975296407"><th class="cellrowborder" valign="top" width="18.84%" id="mcps1.1.4.1.1"><p id="p29761897407"><a name="p29761897407"></a><a name="p29761897407"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.97%" id="mcps1.1.4.1.2"><p id="p12976189174010"><a name="p12976189174010"></a><a name="p12976189174010"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.19%" id="mcps1.1.4.1.3"><p id="p797629124017"><a name="p797629124017"></a><a name="p797629124017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1097609174012"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p28090732115456"><a name="en-us_topic_0064390794_p28090732115456"></a><a name="en-us_topic_0064390794_p28090732115456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60756818115456"><a name="en-us_topic_0064390794_p60756818115456"></a><a name="en-us_topic_0064390794_p60756818115456"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p53809467171857"><a name="en-us_topic_0064390794_p53809467171857"></a><a name="en-us_topic_0064390794_p53809467171857"></a>Specifies the links of shared file systems.</p>
    </td>
    </tr>
    <tr id="row29765984012"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p20630446115456"><a name="en-us_topic_0064390794_p20630446115456"></a><a name="en-us_topic_0064390794_p20630446115456"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60453459115456"><a name="en-us_topic_0064390794_p60453459115456"></a><a name="en-us_topic_0064390794_p60453459115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p35525415171857"><a name="en-us_topic_0064390794_p35525415171857"></a><a name="en-us_topic_0064390794_p35525415171857"></a>Specifies the availability zone.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5492535895012"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1976898095012"><a name="en-us_topic_0064390794_p1976898095012"></a><a name="en-us_topic_0064390794_p1976898095012"></a>share_server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4995572295012"><a name="en-us_topic_0064390794_p4995572295012"></a><a name="en-us_topic_0064390794_p4995572295012"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1988170695012"><a name="en-us_topic_0064390794_p1988170695012"></a><a name="en-us_topic_0064390794_p1988170695012"></a>Specifies the UUID for managing share services.</p>
    </td>
    </tr>
    <tr id="row169763954018"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p27750209115456"><a name="en-us_topic_0064390794_p27750209115456"></a><a name="en-us_topic_0064390794_p27750209115456"></a>share_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p33174447115456"><a name="en-us_topic_0064390794_p33174447115456"></a><a name="en-us_topic_0064390794_p33174447115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59674002171857"><a name="en-us_topic_0064390794_p59674002171857"></a><a name="en-us_topic_0064390794_p59674002171857"></a>Specifies the UUID of the share network. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row39279891115440"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p39186779115456"><a name="en-us_topic_0064390794_p39186779115456"></a><a name="en-us_topic_0064390794_p39186779115456"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p20012545115456"><a name="en-us_topic_0064390794_p20012545115456"></a><a name="en-us_topic_0064390794_p20012545115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p17092907171857"><a name="en-us_topic_0064390794_p17092907171857"></a><a name="en-us_topic_0064390794_p17092907171857"></a>Specifies the UUID of the source snapshot that is used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5321904710035"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1577556910035"><a name="en-us_topic_0064390794_p1577556910035"></a><a name="en-us_topic_0064390794_p1577556910035"></a>snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2164239410035"><a name="en-us_topic_0064390794_p2164239410035"></a><a name="en-us_topic_0064390794_p2164239410035"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p199771793401"><a name="p199771793401"></a><a name="p199771793401"></a>Specifies whether snapshots are supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.2 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66254026115429"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66240344115456"><a name="en-us_topic_0064390794_p66240344115456"></a><a name="en-us_topic_0064390794_p66240344115456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p63867663115456"><a name="en-us_topic_0064390794_p63867663115456"></a><a name="en-us_topic_0064390794_p63867663115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p45589478171857"><a name="en-us_topic_0064390794_p45589478171857"></a><a name="en-us_topic_0064390794_p45589478171857"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row25775244115437"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p57485250115456"><a name="en-us_topic_0064390794_p57485250115456"></a><a name="en-us_topic_0064390794_p57485250115456"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p25793701115456"><a name="en-us_topic_0064390794_p25793701115456"></a><a name="en-us_topic_0064390794_p25793701115456"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p42544068172855"><a name="en-us_topic_0064390794_p42544068172855"></a><a name="en-us_topic_0064390794_p42544068172855"></a>Specifies the size (GB) of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2811743793851"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p597717920405"><a name="p597717920405"></a><a name="p597717920405"></a>share_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p14977149134016"><a name="p14977149134016"></a><a name="p14977149134016"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p1597769184019"><a name="p1597769184019"></a><a name="p1597769184019"></a>Specifies the UUID of the consistency group. This parameter is reserved, because consistency groups are not supported currently. This field is supported by API versions from v2.31 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row14146850115432"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p43647722115456"><a name="en-us_topic_0064390794_p43647722115456"></a><a name="en-us_topic_0064390794_p43647722115456"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p45804593115456"><a name="en-us_topic_0064390794_p45804593115456"></a><a name="en-us_topic_0064390794_p45804593115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p36017679171857"><a name="en-us_topic_0064390794_p36017679171857"></a><a name="en-us_topic_0064390794_p36017679171857"></a>Specifies the UUID of the project to which the shared file system belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row27677209115427"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p30561506115456"><a name="en-us_topic_0064390794_p30561506115456"></a><a name="en-us_topic_0064390794_p30561506115456"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p59562882115456"><a name="en-us_topic_0064390794_p59562882115456"></a><a name="en-us_topic_0064390794_p59562882115456"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390792_p42083247173855"><a name="en-us_topic_0064390792_p42083247173855"></a><a name="en-us_topic_0064390792_p42083247173855"></a>Sets one or more metadata key and value pairs as a dictionary of strings. <strong id="b689593910425"><a name="b689593910425"></a><a name="b689593910425"></a>share_used</strong> is the key, and the corresponding value is the used capacity of the shared file system in the unit of Bytes. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row21024096115415"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p23577146115456"><a name="en-us_topic_0064390794_p23577146115456"></a><a name="en-us_topic_0064390794_p23577146115456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p30700686115456"><a name="en-us_topic_0064390794_p30700686115456"></a><a name="en-us_topic_0064390794_p30700686115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p9195044171857"><a name="en-us_topic_0064390794_p9195044171857"></a><a name="en-us_topic_0064390794_p9195044171857"></a>Specifies the status of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row665580195924"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p39782912408"><a name="p39782912408"></a><a name="p39782912408"></a>task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p5905231595924"><a name="en-us_topic_0064390794_p5905231595924"></a><a name="en-us_topic_0064390794_p5905231595924"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1850821095924"><a name="en-us_topic_0064390794_p1850821095924"></a><a name="en-us_topic_0064390794_p1850821095924"></a>Specifies the data migration status. This parameter is reserved, because data migration is not supported currently. This field is supported by API v2.5 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row939599610316"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p2287823910316"><a name="en-us_topic_0064390794_p2287823910316"></a><a name="en-us_topic_0064390794_p2287823910316"></a>has_replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4870772510316"><a name="en-us_topic_0064390794_p4870772510316"></a><a name="en-us_topic_0064390794_p4870772510316"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5301165710316"><a name="en-us_topic_0064390794_p5301165710316"></a><a name="en-us_topic_0064390794_p5301165710316"></a>Specifies whether replicas exist. This parameter is reserved, because replication is not supported currently. This field is supported by API versions from v2.11 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row48841735810"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1388510311817"><a name="en-us_topic_0064390794_p1388510311817"></a><a name="en-us_topic_0064390794_p1388510311817"></a>replication_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p20978129114014"><a name="p20978129114014"></a><a name="p20978129114014"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p129782924020"><a name="p129782924020"></a><a name="p129782924020"></a>Specifies the replication type. This parameter is reserved, because replication is not supported currently. This field is supported by API versions from v2.11 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row38372338115421"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p61202789115456"><a name="en-us_topic_0064390794_p61202789115456"></a><a name="en-us_topic_0064390794_p61202789115456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p58478870115456"><a name="en-us_topic_0064390794_p58478870115456"></a><a name="en-us_topic_0064390794_p58478870115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59409689171857"><a name="en-us_topic_0064390794_p59409689171857"></a><a name="en-us_topic_0064390794_p59409689171857"></a>Describes the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row35274029115424"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p58169755115456"><a name="en-us_topic_0064390794_p58169755115456"></a><a name="en-us_topic_0064390794_p58169755115456"></a>host</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p14129699115456"><a name="en-us_topic_0064390794_p14129699115456"></a><a name="en-us_topic_0064390794_p14129699115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p24446366171857"><a name="en-us_topic_0064390794_p24446366171857"></a><a name="en-us_topic_0064390794_p24446366171857"></a>Specifies the name of the host. This field is visible only to the administrator.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row10855127115417"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66003741115456"><a name="en-us_topic_0064390794_p66003741115456"></a><a name="en-us_topic_0064390794_p66003741115456"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p44702790115456"><a name="en-us_topic_0064390794_p44702790115456"></a><a name="en-us_topic_0064390794_p44702790115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p37552527171857"><a name="en-us_topic_0064390794_p37552527171857"></a><a name="en-us_topic_0064390794_p37552527171857"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6259894411544"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66214260115456"><a name="en-us_topic_0064390794_p66214260115456"></a><a name="en-us_topic_0064390794_p66214260115456"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p61754840115456"><a name="en-us_topic_0064390794_p61754840115456"></a><a name="en-us_topic_0064390794_p61754840115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p62484878171857"><a name="en-us_topic_0064390794_p62484878171857"></a><a name="en-us_topic_0064390794_p62484878171857"></a>Specifies the date and time stamp when the shared file system was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2256685795641"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1597610695641"><a name="en-us_topic_0064390794_p1597610695641"></a><a name="en-us_topic_0064390794_p1597610695641"></a>access_rules_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6230051595641"><a name="en-us_topic_0064390794_p6230051595641"></a><a name="en-us_topic_0064390794_p6230051595641"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1317697095641"><a name="en-us_topic_0064390794_p1317697095641"></a><a name="en-us_topic_0064390794_p1317697095641"></a>Specifies the configuration status of the access rule. Possible values are <strong id="b99731727163914"><a name="b99731727163914"></a><a name="b99731727163914"></a>active</strong> (effective), <strong id="b199745279398"><a name="b199745279398"></a><a name="b199745279398"></a>error</strong> (configuration failed), and <strong id="b99741927153913"><a name="b99741927153913"></a><a name="b99741927153913"></a>syncing</strong> (configuration in progress). This field is supported by API v2.10 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66328432115411"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p11825073115456"><a name="en-us_topic_0064390794_p11825073115456"></a><a name="en-us_topic_0064390794_p11825073115456"></a>share_proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p18306875115456"><a name="en-us_topic_0064390794_p18306875115456"></a><a name="en-us_topic_0064390794_p18306875115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p51666373171857"><a name="en-us_topic_0064390794_p51666373171857"></a><a name="en-us_topic_0064390794_p51666373171857"></a>Specifies the protocol for sharing file systems.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row4389128911547"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p49791910406"><a name="p49791910406"></a><a name="p49791910406"></a>share_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6682275212118"><a name="en-us_topic_0064390794_p6682275212118"></a><a name="en-us_topic_0064390794_p6682275212118"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p55872650172937"><a name="en-us_topic_0064390794_p55872650172937"></a><a name="en-us_topic_0064390794_p55872650172937"></a>Specifies the storage service type assigned for the shared file system, such as high-performance storage (composed of SSDs) and large-capacity storage (composed of SATA disks). This field is supported by API v2.6 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1997612012118"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p89791892404"><a name="p89791892404"></a><a name="p89791892404"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2135204095244"><a name="en-us_topic_0064390794_p2135204095244"></a><a name="en-us_topic_0064390794_p2135204095244"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5179364095244"><a name="en-us_topic_0064390794_p5179364095244"></a><a name="en-us_topic_0064390794_p5179364095244"></a>Specifies the UUID of the share type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6380688295244"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p945114017196"><a name="p945114017196"></a><a name="p945114017196"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p54519014190"><a name="p54519014190"></a><a name="p54519014190"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p114511106197"><a name="p114511106197"></a><a name="p114511106197"></a>Specifies the volume type. The definition of this parameter is the same as that of <strong id="b952125017392"><a name="b952125017392"></a><a name="b952125017392"></a>share_type</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1256499495932"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p1097929134019"><a name="p1097929134019"></a><a name="p1097929134019"></a>export_locations</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p1697929134011"><a name="p1697929134011"></a><a name="p1697929134011"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p199791797409"><a name="p199791797409"></a><a name="p199791797409"></a>Lists the mount locations. Currently, only a single mount location is supported. This parameter exists only when <strong id="b12615196587"><a name="b12615196587"></a><a name="b12615196587"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b11721914582"><a name="b11721914582"></a><a name="b11721914582"></a>2.9</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1105050495936"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p1897917916405"><a name="p1897917916405"></a><a name="p1897917916405"></a>export_location</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p79804964014"><a name="p79804964014"></a><a name="p79804964014"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p3980199174018"><a name="p3980199174018"></a><a name="p3980199174018"></a>Specifies the mount location. This parameter exists only when <strong id="b12244021125810"><a name="b12244021125810"></a><a name="b12244021125810"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b182448217589"><a name="b182448217589"></a><a name="b182448217589"></a>2.9</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row760346112115"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1190063912115"><a name="en-us_topic_0064390794_p1190063912115"></a><a name="en-us_topic_0064390794_p1190063912115"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2442773012115"><a name="en-us_topic_0064390794_p2442773012115"></a><a name="en-us_topic_0064390794_p2442773012115"></a>bool</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p19950543172949"><a name="en-us_topic_0064390794_p19950543172949"></a><a name="en-us_topic_0064390794_p19950543172949"></a>Specifies the visibility level of the shared file system. If it is set to <strong id="b950452313404"><a name="b950452313404"></a><a name="b950452313404"></a>true</strong>, the file system can be seen publicly. If it is set to <strong id="b55041423114019"><a name="b55041423114019"></a><a name="b55041423114019"></a>false</strong>, the file system can be seen privately. The default value is <strong id="b850562334017"><a name="b850562334017"></a><a name="b850562334017"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row138591369913"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p998099144018"><a name="p998099144018"></a><a name="p998099144018"></a>source_share_group_snapshot_member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p1486018614919"><a name="en-us_topic_0064390794_p1486018614919"></a><a name="en-us_topic_0064390794_p1486018614919"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p1098113974020"><a name="p1098113974020"></a><a name="p1098113974020"></a>Specifies the UUID of the snapshot's source. This parameter is reserved, because consistency snapshots are not supported currently. This field is supported by API v2.31 and later versions.</p>
    </td>
    </tr>
    <tr id="row10981129124012"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p109814911401"><a name="p109814911401"></a><a name="p109814911401"></a>revert_to_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p1198112915409"><a name="p1198112915409"></a><a name="p1198112915409"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p17981149104019"><a name="p17981149104019"></a><a name="p17981149104019"></a>Specifies whether rollback from snapshot is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.27 and later versions.</p>
    </td>
    </tr>
    <tr id="row198189104011"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p179811995401"><a name="p179811995401"></a><a name="p179811995401"></a>create_share_from_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p19981295402"><a name="p19981295402"></a><a name="p19981295402"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p199811395404"><a name="p199811395404"></a><a name="p199811395404"></a>Specifies whether creation of shared file systems from snapshot is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.24 and later versions.</p>
    </td>
    </tr>
    <tr id="row59811097405"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p16982692406"><a name="p16982692406"></a><a name="p16982692406"></a>mount_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p89821799408"><a name="p89821799408"></a><a name="p89821799408"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p8982159184017"><a name="p8982159184017"></a><a name="p8982159184017"></a>Specifies whether snapshot mount is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.32 and later versions.</p>
    </td>
    </tr>
    <tr id="row179829974016"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p14982199154017"><a name="p14982199154017"></a><a name="p14982199154017"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.1.4.1.2 "><p id="p698317964015"><a name="p698317964015"></a><a name="p698317964015"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.19%" headers="mcps1.1.4.1.3 "><p id="p1998312944010"><a name="p1998312944010"></a><a name="p1998312944010"></a>Specifies the user ID. This field is supported by API v2.16 and later versions.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "count": 1,
        "shares": [
            {
                "links": [
                    {
                        "href": "https://192.168.170.97:8796/v2/61b01a94b84448cfac2424e46553d7e7/shares/54d0bac6-45c8-471c-bf0d-16ffd81ef88a",
                        "rel": "self"
                    },
                    {
                        "href": "https://192.168.170.97:8796/61b01a94b84448cfac2424e46553d7e7/shares/54d0bac6-45c8-471c-bf0d-16ffd81ef88a",
                        "rel": "bookmark"
                    }
                ],
                "export_location": "sfs.dong.com:/share-e1c2d35e",
                "availability_zone": "az1.dc1",
                "share_network_id": null,
                "snapshot_id": null,
                "id": "54d0bac6-45c8-471c-bf0d-16ffd81ef88a",
                "size": 1,
                "share_type": "default",
                "share_group_id": null,
                "project_id": "da0f615c35eb4d72812d1547a77b5394",
                "metadata": { 
                              
                             "share_used": "1048576000000"
                 },
                "status": "available",
                "description": "test description",
                "export_locations": ["sfs.dong.com:/share-e1c2d35e"],
                "host": "DJ01@9656beb1-7ce2-4c46-9911-ecd51ab632bf#9656beb1-7ce2-4c46-9911-ecd51ab632bf",
                "is_public": false,
                "name": "cl01",
                "created_at": "2017-07-07T03:15:06.858662",
                "share_proto": "NFS",
                "volume_type": "default"
            }
    ]
    }
    ```


## Status Codes<a name="se0c4d410452c4426a20466f6442b0893"></a>

-   Normal

    200

-   Abnormal

    <a name="t15a6873847cf459ea75dfe46163aea23"></a>
    <table><thead align="left"><tr id="rec58d1f4cbcf4483a5c1957f1b542c24"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="adf60d9b578e94c76b4a9d76b55e1c726"><a name="adf60d9b578e94c76b4a9d76b55e1c726"></a><a name="adf60d9b578e94c76b4a9d76b55e1c726"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="a8f550f53524f4dc3a7b4242f96152d12"><a name="a8f550f53524f4dc3a7b4242f96152d12"></a><a name="a8f550f53524f4dc3a7b4242f96152d12"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r4da03cbaa5664d1da6893ce49b1779bd"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="aa44aa2a6e107432192d6759ce423acce"><a name="aa44aa2a6e107432192d6759ce423acce"></a><a name="aa44aa2a6e107432192d6759ce423acce"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390792_p34248173855"><a name="en-us_topic_0064390792_p34248173855"></a><a name="en-us_topic_0064390792_p34248173855"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="r7f6ac62cfb2f491a8b4a2e2f11cf9c20"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a8fc1510546cd4ed1959c09a88d5bac60"><a name="a8fc1510546cd4ed1959c09a88d5bac60"></a><a name="a8fc1510546cd4ed1959c09a88d5bac60"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ad26ed004d86b40e7966a73ccd8d43ce4"><a name="ad26ed004d86b40e7966a73ccd8d43ce4"></a><a name="ad26ed004d86b40e7966a73ccd8d43ce4"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="r8ae4e8681f5242d9b397c804064ca33f"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a98a3ea58687441aa8c9c1f0d02ca077c"><a name="a98a3ea58687441aa8c9c1f0d02ca077c"></a><a name="a98a3ea58687441aa8c9c1f0d02ca077c"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a625a0c6f375643ba993ba54ca87aae69"><a name="a625a0c6f375643ba993ba54ca87aae69"></a><a name="a625a0c6f375643ba993ba54ca87aae69"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="r5d360145578f4355987f32939a6455fc"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a07e571f2662242a2906516b439b71a67"><a name="a07e571f2662242a2906516b439b71a67"></a><a name="a07e571f2662242a2906516b439b71a67"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ad9534a9374764712a97a5ca62d1e8c26"><a name="ad9534a9374764712a97a5ca62d1e8c26"></a><a name="ad9534a9374764712a97a5ca62d1e8c26"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="r7994b313fd1f47ccb5bc64178d3883da"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a70db46d18ac548c3990476c1fd80c137"><a name="a70db46d18ac548c3990476c1fd80c137"></a><a name="a70db46d18ac548c3990476c1fd80c137"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="af1d47efa0e714738972dcbab6cbbd7d4"><a name="af1d47efa0e714738972dcbab6cbbd7d4"></a><a name="af1d47efa0e714738972dcbab6cbbd7d4"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="r4a02fad128674e5e871460c2d2b80a7c"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a5f489c51d75f46c39c050befc05f3755"><a name="a5f489c51d75f46c39c050befc05f3755"></a><a name="a5f489c51d75f46c39c050befc05f3755"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a1a85e383d41743d58351b7b802bb6194"><a name="a1a85e383d41743d58351b7b802bb6194"></a><a name="a1a85e383d41743d58351b7b802bb6194"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="rd8b7ebe27cff40b086904b884222ea69"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ae3e0f932bb96402bb1a99f7b6aa4ba91"><a name="ae3e0f932bb96402bb1a99f7b6aa4ba91"></a><a name="ae3e0f932bb96402bb1a99f7b6aa4ba91"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a9041f0278f7a4ea0974a57fee400802e"><a name="a9041f0278f7a4ea0974a57fee400802e"></a><a name="a9041f0278f7a4ea0974a57fee400802e"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="r8a85fa22e71a453094af9f3dc801c7e0"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ae6ad0580e0184d99b493480954912935"><a name="ae6ad0580e0184d99b493480954912935"></a><a name="ae6ad0580e0184d99b493480954912935"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ab94dc53d0e9a4c239253780c8a7d74e5"><a name="ab94dc53d0e9a4c239253780c8a7d74e5"></a><a name="ab94dc53d0e9a4c239253780c8a7d74e5"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="r86ca60e4bef94a4b8891f7da508998f0"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a6a425e7691e94e82b497a50eaf361085"><a name="a6a425e7691e94e82b497a50eaf361085"></a><a name="a6a425e7691e94e82b497a50eaf361085"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a692195918d884a03a4dce6cdaa48eb3c"><a name="a692195918d884a03a4dce6cdaa48eb3c"></a><a name="a692195918d884a03a4dce6cdaa48eb3c"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="r4453397d1224431790a974a39e12fc18"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a70d9b493630948b0abab3eaec75f2e9e"><a name="a70d9b493630948b0abab3eaec75f2e9e"></a><a name="a70d9b493630948b0abab3eaec75f2e9e"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac9c0eae6bb58494e9ded7e44000f9e41"><a name="ac9c0eae6bb58494e9ded7e44000f9e41"></a><a name="ac9c0eae6bb58494e9ded7e44000f9e41"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="r60d72d4924aa44a788538ab3aef3f286"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ab9636a0d398b448cba546272eb10f1df"><a name="ab9636a0d398b448cba546272eb10f1df"></a><a name="ab9636a0d398b448cba546272eb10f1df"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a283facd9ae15465096f58dc984e0a3b9"><a name="a283facd9ae15465096f58dc984e0a3b9"></a><a name="a283facd9ae15465096f58dc984e0a3b9"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="r6ec8d991d19d4923af8c04ae54da81cb"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ab510a584c3df413c9931a2ec57b0ed7d"><a name="ab510a584c3df413c9931a2ec57b0ed7d"></a><a name="ab510a584c3df413c9931a2ec57b0ed7d"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="aa607f587f9034835a627f7db800f440c"><a name="aa607f587f9034835a627f7db800f440c"></a><a name="aa607f587f9034835a627f7db800f440c"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="r81b4cf0c04fc437c859c8d67037cfea6"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a8ed6c18ac0cd41a1a3e060e52b26bfc3"><a name="a8ed6c18ac0cd41a1a3e060e52b26bfc3"></a><a name="a8ed6c18ac0cd41a1a3e060e52b26bfc3"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ad9e54ab61bbb4136ac2213db6a9b1aa4"><a name="ad9e54ab61bbb4136ac2213db6a9b1aa4"></a><a name="ad9e54ab61bbb4136ac2213db6a9b1aa4"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="rb4b32bb1ae0d4ccaaf400600b9a059aa"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="ac61ab8b8880740e8a8645cd77f4853f6"><a name="ac61ab8b8880740e8a8645cd77f4853f6"></a><a name="ac61ab8b8880740e8a8645cd77f4853f6"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a4437817812da4fc39cf0018827eb7b79"><a name="a4437817812da4fc39cf0018827eb7b79"></a><a name="a4437817812da4fc39cf0018827eb7b79"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


