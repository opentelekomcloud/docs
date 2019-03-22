#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import commands

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        bucket_nameurl = str(sys.argv[1:][0])
    else:
        bucket_nameurl = ""
        print("bucket name should be specified\nAbortMultipartUploads.py [s3://BucketName]")
        sys.exit()

    while True:
        ls_cmd = "s3cmd multipart %s" % bucket_nameurl
        out = commands.getoutput(ls_cmd)
        if len(out.splitlines()) < 3:
            print("All multiuploads have been aborted.")
            sys.exit()

        if len(sys.argv[1:]) > 1 and sys.argv[2:][0].lower() == "list":
            print("only up to 1000 multiuploads can be displayed !\n")
            print(out)
            sys.exit()

        for line in out.splitlines()[2:]:
            obj_uid = line.split("\t")
            url = obj_uid[1]
            uploadId = obj_uid[2]
            print("url:[%s], uploadId:[%s]" % (url, uploadId))
            abort_cmd = "s3cmd abortmp %s %s" % (url, uploadId)
            out = commands.getoutput(abort_cmd)
            print(out)

