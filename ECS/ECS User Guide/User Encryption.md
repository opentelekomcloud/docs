## User Encryption

User encryption allows you to use the encryption feature provided on the public
cloud platform to encrypt ECS resources, improving data security. User
encryption includes image encryption and EVS disk encryption.

### Image Encryption

Key encryption supports encrypting private images. When creating an ECS, if you
select an encrypted image, the system disk of the created ECS automatically has
encryption enabled, implementing system disk encryption and improving data
security.

Use either of the following methods to create an encrypted image:


- Create an encrypted image using an existing encrypted ECS.
- Create an encrypted image using an external image file.

For more information about image encryption, see ***Image Management Service User
Guide***.

### EVS Disk Encryption

EVS disk encryption supports system disk encryption and data disk encryption.


- When creating an ECS, you can encrypt added data disks.
- System disk encryption relies on the image. When creating an ECS, if you select an encrypted image, the system disk of the created ECS automatically has encryption enabled, and the encryption mode complies with the image encryption mode.

For more information about EVS disk encryption, see ***Elastic Volume Service User
Guide***.

### Impact on AS

If you use an encrypted ECS to create an Auto Scaling (AS) configuration, the encryption mode of the created AS configuration complies with the ECS encryption mode.

### About Keys
The keys used for encryption rely on the Key Management Service (KMS). You must use KMS to create a key and then use the key to encrypt resources.

Keys provided by KMS include the default customer master key (CMK) and CMK. The default CMK is **evs/default**.



- Default CMKs cannot be disabled and do not support scheduled deletion.
- CMKs can be disabled and support scheduled deletion. After disabling a CMK or scheduling the deletion of a CMK takes effect, the EVS disk encrypted using this CMK can still be used until the disk is detached from and then attached to an ECS again. During this process, the disk fails to be attached to the ECS because the CMK cannot be obtained. Therefore, the EVS disk becomes unavailable.

For details about KMS, see ***Key Management Service User Guide***.
