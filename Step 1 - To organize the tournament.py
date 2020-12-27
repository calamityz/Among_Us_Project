# -*- coding: utf-8 -*-


import random

class Player:
    def __init__(self,player_id=None):
        self.score = 0
        self.finalScore = 0
        self.impostor = False
        self.player_id = player_id
        self.count_games = 0
    
    def resetScore(self):
        self.finalScore=0
    
class Game:
    def __init__(self, players):
        self.players = players
        
    def start(self):
        for player in self.players:
            player.count_games += 1
        impostors = random.sample(self.players, 2)
        for player in impostors :
            player.impostor=True
    
    def setScore_impostors(self):
        murders_1=random.randint(0,8)
        covertsmurders_1=random.randint(0,murders_1)
        murders_2=random.randint(0,8-murders_1)
        covertsmurders_2=random.randint(0,murders_2)
        impostors=[]
        for player in self.players:
            if player.impostor:
                impostors.append(player)
        impostors[0].score += murders_1 + 3*covertsmurders_1
        impostors[1].score += murders_2 + 3*covertsmurders_2
                
    def setScore_crewmate(self):
         for player in self.players:
                if not player.impostor:
                    player.score += random.randint(0,1) + 3*random.randint(0,2)
        
    def are_winner(self):
        if (random.randint(0,1)==0):
            for player in self.players:
                if not player.impostor:
                    player.score += 5
        else:
            for player in self.players:
                if player.impostor:
                    player.score += 10  
    
    def finalScoreCalculation(self):
        for player in self.players:
            player.finalScore = player.score/player.count_games
            
    def resetRoles(self): 
        for player in self.players:
            player.impostor = False


class Node:
    
    def __init__(self, player, left=None, right=None):
        self.left = left
        self.right = right
        self.val = player
        self.height = 1
    
        
    def insert(self, value):
    
        if self.val:
            if value.finalScore < self.val.finalScore:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value.finalScore > self.val.finalScore:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.val = value
    


class Ranking(): 
    

	def insert(self, root, key): 
		
		if not root: 
			return Node(key) 
		elif key.finalScore < root.val.finalScore: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 

		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		balance = self.getBalance(root) 

		if balance > 1 and key.finalScore < root.left.val.finalScore: 
			return self.rightRotate(root) 

		if balance < -1 and key.finalScore > root.right.val.finalScore: 
			return self.leftRotate(root) 

		if balance > 1 and key.finalScore > root.left.val.finalScore: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 
        
		if balance < -1 and key.finalScore < root.right.val.finalScore: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def delete(self, root, key): 

		if not root: 
			return root 

		elif key.val.finalScore < root.val.finalScore: 
			root.left = self.delete(root.left, key) 

		elif key.val.finalScore > root.val.finalScore: 
			root.right = self.delete(root.right, key) 

		else: 
			if root.left is None: 
				temp = root.right 
				root = None
				return temp 

			elif root.right is None: 
				temp = root.left 
				root = None
				return temp 

			temp = self.getMinValueNode(root.right) 
			root.val = temp.val 
			root.right = self.delete(root.right, 
									temp.val) 

		if root is None: 
			return root 

		root.height = 1 + max(self.getHeight(root.left), 
							self.getHeight(root.right)) 

		balance = self.getBalance(root) 

		if balance > 1 and self.getBalance(root.left) >= 0: 
			return self.rightRotate(root) 

		if balance < -1 and self.getBalance(root.right) <= 0: 
			return self.leftRotate(root) 

		if balance > 1 and self.getBalance(root.left) < 0: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		if balance < -1 and self.getBalance(root.right) > 0: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def leftRotate(self, z): 

		y = z.right 
		T2 = y.left 

		y.left = z 
		z.right = T2 

		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		return y 

	def rightRotate(self, z): 

		y = z.left
		if y is not None:
		    T3 = y.right
		    y.right = z
		    z.left = T3

		else :
		    y = z
		    
 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		return y 
    
	def getHeight(self, root): 
		if not root: 
			return 0
        
		return root.height 

	def getBalance(self, root): 
		if not root: 
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right) 

	def getMinValueNode(self, root): 
		if root is None or root.left is None: 
			return root 

		return self.getMinValueNode(root.left)
                              
	def getMaxValueNode(self, root): 
		if root is None or root.right is None: 
			return root 

		return self.getMaxValueNode(root.right)                               
    
	def podium(self, root): 
     
		if not root: 
			return
        
		self.podium(root.right)
		print("The player {0} has a final score of {1}".format(root.val.player_id, root.val.finalScore))
		self.podium(root.left)  

	def inOrderArray(self, root, tab = None): 
		if root: 
			self.inOrderArray(root.left)
			tab.append(root)
			self.inOrderArray(root.right)
		return tab 

     
def bstToArray(bst, array):
    if bst is not None:
        if bst.val:
            bstToArray(bst.left, array)
            array.append(bst.val)
            bstToArray(bst.right, array)
        return array

def getKey(player):
        return player.finalScore
    
def playGame(players):
    game = Game(players)
    game.start()
    game.setScore_crewmate()
    game.setScore_impostors()
    game.are_winner()
    game.resetRoles()
    game.finalScoreCalculation()

def playTournament():
    ranking = None
    Avl = Ranking()
    for i in range(100):
        ranking = Avl.insert(ranking, Player(i))
        
    for i in range (3):
        allPlayers = bstToArray(ranking, [])
        allPlayers = random.sample(allPlayers, 100)
        for i in range (int(len(allPlayers)/10)):
            player_of_this_game = allPlayers[i*10:(i+1)*10]
            playGame(player_of_this_game)
    
    ranking = None
    for i in range(len(allPlayers)):
        ranking = Avl.insert(ranking, allPlayers[i])
                                                      
    while (Avl.getHeight(ranking)>10):
       allPlayers = bstToArray(ranking, [])
       allPlayers = random.sample(allPlayers, int(len(allPlayers)))
       for i in range (int(len(allPlayers)/10)):
            player_of_this_game = allPlayers[i*10:(i+1)*10]
            playGame(player_of_this_game)
       ranking = None
       for i in range(0,len(allPlayers)):
           ranking = Avl.insert(ranking, allPlayers[i])
       for i in range (10):
           ranking = Avl.delete(ranking,Avl.getMinValueNode(ranking))

    allPlayers = bstToArray(ranking, [])
    for player in allPlayers:
        player.resetScore()
    for i in range (5):
        player_of_this_game = allPlayers[:10]
        playGame(player_of_this_game)
     
    ranking = None
    for i in range(10):
        ranking = Avl.insert(ranking, allPlayers[i])
     
    print("The podium is :\n")  
    Avl.podium(ranking)
    allPlayers = sorted(allPlayers, key=getKey, reverse=True)
    print("\nList of players : \n")
    for player in allPlayers:
        print("Player ID : " + str(player.player_id) + " ;" + " Final score : " + str(player.finalScore))

if __name__ == "__main__":
    playTournament()

