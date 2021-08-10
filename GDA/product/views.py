from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from GDA.product.models import GroceryDetails, CatogeryDetails
from GDA.product.serializers import GrocerySerializer, GroceryListSerializer
from GDA.product.lib.common import Common
from datetime import datetime
# Create your views here.

class AddGrocery(APIView):
    def post(self,request):
        try:
            if "product_image" in request.data:
                serializer = GrocerySerializer(data = request.data)
                if serializer.is_valid():
                    common = Common()
                    fileId = common.fileUpload(request.data["product_image"])
                    if fileId:
                        serializer.save(file_id = int(fileId), status = 1, created_by = 1, created_date = datetime.now().strftime("%Y-%m/%d, %H:%M:%S"))
                        return Response({"error":False,"status_code":200,"message":"OK"})
                    else:
                        raise Exception
                else:
                    return Response({"error":True,"status_code":400,"message":serializer.errors})
            else:
                return Response({"error":True,"status_code":400,"message":"product_image is required"})

        except KeyError:
            return Response({"error":True,"status_code":400,"message":"Invalid Input Fields"})

        except Exception as e:
            return Response({"error":True,"status_code":500,"message":str(e)})


class GroceryList(APIView):
    def post(self,request):
        try:
            if "catogery_id" in request.data:
                response = GroceryDetails.list(catogery_id = request.data["catogery_id"])
                serializer = GroceryListSerializer(response,many=True)
                for data in serializer.data:
                    data["product_image"] = settings.PRODUCT_IMAGE_URL + data["file_name"]
                return Response({"error":False,"status_code":200,"data":serializer.data})
            else:
                raise KeyError
        except KeyError:
            return Response({"error":True,"status_code":400,"message":"Invalid Input Fields"})

        except Exception as e:
            return Response({"error":True,"status_code":500,"message":str(e)})

