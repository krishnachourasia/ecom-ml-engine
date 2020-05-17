from django.shortcuts import render
from .apps import PredictiorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import numpy as np
import pandas as pd
# Create your views here.
class call_model(APIView):
	def get(self, request):
		if request.method == 'GET':

			#get user_id from the request
			user_id = request.GET.get('user_id')

			prediction = PredictiorConfig.model.predict(user_id,np.arange(PredictiorConfig.n_items))
			prediction = list(pd.Series(prediction).sort_values(ascending=False).index)	
			res = list(prediction[:10])
			response = {'recommends': res}

			return JsonResponse(response)