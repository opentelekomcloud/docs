# Creating a Secret<a name="cce_01_0153"></a>

A  secret  is a type of resource that holds sensitive data, such as authentication and key information. All content is user-defined. After creating secrets, you can use them as files or environment variables in a containerized workload.

## Prerequisites<a name="section19209149103913"></a>

Cluster and node resources have been created. For more information, see  [Creating a VM Cluster](creating-a-vm-cluster.md). If you have available clusters and node resources, skip this operation.

## Creating a Secret<a name="section18512531861"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Configuration Center**  \>  **Secrets**. Click  **Create Secret**.
2.  You can create a secret directly or based on YAML. If you want to create a ConfigMap based on YAML, go to  [4](#li69121840101813).
3.  Method 1: Create a secret directly.

    Set the basic information by referring to  [Table 1](#table16321825732).

    **Table  1**  Parameters for creating a secret

    <a name="table16321825732"></a>
    <table><thead align="left"><tr id="row173212251235"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p43211725338"><a name="p43211725338"></a><a name="p43211725338"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p0322102516320"><a name="p0322102516320"></a><a name="p0322102516320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1752613417216"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p360313397217"><a name="p360313397217"></a><a name="p360313397217"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p1161911390211"><a name="p1161911390211"></a><a name="p1161911390211"></a>Name of the secret you create, which must be unique.</p>
    </td>
    </tr>
    <tr id="row6334727910"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p233592498"><a name="p233592498"></a><a name="p233592498"></a>Cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p2020234461913"><a name="p2020234461913"></a><a name="p2020234461913"></a><span class="keyword" id="keyword2023595853141921"><a name="keyword2023595853141921"></a><a name="keyword2023595853141921"></a>Cluster</span> that will use the secret you create.</p>
    </td>
    </tr>
    <tr id="row11291645181017"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p16293114519103"><a name="p16293114519103"></a><a name="p16293114519103"></a>Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p129384511101"><a name="p129384511101"></a><a name="p129384511101"></a>Namespace to which the configuration item belongs. If you do not specify this parameter, the value <strong id="b810496371104144"><a name="b810496371104144"></a><a name="b810496371104144"></a>default</strong> is used by default.</p>
    </td>
    </tr>
    <tr id="row1984015472115"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p815351112212"><a name="p815351112212"></a><a name="p815351112212"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p5153121142219"><a name="p5153121142219"></a><a name="p5153121142219"></a>Description of a secret.</p>
    </td>
    </tr>
    <tr id="row1541115718414"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p14412774420"><a name="p14412774420"></a><a name="p14412774420"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p1441319714414"><a name="p1441319714414"></a><a name="p1441319714414"></a>Type of the secret you create.</p>
    <a name="ul4570185817249"></a><a name="ul4570185817249"></a><ul id="ul4570185817249"><li><span class="keyword" id="keyword30498699141939"><a name="keyword30498699141939"></a><a name="keyword30498699141939"></a>Opaque</span>: common secret.</li><li><span class="keyword" id="keyword980727399141941"><a name="keyword980727399141941"></a><a name="keyword980727399141941"></a>kubernetes.io/dockerconfigjson</span>: a secret that stores the authentication information required for pulling images from a private repository.</li><li><span class="keyword" id="keyword580479947141945"><a name="keyword580479947141945"></a><a name="keyword580479947141945"></a>IngressTLS</span>: a secret that stores the certificate required by ingress services (layer-7 load balancing services).</li><li>Other: Another type of secret, which is specified manually.</li></ul>
    </td>
    </tr>
    <tr id="row133224252315"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p23228259314"><a name="p23228259314"></a><a name="p23228259314"></a>Secret Data</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p133223251335"><a name="p133223251335"></a><a name="p133223251335"></a>Workload secret data can be used in containers.</p>
    <a name="ul180611337469"></a><a name="ul180611337469"></a><ul id="ul180611337469"><li>If the secret is of the Opaque type:<a name="ol10322425232"></a><a name="ol10322425232"></a><ol id="ol10322425232"><li>Click <strong id="b33521139104319"><a name="b33521139104319"></a><a name="b33521139104319"></a>Add Data</strong>.</li><li>Enter the key and value. The value must be based on the Base64 coding method. For details about the method, see <a href="#section175000605919">Base64 Encoding</a>.</li></ol>
    </li><li>If the secret type is <span class="keyword" id="keyword9993330195113"><a name="keyword9993330195113"></a><a name="keyword9993330195113"></a>kubernetes.io/</span>dockerconfigjson, enter the account and password of the private image repository.</li><li>If the secret type is IngressTLS, upload the certificate file and private key file.<div class="note" id="note1890215211325"><a name="note1890215211325"></a><a name="note1890215211325"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1280017919332"></a><a name="ul1280017919332"></a><ul id="ul1280017919332"><li>A certificate is a self-signed or CA-signed credential used for identity authentication.</li><li>A certificate request is a request for a signature with a private key.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row123142814330"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p17322225134"><a name="p17322225134"></a><a name="p17322225134"></a>Secret Label</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p1932211253312"><a name="p1932211253312"></a><a name="p1932211253312"></a>Labels are attached to objects such as workloads, nodes, and services in key-value pairs.</p>
    <p id="p1932220252316"><a name="p1932220252316"></a><a name="p1932220252316"></a>Labels define the identifiable attributes of these objects and are used to manage and select the objects.</p>
    <a name="ol11394016509"></a><a name="ol11394016509"></a><ol id="ol11394016509"><li>Click <strong id="b564414540104435"><a name="b564414540104435"></a><a name="b564414540104435"></a>Add Label</strong>.</li><li>Enter the key and value.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

4.  <a name="li69121840101813"></a>Method 2: Create a secret based on the YAML file.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To create a resource by uploading a file, ensure that the resource description file has been created. CCE supports files in JSON or YAML format. For more information, see  [Secret Resource File Configuration](#section187197531454).  

    Click  **Create** **YAML**  on the right of the page.

    -   Method 1: Import the orchestration file.

        Click  **Add File**  to import the file in YAML or JSON format. The orchestration content can be directly displayed.

    -   Method 2: Directly orchestrate the content.

        In the orchestration content area, enter the content of the YAML or JSON file.

5.  After the configuration is complete, click  **Create**.

    The new secret is displayed in the key list.


## Secret Resource File Configuration<a name="section187197531454"></a>

This section describes configuration examples of secret resource description files.

For example, you can retrieve the username and password for a workload through a secret.

-   YAML format

    The  **secret.yaml**  file is defined as shown below. The value must be based on the Base64 coding method. For details about the method, see  [Base64 Encoding](#section175000605919).

    ```
    apiVersion: v1
    kind: Secret
    metadata:
      name: mysecret           #Secret name
      namespace: default       #Namespace. The default value is default.
    data:
      username: my-username  #Username
      password: ******  #The value must be encoded using Base64.
    type: Opaque     #You are advised not to change this parameter value.
    ```

-   JSON format

    The  **secret.json**  file is defined as shown in the following content.

    ```
    {
      "apiVersion": "v1",
      "kind": "Secret",
      "metadata": {
        "name": "mysecret",
        "namespace": "default"
      },
      "data": {
        "username": "my-username",
        "password": "******"
      },
      "type": "Opaque"
    }
    ```


## Creating a Secret Using kubectl<a name="section821112149514"></a>

1.  According to  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md), configure the  **kubectl**  command to connect an ECS to the cluster.
2.  Create and edit the  **cce-secrets.yaml**  file based on the Base64 encoding method.

    ```
    # echo -n "content to be encoded" | base64
    ******
    ```

    **vi cce-secret.yaml**

    ```
    apiVersion: v1
    kind: Secret
    metadata:
      name: mysecret
    type: Opaque
    data:
      username: admin
      password: ******
    ```

3.  Create a secret.

    **kubectl create -f cce-secret.yaml**

    You can query the secret after creation.

    **kubectl get secret**


## Related Operations<a name="section359413445405"></a>

After creating a configuration item, you can update or delete it as described in  [Table 2](#table555785274319).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The secret list contains system secret resources that can be queried only. The system secret resources cannot be updated or deleted.  

**Table  2**  Related Operations

<a name="table555785274319"></a>
<table><thead align="left"><tr id="row19412155014112"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="p154122501516"><a name="p154122501516"></a><a name="p154122501516"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="p94129501313"><a name="p94129501313"></a><a name="p94129501313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row155037195247"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p163331851201"><a name="p163331851201"></a><a name="p163331851201"></a>Viewing a YAML file</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1633314512016"><a name="p1633314512016"></a><a name="p1633314512016"></a>Click <strong id="b84235270611425"><a name="b84235270611425"></a><a name="b84235270611425"></a>View YAML</strong> next to the secret name to view the YAML file corresponding to the current secret.</p>
</td>
</tr>
<tr id="row8412185010116"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p1541213501611"><a name="p1541213501611"></a><a name="p1541213501611"></a>Updating a secret</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><a name="ol1341225020114"></a><a name="ol1341225020114"></a><ol id="ol1341225020114"><li>Select the name of the secret to be updated and click <strong id="b842352706114220"><a name="b842352706114220"></a><a name="b842352706114220"></a>Update</strong>.</li><li>Modify the secret data. For more information, see <a href="#table16321825732">Table 1</a>.</li><li>Click <strong id="b8227911204520"><a name="b8227911204520"></a><a name="b8227911204520"></a>Update</strong>.</li></ol>
</td>
</tr>
<tr id="row1541219508112"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p141245010120"><a name="p141245010120"></a><a name="p141245010120"></a>Deleting a secret</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p241218502119"><a name="p241218502119"></a><a name="p241218502119"></a>Select the secret you want to delete and click <strong id="b84235270613133"><a name="b84235270613133"></a><a name="b84235270613133"></a>Delete</strong>.</p>
<p id="p18412195016114"><a name="p18412195016114"></a><a name="p18412195016114"></a>Follow the prompts to delete the secret.</p>
</td>
</tr>
<tr id="row24121750518"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p841215015117"><a name="p841215015117"></a><a name="p841215015117"></a>Deleting secrets in batches</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><a name="ol8412145016116"></a><a name="ol8412145016116"></a><ol id="ol8412145016116"><li>Select the secrets to be deleted.</li><li>Click <strong id="b786415800104925"><a name="b786415800104925"></a><a name="b786415800104925"></a>Delete</strong> above the secret list.</li><li>Follow the prompts to delete the secrets.</li></ol>
</td>
</tr>
</tbody>
</table>

## Base64 Encoding<a name="section175000605919"></a>

To encrypt a character string using Base64, run the  **echo -n  _to-be-encoded content_  | base64**  command. The following is an example.

```
root@ubuntu:~# echo -n "content to be encoded" | base64
******
```

