from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class PredictiorConfig(AppConfig):
    name = 'predictior'

    path = os.path.join(settings.MODELS,'model.p')

    with open(path,'rb') as pickled:
    	data = pickle.load(pickled)

    model = data['model']
    n_items = data['n_items']

    path2 = os.path.join(settings.MODELS,'model2.p')
    with open(path2,'rb') as pickled:
    	data = pickle.load(pickled)

    model2 = data['model']
    dataset = data['dataset']