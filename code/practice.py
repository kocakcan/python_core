class Boss:
	def __init__(self, name: str, location: str, hp: int, souls: int, rewards: list[str]):
		self._name = name
		self._location = location
		self._hp = hp
		self._souls = souls
		self._rewards = rewards

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name: str):
		self._name = name

	@name.deleter
	def name(self):
		del self._name

	@property
	def rewards(self):
		return self._rewards
	
	@rewards.setter
	def rewards(self, rewards: str):
		self._rewards = rewards

	@rewards.deleter
	def rewards(self):
		del self._rewards

	def __str__(self):
		return f"Name: {self._name} | Location: {self._location} | HP: {self._hp} | Souls: {self._souls} | Rewards: {self._rewards}"

def main():
	artorias = Boss("Knight Artorias", "Royal Wood", 3750, 50000, ["Soul of Artorias", "Humanity"])
	manus = Boss("Manus, Father of the Abyss", "Chasm of the Abyss", 6665, 60000, ["Soul of Manus", "Humanity (x10)"])
	kalameet = Boss("Black Dragon Kalameet", "Royal Wood", 5400, 60000, ["Calamity Ring", "Obsidian Greatsword (tail cut)"])
	gwyn = Boss("Gwyn, Lord of Cinder", "Kiln of the First Flame", 4185, 70000, ["Soul of Gwyn, Lord of Cinder"])

	bosses: list[Boss] = [artorias, manus, kalameet, gwyn]

	for _ in bosses:
		print(_)

if __name__ == "__main__":
	main()
