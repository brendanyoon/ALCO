#Experience Chart: https://docs.google.com/spreadsheets/d/1sYQTUqBOxJVputH8zmnkSFZIXA6tTsByn9aRhFqn7hk
#Experience Planning: https://docs.google.com/document/d/1iKNZmrXYtaW9B4JDMm5cNAAQKP16cdXz5JMruK--wOU

import math

MAX_EXP = 1250000
MAX_LEVEL = 100

class exp:

	#Checks if xp is over the bounds of the maximum possible xp
	#Used in GainExp
	def ExpOverBounds(xp):	
		if (xp > MAX_EXP):
			return True
		else: 
			return False

	def roundup(xp):
		return ((xp * 100 + 1) / 100)

	#Gets level of user based on their xp
	#IMPORTANT NOTE: GetLevel returns a number from 0-99, add 1 in displays for actual level
	def GetLevel(xp):
		return math.floor(exp.roundup(math.pow((4 * xp) / 5, (1/3))))
	
	#Calculates the base amount of xp from level
	def GetExpFromLevel(level): 
		return round((math.pow(level, 3) * 5) / 4)

	#Calculates the base amount of xp needed to get from one level to another
	def BaseExpToNextLevel(xp):
		if (xp == MAX_EXP):
			return 0			#Max level has been reached
		level = exp.GetLevel(xp)
		return exp.GetExpFromLevel(level+1) - exp.GetExpFromLevel(level)

	#Calculates the amount of xp needed to get to the next level from the current xp value
	def ExpToNextLevel(xp):		
		return (exp.GetExpFromLevel(exp.GetLevel(xp)+1) - xp)

	def ToNextLevelPercent(xp): #Calculates percentage of xp to next level. Used in student progress bar
		if (round(exp.ExpToNextLevel(xp) / exp.BaseExpToNextLevel(xp), 3) == 1.0): #if percentage = 100% display 0%
			return 0.0
		return round(exp.ExpToNextLevel(xp) / exp.BaseExpToNextLevel(xp), 3) #rounded to three decimal points

#	def GainExp(student, assignment):		#This code is commented out because it needs a student and assignment class.
#		if ((student.xp + assignment.xp) > MAX_EXP): #assignment class should handle xp gain modification
#			student.xp = MAX_EXP
#			return
#		student.xp += xp
#		return

#example run
#xprn = 270
#print(exp.GetLevel(xprn))
#print(exp.ExpToNextLevel(xprn))
#print(exp.ToNextLevelPercent(xprn))