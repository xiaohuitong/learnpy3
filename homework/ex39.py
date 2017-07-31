class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(['happy bitthday to you',
                  'i dont want to get sued',
				  'so i will stop right there'])

bulls_on_parade = Song(['they really around the famoly',
                       'whith pockets full of shells'])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()