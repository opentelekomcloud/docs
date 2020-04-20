# Adding a Tag<a name="rds_01_0006"></a>

## Function<a name="sdb96d603244345c391f4b5ebd12a22fa"></a>

This API is used to add a tag to a DB instance.

## URI<a name="sf61442e26fcc4259a131c02dee020a10"></a>

-   URI format

    PATH: /v1/\{project\_id\}/rds/\{instanceId\}/tags

    Method: POST

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0091754391_table58427690"></a>
    <table><thead align="left"><tr id="en-us_topic_0091754391_row1482002"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0091754391_p52933326"><a name="en-us_topic_0091754391_p52933326"></a><a name="en-us_topic_0091754391_p52933326"></a><strong id="en-us_topic_0091754391_b84235270691445"><a name="en-us_topic_0091754391_b84235270691445"></a><a name="en-us_topic_0091754391_b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="en-us_topic_0091754391_p59740974"><a name="en-us_topic_0091754391_p59740974"></a><a name="en-us_topic_0091754391_p59740974"></a><strong id="en-us_topic_0091754391_b842352706102346"><a name="en-us_topic_0091754391_b842352706102346"></a><a name="en-us_topic_0091754391_b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0091754391_p7180698"><a name="en-us_topic_0091754391_p7180698"></a><a name="en-us_topic_0091754391_p7180698"></a><strong id="en-us_topic_0091754391_b842352706163417"><a name="en-us_topic_0091754391_b842352706163417"></a><a name="en-us_topic_0091754391_b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0091754391_row44765691"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091754391_p2142393"><a name="en-us_topic_0091754391_p2142393"></a><a name="en-us_topic_0091754391_p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091754391_p39316155"><a name="en-us_topic_0091754391_p39316155"></a><a name="en-us_topic_0091754391_p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091754391_p30492010"><a name="en-us_topic_0091754391_p30492010"></a><a name="en-us_topic_0091754391_p30492010"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091754391_row5992637"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091754391_p15641626"><a name="en-us_topic_0091754391_p15641626"></a><a name="en-us_topic_0091754391_p15641626"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091754391_p59012183"><a name="en-us_topic_0091754391_p59012183"></a><a name="en-us_topic_0091754391_p59012183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions
    -   A maximum of 20 tags can be added for each DB instance. The tag key must be unique.
    -   If the key in the request body is the same as an existing key in the specified DB instance, the value of the key is overwritten.
    -   Standby DB instances do not support tag adding.


## Request<a name="s09d438844e694f72b12fc288c723116a"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="te7f01ccb355a4f29a1a97bea177cc736"></a>
    <table><thead align="left"><tr id="r1d2e972ffada4dd7be764ebfa5663add"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="a40b2b823012a4d6c8da07baa32d6a263"><a name="a40b2b823012a4d6c8da07baa32d6a263"></a><a name="a40b2b823012a4d6c8da07baa32d6a263"></a><strong id="b1658597578"><a name="b1658597578"></a><a name="b1658597578"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="a61de8d6c3e1641b5ad4b6acab98c5481"><a name="a61de8d6c3e1641b5ad4b6acab98c5481"></a><a name="a61de8d6c3e1641b5ad4b6acab98c5481"></a><strong id="b268212627"><a name="b268212627"></a><a name="b268212627"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="a61b7a35f766c43abb8fb7264a42b0364"><a name="a61b7a35f766c43abb8fb7264a42b0364"></a><a name="a61b7a35f766c43abb8fb7264a42b0364"></a><strong id="en-us_topic_0091754391_b842352706164541"><a name="en-us_topic_0091754391_b842352706164541"></a><a name="en-us_topic_0091754391_b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="ae587cc1de1d84c97a12c5031d2b53a53"><a name="ae587cc1de1d84c97a12c5031d2b53a53"></a><a name="ae587cc1de1d84c97a12c5031d2b53a53"></a><strong id="b141457549"><a name="b141457549"></a><a name="b141457549"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ree816e332a0a4172a254e355bbaa7734"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="ad71579417ad24b1aa1621e885ff73f38"><a name="ad71579417ad24b1aa1621e885ff73f38"></a><a name="ad71579417ad24b1aa1621e885ff73f38"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="a62aeed04cd364a9481c3269d54dda6f5"><a name="a62aeed04cd364a9481c3269d54dda6f5"></a><a name="a62aeed04cd364a9481c3269d54dda6f5"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="af79610cdc59c4d20a1ea874e087c9662"><a name="af79610cdc59c4d20a1ea874e087c9662"></a><a name="af79610cdc59c4d20a1ea874e087c9662"></a>Dictionary data structure. For details, see <a href="#teb132a9896b14904b643d3159d0c06eb">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="a164aa9b6ed6f4d20a34b354446c9be00"><a name="a164aa9b6ed6f4d20a34b354446c9be00"></a><a name="a164aa9b6ed6f4d20a34b354446c9be00"></a>Specifies the tag information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  tag field data structure description

    <a name="teb132a9896b14904b643d3159d0c06eb"></a>
    <table><thead align="left"><tr id="r205f2a4045b24af7bfbe9a7542aa07aa"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="ac93bd30b77444614884618eb51b6d66a"><a name="ac93bd30b77444614884618eb51b6d66a"></a><a name="ac93bd30b77444614884618eb51b6d66a"></a><strong id="b360994920"><a name="b360994920"></a><a name="b360994920"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="aca36c6e0753c4472a37da4fd1a14d498"><a name="aca36c6e0753c4472a37da4fd1a14d498"></a><a name="aca36c6e0753c4472a37da4fd1a14d498"></a><strong id="b1003120395"><a name="b1003120395"></a><a name="b1003120395"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="ad77f9074312f4e0eb280a9f2053986ac"><a name="ad77f9074312f4e0eb280a9f2053986ac"></a><a name="ad77f9074312f4e0eb280a9f2053986ac"></a><strong id="b1336592741"><a name="b1336592741"></a><a name="b1336592741"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="aeabe62f6ada64b35a7cf47c0100b800c"><a name="aeabe62f6ada64b35a7cf47c0100b800c"></a><a name="aeabe62f6ada64b35a7cf47c0100b800c"></a><strong id="b1755746050"><a name="b1755746050"></a><a name="b1755746050"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r46e744ec5f4f42e1b8fbb38ed61fe49b"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="a7ccf99b01cbe4d03ae33e405286a25ea"><a name="a7ccf99b01cbe4d03ae33e405286a25ea"></a><a name="a7ccf99b01cbe4d03ae33e405286a25ea"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="ab11d8114c8dc45a2b22a63be35799395"><a name="ab11d8114c8dc45a2b22a63be35799395"></a><a name="ab11d8114c8dc45a2b22a63be35799395"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="ac7a918d5d8e3418b8836f6d7ccde7146"><a name="ac7a918d5d8e3418b8836f6d7ccde7146"></a><a name="ac7a918d5d8e3418b8836f6d7ccde7146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="a88527f11e625412d85ede0d88559c1d9"><a name="a88527f11e625412d85ede0d88559c1d9"></a><a name="a88527f11e625412d85ede0d88559c1d9"></a>Specifies the tag key.</p>
    <p id="a371449e7ea214290915083393b3224f4"><a name="a371449e7ea214290915083393b3224f4"></a><a name="a371449e7ea214290915083393b3224f4"></a>Its value cannot be empty and must be 1 to 36 Unicode characters in length. It cannot contain nonprintable ASCII characters (0–31) and the following special characters: *&lt;&gt;\=</p>
    </td>
    </tr>
    <tr id="r4a2647fcd1cd4ffd962c1259e00434a6"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="afc9ec9d0e20a45beb6b5ae95ecba77d2"><a name="afc9ec9d0e20a45beb6b5ae95ecba77d2"></a><a name="afc9ec9d0e20a45beb6b5ae95ecba77d2"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="a10261134ed3a4648be213560ea5aefd9"><a name="a10261134ed3a4648be213560ea5aefd9"></a><a name="a10261134ed3a4648be213560ea5aefd9"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="a9303a484901b4e15a84aed1ed75013a2"><a name="a9303a484901b4e15a84aed1ed75013a2"></a><a name="a9303a484901b4e15a84aed1ed75013a2"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="adfe36c1c74934a85a6fb050c28a15027"><a name="adfe36c1c74934a85a6fb050c28a15027"></a><a name="adfe36c1c74934a85a6fb050c28a15027"></a>Specifies the tag value.</p>
    <p id="a3ae0e5212c2a406bb60d9c0add4280d2"><a name="a3ae0e5212c2a406bb60d9c0add4280d2"></a><a name="a3ae0e5212c2a406bb60d9c0add4280d2"></a>Its value can be empty or 1 to 43 Unicode characters in length. It cannot contain nonprintable ASCII characters (0–31) and the following special characters: *&lt;&gt;\=</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    {
         "tag":
            {
                "key": "ENV", 
                "value":"DEV"
            }    
    }
    ```


## Normal Response<a name="s6499f6b27f174646b4d1b864e8588c72"></a>

```
{}
```

## Abnormal Response<a name="s11e128e8e77a46e6aea356c44f891de4"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

