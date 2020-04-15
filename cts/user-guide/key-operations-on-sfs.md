# Key Operations on SFS<a name="en-us_topic_0100273715"></a>

Scalable File Service \(SFS\) enables high-performance file storage that can be expanded and shrunk on demand. It provides file sharing services for multiple Elastic Cloud Servers \(ECSs\).

With CTS, you can record operations associated with SFS for later query, audit, and backtrack operations.

**Table  1**  SFS operations that can be recorded by CTS

<a name="table19033961114053"></a>
<table><thead align="left"><tr id="r2760a4e7e0854d068ebea8a1a8778852"><th class="cellrowborder" valign="top" width="31.630000000000003%" id="mcps1.2.4.1.1"><p id="ad0f4b8c1c4d543309cf937a44470c5d5"><a name="ad0f4b8c1c4d543309cf937a44470c5d5"></a><a name="ad0f4b8c1c4d543309cf937a44470c5d5"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.59%" id="mcps1.2.4.1.2"><p id="a1ef40b42f97441d6980b2b718a1cf9cc"><a name="a1ef40b42f97441d6980b2b718a1cf9cc"></a><a name="a1ef40b42f97441d6980b2b718a1cf9cc"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.78%" id="mcps1.2.4.1.3"><p id="aaca1b89d0fe649538c2044aef5d9e048"><a name="aaca1b89d0fe649538c2044aef5d9e048"></a><a name="aaca1b89d0fe649538c2044aef5d9e048"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc8fc25fafe67465faa2dbf30806ca376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="aff81428a16a64b9294ea68582b2a6d7e"><a name="aff81428a16a64b9294ea68582b2a6d7e"></a><a name="aff81428a16a64b9294ea68582b2a6d7e"></a>Creating a share</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a589201240339448ab6853d942916ab2b"><a name="a589201240339448ab6853d942916ab2b"></a><a name="a589201240339448ab6853d942916ab2b"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="ae6ec0b32c5d74638a67a9035502ff164"><a name="ae6ec0b32c5d74638a67a9035502ff164"></a><a name="ae6ec0b32c5d74638a67a9035502ff164"></a>createShare</p>
</td>
</tr>
<tr id="rb769f5a71c504925a42c452436645716"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p920237114444"><a name="en-us_topic_0100240354_p920237114444"></a><a name="en-us_topic_0100240354_p920237114444"></a>Updating a share</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="af28b6f70c100437fb34d5c19be547770"><a name="af28b6f70c100437fb34d5c19be547770"></a><a name="af28b6f70c100437fb34d5c19be547770"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="ae38ed7272a424145963810ffdbe4252a"><a name="ae38ed7272a424145963810ffdbe4252a"></a><a name="ae38ed7272a424145963810ffdbe4252a"></a>updateShareInfo</p>
</td>
</tr>
<tr id="rb24078cc63bb41298a0865b7301f3476"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a5e9af1deb2394359b55aee37a647854c"><a name="a5e9af1deb2394359b55aee37a647854c"></a><a name="a5e9af1deb2394359b55aee37a647854c"></a>Deleting a share</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a0d1d3d9580c849ac8bf3a8de96ecb565"><a name="a0d1d3d9580c849ac8bf3a8de96ecb565"></a><a name="a0d1d3d9580c849ac8bf3a8de96ecb565"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a7753816d6ff24383965db087bc4b4969"><a name="a7753816d6ff24383965db087bc4b4969"></a><a name="a7753816d6ff24383965db087bc4b4969"></a>deleteShare</p>
</td>
</tr>
<tr id="rba6acf8a377a41cd8f9774ad66b9060a"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a2070bb7997c24e59a2889a5408ebf882"><a name="a2070bb7997c24e59a2889a5408ebf882"></a><a name="a2070bb7997c24e59a2889a5408ebf882"></a>Adding a share access rule</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="aafe608450e4d416b8ad76e9c06766b86"><a name="aafe608450e4d416b8ad76e9c06766b86"></a><a name="aafe608450e4d416b8ad76e9c06766b86"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p614308711453"><a name="en-us_topic_0100240354_p614308711453"></a><a name="en-us_topic_0100240354_p614308711453"></a>addShareACL</p>
</td>
</tr>
<tr id="r39d0ebf1ca0f410baa584abd5bd75c7d"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a8472fada2e8241eb95a00dfdfac75a44"><a name="a8472fada2e8241eb95a00dfdfac75a44"></a><a name="a8472fada2e8241eb95a00dfdfac75a44"></a>Deleting a share access rule</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a237d87d8aae1461db6ae7a610a0e1241"><a name="a237d87d8aae1461db6ae7a610a0e1241"></a><a name="a237d87d8aae1461db6ae7a610a0e1241"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a0957979c09fd4cb0a1f5043fcdd651c2"><a name="a0957979c09fd4cb0a1f5043fcdd651c2"></a><a name="a0957979c09fd4cb0a1f5043fcdd651c2"></a>deleteShareACL</p>
</td>
</tr>
<tr id="r52a90186293e488e8e3b477411ba122c"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a012275dc5ffc4f578ac592dccc0d985f"><a name="a012275dc5ffc4f578ac592dccc0d985f"></a><a name="a012275dc5ffc4f578ac592dccc0d985f"></a>Expanding a share</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="ab8336147960b41498ed07f4bf7203cef"><a name="ab8336147960b41498ed07f4bf7203cef"></a><a name="ab8336147960b41498ed07f4bf7203cef"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a2a1836c642d347e6936eb5f8b52e74e5"><a name="a2a1836c642d347e6936eb5f8b52e74e5"></a><a name="a2a1836c642d347e6936eb5f8b52e74e5"></a>extendShare</p>
</td>
</tr>
<tr id="r27a65fd9567449279935ec6a6ab4495c"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="a9a47d79be6094593a40197e20815c781"><a name="a9a47d79be6094593a40197e20815c781"></a><a name="a9a47d79be6094593a40197e20815c781"></a>Shrinking a share</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="a4575eab260414c57a18bea087d3c5d32"><a name="a4575eab260414c57a18bea087d3c5d32"></a><a name="a4575eab260414c57a18bea087d3c5d32"></a>sfs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a0fc193ed787a4c98818014ece1ca5229"><a name="a0fc193ed787a4c98818014ece1ca5229"></a><a name="a0fc193ed787a4c98818014ece1ca5229"></a>shrinkShare</p>
</td>
</tr>
</tbody>
</table>

