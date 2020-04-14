# What Can I Do If I Configure an Incorrect OS or System Disk Size During Private Image Registration Using an Image File?<a name="EN-US_TOPIC_0030713213"></a>

If you select an incorrect OS, ECSs may fail to be created from the private image. If the configured system disk size is less than the system disk size in the image file, the image will fail to be created.

In this case, delete the incorrect image and create a private image again using the correct parameter settings.

