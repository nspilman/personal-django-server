from django.shortcuts import render
import boto3
from rest_framework.views import APIView
from rest_framework.response import Response


class photos(APIView):
    def get(self, request):
        return Response({"response":'whatsgood?'})

    def post(self, request):
        data = request.data
        photo_category = data['category']

        s3_client = boto3.client(
            's3',
            )
        s3_resource = boto3.resource('s3')
        bucket_name = 'website-photographs'
        my_bucket = s3_resource.Bucket(bucket_name)

        urls = []
        for file in my_bucket.objects.all():
            dir = file.key.split('/')[0]
            if dir == photo_category:
                params = {'Bucket': bucket_name, 'Key': file.key}
                url = s3_client.generate_presigned_url('get_object', params)
                urls.append(url)

        return Response({"response":urls})


# Create your views here.


# Do not hard code credentials



# def getPhotoUrlsByDirectoryName(directory_name):
#     for file in my_bucket.objects.all():
#         dir = file.key.split('/')[0]
#         if dir == directory_name:
#             params = {'Bucket': bucket_name, 'Key': file.key}
#             url = s3_client.generate_presigned_url('get_object', params)
#             print(url)

# getPhotoUrlsByDirectoryName('photos-wedding')