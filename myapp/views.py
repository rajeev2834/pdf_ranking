from io import BytesIO

from django.db.models import F
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import FileData
from .pdf_parser import parse_pdf
from .serializers import (FileDataCreateSerializer, FileDataSerializer,
                          FileScoreSerializer)


class FileDataViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FileData.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return FileDataCreateSerializer
        return FileDataSerializer
    
    # get list of user related files
    def get_queryset(self):
        return FileData.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        # Get the serializer with the request data
        serializer = self.get_serializer(data=request.data)
        # Validate the data
        serializer.is_valid(raise_exception=True)
        # Get the uploaded file from the validated data
        uploaded_pdf = serializer.validated_data.get('file')

        # Check if the file is uploaded
        if not uploaded_pdf:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the file is empty
        if uploaded_pdf.size == 0:
             return Response({'error': 'Uploaded PDF is empty'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the file is a pdf
        if uploaded_pdf.content_type != 'application/pdf':
            return Response({'error': 'Uploaded file is not a pdf'}, status=status.HTTP_400_BAD_REQUEST)
        

        pdf_data = uploaded_pdf.read()
        pdf_stream = BytesIO(pdf_data)

        # Parse the pdf
        scores = parse_pdf(pdf_stream)
        print("scores: ", scores)

        # Check if the extracted text is empty
        if scores is None:
             return Response({'error': 'PDF content is empty'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the object instance with the user and the file
        self.perform_create(serializer, scores)
        # Return a success response with the created object data
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, scores):
        
        try:
                
                instance = serializer.save(user=self.request.user)
                # Update the instance with the scores
                instance.sde = scores[0]
                instance.research = scores[1]
                instance.operations = scores[2]
                instance.supplychain = scores[3]
                instance.project = scores[4]
                instance.data = scores[5]
                instance.healthcare = scores[6]
                instance.content = scores[7]
                instance.marketing = scores[8]
                instance.teaching = scores[9]
                instance.security = scores[10]

                # Save the instance
                instance.save()
            
        except Exception as e:
                # If there is any error, delete the instance
                return Response({'error': "pdf parsing failed"}, status=status.HTTP_400_BAD_REQUEST)
        

class FileScoreListView(APIView):

    #permission_classes = [IsAdminUser]
    
    def get_score_field(self):
        # Get the score field name from the URL String
        return self.kwargs.get('score_field')
    
    def get(self, request, *args, **kwargs):
        # Get the score field name from the URL parameter
        score_field = self.get_score_field()
        
        # Get the queryset of the model
        #queryset = FileData.objects.all()

        # Annotate the queryset with the dynamic score field
        annotated_queryset = FileData.objects.annotate(
            dynamic_score=F(score_field)
        )
        
        # Order the queryset by the dynamic score field in descending order
        sorted_queryset = annotated_queryset.order_by('-dynamic_score')
        
        # Get the serializer class
        serializer_class = FileScoreSerializer
        
        # Get the serializer context
        context = {'score_field': score_field, 'request': request}
        
        # Get the serializer with the queryset, context and many=True
        serializer = serializer_class(sorted_queryset, context=context, many=True)
        
        # Return the response with the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
