from django.shortcuts import render, redirect
from .models import Project, Skill, Message, Endoresment
from .forms import ProjectForm, MessageForm, SkillForm, EndoresmentForm, CommentForm
from django.contrib import messages


# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')

    endoresments = Endoresment.objects.filter(approved=True)

    skills = Skill.objects.filter(body='')

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message envoye.')

    context = {'projects': projects, 'skills': skills, 'form': form, 'endoresments': endoresments,
               'detailedSkills': detailedSkills}
    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count()

    comments = project.comment_set.all()

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request, 'Commentaire sent.')

    context = {'project': project, 'count': count, 'comments': comments, 'form': form}
    return render(request, 'base/project.html', context)


def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')

    unreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'base/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/message.html', context)


def addSkill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        form.save()
        messages.success(request, 'Skill ajouté.')
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/skill_form.html', context)


def addEndoresment(request):
    form = EndoresmentForm()
    if request.method == 'POST':
        form = EndoresmentForm(request.POST)
        form.save()
        messages.success(request, 'Endoresment ajouté.')
        return redirect('home')
    context = {'form': form}
    return render(request, 'base/endoresment_form.html', context)


def donation(request):
    return render(request, 'base/donation.html')