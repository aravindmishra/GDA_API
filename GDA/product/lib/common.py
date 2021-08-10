from django.core.files.storage import default_storage
from django.conf import settings
import os, time
from datetime import datetime
from GDA.product.models import FileDetails

class Common:

    def addTimeStamp(self,filename):
        if filename:
            splitedName = filename.split('.')
            return splitedName[0] +'_'+str(round(time.time())) +'.'+splitedName [1]
        return False

    def fileUpload(self,file):
        try:
            if file:
                # File Rename
                file_name = self.addTimeStamp(filename = file.name)
                path = 'product/' + file_name
                # Save Image.
                default_storage.save(path, file)
                # Save File Details.
                FileDetails.objects.create(file_name = file_name, file_path = settings.MEDIA_PRODUCT_ROOT, file_size = file.size, created_by = 1, created_date = datetime.now().strftime("%Y-%m/%d, %H:%M:%S"))
                fileId = FileDetails.objects.values('file_id').latest('file_id')
                print(fileId)
                return fileId["file_id"]
            return False
        
        except Exception as e:
            print(str(e))
            return False
