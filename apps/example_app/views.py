import functools

from django.shortcuts import HttpResponse, render, get_object_or_404

from ..another_app.do_something import slow_function

from .models import Progress


def index(request):
    """基本となるページ"""
    return render(request, "example_app/index.html")


def setup(request):
    progress = Progress.objects.create()
    return HttpResponse(progress.pk)


def show_progress(request):
    """時間のかかる関数を実行する"""
    if "progress_pk" in request.GET:
        # progress_pkが指定されている場合の処理
        progress_pk = request.GET.get("progress_pk")
        progress = get_object_or_404(Progress, pk=progress_pk)
        persent = str(int(progress.now / progress.total * 100)) + "%"
        return render(request, "example_app/progress_bar.html", {"persent": persent})
    else:
        # progress_pkが指定されていない場合の処理
        return HttpResponse("エラー")


def make_progress(pk):
    progress = get_object_or_404(Progress, pk=pk)
    progress.now += 10
    progress.save()


def set_hikisuu(pk):
    """引数を設定する"""
    return functools.partial(make_progress, pk=pk)


def do_something(request):
    """時間のかかる関数を実行する"""
    if "progress_pk" in request.GET:
        # progress_pkが指定されている場合の処理
        progress_pk = request.GET.get("progress_pk")
        result = slow_function(set_hikisuu(progress_pk))
        return render(request, "example_app/result.html", {"result": result})
    else:
        # progress_pkが指定されていない場合の処理
        return HttpResponse("エラー")
