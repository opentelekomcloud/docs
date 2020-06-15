# Patch Request Method Operation Description<a name="cce_02_0085"></a>

Kubernetes APIs use the HTTP header "Content-Type" to distinguish between patch request method operations.

## Operation Description<a name="s8aafd6c4a7764494b1ed22d2e4a178bf"></a>

Currently, three types of patch request method operations are supported:

1.  **JSON Patch, Content-Type: application/json-patch+json**

    According to RFC 6902, JSON patch operations indicate a series of operations performed on resource objects. The following provides an example of the JSON patch operation:

    ```
    { 
         "op": "add", 
         "path": "/spec/containers/0/image", 
         "value": "busybox:latest" 
     }
    ```

    In the preceding example:

    -   "op" indicates a series of operations performed on resource objects, and it contains the following operations:

        add

        replace

        remove \(not supported\)

        move \(not supported\)

        copy \(not supported\)

        test \(not supported\)

    -   "path" indicates the path to the to-be-operated resource object.

        For example,  **/spec/containers/0/image** indicates that the object to be operated is **spec.containers\[0\].image**.

    -   "value" indicates the to-be-modified value.

2.  **Merge Patch, Content-Type: application/merge-patch+json**

    According to RFC 7386, merge patch contains some description of a resource object \(namely, JSON object\). The JSON object is submitted to the server end, and merges with the current object of the server end \(that is, replaces the list field of the current resource object\) to form a new object.

3.  **Strategic Merge Patch, Content-Type: application/strategic-merge-patch+json**

    Strategic merge patch is used to add legal metadata to API objects, and uses new metadata to determine which list should be merged and which should not. The current metadata is used as the structure labels.


For more information about the difference between  **Merge Patch** and **Strategic Merge Patch**, see [Patch Request Method Operation Example](patch-request-method-operation-example.md).

