# Using a ConfigMap<a name="cce_01_0015"></a>

After a ConfigMap is created, it can be used in three workload scenarios:  environment variables, command line parameters, and data volumes.

-   [Using a ConfigMap to Set Workload Environment Variables](#section1737733192813)
-   [Setting Command Line Parameters](#section17930105710189)
-   [Attaching a ConfigMap to the Workload Data Volume](#section1490261161916)

The following example shows how to use a ConfigMap.

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: cce-configmap
data:
  SPECIAL_LEVEL: Hello
  SPECIAL_TYPE: CCE
```

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>When ConfigMap is used in a pod, the pod and ConfigMap must be in the same cluster and namespace.  

## Using a ConfigMap to Set Workload Environment Variables<a name="section1737733192813"></a>

When creating a workload, you can set the configuration item to an environment variable and use the valueFrom parameter to obtain the key-value pair in ConfigMap.

```
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod-1
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "env" ]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:                             ## Use valueFrom to specify the value of the env that refers to the ConfigMap.
            configMapKeyRef:
              name: cce-configmap                ## Name of the referenced configuration file.
              key: SPECIAL_LEVEL                 ## Key of the referenced ConfigMap.
  restartPolicy: Never
```

If you need to define the values of multiple configuration items as the environment variables of the pods, add multiple environment parameters to the pods.

```
env:
- name: SPECIAL_LEVEL_KEY
  valueFrom:
?configMapKeyRef:
          name: cce-configmap
          key: SPECIAL_LEVEL
- name: SPECIAL_TYPE_KEY
  valueFrom:
?configMapKeyRef:
          name: cce-configmap
          key: SPECIAL_TYPE
```

To add all data in a configuration item to environment variables, use the envFrom parameter. The keys in the configuration item will become names of environment variables in pods.

```
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod-2
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "env" ]
      envFrom:
      - configMapRef:
          name: cce-configmap
  restartPolicy: Never
```

## Setting Command Line Parameters<a name="section17930105710189"></a>

You can use a configuration item to set the commands or parameter values for a container by using environment variable substitution syntax $\(VAR\_NAME\). The following shows an example.

```
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod-3
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "echo $(SPECIAL_LEVEL_KEY) $(SPECIAL_TYPE_KEY)" ]
      env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:
            configMapKeyRef:
              name: cce-configmap
              key: SPECIAL_LEVEL
        - name: SPECIAL_TYPE_KEY
          valueFrom:
            configMapKeyRef:
              name: cce-configmap
              key: SPECIAL_TYPE
  restartPolicy: Never
```

After the Pod runs, the following information is displayed:

```
Hello CCE
```

## Attaching a ConfigMap to the Workload Data Volume<a name="section1490261161916"></a>

A ConfigMap can also be used in the data volume. You only need to attach the ConfigMap to the workload when creating the workload. After the mounting is complete, a configuration file with key as the file name and value as the file content is generated.

```
apiVersion: v1
kind: Pod
metadata:
  name: configmap-pod-4
spec:
  containers:
    - name: test-container
      image: busybox
      command: [ "/bin/sh", "-c", "ls /etc/config/" ]   ## Lists the file names in the directory.
      volumeMounts:
      - name: config-volume
        mountPath: /etc/config                          ## Attaches to the /etc/config directory.
  volumes:
    - name: config-volume
      configMap:
        name: cce-configmap
  restartPolicy: Never
```

After the pod is run, the SPECIAL\_LEVEL and SPECIAL\_TYPE files are generated in the /etc/config directory. The contents of the files are Hello and CCE, respectively. Also, the following file names will be displayed.

```
SPECIAL_TYPE
SPECIAL_LEVEL
```

To mount a ConfigMap to a data volume, you can also perform operations on the CCE console. When creating a workload, set advanced settings for the container, choose  **Data Storage \> Local Disk**, click **Add Local Disk**, and select **ConfigMap**. For details, see [ConfigMap](using-local-disks-for-storage.md#section18638191594712).

