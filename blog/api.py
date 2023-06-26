import time
import requests as req
import webbrowser



base_url = 'https://api.themoviedb.org/'
base_url_sl = 'https://exe.io/api?'

# base_url+'/3'
api_key_v3 = '886f45aceef91357640893d9a9bc8395'
api_ls = '683bf923a09b3aeb821e42112a762f1e765947f4'
# base_url+'/4'
api_key_v4 = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ODZmNDVhY2VlZjkxMzU3NjQwODkzZDlhOWJjODM5NSIsInN1YiI6IjYyYTFmNDBiODUwMDVkMDBhY2I2OThkMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vGoKyHc0NtDjvfrdNQS6mSum0vMfkeHuzDj1Qlef_Cc'



def movie_home(pgno=None):
    
    page_no = pgno


    # v4 movie lists
    if page_no is None:
        url = base_url+f'3/trending/movie/day?api_key={api_key_v3}'
    else:
        url = base_url+f'3/trending/movie/day?api_key={api_key_v3}&page={page_no}'

    r = req.get(url)

    data = r.json()
    return data


def genres():

    url = base_url+'3/genre/movie/list?api_key=886f45aceef91357640893d9a9bc8395&language=en-US'

    r = req.get(url)
    genres = r.json()
    return genres


def fea_post():
    
    url = base_url+f'3/movie/popular?api_key={api_key_v3}&language=en-US'

    r = req.get(url)

    data = r.json()

    return data


def search(search,page_no=1):

    url = base_url+ f'3/search/movie?api_key={api_key_v3}&language=en-US&query={search}&page={page_no}&include_adult=false'

    r = req.get(url)

    data = r.json()

    return data



def details(movie_id):
    
    url = base_url+f'3/movie/{movie_id}?api_key={api_key_v3}&language=en-US'

    r = req.get(url)

    data = r.json()

    return data


def credits(movie_id):

    url = base_url+f'3/movie/{movie_id}/credits?api_key={api_key_v3}&language=en-US'

    r = req.get(url)
    data = r.json()
    return data

def link_stn(link):

    url = base_url_sl+f'api={api_ls}&url={link}'

    r = req.get(url)
    link = r.json()
    return link

# def watch_pro(rgn='USA'):
#     url = base_url+f'3/watch/providers/movie?api_key={api_key_v3}&language=en-US&watch_region={rgn}'
#     r = req.get(url)
#     provider = r.json()
#     return provider


def movie_rec(move_id):
    url = base_url+f'3/movie/{move_id}/recommendations?api_key={api_key_v3}&language=en-US&page=1'
    r = req.get(url)
    data = r.json()
    return data

def simlar_mov(move_id):
    url = base_url+f'3/movie/{move_id}/similar?api_key={api_key_v3}&language=en-US&page=1'
    r = req.get(url)
    data = r.json()
    return data