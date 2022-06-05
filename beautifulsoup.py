from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
res = rq.get('https://movie.naver.com/movie/running/current.nhn')
soup = bs(res.content, 'html.parser')
movieTitle = soup.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dt > a')
movieRating = soup.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl > dd > div > a > span.num') 
movieVote = soup.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl > dd > div > a > span.num2 > em')

movie=[]
rating=[]
numOfParti = []

for title in movieTitle :
    movie.append(title.text.strip())
for rate in movieRating :
    rating.append(rate.get_text())
for vote in movieVote : 
    numOfParti.append(vote.get_text())

dic = {
    '제목' : movie,
    '평점' : rating,
    '참여인원' : numOfParti
}

naverMovie = pd.DataFrame.from_dict(dic, orient='index')

naverMovie = naverMovie.transpose()
naverMovie
