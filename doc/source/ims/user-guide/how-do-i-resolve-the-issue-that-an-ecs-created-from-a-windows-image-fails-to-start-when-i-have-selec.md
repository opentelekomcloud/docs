# How Do I Resolve the Issue That an ECS Created from a Windows Image Fails to Start When I Have Selected Enable Automatic Configuration During Image Registration?<a name="EN-US_TOPIC_0113403127"></a>

## Symptom<a name="section6703121915151"></a>

This issue is probably caused by the failure of offline VirtIO driver injection.

## Solution<a name="section22051931161519"></a>

When you inject the VirtIO driver for a Windows ECS offline, there are some restrictions:

-   If the boot mode of the image file is UEFI, the VirtIO driver cannot be injected offline.
-   It is recommended that you disable Group Policy Object \(GPO\). Some policies may cause the failure to inject the VirtIO driver offline.
-   It is recommended that you stop the antivirus software. Otherwise, the VirtIO driver may fail to be injected offline.

To update the VirtIO driver, you must install UVP VMTools. For how to install UVP VMTools, see "Optimizing a Windows Private Image" in  _Image Management Service User Guide_.

