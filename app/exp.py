#Experience Chart: https://docs.google.com/spreadsheets/d/1sYQTUqBOxJVputH8zmnkSFZIXA6tTsByn9aRhFqn7hk
#Experience Planning: https://docs.google.com/document/d/1iKNZmrXYtaW9B4JDMm5cNAAQKP16cdXz5JMruK--wOU

import math

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
		return round((math.pow(level, 3) * 5) / 4)

	#Calculates the base amount of xp needed to get from one level to another
	def __BaseExpToNextLevel(xp):
		if (xp == MAX_EXP):
			return 0			#Max level has been reached
		level = exp.GetLevel(xp)
		return (exp.__GetMinExpLevel(level+1) - exp.__GetMinExpLevel(level))

	#Gets level of user based on their xp
	def GetLevel(xp):
		if (exp.__ExpOOB(xp)):
			return False
		if(xp <= 1):
			return 1
		return math.floor((math.pow((4 * xp) / 5, (1/3))))

	#Calculates the amount of xp needed to get to the next level from the current xp value
	def ExpToNextLevel(xp):		
		if (exp.__ExpOOB(xp)):
			return False
		if (xp == MAX_EXP): #largest and smallest edge cases
			return 0
		if (xp == 0): 
			return 10
		return (exp.__GetExpFromLevel(exp.GetLevel(xp)+1) - xp)

	def ToNextLevelPercent(xp): #Calculates percentage of xp to next level. Used in student progress bar
		if (exp.__ExpOOB(xp)):
			return False
		if (exp.ExpToNextLevel(xp) == 0): #stop before we div by zero
			return 1.0
		if (round(exp.__BaseExpToNextLevel(xp) / exp.ExpToNextLevel(xp), 3) == 1.0): #if percentage = 100% display 0%
			return 0.0
		print(str(exp.__BaseExpToNextLevel(xp)) + "/" + str(exp.ExpToNextLevel(xp)) + "=" + str(exp.__BaseExpToNextLevel(xp) / exp.ExpToNextLevel(xp)))
		return round(exp.__BaseExpToNextLevel(xp) / exp.ExpToNextLevel(xp), 3) #rounded to three decimal points

#	def GainExp(student, assignment):		#This code is commented out because it needs a student and assignment class.
#		if (__ExpOverBounds(assignment.xp + student.xp)): #assignment class should handle xp gain modification
#			student.xp = MAX_EXP
#			return
#		student.xp += assignment.xp
#		return

#example
#for x in range(35):
#	print("exp: " + str(x) + " = lvl: " + str(exp.GetLevel(x)))
for x in range(35):
	print("lvl: " + str(exp.GetLevel(x)) + " = exp: " + str(exp._exp__GetMinExpLevel(exp.GetLevel(x))))
for x in range(35):
	print("lvl: " + str(exp.GetLevel(x)) + " = exp to next level: " + str(exp._exp__BaseExpToNextLevel(x)))