#siple recommendation class
# It will take the user like list and return the movies he may like 

import re
import Thingy

class SimpleRecommendation:
	def __init__(self):
		self.data = []
	def loadmoviegenres(self):
		self.movies = {}
		with open("//shared/movie/data/processed/movie_genre.list") as f:
			moviegenres = f.readlines()
		
		for moviegenre in moviegenres:
			# print moviegenre
			splited = re.sub(r'{.*}','',moviegenre)
			splited = re.sub(r'\([^(]*\)','',splited)
			# print splited
			splited = filter(lambda x: x,splited.replace("\"","").split("\t")) 			
			genre = splited[1].strip()
			movie = splited[0].strip()
			moviethingy = {}
			if movie in self.movies:
				moviethingy = self.movies[movie]
			else:
				moviethingy = Thingy.Thingy(movie)
				self.movies[movie] = moviethingy					
			moviethingy.isLike(genre,1)
		
	def GetRecommendation(self,user):
		userLikes = []
		with open("//shared/movie/data/processed/user_likes_movie.list") as f:
			userLikes = f.readlines()
				
		userThingy = Thingy.Thingy(user)		
		for userAndLike in userLikes:
			splited = userAndLike.split("\t")			
			user = splited[0].strip()
			like = splited[1].strip()				
			if userThingy.name == user:				
				if like in self.movies:
					movieThingy = self.movies[like].definedLike()
					for k in movieThingy:
						userThingy.isLike(k,movieThingy[k])
		
		recentmovies = []
		with open("//shared/movie/data/processed/2013.movie.list") as f:
			recentmovies = map(lambda x: x.strip(),f.readlines())			
		print
			
		pr = {}
		
		for recentmovie in recentmovies:			
			if recentmovie in self.movies:				
				movieThingy = self.movies[recentmovie]
				distance = self.GetDistance(userThingy,movieThingy)
				pr[movieThingy.name] = distance
		rec = sorted(pr.items(),key = lambda x: x[1],reverse = False)
		
		print userThingy.definedLike()
		return rec[:5]
		
	def GetDistance(self,a,b):
		a = a.definedLike()
		b = b.definedLike()
		distance = 0 
		for k in a:
			if k in b:
				distance += abs(a[k]-b[k])
			else:
				distance += 99 
		return distance
			


