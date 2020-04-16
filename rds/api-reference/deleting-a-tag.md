# Deleting a Tag<a name="rds_01_0008"></a>

## Function<a name="sc24930a14ced466ea18b344b5e1c2ec5"></a>

This API is used to delete the tag associated with a DB instance.

## URI<a name="s33dc7d61a8354d16b17088f295ad3753"></a>

-   URI format

    PATH: /v1/\{project\_id\}/rds/\{instanceId\}/tags

    Method: DELETE

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0091754394_table58427690"></a>
    <table><thead align="left"><tr id="en-us_topic_0091754394_row1482002"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="en-us_topic_0091754394_p52933326"><a name="en-us_topic_0091754394_p52933326"></a><a name="en-us_topic_0091754394_p52933326"></a><strong id="en-us_topic_0091754394_b84235270691445"><a name="en-us_topic_0091754394_b84235270691445"></a><a name="en-us_topic_0091754394_b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="en-us_topic_0091754394_p59740974"><a name="en-us_topic_0091754394_p59740974"></a><a name="en-us_topic_0091754394_p59740974"></a><strong id="en-us_topic_0091754394_b842352706102346"><a name="en-us_topic_0091754394_b842352706102346"></a><a name="en-us_topic_0091754394_b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0091754394_p7180698"><a name="en-us_topic_0091754394_p7180698"></a><a name="en-us_topic_0091754394_p7180698"></a><strong id="en-us_topic_0091754394_b842352706163417"><a name="en-us_topic_0091754394_b842352706163417"></a><a name="en-us_topic_0091754394_b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0091754394_row44765691"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091754394_p2142393"><a name="en-us_topic_0091754394_p2142393"></a><a name="en-us_topic_0091754394_p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091754394_p39316155"><a name="en-us_topic_0091754394_p39316155"></a><a name="en-us_topic_0091754394_p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091754394_p30492010"><a name="en-us_topic_0091754394_p30492010"></a><a name="en-us_topic_0091754394_p30492010"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091754394_row5992637"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091754394_p15641626"><a name="en-us_topic_0091754394_p15641626"></a><a name="en-us_topic_0091754394_p15641626"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091754394_p59012183"><a name="en-us_topic_0091754394_p59012183"></a><a name="en-us_topic_0091754394_p59012183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Standby DB instances do not support tag deletion.


## Request<a name="sf06afd7786da4b0b8cab9b89400ed6f8"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="t6d1d2d3bdb4d43eabd411394581198c0"></a>
    <table><thead align="left"><tr id="r419b47533bc54a24a76a948e5e31bf1e"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="ab024fa51f0324612a83a99f5ed69adc6"><a name="ab024fa51f0324612a83a99f5ed69adc6"></a><a name="ab024fa51f0324612a83a99f5ed69adc6"></a><strong id="b952140185"><a name="b952140185"></a><a name="b952140185"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.2"><p id="a0e13f02ca0b54b2c80768eab0f4c65fc"><a name="a0e13f02ca0b54b2c80768eab0f4c65fc"></a><a name="a0e13f02ca0b54b2c80768eab0f4c65fc"></a><strong id="b508641759"><a name="b508641759"></a><a name="b508641759"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="acabf1f89ef0843c7816a1d5cd35f6284"><a name="acabf1f89ef0843c7816a1d5cd35f6284"></a><a name="acabf1f89ef0843c7816a1d5cd35f6284"></a><strong id="en-us_topic_0091754394_b842352706164541"><a name="en-us_topic_0091754394_b842352706164541"></a><a name="en-us_topic_0091754394_b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="a282eb3de69ea4de6a64f7dd8aa2c461b"><a name="a282eb3de69ea4de6a64f7dd8aa2c461b"></a><a name="a282eb3de69ea4de6a64f7dd8aa2c461b"></a><strong id="b1782389958"><a name="b1782389958"></a><a name="b1782389958"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ra25a6ca010cc4536802a5831308af8cb"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p63311645161424"><a name="p63311645161424"></a><a name="p63311645161424"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.2 "><p id="p27969644161424"><a name="p27969644161424"></a><a name="p27969644161424"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p50948687161424"><a name="p50948687161424"></a><a name="p50948687161424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p33202991161424"><a name="p33202991161424"></a><a name="p33202991161424"></a>Specifies the tag key.</p>
    <p id="p30391465161424"><a name="p30391465161424"></a><a name="p30391465161424"></a>Its value cannot be empty and must be 1 to 36 Unicode characters in length. It cannot contain nonprintable ASCII characters (0–31) and the following special characters: *&lt;&gt;\=</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    {
         
        "key": "ENV"
    }
    ```


## Normal Response<a name="s8d27102bb15a4908a3e92a37bbb7b050"></a>

None

## Abnormal Response<a name="sbc975b2481f04840a631eec0939aff8f"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

