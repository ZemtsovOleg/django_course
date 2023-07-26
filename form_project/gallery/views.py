from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Gallery

# Create your views here.


class GalleryCreateView(CreateView):
    model = Gallery
    fields = '__all__'
    template_name = 'gallery/load_file.html'
    success_url = 'load_file'


class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'files'


''' Отсутствие проверки типа файла: Ваш код в настоящее время не проверяет тип загружаемого файла. Это может привести к загрузке и выполнению вредоносных файлов, таких как исполняемые скрипты (например, .exe, .sh) или файлы с вредоносным кодом. Рекомендуется добавить проверку на допустимые типы файлов и разрешать только загрузку разрешенных расширений.

Нет контроля размера файла: Ваш код не ограничивает размер загружаемых файлов, что может привести к DoS-атаке или переполнению дискового пространства. Желательно установить ограничение на размер файла и отвергать загрузку слишком больших файлов.

Неправильное имя файла: Ваш код использует file.name в качестве имени файла для сохранения на сервере. Если имя файла предоставляется пользователем, это может привести к Directory Traversal Attack или файловой инъекции. Рекомендуется создавать собственное безопасное имя файла, чтобы избежать подобных атак. '''

# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/gallery.html', {'form': form})

#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/gallery.html', {'form': form})
