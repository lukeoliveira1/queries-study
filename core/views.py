from django.db.models import Count
from django.shortcuts import render
from .models import Book, Author, Review, Profile

def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='teste')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='nome do autor')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='nome da tag')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='nome do autor')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='nome do autor').count()

    # Envie todas as consultas para o template
    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
    }

    return render(request, 'core/teste1.html', context)

def exercises(request):
    
    # a)
    books_by_author = Book.objects.filter(author__name='Amanda Oliveira')
    
    # b)
    books_for_tags = Book.objects.filter(tags__name__contains='Ficção')
    
    # c)
    bio_author_that_contain_words = Author.objects.filter(bio__contains='quidem')
    
    # d)
    books_with_high_ratings = Book.objects.filter(reviews__rating__gte=4)
    
    # e)
    user_profile_with_specific_websites = Profile.objects.filter(website="https://www.barros.net/")
    
    # f) https://docs.djangoproject.com/en/5.0/ref/models/querysets/
    books_without_reviews = Book.objects.exclude(reviews__isnull=False)
   
    # g) https://docs.djangoproject.com/en/4.2/topics/db/aggregation/#order-of-annotate-and-filter-clauses
    authors_with_most_books = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')
    
    # h) 
    books_with_long_summaries = []
    for book in Book.objects.all():
        if len(book.summary.split()) > 150:
            books_with_long_summaries.append(book)

    # i)
    reviews_of_books_by_author = Review.objects.filter(book__author__name='Dr. João Lucas Cavalcanti')

    # j)
    tags_to_filter = ['Biografia', 'Tecnologia']
    books_with_multiple_tags = Book.objects.filter(tags__name__in=tags_to_filter).annotate(num_tags=Count('tags')).filter(num_tags=len(tags_to_filter))
    
    context = {
        # a)
        'books_by_author': books_by_author,
        # b)
        'books_for_tags': books_for_tags,
        # c)
        'bio_author_that_contain_words': bio_author_that_contain_words,
        # d)
        'books_with_high_ratings': books_with_high_ratings,
        # e)
        'user_profile_with_specific_websites': user_profile_with_specific_websites,
        # f)
        'books_without_reviews': books_without_reviews,
        # g)
        'authors_with_most_books': authors_with_most_books,
        # h)
        'books_with_long_summaries': books_with_long_summaries,
        # i)
        'reviews_of_books_by_author': reviews_of_books_by_author,
        # j)
        'books_with_multiple_tags': books_with_multiple_tags,
        
    }

    return render(request, 'core/exercises.html', context)
    