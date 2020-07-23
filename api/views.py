from django.shortcuts import render

# Create your views here.
import json

data = {'id': 1, 'name': 'hoge'}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
