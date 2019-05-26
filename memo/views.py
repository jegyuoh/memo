from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo

# Create your views here.
def memohome(req):
    memos = Memo.objects.all()
    return render(req, 'memohome.html', {'memos': memos})

def memonew(req):
    return render(req, 'memonew.html')

def memocreate(req):
    new_memo = Memo()
    new_memo.title = req.POST['title']
    new_memo.content = req.POST['content']
    
    if 'image' in req.FILES.keys():
        new_memo.image = req.FILES['image']
    new_memo.save()
    return redirect('/memo')

def memoshow(req, memo_id):
    one_memo = get_object_or_404(Memo, id=memo_id)
    coments = one_memo.memocoment_set.all()
    return render(req, 'memoshow.html', {'memo': one_memo, 'coments': coments})

def memoedit(req, memo_id):
    one_memo = get_object_or_404(Memo, id=memo_id)
    return render(req, 'memoedit.html', {'memo': one_memo})

def memoupdate(req, memo_id):
    if (req.method == 'POST'):
        one_memo = get_object_or_404(Memo, id=memo_id)
        one_memo.title = req.POST['title']
        one_memo.content = req.POST['content']
        one_memo.save()
    
    return redirect('/memo/show/'+str(one_memo.id))

def memodelete(req, memo_id):
    one_memo = get_object_or_404(Memo, id=memo_id)
    one_memo.delete()
    
    return redirect('/memo')

def comentcreate(req, memo_id):
    if (req.method == 'POST'):
        one_memo = get_object_or_404(Memo, id=memo_id)
        one_memo.memocoment_set.create(content=req.POST['coment_content'])
    return redirect('/memo/show/' + str(memo_id))