# Key Operations on CCE<a name="en-us_topic_0100273723"></a>

Cloud Container Engine \(CCE\) is a high-performance, high-reliability service through which enterprises can manage containerized applications. CCE supports native Kubernetes applications and tools, allowing you to easily set up a container runtime environment on the cloud.

With CTS, you can record operations associated with CCE for later query, audit, and backtrack operations.

**Table  1**  CCE operations that can be recorded by CTS

<a name="table10108575152351"></a>
<table><thead align="left"><tr id="rccad9ebebc8d4ffd970376d34a3aa77b"><th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.1"><p id="a6e50e1e545b84cc58b8859384104cfb1"><a name="a6e50e1e545b84cc58b8859384104cfb1"></a><a name="a6e50e1e545b84cc58b8859384104cfb1"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.4.1.2"><p id="a1dbd11aff07f461990352d68de0f1536"><a name="a1dbd11aff07f461990352d68de0f1536"></a><a name="a1dbd11aff07f461990352d68de0f1536"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.4.1.3"><p id="ad4ded60fc19c4179967760d4c251e042"><a name="ad4ded60fc19c4179967760d4c251e042"></a><a name="ad4ded60fc19c4179967760d4c251e042"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rbfd9698e326e4eebb9ecc62fd4caab15"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="abcdf3b5133a2461ea15b5d85f3aaa8b2"><a name="abcdf3b5133a2461ea15b5d85f3aaa8b2"></a><a name="abcdf3b5133a2461ea15b5d85f3aaa8b2"></a>Uploading a certificate</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ae52cd0c82aac4420aac92cc0b45ba292"><a name="ae52cd0c82aac4420aac92cc0b45ba292"></a><a name="ae52cd0c82aac4420aac92cc0b45ba292"></a>aksk</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a042c303e5a4649498d8b981adb2720fd"><a name="a042c303e5a4649498d8b981adb2720fd"></a><a name="a042c303e5a4649498d8b981adb2720fd"></a>uploadAKSK</p>
</td>
</tr>
<tr id="r08208c293c6e4eca99edac92fce53f58"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a343b1b84d75247d98d1bd146b7120042"><a name="a343b1b84d75247d98d1bd146b7120042"></a><a name="a343b1b84d75247d98d1bd146b7120042"></a>Creating a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a443202b17a7e4f0c91f9d36b3db1f6a2"><a name="a443202b17a7e4f0c91f9d36b3db1f6a2"></a><a name="a443202b17a7e4f0c91f9d36b3db1f6a2"></a>cluster_cce</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="adb93647b5c4d4db2af757a76ddec8a6d"><a name="adb93647b5c4d4db2af757a76ddec8a6d"></a><a name="adb93647b5c4d4db2af757a76ddec8a6d"></a>createCluster</p>
</td>
</tr>
<tr id="r1bee83e1bbd0438fbc7bab46bd5efbb0"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="af107d0423da34df088ddcc14ae778ab5"><a name="af107d0423da34df088ddcc14ae778ab5"></a><a name="af107d0423da34df088ddcc14ae778ab5"></a>Upgrading a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ae24b4f140fda4c9eb4aed925e9465a1c"><a name="ae24b4f140fda4c9eb4aed925e9465a1c"></a><a name="ae24b4f140fda4c9eb4aed925e9465a1c"></a>cluster_cce</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ac1e6c98659d54e14b78542709c231177"><a name="ac1e6c98659d54e14b78542709c231177"></a><a name="ac1e6c98659d54e14b78542709c231177"></a>upgradeCluster</p>
</td>
</tr>
<tr id="rfa888a983cc9454fbac4e979f4189abb"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a4399aba81dad428d8195919d205ee547"><a name="a4399aba81dad428d8195919d205ee547"></a><a name="a4399aba81dad428d8195919d205ee547"></a>Updating a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a8ce1512af60241ab8b970d5f61d573d2"><a name="a8ce1512af60241ab8b970d5f61d573d2"></a><a name="a8ce1512af60241ab8b970d5f61d573d2"></a>cluster_cce</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="af0347ca1242a424793c72287e5353cb5"><a name="af0347ca1242a424793c72287e5353cb5"></a><a name="af0347ca1242a424793c72287e5353cb5"></a>updateCluster</p>
</td>
</tr>
<tr id="rb11d8a0ca7e347e4a8633ea0b7339c8c"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="ac4199bc49d2e424b85de19b74823eb43"><a name="ac4199bc49d2e424b85de19b74823eb43"></a><a name="ac4199bc49d2e424b85de19b74823eb43"></a>Deleting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="aee9e7b9a920a4792a4e4945d7c421e32"><a name="aee9e7b9a920a4792a4e4945d7c421e32"></a><a name="aee9e7b9a920a4792a4e4945d7c421e32"></a>cluster_cce</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="aa7920d65f5944faba25384a13ae1ba20"><a name="aa7920d65f5944faba25384a13ae1ba20"></a><a name="aa7920d65f5944faba25384a13ae1ba20"></a>deleteCluster</p>
</td>
</tr>
<tr id="r6895ca0928e64a29b0accee68ea6ea3a"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a830ce504bd364bec9b405ed8af726bf3"><a name="a830ce504bd364bec9b405ed8af726bf3"></a><a name="a830ce504bd364bec9b405ed8af726bf3"></a>Creating a node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a7078a4c66c5345f78ae2700c499e2a75"><a name="a7078a4c66c5345f78ae2700c499e2a75"></a><a name="a7078a4c66c5345f78ae2700c499e2a75"></a>node</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ac7add8a14da343d2958bcec01b394980"><a name="ac7add8a14da343d2958bcec01b394980"></a><a name="ac7add8a14da343d2958bcec01b394980"></a>createNode</p>
</td>
</tr>
<tr id="red0f2c33b311446c80e7fedfcb5a0f94"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a2799bff83993491f8d3ef5265674fbd8"><a name="a2799bff83993491f8d3ef5265674fbd8"></a><a name="a2799bff83993491f8d3ef5265674fbd8"></a>Deleting a node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a57cfdc5056504ae7bc808adfb4f6c2b9"><a name="a57cfdc5056504ae7bc808adfb4f6c2b9"></a><a name="a57cfdc5056504ae7bc808adfb4f6c2b9"></a>node</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a141e652e3340407cb31b6dafa115d3a5"><a name="a141e652e3340407cb31b6dafa115d3a5"></a><a name="a141e652e3340407cb31b6dafa115d3a5"></a>deleteNode</p>
</td>
</tr>
<tr id="rf73abaaeb2944ee089c18af97211c57d"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a98c75de4bb6341b0a88035b1d8f79a14"><a name="a98c75de4bb6341b0a88035b1d8f79a14"></a><a name="a98c75de4bb6341b0a88035b1d8f79a14"></a>Creating a template</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a24e219d18d9e47fcb634d7455466e5d0"><a name="a24e219d18d9e47fcb634d7455466e5d0"></a><a name="a24e219d18d9e47fcb634d7455466e5d0"></a>component</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="add7ea373956441eb890b076da88e5c18"><a name="add7ea373956441eb890b076da88e5c18"></a><a name="add7ea373956441eb890b076da88e5c18"></a>createComponent</p>
</td>
</tr>
<tr id="rfe246f9763e64cd5a7e5ef0a901b67ca"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a9734b004509d4555bdeb5b121179b11a"><a name="a9734b004509d4555bdeb5b121179b11a"></a><a name="a9734b004509d4555bdeb5b121179b11a"></a>Updating a template</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a0b0e84c865524d0ab07ebc68a42f30b3"><a name="a0b0e84c865524d0ab07ebc68a42f30b3"></a><a name="a0b0e84c865524d0ab07ebc68a42f30b3"></a>component</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a14a2efed8749453bb3a8fecce539c16b"><a name="a14a2efed8749453bb3a8fecce539c16b"></a><a name="a14a2efed8749453bb3a8fecce539c16b"></a>updateComponent</p>
</td>
</tr>
<tr id="r438860480cc846eaa6d1cfbe75a5c15e"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a9f6d6f620a794fcaa9a356bdb17e562b"><a name="a9f6d6f620a794fcaa9a356bdb17e562b"></a><a name="a9f6d6f620a794fcaa9a356bdb17e562b"></a>Deleting a template</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a339285cb0ffb49c983b66d48355db380"><a name="a339285cb0ffb49c983b66d48355db380"></a><a name="a339285cb0ffb49c983b66d48355db380"></a>component</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ab02ef469117445ecacc364eea3e4e977"><a name="ab02ef469117445ecacc364eea3e4e977"></a><a name="ab02ef469117445ecacc364eea3e4e977"></a>deleteComponent</p>
</td>
</tr>
<tr id="r8954589fe51c4ba09ac2f64a262a29e8"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a82a3a37154f94163952f808e2939ec56"><a name="a82a3a37154f94163952f808e2939ec56"></a><a name="a82a3a37154f94163952f808e2939ec56"></a>Creating an application</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a480f1545d49d45379a03b623dce274fb"><a name="a480f1545d49d45379a03b623dce274fb"></a><a name="a480f1545d49d45379a03b623dce274fb"></a>app</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ada0d033f43e74071a1f741fcd1e77eb4"><a name="ada0d033f43e74071a1f741fcd1e77eb4"></a><a name="ada0d033f43e74071a1f741fcd1e77eb4"></a>createApp</p>
</td>
</tr>
<tr id="r84cd58bd7d25491c95689686f6e0b32a"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="aee6f0fa2ea3443ee91fd61319dad59b1"><a name="aee6f0fa2ea3443ee91fd61319dad59b1"></a><a name="aee6f0fa2ea3443ee91fd61319dad59b1"></a>Updating an application</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a018b84ca41d446b3bdeb4633f24110d7"><a name="a018b84ca41d446b3bdeb4633f24110d7"></a><a name="a018b84ca41d446b3bdeb4633f24110d7"></a>app</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a46c1af8ca98b4e73977ac0e678f262cf"><a name="a46c1af8ca98b4e73977ac0e678f262cf"></a><a name="a46c1af8ca98b4e73977ac0e678f262cf"></a>updateApp</p>
</td>
</tr>
<tr id="r6285c0042d8e43419d8ba42e9e2db325"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a879447fb596a47f9b4f47c7419b58c92"><a name="a879447fb596a47f9b4f47c7419b58c92"></a><a name="a879447fb596a47f9b4f47c7419b58c92"></a>Rolling back an application</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a3e557b2d739a4eebb92705aa39251436"><a name="a3e557b2d739a4eebb92705aa39251436"></a><a name="a3e557b2d739a4eebb92705aa39251436"></a>app</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="acd48a9ce5c50410ca777cd42fe08f091"><a name="acd48a9ce5c50410ca777cd42fe08f091"></a><a name="acd48a9ce5c50410ca777cd42fe08f091"></a>rollBackApp</p>
</td>
</tr>
<tr id="r075654a3eff34c84ba618fd6c59020ed"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a5fc089b835954534b206f60fe9ad67aa"><a name="a5fc089b835954534b206f60fe9ad67aa"></a><a name="a5fc089b835954534b206f60fe9ad67aa"></a>Deleting an application</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="aaab1df01e2a34db388561c0ace12b3e6"><a name="aaab1df01e2a34db388561c0ace12b3e6"></a><a name="aaab1df01e2a34db388561c0ace12b3e6"></a>app</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ae58140cbd79f4987842d4bd21286f78c"><a name="ae58140cbd79f4987842d4bd21286f78c"></a><a name="ae58140cbd79f4987842d4bd21286f78c"></a>deleteApp</p>
</td>
</tr>
<tr id="r67cdbf509fac44aeab8738d419258d6c"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a2995df0e34564d50af87a7cccd7c7fdf"><a name="a2995df0e34564d50af87a7cccd7c7fdf"></a><a name="a2995df0e34564d50af87a7cccd7c7fdf"></a>Creating an application using a blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ae07c7e6c01a74234943808f31b3115d6"><a name="ae07c7e6c01a74234943808f31b3115d6"></a><a name="ae07c7e6c01a74234943808f31b3115d6"></a>app</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a0512e9ff0b9746f9bdf03e8e1b8ffd93"><a name="a0512e9ff0b9746f9bdf03e8e1b8ffd93"></a><a name="a0512e9ff0b9746f9bdf03e8e1b8ffd93"></a>createAppByBlueprint</p>
</td>
</tr>
<tr id="rbcbb0150a78045c7aa9ddf8302d28a4e"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="aadc22efba3a14a2697b3d94b9eeb4cf7"><a name="aadc22efba3a14a2697b3d94b9eeb4cf7"></a><a name="aadc22efba3a14a2697b3d94b9eeb4cf7"></a>Creating a blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a6292c16461e747d1a9246d36d541bf0b"><a name="a6292c16461e747d1a9246d36d541bf0b"></a><a name="a6292c16461e747d1a9246d36d541bf0b"></a>blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a2b8071ed6fda4e6f8603f4da675ee5c2"><a name="a2b8071ed6fda4e6f8603f4da675ee5c2"></a><a name="a2b8071ed6fda4e6f8603f4da675ee5c2"></a>createBlueprint</p>
</td>
</tr>
<tr id="r6e3f616fb954401f88f811bea5df5ea4"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a2ace9e14651744a49b0f7eb21b291114"><a name="a2ace9e14651744a49b0f7eb21b291114"></a><a name="a2ace9e14651744a49b0f7eb21b291114"></a>Deleting a blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ac52778c6fa544a3db3faa4a0022bedec"><a name="ac52778c6fa544a3db3faa4a0022bedec"></a><a name="ac52778c6fa544a3db3faa4a0022bedec"></a>blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a1023a19f47ef4bbf888e99badad228fe"><a name="a1023a19f47ef4bbf888e99badad228fe"></a><a name="a1023a19f47ef4bbf888e99badad228fe"></a>deleteBlueprint</p>
</td>
</tr>
<tr id="r3a2b507f6edb4201a64c922c1e5cc1c9"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="ae52ee699537d49138df9daea08bab2f2"><a name="ae52ee699537d49138df9daea08bab2f2"></a><a name="ae52ee699537d49138df9daea08bab2f2"></a>Updating a blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ac7789888885a4bfe89d7b0c63ac5b920"><a name="ac7789888885a4bfe89d7b0c63ac5b920"></a><a name="ac7789888885a4bfe89d7b0c63ac5b920"></a>blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a5b0e4ccad2494daa8761fcc3a01119b4"><a name="a5b0e4ccad2494daa8761fcc3a01119b4"></a><a name="a5b0e4ccad2494daa8761fcc3a01119b4"></a>updateBlueprint</p>
</td>
</tr>
<tr id="r5cb44f1bc813459f9640599522885204"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a6c39114bd19547b5b1e86300c67ffbf1"><a name="a6c39114bd19547b5b1e86300c67ffbf1"></a><a name="a6c39114bd19547b5b1e86300c67ffbf1"></a>Renaming a blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a8119c40f8985452888832171e4ef8003"><a name="a8119c40f8985452888832171e4ef8003"></a><a name="a8119c40f8985452888832171e4ef8003"></a>blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a5d3b02ee15e84c60955e9b2ad50d9e8a"><a name="a5d3b02ee15e84c60955e9b2ad50d9e8a"></a><a name="a5d3b02ee15e84c60955e9b2ad50d9e8a"></a>renameBlueprint</p>
</td>
</tr>
<tr id="rfcd39de0573d49e1bce820a0db6e514d"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a6177ad581c9f47498c0a6639531d15e8"><a name="a6177ad581c9f47498c0a6639531d15e8"></a><a name="a6177ad581c9f47498c0a6639531d15e8"></a>Validating a blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a0fe873eeaef34458b7da0675805ddaf7"><a name="a0fe873eeaef34458b7da0675805ddaf7"></a><a name="a0fe873eeaef34458b7da0675805ddaf7"></a>blueprint</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a3a23f4dbec0743ce94c15b30566f695e"><a name="a3a23f4dbec0743ce94c15b30566f695e"></a><a name="a3a23f4dbec0743ce94c15b30566f695e"></a>validateBlueprint</p>
</td>
</tr>
<tr id="r07c462a9b44b44b5b8086e921764074a"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a8278444b4b86492b9afbd15a3f0ac4a4"><a name="a8278444b4b86492b9afbd15a3f0ac4a4"></a><a name="a8278444b4b86492b9afbd15a3f0ac4a4"></a>Deleting junk images</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ac8773908e50e4a5fa4de345fd85764b9"><a name="ac8773908e50e4a5fa4de345fd85764b9"></a><a name="ac8773908e50e4a5fa4de345fd85764b9"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ab38598a297d24a32a6daa98485ffd7ea"><a name="ab38598a297d24a32a6daa98485ffd7ea"></a><a name="ab38598a297d24a32a6daa98485ffd7ea"></a>garbageCollectImage</p>
</td>
</tr>
<tr id="r8a07328310414dc99ee8873acf61327f"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a4823be3b9e684221bba326d2c00281e3"><a name="a4823be3b9e684221bba326d2c00281e3"></a><a name="a4823be3b9e684221bba326d2c00281e3"></a>Deleting a specified image</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ac361fd94576a4376b56b3f315682753a"><a name="ac361fd94576a4376b56b3f315682753a"></a><a name="ac361fd94576a4376b56b3f315682753a"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="aa16caf86e471464aa1949cf9af9d03a7"><a name="aa16caf86e471464aa1949cf9af9d03a7"></a><a name="aa16caf86e471464aa1949cf9af9d03a7"></a>deleteImage</p>
</td>
</tr>
<tr id="r162e8c98283f4222b18ec3d9137e89c6"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a695231f29cee41f2b86342a0b324ed6c"><a name="a695231f29cee41f2b86342a0b324ed6c"></a><a name="a695231f29cee41f2b86342a0b324ed6c"></a>Deleting a tag image</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a299807956cc245a5b72fe411896912ee"><a name="a299807956cc245a5b72fe411896912ee"></a><a name="a299807956cc245a5b72fe411896912ee"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ad1be3c1b323d419496c95325343e2d9a"><a name="ad1be3c1b323d419496c95325343e2d9a"></a><a name="ad1be3c1b323d419496c95325343e2d9a"></a>deleteTagImage</p>
</td>
</tr>
<tr id="rff1a53a4df7144c8b86f797669aec906"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a706f93cc61f942cf94f93f2e79867ce7"><a name="a706f93cc61f942cf94f93f2e79867ce7"></a><a name="a706f93cc61f942cf94f93f2e79867ce7"></a>Updating the description of an image</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a53b573800c92457290cd50981aa41d9f"><a name="a53b573800c92457290cd50981aa41d9f"></a><a name="a53b573800c92457290cd50981aa41d9f"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="afe5b9fdd624043869d15e5191396c1ef"><a name="afe5b9fdd624043869d15e5191396c1ef"></a><a name="afe5b9fdd624043869d15e5191396c1ef"></a>updateImageDesc</p>
</td>
</tr>
<tr id="r5e85d638b0d64719bb68ff2086b0ed3a"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a39d12bb11e66430d8f320d2db2bc2a82"><a name="a39d12bb11e66430d8f320d2db2bc2a82"></a><a name="a39d12bb11e66430d8f320d2db2bc2a82"></a>Creating a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="aeb5e3bd8f61642269bbf2d84f84ed0f8"><a name="aeb5e3bd8f61642269bbf2d84f84ed0f8"></a><a name="aeb5e3bd8f61642269bbf2d84f84ed0f8"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a8864644a5cb44c2fa8632d6feb2b27f6"><a name="a8864644a5cb44c2fa8632d6feb2b27f6"></a><a name="a8864644a5cb44c2fa8632d6feb2b27f6"></a>createPolicy</p>
</td>
</tr>
<tr id="r7aeb0ed41c034858b8ccfa751f98cbad"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="af0a41265a29547ea837069f2d8ec8303"><a name="af0a41265a29547ea837069f2d8ec8303"></a><a name="af0a41265a29547ea837069f2d8ec8303"></a>Updating a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a535b2744054e4754bdf2a36c60a42717"><a name="a535b2744054e4754bdf2a36c60a42717"></a><a name="a535b2744054e4754bdf2a36c60a42717"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a1c008d8ba536447fa9bf5195a8101d9c"><a name="a1c008d8ba536447fa9bf5195a8101d9c"></a><a name="a1c008d8ba536447fa9bf5195a8101d9c"></a>updatePolicy</p>
</td>
</tr>
<tr id="r373569f690f54c9db4d84d42762d4b33"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="ab003b63f3a43405e86abdea95191332f"><a name="ab003b63f3a43405e86abdea95191332f"></a><a name="ab003b63f3a43405e86abdea95191332f"></a>Deleting a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a15aba748a6564446851c606cd57ff992"><a name="a15aba748a6564446851c606cd57ff992"></a><a name="a15aba748a6564446851c606cd57ff992"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a2a32bd19f18f4dc4b328ccc174747068"><a name="a2a32bd19f18f4dc4b328ccc174747068"></a><a name="a2a32bd19f18f4dc4b328ccc174747068"></a>deletePolicy</p>
</td>
</tr>
<tr id="rcd4b65cfe14948f789f2a24f889c198e"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a15b7a5d91a9846e9bf27c9c981923e11"><a name="a15b7a5d91a9846e9bf27c9c981923e11"></a><a name="a15b7a5d91a9846e9bf27c9c981923e11"></a>Enabling a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a84460a9cc90c4e378e4f56af457dc58f"><a name="a84460a9cc90c4e378e4f56af457dc58f"></a><a name="a84460a9cc90c4e378e4f56af457dc58f"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ab02713236ad34695a01a0b9f2c6844e5"><a name="ab02713236ad34695a01a0b9f2c6844e5"></a><a name="ab02713236ad34695a01a0b9f2c6844e5"></a>enablePolicy</p>
</td>
</tr>
<tr id="ra50b9b321c0f4df280eaccde8a15e080"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="aef89117d9f2b400e8cd40aca03f5d4a1"><a name="aef89117d9f2b400e8cd40aca03f5d4a1"></a><a name="aef89117d9f2b400e8cd40aca03f5d4a1"></a>Disabling a policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240378_p443309917471"><a name="en-us_topic_0100240378_p443309917471"></a><a name="en-us_topic_0100240378_p443309917471"></a>policy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ad077c31699634598ba16e37520b1391f"><a name="ad077c31699634598ba16e37520b1391f"></a><a name="ad077c31699634598ba16e37520b1391f"></a>disablePolicy</p>
</td>
</tr>
<tr id="rdfd61a36e06944859271bb8d8e3b540a"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="adc7aecd9ff6944ebb2a7d5ab5577f07d"><a name="adc7aecd9ff6944ebb2a7d5ab5577f07d"></a><a name="adc7aecd9ff6944ebb2a7d5ab5577f07d"></a>Creating a periodic or scheduled scaling policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="aff378c7f8d0247be872ac812530d04a0"><a name="aff378c7f8d0247be872ac812530d04a0"></a><a name="aff378c7f8d0247be872ac812530d04a0"></a>scaling_policy_cce</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ab40eec9ad0364ae59a847da519bab4dd"><a name="ab40eec9ad0364ae59a847da519bab4dd"></a><a name="ab40eec9ad0364ae59a847da519bab4dd"></a>createScalingPolicy</p>
</td>
</tr>
<tr id="r6d9a87d3e9d84d1a8ab9dda1d359502e"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="acd7e32710ffa430794df553948d40e6f"><a name="acd7e32710ffa430794df553948d40e6f"></a><a name="acd7e32710ffa430794df553948d40e6f"></a>Deleting a periodic or scheduled scaling policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a79ac94c510174dea96807c843f65199e"><a name="a79ac94c510174dea96807c843f65199e"></a><a name="a79ac94c510174dea96807c843f65199e"></a>scaling_policy_cce</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a06e10cb583ff4b97afb981702329e1d6"><a name="a06e10cb583ff4b97afb981702329e1d6"></a><a name="a06e10cb583ff4b97afb981702329e1d6"></a>deleteScalingPolicy</p>
</td>
</tr>
<tr id="row262067079446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p6289938594550"><a name="p6289938594550"></a><a name="p6289938594550"></a>Creating a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4328910994614"><a name="p4328910994614"></a><a name="p4328910994614"></a>clusters</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p704508994631"><a name="p704508994631"></a><a name="p704508994631"></a>createCluster</p>
</td>
</tr>
<tr id="row379349999446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1829780594550"><a name="p1829780594550"></a><a name="p1829780594550"></a>Updating a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1659463394614"><a name="p1659463394614"></a><a name="p1659463394614"></a>clusters</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3559644694631"><a name="p3559644694631"></a><a name="p3559644694631"></a>updateCluster</p>
</td>
</tr>
<tr id="row84346359446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5154478594550"><a name="p5154478594550"></a><a name="p5154478594550"></a>Deleting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1789194994614"><a name="p1789194994614"></a><a name="p1789194994614"></a>clusters</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p4578780294631"><a name="p4578780294631"></a><a name="p4578780294631"></a>deleteCluster</p>
</td>
</tr>
<tr id="row227509529446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p6229388294550"><a name="p6229388294550"></a><a name="p6229388294550"></a>Creating a node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2411179894614"><a name="p2411179894614"></a><a name="p2411179894614"></a>clusters-nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2620245694631"><a name="p2620245694631"></a><a name="p2620245694631"></a>createNode</p>
</td>
</tr>
<tr id="row303075359446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4664845094550"><a name="p4664845094550"></a><a name="p4664845094550"></a>Adding a static node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p6208777494614"><a name="p6208777494614"></a><a name="p6208777494614"></a>clusters-nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p4267337994631"><a name="p4267337994631"></a><a name="p4267337994631"></a>addStaticNode</p>
</td>
</tr>
<tr id="row132155299446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4963543694550"><a name="p4963543694550"></a><a name="p4963543694550"></a>Updating a node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3061348094614"><a name="p3061348094614"></a><a name="p3061348094614"></a>clusters-nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3748980794631"><a name="p3748980794631"></a><a name="p3748980794631"></a>updateNode</p>
</td>
</tr>
<tr id="row603918479446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1255584494550"><a name="p1255584494550"></a><a name="p1255584494550"></a>Deleting a host</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3708476894614"><a name="p3708476894614"></a><a name="p3708476894614"></a>clusters-nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1676178194631"><a name="p1676178194631"></a><a name="p1676178194631"></a>deleteOneHost</p>
</td>
</tr>
<tr id="row562156189446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2640495594550"><a name="p2640495594550"></a><a name="p2640495594550"></a>Deleting all hosts</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5703272794614"><a name="p5703272794614"></a><a name="p5703272794614"></a>clusters-nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p552562694631"><a name="p552562694631"></a><a name="p552562694631"></a>deleteAllHosts</p>
</td>
</tr>
<tr id="row456723169446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5607758294550"><a name="p5607758294550"></a><a name="p5607758294550"></a>Suspending user resources</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3647165894614"><a name="p3647165894614"></a><a name="p3647165894614"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p164980094631"><a name="p164980094631"></a><a name="p164980094631"></a>suspendUserResource</p>
</td>
</tr>
<tr id="row444699179446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1125926294550"><a name="p1125926294550"></a><a name="p1125926294550"></a>Creating a ConfigMap</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1272869894614"><a name="p1272869894614"></a><a name="p1272869894614"></a>configmaps</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p6185365094631"><a name="p6185365094631"></a><a name="p6185365094631"></a>createConfigmaps</p>
</td>
</tr>
<tr id="row434042779446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2072124094550"><a name="p2072124094550"></a><a name="p2072124094550"></a>Creating a DaemonSet</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1819826094614"><a name="p1819826094614"></a><a name="p1819826094614"></a>daemonsets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p6126318794631"><a name="p6126318794631"></a><a name="p6126318794631"></a>createDaemonsets</p>
</td>
</tr>
<tr id="row495275839446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p629006294550"><a name="p629006294550"></a><a name="p629006294550"></a>Creating a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4608583494614"><a name="p4608583494614"></a><a name="p4608583494614"></a>deployments</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3346887894631"><a name="p3346887894631"></a><a name="p3346887894631"></a>createDeployments</p>
</td>
</tr>
<tr id="row61822039446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2205289194550"><a name="p2205289194550"></a><a name="p2205289194550"></a>Creating an event</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4214143194614"><a name="p4214143194614"></a><a name="p4214143194614"></a>events</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3829467094631"><a name="p3829467094631"></a><a name="p3829467094631"></a>createEvents</p>
</td>
</tr>
<tr id="row565870589446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3753952294550"><a name="p3753952294550"></a><a name="p3753952294550"></a>Creating an ingress</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5235283094614"><a name="p5235283094614"></a><a name="p5235283094614"></a>ingress</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p6663632794631"><a name="p6663632794631"></a><a name="p6663632794631"></a>createIngresses</p>
</td>
</tr>
<tr id="row449295269446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5300449594550"><a name="p5300449594550"></a><a name="p5300449594550"></a>Creating a job</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4737892394614"><a name="p4737892394614"></a><a name="p4737892394614"></a>jobs</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5817374694631"><a name="p5817374694631"></a><a name="p5817374694631"></a>createJobs</p>
</td>
</tr>
<tr id="row474748789446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5268014794550"><a name="p5268014794550"></a><a name="p5268014794550"></a>Creating a namespace</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4527886394614"><a name="p4527886394614"></a><a name="p4527886394614"></a>namespaces</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p6296808494631"><a name="p6296808494631"></a><a name="p6296808494631"></a>createNamespaces</p>
</td>
</tr>
<tr id="row567463179446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1755735594550"><a name="p1755735594550"></a><a name="p1755735594550"></a>Creating a node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5783930394614"><a name="p5783930394614"></a><a name="p5783930394614"></a>nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p127045594631"><a name="p127045594631"></a><a name="p127045594631"></a>createNodes</p>
</td>
</tr>
<tr id="row443356589446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4862770494550"><a name="p4862770494550"></a><a name="p4862770494550"></a>Creating a PersistentVolumeClaim</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2048536494614"><a name="p2048536494614"></a><a name="p2048536494614"></a>persistentvolumeclaims</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5374650994631"><a name="p5374650994631"></a><a name="p5374650994631"></a>createPersistentvolumeclaims</p>
</td>
</tr>
<tr id="row288591129446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1611658394550"><a name="p1611658394550"></a><a name="p1611658394550"></a>Creating a pod</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3566310794614"><a name="p3566310794614"></a><a name="p3566310794614"></a>pods</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5673806894631"><a name="p5673806894631"></a><a name="p5673806894631"></a>createPods</p>
</td>
</tr>
<tr id="row34084799446"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p493821894550"><a name="p493821894550"></a><a name="p493821894550"></a>Creating a replica set</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2727504694614"><a name="p2727504694614"></a><a name="p2727504694614"></a>replicasets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2299137294631"><a name="p2299137294631"></a><a name="p2299137294631"></a>createReplicasets</p>
</td>
</tr>
<tr id="row337031779455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4319148494550"><a name="p4319148494550"></a><a name="p4319148494550"></a>Creating a resource quota</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1928514494614"><a name="p1928514494614"></a><a name="p1928514494614"></a>resourcequotas</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5060320194631"><a name="p5060320194631"></a><a name="p5060320194631"></a>createResourcequotas</p>
</td>
</tr>
<tr id="row329082439455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1253500894550"><a name="p1253500894550"></a><a name="p1253500894550"></a>Creating a key</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3311778894614"><a name="p3311778894614"></a><a name="p3311778894614"></a>secrets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p4696755894631"><a name="p4696755894631"></a><a name="p4696755894631"></a>createSecrets</p>
</td>
</tr>
<tr id="row597121439455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1121584294550"><a name="p1121584294550"></a><a name="p1121584294550"></a>Creating a service</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5078579094614"><a name="p5078579094614"></a><a name="p5078579094614"></a>services</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1382981594631"><a name="p1382981594631"></a><a name="p1382981594631"></a>createServices</p>
</td>
</tr>
<tr id="row275256709455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5617627594550"><a name="p5617627594550"></a><a name="p5617627594550"></a>Creating a StatefulSet</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4585684794614"><a name="p4585684794614"></a><a name="p4585684794614"></a>statefulsets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1560587894631"><a name="p1560587894631"></a><a name="p1560587894631"></a>createStatefulsets</p>
</td>
</tr>
<tr id="row483593069455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1609774394550"><a name="p1609774394550"></a><a name="p1609774394550"></a>Creating a volume</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p942749994614"><a name="p942749994614"></a><a name="p942749994614"></a>volumes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3528714994631"><a name="p3528714994631"></a><a name="p3528714994631"></a>createVolumes</p>
</td>
</tr>
<tr id="row533754749455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5831301894550"><a name="p5831301894550"></a><a name="p5831301894550"></a>Deleting a ConfigMap</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2754335094614"><a name="p2754335094614"></a><a name="p2754335094614"></a>configmaps</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2163739394631"><a name="p2163739394631"></a><a name="p2163739394631"></a>deleteConfigmaps</p>
</td>
</tr>
<tr id="row649264979455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3027967894550"><a name="p3027967894550"></a><a name="p3027967894550"></a>Deleting a DaemonSet</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1355228294614"><a name="p1355228294614"></a><a name="p1355228294614"></a>daemonsets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p307708494631"><a name="p307708494631"></a><a name="p307708494631"></a>deleteDaemonsets</p>
</td>
</tr>
<tr id="row387711029455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p6217819094550"><a name="p6217819094550"></a><a name="p6217819094550"></a>Deleting a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1461089094614"><a name="p1461089094614"></a><a name="p1461089094614"></a>deployments</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2860238694631"><a name="p2860238694631"></a><a name="p2860238694631"></a>deleteDeployments</p>
</td>
</tr>
<tr id="row186687969455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2941757394550"><a name="p2941757394550"></a><a name="p2941757394550"></a>Deleting an event</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4813856194614"><a name="p4813856194614"></a><a name="p4813856194614"></a>events</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p4739161294631"><a name="p4739161294631"></a><a name="p4739161294631"></a>deleteEvents</p>
</td>
</tr>
<tr id="row6133026394522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3768339894550"><a name="p3768339894550"></a><a name="p3768339894550"></a>Deleting an ingress</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p6218425894614"><a name="p6218425894614"></a><a name="p6218425894614"></a>ingresses</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5452932694631"><a name="p5452932694631"></a><a name="p5452932694631"></a>deleteIngresses</p>
</td>
</tr>
<tr id="row499044494522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2367218894550"><a name="p2367218894550"></a><a name="p2367218894550"></a>Deleting a job</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3384130494614"><a name="p3384130494614"></a><a name="p3384130494614"></a>jobs</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2343174894631"><a name="p2343174894631"></a><a name="p2343174894631"></a>deleteJobs</p>
</td>
</tr>
<tr id="row4804008694522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1004764394550"><a name="p1004764394550"></a><a name="p1004764394550"></a>Deleting a namespace</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4135816794614"><a name="p4135816794614"></a><a name="p4135816794614"></a>namespaces</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3609308894631"><a name="p3609308894631"></a><a name="p3609308894631"></a>deleteNamespaces</p>
</td>
</tr>
<tr id="row111861594522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p986578894550"><a name="p986578894550"></a><a name="p986578894550"></a>Deleting a node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1822402494614"><a name="p1822402494614"></a><a name="p1822402494614"></a>nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p518647694631"><a name="p518647694631"></a><a name="p518647694631"></a>deleteNodes</p>
</td>
</tr>
<tr id="row4280933494522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1151162094550"><a name="p1151162094550"></a><a name="p1151162094550"></a>Deleting a pod</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p6486790494614"><a name="p6486790494614"></a><a name="p6486790494614"></a>pods</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2284521394631"><a name="p2284521394631"></a><a name="p2284521394631"></a>deletePods</p>
</td>
</tr>
<tr id="row1958701494522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p336335794550"><a name="p336335794550"></a><a name="p336335794550"></a>Deleting a replica set</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4406213794614"><a name="p4406213794614"></a><a name="p4406213794614"></a>replicasets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1116254194631"><a name="p1116254194631"></a><a name="p1116254194631"></a>deleteReplicasets</p>
</td>
</tr>
<tr id="row5445846394522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3596837894550"><a name="p3596837894550"></a><a name="p3596837894550"></a>Deleting a resource quota</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4326111094614"><a name="p4326111094614"></a><a name="p4326111094614"></a>resourcequotas</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1732041594631"><a name="p1732041594631"></a><a name="p1732041594631"></a>deleteResourcequotas</p>
</td>
</tr>
<tr id="row971485094522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4849077494550"><a name="p4849077494550"></a><a name="p4849077494550"></a>Deleting a secret</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p6329214694614"><a name="p6329214694614"></a><a name="p6329214694614"></a>secrets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1011679994631"><a name="p1011679994631"></a><a name="p1011679994631"></a>deleteSecrets</p>
</td>
</tr>
<tr id="row2982840894522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5051198894550"><a name="p5051198894550"></a><a name="p5051198894550"></a>Deleting a service</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3618507294614"><a name="p3618507294614"></a><a name="p3618507294614"></a>services</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p6028047894631"><a name="p6028047894631"></a><a name="p6028047894631"></a>deleteServices</p>
</td>
</tr>
<tr id="row1589985994522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4758211194550"><a name="p4758211194550"></a><a name="p4758211194550"></a>Deleting a StatefulSet</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p513426794614"><a name="p513426794614"></a><a name="p513426794614"></a>statefulsets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5527189794631"><a name="p5527189794631"></a><a name="p5527189794631"></a>deleteStatefulsets</p>
</td>
</tr>
<tr id="row5459313094522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5918564394550"><a name="p5918564394550"></a><a name="p5918564394550"></a>Deleting a volume</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5189367194614"><a name="p5189367194614"></a><a name="p5189367194614"></a>volumes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2789467394631"><a name="p2789467394631"></a><a name="p2789467394631"></a>deleteVolumes</p>
</td>
</tr>
<tr id="row194291194522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p6244318594550"><a name="p6244318594550"></a><a name="p6244318594550"></a>Replacing a specified ConfigMap</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4819585394614"><a name="p4819585394614"></a><a name="p4819585394614"></a>configmaps</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p123147594631"><a name="p123147594631"></a><a name="p123147594631"></a>updateConfigmaps</p>
</td>
</tr>
<tr id="row2614690894522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2127259894550"><a name="p2127259894550"></a><a name="p2127259894550"></a>Replacing a specified DaemonSet</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3684149094614"><a name="p3684149094614"></a><a name="p3684149094614"></a>daemonsets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2533054594631"><a name="p2533054594631"></a><a name="p2533054594631"></a>updateDaemonsets</p>
</td>
</tr>
<tr id="row4738772994522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p557664494550"><a name="p557664494550"></a><a name="p557664494550"></a>Replacing a specified deployment</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1390089694614"><a name="p1390089694614"></a><a name="p1390089694614"></a>deployments</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1103015094631"><a name="p1103015094631"></a><a name="p1103015094631"></a>updateDeployments</p>
</td>
</tr>
<tr id="row6367333594522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3884177494550"><a name="p3884177494550"></a><a name="p3884177494550"></a>Replacing a specified event</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p31485894614"><a name="p31485894614"></a><a name="p31485894614"></a>events</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5502501394631"><a name="p5502501394631"></a><a name="p5502501394631"></a>updateEvents</p>
</td>
</tr>
<tr id="row5447051194522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p6282158394550"><a name="p6282158394550"></a><a name="p6282158394550"></a>Replacing a specified ingress</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2820497194614"><a name="p2820497194614"></a><a name="p2820497194614"></a>ingresses</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p4924327494631"><a name="p4924327494631"></a><a name="p4924327494631"></a>updateIngresses</p>
</td>
</tr>
<tr id="row4321040294522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2868887494550"><a name="p2868887494550"></a><a name="p2868887494550"></a>Replacing a specified job</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2611159094614"><a name="p2611159094614"></a><a name="p2611159094614"></a>jobs</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p6221346294631"><a name="p6221346294631"></a><a name="p6221346294631"></a>updateJobs</p>
</td>
</tr>
<tr id="row5881996994522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4333268294550"><a name="p4333268294550"></a><a name="p4333268294550"></a>Replacing a specified namespace</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4354083894614"><a name="p4354083894614"></a><a name="p4354083894614"></a>namespaces</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5513099894631"><a name="p5513099894631"></a><a name="p5513099894631"></a>updateNamespaces</p>
</td>
</tr>
<tr id="row935789494522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4835955594550"><a name="p4835955594550"></a><a name="p4835955594550"></a>Replacing a specified node</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p6588755194614"><a name="p6588755194614"></a><a name="p6588755194614"></a>nodes</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5939693994631"><a name="p5939693994631"></a><a name="p5939693994631"></a>updateNodes</p>
</td>
</tr>
<tr id="row3084433694522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2196203094550"><a name="p2196203094550"></a><a name="p2196203094550"></a>Replacing a specified PersistentVolumeClaim</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4918695494614"><a name="p4918695494614"></a><a name="p4918695494614"></a>persistentvolumeclaims</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1515181094631"><a name="p1515181094631"></a><a name="p1515181094631"></a>updatePersistentvolumeclaims</p>
</td>
</tr>
<tr id="row243642694522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3841067294550"><a name="p3841067294550"></a><a name="p3841067294550"></a>Replacing a specified pod</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2115652494614"><a name="p2115652494614"></a><a name="p2115652494614"></a>pods</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3981620594631"><a name="p3981620594631"></a><a name="p3981620594631"></a>updatePods</p>
</td>
</tr>
<tr id="row928758794522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1698379594550"><a name="p1698379594550"></a><a name="p1698379594550"></a>Replacing a specified replica set</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5517633594614"><a name="p5517633594614"></a><a name="p5517633594614"></a>replicasets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3498455194631"><a name="p3498455194631"></a><a name="p3498455194631"></a>updateReplicasets</p>
</td>
</tr>
<tr id="row6288859894522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3315562594550"><a name="p3315562594550"></a><a name="p3315562594550"></a>Replacing a specified resource quota</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2533872594614"><a name="p2533872594614"></a><a name="p2533872594614"></a>resourcequotas</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p236974794631"><a name="p236974794631"></a><a name="p236974794631"></a>updateResourcequotas</p>
</td>
</tr>
<tr id="row753958794522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1126030494550"><a name="p1126030494550"></a><a name="p1126030494550"></a>Replacing a specified secret</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1699364494614"><a name="p1699364494614"></a><a name="p1699364494614"></a>secrets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p4982447794631"><a name="p4982447794631"></a><a name="p4982447794631"></a>updateSecrets</p>
</td>
</tr>
<tr id="row4225064394522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2148023294550"><a name="p2148023294550"></a><a name="p2148023294550"></a>Replacing a specified service</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p4033552494614"><a name="p4033552494614"></a><a name="p4033552494614"></a>services</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1614831094631"><a name="p1614831094631"></a><a name="p1614831094631"></a>updateServices</p>
</td>
</tr>
<tr id="row1408869694522"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2272396594550"><a name="p2272396594550"></a><a name="p2272396594550"></a>Replacing a specified StatefulSet</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1091471394614"><a name="p1091471394614"></a><a name="p1091471394614"></a>statefulsets</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p2806709894631"><a name="p2806709894631"></a><a name="p2806709894631"></a>updateStatefulsets</p>
</td>
</tr>
<tr id="row298834119455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p5699030694550"><a name="p5699030694550"></a><a name="p5699030694550"></a>Replacing the specified status</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3798019094614"><a name="p3798019094614"></a><a name="p3798019094614"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5982049394631"><a name="p5982049394631"></a><a name="p5982049394631"></a>updateStatus</p>
</td>
</tr>
<tr id="row205366449455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p554693194550"><a name="p554693194550"></a><a name="p554693194550"></a>Uploading a chart</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3870721594614"><a name="p3870721594614"></a><a name="p3870721594614"></a>uploadchart</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5548712994631"><a name="p5548712994631"></a><a name="p5548712994631"></a>uploadChart</p>
</td>
</tr>
<tr id="row43337529455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1718120294550"><a name="p1718120294550"></a><a name="p1718120294550"></a>Updating a chart</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3183719894614"><a name="p3183719894614"></a><a name="p3183719894614"></a>charts</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5058123394631"><a name="p5058123394631"></a><a name="p5058123394631"></a>updateChart</p>
</td>
</tr>
<tr id="row381226569455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4284765794550"><a name="p4284765794550"></a><a name="p4284765794550"></a>Deleting a chart</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5675936594614"><a name="p5675936594614"></a><a name="p5675936594614"></a>charts</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3095278494631"><a name="p3095278494631"></a><a name="p3095278494631"></a>deleteChart</p>
</td>
</tr>
<tr id="row98783909455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p3032087794550"><a name="p3032087794550"></a><a name="p3032087794550"></a>Creating a template application</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p3851754594614"><a name="p3851754594614"></a><a name="p3851754594614"></a>releases</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1600152994631"><a name="p1600152994631"></a><a name="p1600152994631"></a>createRelease</p>
</td>
</tr>
<tr id="row500255299455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p2510370494550"><a name="p2510370494550"></a><a name="p2510370494550"></a>Updating a template application</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p2778578094614"><a name="p2778578094614"></a><a name="p2778578094614"></a>releases</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p5528159194631"><a name="p5528159194631"></a><a name="p5528159194631"></a>updateRelease</p>
</td>
</tr>
<tr id="row58543889455"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p4698987094550"><a name="p4698987094550"></a><a name="p4698987094550"></a>Deleting a template application</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p5606621894614"><a name="p5606621894614"></a><a name="p5606621894614"></a>releases</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p3496207894631"><a name="p3496207894631"></a><a name="p3496207894631"></a>deleteRelease</p>
</td>
</tr>
</tbody>
</table>

