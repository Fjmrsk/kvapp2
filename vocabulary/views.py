from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render
from .models import Vocabulary

def random_vocabulary(request):
    vocab_count = Vocabulary.objects.count()
    if vocab_count > 0:
        random_vocab = Vocabulary.objects.all()[random.randint(0, vocab_count - 1)]
    else:
        random_vocab = None
    return render(request, 'vocabulary/random.html', {'vocab': random_vocab})
