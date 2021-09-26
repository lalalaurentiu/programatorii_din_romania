from django.core.files.storage import FileSystemStorage
from django.conf import settings
import re
import os


def verifyFile(filename, *args):
    fs = FileSystemStorage()
    data = ""
    try:
        searchExtensionHtml = re.search(*args,filename.name)
        if searchExtensionHtml:
            fs.save(filename.name, filename)
            file_size = fs.size(filename.name)
            if file_size <= 2*1024*1024:
                with open(os.path.join(settings.MEDIA_ROOT, filename.name)) as f:
                    words = f.readlines()
                
                for i in words:
                    data += i

                return data
            else:
                return "Fisier prea mare. Dimensiunea nu trebuie să depășească 2 MiB."
        else:
            return "fisier neacceptat"
    except AttributeError:
        return data