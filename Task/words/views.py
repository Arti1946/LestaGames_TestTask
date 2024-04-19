import os
from math import log
import re

from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .forms import WordForm
from .models import Word, Table

WORDS_PER_PAGE = 50


def paginate_page(words_list, page_number):
    paginator = Paginator(words_list, WORDS_PER_PAGE)
    page_obj = paginator.get_page(page_number)
    return page_obj


def upload_file(request):
    if request.method == "POST":
        form = WordForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            file = form.cleaned_data["file"]
            new_file = Word(file=file, name=file.name)
            new_file.save()
            return redirect("words:table", file.name)
        return render(request, "words/upload_file.html", {"form": form})
    form = WordForm(request.POST)
    return render(request, "words/upload_file.html", {"form": form})


def words(file_name: str):
    file_name = file_name.replace(" ", "_")
    file_path = os.path.join(
        settings.BASE_DIR, settings.MEDIA_ROOT, "media\\files", file_name
    )
    with open(file_path, "r", encoding="UTF-8") as f:
        pattern = "[^а-яА-ЯёЁa-zA-Z]"
        text = list(re.sub(pattern, " ", f.read().lower()).split())
    words_tf = []
    all_files = Word.objects.all()
    files_names = all_files.values_list("name", flat=True)
    uniq_words = dict()
    for word in text:
        if word in uniq_words:
            uniq_words[word] += 1
        else:
            uniq_words[word] = 1
    words_df = dict()
    for word in uniq_words:
        words_df[word] = 0
    for name in files_names:
        name = name.replace(" ", "_")
        path = os.path.join(
            settings.BASE_DIR, settings.MEDIA_ROOT, "media\\files", name
        )
        with open(path, "r", encoding="UTF-8") as p:
            pattern = "[^а-яА-ЯёЁa-zA-Z]"
            file_text = set(re.sub(pattern, " ", p.read().lower()).split())
            for word in file_text:
                if word in words_df:
                    words_df[word] += 1
    files_count = Word.objects.all().count()
    for word in uniq_words:
        count = words_df[word]
        idf = log(files_count / count)
        words_tf.append(Table(word=word, tf=uniq_words[word], idf=idf))
    words_tf.sort(key=lambda x: x.idf, reverse=True)
    return words_tf


def table(request, file_name):
    info = words(file_name)
    page_num = request.GET.get("page")
    page_obj = paginate_page(info, page_num)
    context = {"page_obj": page_obj}
    return render(request, "words/table.html", context)
