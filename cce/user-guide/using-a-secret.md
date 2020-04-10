# Using a Secret<a name="cce_01_0016"></a>

After secrets are created, they can be mounted as  data volumes or be exposed as  environment variables to be used by a container in a pod.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>The following secrets are used by the CCE system. Do not perform any operations on them.  
>-   Do not operate secrets under kube-system.  
>-   Do not operate default-secret and paas.elb in other namespaces. The default-secret is used to pull the private image of SWR, and the paas.elb is used to connect the service in the namespace to the ELB service.  

-   [Configuring the Data Volume of a Pod](#section472505211214)
-   [Setting Environment Variables of a Pod](#section207271352141216)

The following example shows how to use a secret.

```
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: my-username  #Username
  password: ******  #The value must be encoded using Base64.
```

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>When a secret is used in a pod, the pod and secret must be in the same cluster and namespace.  

## Configuring the Data Volume of a Pod<a name="section472505211214"></a>

A secret can be used as a file in a pod. As shown in the following example, the username and password of the  **mysecret**  secret are saved in the  **/etc/foo**  directory as files.

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
      readOnly: true
  volumes:
  - name: foo
    secret:
      secretName: mysecret
```

In addition, you can specify the directory and permission to access a secret. The username is stored in the  **/etc/foo/my-group/my-username**  directory of the container.

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mypod
    image: redis
    volumeMounts:
    - name: foo
      mountPath: "/etc/foo"
  volumes:
  - name: foo
    secret:
      secretName: mysecret
      items:
      - key: username
        path: my-group/my-username
        mode: 511
```

To mount a secret to a data volume, you can also perform operations on the CCE console. When creating a workload, set advanced settings for the container, choose  **Data Storage \> Local Disk**, click  **Add Local Disk**, and select  **Secret**. For details, see  [Secret](using-local-disks-for-storage.md#section10197243134710).

## Setting Environment Variables of a Pod<a name="section207271352141216"></a>

A secret can be used as an environment variable of a pod. As shown in the following example, the username and password of the  **mysecret**  secret are defined as an environment variable of the pod.

```
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: mycontainer
    image: redis
    env:
      - name: SECRET_USERNAME
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: username
      - name: SECRET_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysecret
            key: password
  restartPolicy: Never
```

