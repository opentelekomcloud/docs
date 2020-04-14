# Key Operations on KMS<a name="en-us_topic_0100291685"></a>

Key Management Service \(KMS\) is a secure and reliable key hosting service used to provide central management of users' masker keys.

With CTS, you can record operations associated with KMS for future query, audit, and backtrack operations.

**Table  1**  KMS operations that can be recorded by CTS

<a name="table25734726175532"></a>
<table><thead align="left"><tr id="r18cd940e1d18441cac772b6393f21eb1"><th class="cellrowborder" valign="top" width="29.217078292170783%" id="mcps1.2.4.1.1"><p id="a71c82d07fa4d4cf09d31a79e024d2ea4"><a name="a71c82d07fa4d4cf09d31a79e024d2ea4"></a><a name="a71c82d07fa4d4cf09d31a79e024d2ea4"></a><strong id="a9ae5896946f04f188ceb612272e0d226"><a name="a9ae5896946f04f188ceb612272e0d226"></a><a name="a9ae5896946f04f188ceb612272e0d226"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.567243275672432%" id="mcps1.2.4.1.2"><p id="abaef4542b74641a0a7e222032398b33f"><a name="abaef4542b74641a0a7e222032398b33f"></a><a name="abaef4542b74641a0a7e222032398b33f"></a><strong id="a67b8823db55342bb84dda91e88156132"><a name="a67b8823db55342bb84dda91e88156132"></a><a name="a67b8823db55342bb84dda91e88156132"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.215678432156786%" id="mcps1.2.4.1.3"><p id="a9a5832c716894ac7831628d0824e6e33"><a name="a9a5832c716894ac7831628d0824e6e33"></a><a name="a9a5832c716894ac7831628d0824e6e33"></a><strong id="en-us_topic_0100240334_b920211020151"><a name="en-us_topic_0100240334_b920211020151"></a><a name="en-us_topic_0100240334_b920211020151"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rd976e4ff91594fddbc168d80856952e5"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="ab5e23f26c7c64f3fab0c5b3b9b186788"><a name="ab5e23f26c7c64f3fab0c5b3b9b186788"></a><a name="ab5e23f26c7c64f3fab0c5b3b9b186788"></a>Creating a secret key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a24e3ce75d6624ca181b455de7da7acbe"><a name="a24e3ce75d6624ca181b455de7da7acbe"></a><a name="a24e3ce75d6624ca181b455de7da7acbe"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="ad53986017b784a89b961273ab026399f"><a name="ad53986017b784a89b961273ab026399f"></a><a name="ad53986017b784a89b961273ab026399f"></a>createKey</p>
</td>
</tr>
<tr id="r989e982846aa46abb69c74354d16a473"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="ac897ea4c71584b9790db412b63458700"><a name="ac897ea4c71584b9790db412b63458700"></a><a name="ac897ea4c71584b9790db412b63458700"></a>Creating a data key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="aa2e78588a2b44b188956ef8b7440e220"><a name="aa2e78588a2b44b188956ef8b7440e220"></a><a name="aa2e78588a2b44b188956ef8b7440e220"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a9f1f6f78f9164e73b98b40bf77b73266"><a name="a9f1f6f78f9164e73b98b40bf77b73266"></a><a name="a9f1f6f78f9164e73b98b40bf77b73266"></a>createDataKey</p>
</td>
</tr>
<tr id="r07262e5492bf454a8100e61b73466fb8"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p233740619237"><a name="en-us_topic_0100240334_p233740619237"></a><a name="en-us_topic_0100240334_p233740619237"></a>Creating a plaintext-free data key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240334_p603085192314"><a name="en-us_topic_0100240334_p603085192314"></a><a name="en-us_topic_0100240334_p603085192314"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="ac3a125734ba643deb01d5d878eb3b752"><a name="ac3a125734ba643deb01d5d878eb3b752"></a><a name="ac3a125734ba643deb01d5d878eb3b752"></a>createDataKeyWithoutPlaintext</p>
</td>
</tr>
<tr id="rfee31c634306416aa849f5a70e8de380"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="aa2b2600b47ed4021b7176955438ae21d"><a name="aa2b2600b47ed4021b7176955438ae21d"></a><a name="aa2b2600b47ed4021b7176955438ae21d"></a>Enabling a secret key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a6f6d1877d96e45daa42793e815ce8087"><a name="a6f6d1877d96e45daa42793e815ce8087"></a><a name="a6f6d1877d96e45daa42793e815ce8087"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a294252474e8d4c5b9a6278377cf5e449"><a name="a294252474e8d4c5b9a6278377cf5e449"></a><a name="a294252474e8d4c5b9a6278377cf5e449"></a>enableKey</p>
</td>
</tr>
<tr id="rdf5705721583462bab5e02c9ba7b5523"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p872563219237"><a name="en-us_topic_0100240334_p872563219237"></a><a name="en-us_topic_0100240334_p872563219237"></a>Disabling a secret key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a5932b884429348f2ace552b0e527a398"><a name="a5932b884429348f2ace552b0e527a398"></a><a name="a5932b884429348f2ace552b0e527a398"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a33d01a36a17f48bba1e61b8b4a0d0193"><a name="a33d01a36a17f48bba1e61b8b4a0d0193"></a><a name="a33d01a36a17f48bba1e61b8b4a0d0193"></a>disableKey</p>
</td>
</tr>
<tr id="r23a5a30cd5ce4ad58b6262b0b5873eb1"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="a6fcc636fa519409eb28b159217f8121b"><a name="a6fcc636fa519409eb28b159217f8121b"></a><a name="a6fcc636fa519409eb28b159217f8121b"></a>Encrypting a data key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a4f8f354b7bc34a689aa0253b016dc913"><a name="a4f8f354b7bc34a689aa0253b016dc913"></a><a name="a4f8f354b7bc34a689aa0253b016dc913"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a1e62e3e39ffc4fa799e5866be381997b"><a name="a1e62e3e39ffc4fa799e5866be381997b"></a><a name="a1e62e3e39ffc4fa799e5866be381997b"></a>encryptDataKey</p>
</td>
</tr>
<tr id="r4211aabed33d40388dc5b74b2c53e03b"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p333607419237"><a name="en-us_topic_0100240334_p333607419237"></a><a name="en-us_topic_0100240334_p333607419237"></a>Decrypting a data key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a5a00f0b808e04182b761e4b89c5043d9"><a name="a5a00f0b808e04182b761e4b89c5043d9"></a><a name="a5a00f0b808e04182b761e4b89c5043d9"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a367ef756461d47789e48e26a61838ac9"><a name="a367ef756461d47789e48e26a61838ac9"></a><a name="a367ef756461d47789e48e26a61838ac9"></a>decryptDataKey</p>
</td>
</tr>
<tr id="r8708bedbd81b4cbb821a12c44e46875c"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="aa8f73ea2e6424f8db9f2b143110fd866"><a name="aa8f73ea2e6424f8db9f2b143110fd866"></a><a name="aa8f73ea2e6424f8db9f2b143110fd866"></a>Scheduling the deletion of a secret key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a0867563d87fa42d3877d93b9c4b39b5a"><a name="a0867563d87fa42d3877d93b9c4b39b5a"></a><a name="a0867563d87fa42d3877d93b9c4b39b5a"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="adcb6fb9479e1461097058df2898c2419"><a name="adcb6fb9479e1461097058df2898c2419"></a><a name="adcb6fb9479e1461097058df2898c2419"></a>scheduleKeyDeletion</p>
</td>
</tr>
<tr id="rf4b746a963344d82a523e1eaf7b836eb"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="aadb23ec222d74a3080cb5e8955322ba1"><a name="aadb23ec222d74a3080cb5e8955322ba1"></a><a name="aadb23ec222d74a3080cb5e8955322ba1"></a>Canceling the scheduled deletion of a secret key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="ab7fa0284f1d04c188234b3e8863a7455"><a name="ab7fa0284f1d04c188234b3e8863a7455"></a><a name="ab7fa0284f1d04c188234b3e8863a7455"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="aa15a5b51e3b44e1fb10701a0e06528c3"><a name="aa15a5b51e3b44e1fb10701a0e06528c3"></a><a name="aa15a5b51e3b44e1fb10701a0e06528c3"></a>cancelKeyDeletion</p>
</td>
</tr>
<tr id="r24710549852f4b0f875ec94d02cbf5c6"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p261425019237"><a name="en-us_topic_0100240334_p261425019237"></a><a name="en-us_topic_0100240334_p261425019237"></a>Changing the alias of a key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a233f45e056dc42be8a1d288027983294"><a name="a233f45e056dc42be8a1d288027983294"></a><a name="a233f45e056dc42be8a1d288027983294"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="ac3abe6e6003842cdb2e5c2380042f487"><a name="ac3abe6e6003842cdb2e5c2380042f487"></a><a name="ac3abe6e6003842cdb2e5c2380042f487"></a>updateKeyAlias</p>
</td>
</tr>
<tr id="r025f3ce6ff424479970e6846cc5c3cf3"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="acbb79030d9c1450db821aeeabd32ebec"><a name="acbb79030d9c1450db821aeeabd32ebec"></a><a name="acbb79030d9c1450db821aeeabd32ebec"></a>Modifying the description of a key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a12f304e4db604c98b8e3e632a80c34a9"><a name="a12f304e4db604c98b8e3e632a80c34a9"></a><a name="a12f304e4db604c98b8e3e632a80c34a9"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a05e4216cbc0546e8bc86b220a6fe8617"><a name="a05e4216cbc0546e8bc86b220a6fe8617"></a><a name="a05e4216cbc0546e8bc86b220a6fe8617"></a>updateKeyDescription</p>
</td>
</tr>
<tr id="r39837f2fd3ef4d25a3f4a6cf9e89dd21"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="adb26fe5373844b1fbd7b205ef2984069"><a name="adb26fe5373844b1fbd7b205ef2984069"></a><a name="adb26fe5373844b1fbd7b205ef2984069"></a>Precautions for deleting a key</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a2d13fca4b8784bf5b939fffa96a615e6"><a name="a2d13fca4b8784bf5b939fffa96a615e6"></a><a name="a2d13fca4b8784bf5b939fffa96a615e6"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="af361d592d0a94076b7bcbcc9e28fbc7e"><a name="af361d592d0a94076b7bcbcc9e28fbc7e"></a><a name="af361d592d0a94076b7bcbcc9e28fbc7e"></a>deleteKeyRiskTips</p>
</td>
</tr>
<tr id="r7ed42259382d4646a47809e5d484a853"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="a13efa2e0af4841d89b751b835f8f7720"><a name="a13efa2e0af4841d89b751b835f8f7720"></a><a name="a13efa2e0af4841d89b751b835f8f7720"></a>Creating an agency</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a8fe709b766a6413f973b2070b8e1dd7a"><a name="a8fe709b766a6413f973b2070b8e1dd7a"></a><a name="a8fe709b766a6413f973b2070b8e1dd7a"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a8e3acc7782ef409f9a0c6cf137a14152"><a name="a8e3acc7782ef409f9a0c6cf137a14152"></a><a name="a8e3acc7782ef409f9a0c6cf137a14152"></a>createGrant</p>
</td>
</tr>
<tr id="rbd81e05fc2e14fa89575d1c2fba6691a"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="a3fc306515b9e4394a12cfa1ce43acc10"><a name="a3fc306515b9e4394a12cfa1ce43acc10"></a><a name="a3fc306515b9e4394a12cfa1ce43acc10"></a>Retiring a grant</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a6e605f399765480cbc005e1426f3d0ed"><a name="a6e605f399765480cbc005e1426f3d0ed"></a><a name="a6e605f399765480cbc005e1426f3d0ed"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="aaad7c649c5114f7bbf1f42e97648b0a4"><a name="aaad7c649c5114f7bbf1f42e97648b0a4"></a><a name="aaad7c649c5114f7bbf1f42e97648b0a4"></a>retireGrant</p>
</td>
</tr>
<tr id="r9c88c053a1a54e00805ae857be5b42b5"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240334_p830128719237"><a name="en-us_topic_0100240334_p830128719237"></a><a name="en-us_topic_0100240334_p830128719237"></a>Revoking a grant</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="a70ef2ed2ce80479e9a84bfd75b1939f5"><a name="a70ef2ed2ce80479e9a84bfd75b1939f5"></a><a name="a70ef2ed2ce80479e9a84bfd75b1939f5"></a>cmk</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="a7d10cee49aa8477a8f5b94b7594ce895"><a name="a7d10cee49aa8477a8f5b94b7594ce895"></a><a name="a7d10cee49aa8477a8f5b94b7594ce895"></a>revokeGrant</p>
</td>
</tr>
<tr id="re1dc75253980442db165785b684d3d72"><td class="cellrowborder" valign="top" width="29.217078292170783%" headers="mcps1.2.4.1.1 "><p id="a7105a439539546709d39645b94a7df96"><a name="a7105a439539546709d39645b94a7df96"></a><a name="a7105a439539546709d39645b94a7df96"></a>Creating random data</p>
</td>
<td class="cellrowborder" valign="top" width="27.567243275672432%" headers="mcps1.2.4.1.2 "><p id="adb194b0f8b6e4afd8de79720fbbf37db"><a name="adb194b0f8b6e4afd8de79720fbbf37db"></a><a name="adb194b0f8b6e4afd8de79720fbbf37db"></a>rng</p>
</td>
<td class="cellrowborder" valign="top" width="43.215678432156786%" headers="mcps1.2.4.1.3 "><p id="afa5b8a96f1ce442c973497c69c66e34d"><a name="afa5b8a96f1ce442c973497c69c66e34d"></a><a name="afa5b8a96f1ce442c973497c69c66e34d"></a>genRandom</p>
</td>
</tr>
</tbody>
</table>

