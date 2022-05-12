#Experience Chart: https://docs.google.com/spreadsheets/d/1sYQTUqBOxJVputH8zmnkSFZIXA6tTsByn9aRhFqn7hk
#Experience Planning: https://docs.google.com/document/d/1iKNZmrXYtaW9B4JDMm5cNAAQKP16cdXz5JMruK--wOU

import math
from app.models import Student, Completed_Quest

MAX_EXP = 1250000
MAX_LEVEL = 100

class exp:
	#Checks if xp is over the bounds of the maximum possible xp
	def __ExpOverBounds(xp):	
		if (xp > MAX_EXP):
			return True
		else: 
			return False

	#Checks if xp is under the bounds of the minimum possible xp
	def __ExpUnderBounds(xp):
		if (xp < 0):
			return True
		else: 
			return False

	#combine over and under
	def __ExpOOB(xp):
		return (exp.__ExpOverBounds(xp) or exp.__ExpUnderBounds(xp))

		#Calculates the base amount of xp from level
	def __GetMinExpLevel(level): 
		if (level == 1): #by the formula minimum possible xp at level is 1- we want it to be 0
		   return 0
		return round((math.pow(level, 3) * 5) / 4)

		#Calculates the base amount of xp needed to get from one level to another
		#Used by ToNextLevelPercent
	def __BaseExpToNextLevel(xp):
		if (xp == MAX_EXP):
			return 0			#Max level has been reached
		level = exp.GetLevel(xp)
		return (exp.__GetMinExpLevel(level+1) - exp.__GetMinExpLevel(level)) #minimum xp of the next level - minimum xp of current level

	#Gets level of user based on their xp
	def GetLevel(xp):
		if (exp.__ExpOOB(xp)):
			return False
		if(xp <= 1):
			return 1
		if(xp == MAX_EXP):
			return 100
		return round((math.pow((4 * xp) / 5, (1/3))))

	#Calculates the amount of xp needed to get to the next level from the current xp value
	def ExpToNextLevel(xp):		
		if (exp.__ExpOOB(xp)):
			return False
		if (xp == MAX_EXP): #largest and smallest edge cases
			return 0
		if (xp == 0): #xp = 0 signifies an unused / new account- exp to next level is hardcoded as 10
			return 10
		return (exp.__GetMinExpLevel(exp.GetLevel(xp)+1) - xp)

	def ToNextLevelPercent(xp): #Calculates percentage of xp to next level. Used in student progress bar
		if (exp.__ExpOOB(xp)):
			return False
		if (exp.ExpToNextLevel(xp) == 0): #div by zero check
			return 1.0
		percent = round(1-(( exp.ExpToNextLevel(xp)) % exp.__BaseExpToNextLevel(xp)) / (exp.__BaseExpToNextLevel(xp)), 3) # (Exp to next level % base exp to next level) / base exp to next level
		if (percent == 1.0): #if percentage = 100% display 0%, since 100% means we're already displaying the next level
			return 0.0
		return percent #rounded to three decimal points

	def GainExp(studentxp, cquestxp):
		if (exp.__ExpOverBounds(studentxp + cquestxp)): #assignment class should handle xp gain modification
			return MAX_EXP
		return studentxp + cquestxp

#example
#for x in range(35):
#	print("exp: " + str(x) + " = lvl: " + str(exp.GetLevel(x)))
#for x in range(35):
#	print("lvl: " + str(exp.GetLevel(x)) + " = exp: " + str(exp._exp__GetMinExpLevel(exp.GetLevel(x))))
#for x in range(1000):
#	print("lvl: " + str(exp.GetLevel(x)) + " = base exp to next level: " + str(exp.__BaseExpToNextLevel(x)))
#for x in range(1000):
#	print("exp: " + str(x) + " = exp to next level: " + str(exp.ExpToNextLevel(x)))
#for x in range(1000):
#	print("exp: " + str(x) + " = % to next level: " + str(exp.ToNextLevelPercent(x)))
#