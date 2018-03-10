# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import ast

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib import messages
from collections import OrderedDict

from pyexcel_ods import get_data, save_data

from website.forms import UploadFileForm
from website.utils import path_file_save


def index(request):
    # TODO: delete cache and file with prefix session_key
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    form = UploadFileForm(files=request.FILES or None)
    if form.is_valid():
        form.ods_save_to_storage(session_key)
        return redirect('website:show_ods')

    return render(request, 'index.html', {'form': form})


def show_ods(request):
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key

    count = cache.get(session_key)
    if count:
        data = get_data(path_file_save(session_key, count))
    else:
        data = get_data(path_file_save(session_key))

    if len(data) > 1:
        messages.warning(request, 'Sorry, Ngods not support multy sheet')
        return redirect('website:index')
    if not data:
        return redirect('website:index')

    context = {
        'sheets': data,
    }

    if request.is_ajax():
        return JsonResponse(data)
    return render(request, 'multi-sheet.html', context)


def save_ods(request):
    session_key = request.session.session_key
    count = cache.get(session_key)
    ods_data = request.GET

    new_data = []
    new_sheet = OrderedDict()
    for name_sheet, list_data in ods_data.items():
        for row in ast.literal_eval(list_data):
            new_row = []
            for _, cell in row.items():
                new_row.append(str(cell))
            new_data.append(new_row)
        new_sheet.update({name_sheet: new_data})

    if count:
        count = int(count) + 1
        save_data(path_file_save(session_key, count), new_sheet)
    else:
        count = 1
        save_data(path_file_save(session_key, count), new_sheet)

    cache.set(session_key, count)
    return JsonResponse(new_sheet)
