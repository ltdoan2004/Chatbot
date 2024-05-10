import os
import gdown

id = "1ly6mD72kWU9fAscfOMhKVXCTBAiv2gcU"
gdown.download(id=id, quiet=False)

os.system("unzip -o ml_docs.zip")
os.system("rm ml_docs.zip")
