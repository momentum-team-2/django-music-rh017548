from django.shortcuts import render, get_object_or_404, redirect
from .models import Albums
from .forms import AlbumForm

# Create your views here.
def list_albums(request):
    album = Albums.objects.all()
    return render(request, "album/list_albums.html",
                  {"albums": album})


def show_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    form = AlbumForm()
    return render(request, "album/show_album.html", {"album": album, "pk": pk, "form": form})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "album/add_album.html", {"form": form})


def edit_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
    if form.is_valid():
        form.save()
        return redirect(to='list_albums')

    return render(request, "album/edit_album.html", {
        "form": form,
        "album": album
    })


def delete_album(request, pk):
    album = get_object_or_404(Albums, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "album/delete_album.html",
                  {"album": album})