from django.shortcuts import render
from .apps import PredictiorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import numpy as np
import pandas as pd
from sklearn import preprocessing
from scipy.sparse import coo_matrix
import json
# Create your views here.
class call_model(APIView):
	def get(self, request):
		if request.method == 'GET':
			temp = None
			#get user_id from the request
			user_id = request.GET.get('user_id')
			if request.GET.get('itemids'):
				
				items = json.loads(request.GET.get('itemids'))
				print(type(items))
				events = json.loads(request.GET.get('events'))
				length = len(items)
				users = list(user_id)
				print(type(users[0]),type(items[0]),type(events[0]))

				PredictiorConfig.dataset.fit_partial(users=(users), items=(items), item_features=None, user_features=None)
				print("fir_partial done")
				(new_interactions, new_weights) = PredictiorConfig.dataset.build_interactions(((users[0], items[ind],events[ind]) for ind in range(length)))
				PredictiorConfig.model2.fit(new_interactions,sample_weight=new_weights,epochs=50)
				prediction = PredictiorConfig.model2.predict(user_id,np.arange(PredictiorConfig.n_items))	

			
			else:
				prediction = PredictiorConfig.model.predict(user_id,np.arange(PredictiorConfig.n_items))
			
			prediction = list(pd.Series(prediction).sort_values(ascending=False).index)	
			res = list(prediction[:10])
			response = {'recommends': res, 'events':temp}

			return JsonResponse(response)