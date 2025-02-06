from .models import Chapter

def chapter_menu(request):
    return {
        'chapters': Chapter.objects.all()
    }
