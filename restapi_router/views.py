from restapi_router.models import RestRouterDetails
import json
from django.http import HttpResponse
from rest_framework import status
import pandas as pd
from .serializers import RestRouterDetailsSerializer
from .models import RestRouterDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class CreateNewRouter(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            objsTable = RestRouterDetails.objects.all().values()
            loopBackPresent = objsTable["loopBack"].to_list()
            hostNamePresent = objsTable["hostName"].to_list()
            if request.data['loopBack'] in loopBackPresent:
                return HttpResponse(json.dumps({"status": "Fail", "reason": "loopBackPresent already present"}),status=status.HTTP_201_CREATED)
            elif request.data['hostName'] in hostNamePresent:
                return HttpResponse(json.dumps({"status": "Fail", "reason":"hostNamePresent already present" }),status=status.HTTP_201_CREATED)
            else:
                RestRouterDetails.objects.create(sapId=request.data['sapId'],hostName=request.data['hostName'], loopBack=request.data['loopBack'],
                                                 type=request.data['type'])
            return HttpResponse({"status" : "Sucess"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return HttpResponse(
                json.dumps({"status": "failed", "reason": str(e)}), status=status.HTTP_201_CREATED)


class UpdateRouterIP(APIView):
    permission_classes = (IsAuthenticated,)
    def update(self, request):
        try:

            obj = RestRouterDetails.objects.filter(loopBack =request.data['loopBack'])
            serializer = RestRouterDetailsSerializer(obj, data=request.data, many=True)

            if serializer.is_valid():
                serializer.save()
            else:
                HttpResponse({"status": "Fail", "reason":"Invalid Data"}, status=status.HTTP_201_CREATED)

            #obj.update(sapId=request.data["sapId"],hostName=request.data["hostName"],type=request.data["type"])
        except Exception as e:
            return HttpResponse(
                json.dumps({"status": "failed", "reason": str(e)}), status=status.HTTP_201_CREATED)

class ListRouterUsingsapId(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            queryset = RestRouterDetails.objects.filter(sapId =request.data['sapId']).order_by('type')
            print(queryset)
            query = RestRouterDetailsSerializer(queryset, many=True).data

            return Response(query)
        except Exception as e:
            return HttpResponse(
                json.dumps({"status": "failed", "reason": str(e)}), status=status.HTTP_201_CREATED)


class DeleteBasedonIP(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self, request):
        try:
            obj = RestRouterDetails.objects.filter(loopBack =request.data['loopBack'])
            obj.delete()
            return HttpResponse(json.dumps({"status": "Sucess",'reason':'Deleted Sucessfully'}), status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return HttpResponse(
                json.dumps({"status": "failed", "reason": str(e)}), status=status.HTTP_201_CREATED)


def convert_ipv4(ip):
    return tuple(int(n) for n in ip.split('.'))

def check_ipv4_in(addr, start, end):
    return convert_ipv4(start) < convert_ipv4(addr) < convert_ipv4(end)

class ListRouterIPRange(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            start = request.data['start']
            end = request.data['end']
            queryset = RestRouterDetails.objects.all().values()
            loopBackList = queryset['queryset'].to_list()
            RangeList = list()
            for loopBack in loopBackList:
                boolVal = check_ipv4_in(loopBack,start,end)
                if boolVal:
                    RangeList.append(loopBack)
            df= pd.DataFrame(queryset)
            df_final = df[df['loopBack'].isin(RangeList)]
            print(queryset)
            query = RestRouterDetailsSerializer(queryset, many=True).data

            return Response(query)
        except Exception as e:
            return HttpResponse(
                json.dumps({"status": "failed", "reason": str(e)}), status=status.HTTP_201_CREATED)



