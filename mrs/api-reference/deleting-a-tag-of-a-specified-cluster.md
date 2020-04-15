# Deleting a Tag of a Specified Cluster<a name="EN-US_TOPIC_0172486195"></a>

## Function<a name="s8e176e6d570e4b9984866689547c9455"></a>

This API is used to delete a tag of a specified cluster.

## URI<a name="sabb5f678ee1d442f8cd06d539f0deadb"></a>

-   Format

    DELETE /v1.1/\{project\_id\}/clusters/\{cluster\_id\}/tags/\{key\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="t23b678c0e6e443bb957bda4013e38032"></a>
    <table><thead align="left"><tr id="r647620be2fa94e4298451667de9ae0c1"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="af61030020714491b8d3ba2166b332eb1"><a name="af61030020714491b8d3ba2166b332eb1"></a><a name="af61030020714491b8d3ba2166b332eb1"></a><strong id="b162721316171012"><a name="b162721316171012"></a><a name="b162721316171012"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110707062_p388412816227"><a name="en-us_topic_0110707062_p388412816227"></a><a name="en-us_topic_0110707062_p388412816227"></a><strong id="b14356138181013"><a name="b14356138181013"></a><a name="b14356138181013"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="ad1dbf0431d044a4d975612f8f743e836"><a name="ad1dbf0431d044a4d975612f8f743e836"></a><a name="ad1dbf0431d044a4d975612f8f743e836"></a><strong id="b619995191018"><a name="b619995191018"></a><a name="b619995191018"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r5390b8e10563492aae44bde4fe3cd776"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a99003688fbce46c1bd9dab407a40ea68"><a name="a99003688fbce46c1bd9dab407a40ea68"></a><a name="a99003688fbce46c1bd9dab407a40ea68"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a87ab8d30896e449eac21fac11c3cbdb5"><a name="a87ab8d30896e449eac21fac11c3cbdb5"></a><a name="a87ab8d30896e449eac21fac11c3cbdb5"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa7e22425547d4b178bd3b7c9d13eb0b0"><a name="aa7e22425547d4b178bd3b7c9d13eb0b0"></a><a name="aa7e22425547d4b178bd3b7c9d13eb0b0"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="r7c49d727a4fa41039b5b611dcaf9382d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110707062_p288462815221"><a name="en-us_topic_0110707062_p288462815221"></a><a name="en-us_topic_0110707062_p288462815221"></a>cluster_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ad357c2193e0f4186951b55237416c742"><a name="ad357c2193e0f4186951b55237416c742"></a><a name="ad357c2193e0f4186951b55237416c742"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110707062_p78845285227"><a name="en-us_topic_0110707062_p78845285227"></a><a name="en-us_topic_0110707062_p78845285227"></a>Cluster ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="saa2d1d6136b44b93b95e23834d329642"></a>

**Request parameters**

None.

## Response<a name="s0395465945ea4ec1939e463c02bad21d"></a>

**Response parameters**

None

## Example<a name="section1210015461189"></a>

-   Example request

    None.

-   Example response

    None


## Status Code<a name="s3121da348aea44ed9c2f4409d4709e9a"></a>

[Table 2](#t72c4159e310d449696ec7ba265e3428e)  describes the status code of this API.

**Table  2**  Status code

<a name="t72c4159e310d449696ec7ba265e3428e"></a>
<table><thead align="left"><tr id="rb300edfab41542bd862a9c36374a3ded"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="a10ad0654fb9d4ef79a187a79b8281b6b"><a name="a10ad0654fb9d4ef79a187a79b8281b6b"></a><a name="a10ad0654fb9d4ef79a187a79b8281b6b"></a><strong id="b185109145712"><a name="b185109145712"></a><a name="b185109145712"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="aca156656628f45d7b617ef94957aadd5"><a name="aca156656628f45d7b617ef94957aadd5"></a><a name="aca156656628f45d7b617ef94957aadd5"></a><strong id="b10103117773"><a name="b10103117773"></a><a name="b10103117773"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r80461b233d74443f8a10d62550880565"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="a5353664480384092a6fcc5cb43584698"><a name="a5353664480384092a6fcc5cb43584698"></a><a name="a5353664480384092a6fcc5cb43584698"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1666511011814"><a name="p1666511011814"></a><a name="p1666511011814"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

