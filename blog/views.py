from django.shortcuts import render
from . import api

# Create your views here.




# global fun
def gen(request):
    url = api.genres()
    return {'genres':url}



def Home(request):

    # pgno qurry
    if request.method == 'GET' and 'page' in request.GET:
        page_no = request.GET.get('page')
    else:
        page_no = 1

    # data = posts.objects.all()
    data = api.movie_home(page_no)
    fea_data = api.fea_post()

    # image base_url
    img_url = 'https://image.tmdb.org/t/p/w1280'

    # feature post content
    fea_data = fea_data['results'][0:5]
    # print(fea_data)

    # genres
    genres = api.genres()
    genre = genres['genres']
    ranges = range(18)

    # for i in tags:
    #     print('i is',i)
    #     for y in i['genre_ids']:
    #         print('y is',y)
    #         for x in :
    #             if y == genres['genres'][x]['id']:
    #                 genre.append(genres['genres'][x]['name'])

    # print('genre is',genre)


    # total page
    total_pg = range(1,data['total_pages']+1)
    total_pg_no = data['total_pages']

    # final page
    for i in total_pg:
        final_pg = i 

    # next page && prev page
    i = data['page']
    if i >= total_pg_no:
        next_pg = i
    else:
        next_pg = i+1
    if i <= 1:
        prev_pg = i
    else:
        prev_pg = i-1


    context = {
        # 'post' : data,
        'url': img_url,
        'data':data,
        'genre':genre,
        'final_pg':final_pg,
        'range':ranges,
        'total_pg_no':total_pg_no-5,
        'fea_data':fea_data,
        'total_pg':total_pg,
        'next_pg':next_pg,
        'prev_pg':prev_pg,
    }
    # print(context)
    return render(request,'blog/home.html',context)



def search(request):

    search = request.GET.get('s')
    if request.GET.get('page'):
        page_no = request.GET.get('page')
        data = api.search(search,page_no)
    else:
        data = api.search(search)

    fea_data = api.fea_post()

     # image base_url
    img_url = 'https://image.tmdb.org/t/p/w1280'

    # feature post content
    fea_data = fea_data['results'][0:5]

    # total page
    total_pg = range(1,data['total_pages']+1)
    total_pg_no = data['total_pages']

    # genres
    genres = api.genres()
    genre = genres['genres']

    # final page
    final_pg = None
    for i in total_pg:
        final_pg = i 


    # next page && prev page
    i = data['page']
    if i >= total_pg_no:
        next_pg = i
    else:
        next_pg = i+1
    if i <= 1:
        prev_pg = i
    else:
        prev_pg = i-1

    context={
        'url': img_url,
        'data':data,
        'genre':genre,
        'search':search,
        'total_pg_no':total_pg_no-5,
        'fea_data':fea_data,
        'total_pg':total_pg,
        'final_pg':final_pg,
        'next_pg':next_pg,
        'prev_pg':prev_pg,
    }

    return render(request,'blog/search.html',context)




def detail(request,id,name):


    movie_id = id
    data = api.details(movie_id)
    credit = api.credits(movie_id)
    movie_rec = api.movie_rec(movie_id)
    silar_mve = api.simlar_mov(movie_id)

    # link shorten
    link = data['homepage']
    link = api.link_stn(link)

    # image base_url
    img_url = 'https://image.tmdb.org/t/p/w300'

    # creadit
    credit = credit['cast'][:5]

    


    context = {
        'data':data,
        'creadit':credit,
        'movie_rec':movie_rec['results'][:5],
        'similar_move':silar_mve['results'][:5],
        's_link':link,
        'img_url':img_url,
    }

    return render(request,'blog/detail.html',context)


def Category(request,cata):


    if request.method == 'GET' and 'page' in request.GET:
        page_no = request.GET.get('page')
    else:
        page_no = 1
        
    data = api.movie_home(page_no)

    # LOGIC
    for x in genre:
        if cata == x['name'].lower():
            cata = x['id']

    datas = []

    if data['results']:
        for i in data['results']:
            for z in i['genre_ids']:
                if cata == z:
                    datas += [i]
                else:
                    continue

    # image base_url
    img_url = 'https://image.tmdb.org/t/p/w1280'

    # total page
    total_pg = range(1,data['total_pages']+1)
    total_pg_no = data['total_pages']

    # genres
    genres = api.genres()
    genre = genres['genres']

    # next page && prev page
    i = data['page']
    if i >= total_pg_no:
        next_pg = i
    else:
        next_pg = i+1
    if i <= 1:
        prev_pg = i
    else:
        prev_pg = i-1

    
    context = {
        'url': img_url,
        'data':datas,
        'genre':genre,
        'total_pg_no':total_pg_no-5,
        'total_pg':total_pg,
        'next_pg':next_pg,
        'prev_pg':prev_pg,
    }
    return render(request,'blog/CATEGORY.html',context)