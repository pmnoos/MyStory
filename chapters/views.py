from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Chapter
from .forms import ChapterForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html') 

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Chapter  # Ensure this model exists

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Chapter

def chapter_list(request):
    chapters = Chapter.objects.order_by('id')  # Ensure consistent ordering
    paginator = Paginator(chapters, 10)  # Paginate with 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'chapters/chapter_list.html', {'page_obj': page_obj})



from django.shortcuts import render, get_object_or_404
from .models import Chapter

def chapter_detail(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)

    # Fetch next and previous chapters
    previous_chapter = Chapter.objects.filter(id__lt=chapter.id).last()  # Previous chapter by ID
    next_chapter = Chapter.objects.filter(id__gt=chapter.id).first()  # Next chapter by ID

    return render(request, 'chapters/chapter_detail.html', {
        'chapter': chapter,
        'previous_chapter': previous_chapter,
        'next_chapter': next_chapter,
    })


def new_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Chapter created successfully!")
            return redirect('chapter_list')  # Ensure this URL name exists
    else:
        form = ChapterForm()

    return render(request, 'chapters/new_chapter.html', {'form': form})



@login_required
def edit_chapter(request, slug):
    chapter = get_object_or_404(Chapter, slug=slug)

    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES, instance=chapter)
        if form.is_valid():
            form.save()
            messages.success(request, "Chapter updated successfully!")
            return redirect('chapter_detail', slug=chapter.slug)
    else:
        form = ChapterForm(instance=chapter)

    return render(request, 'chapters/edit_chapter.html', {'form': form, 'chapter': chapter})




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to homepage after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'chapter_list')
            return redirect(next_url)
        else:
            # Handle invalid login
            pass
    else:
        next_url = request.GET.get('next', '')
    return render(request, 'registration/login.html', {'next': next_url})
