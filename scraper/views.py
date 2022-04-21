from distutils.log import error
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .utils import Scraper


class ScraperServiceView(APIView):
    def post(self, request):
        data = request.data
        link = data['link']
        # try:
        scraper = Scraper(link)
        response = scraper.scrape_page()
        return Response(response, status=status.HTTP_200_OK)
        # except:
        #   return Response({"error": "something went wrong"}, status=status.HTTP_200_OK)
