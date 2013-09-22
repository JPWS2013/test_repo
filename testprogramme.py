import numpy as np


def gradientdescentalgorithm(dataset, alpha, thetazero, thetaone, thetatwo, thetathree):
	
	#Initial Parameters
	#dataset=np.array(indataset)
	thetazero=float(thetazero)
	thetaone=float(thetaone)
	thetatwo=float(thetatwo)
	thetathree=float(thetathree)
	meanerror=1000
	meanerror2=1000
	threshold=0.001
	iterationcounter=0
	meanerrorcollection={}

	#Data Processing

	xvalues=dataset['XValues']

	yvalues=dataset['YValues']


	#xvalues=dataset[0, :]

	

	while (abs(meanerror) >= threshold) or (abs(meanerror2) >= threshold) or (abs(meanerror3) >= threshold): # or (abs(meanerror4) >= threshold): #(iterationcounter<1):
		if iterationcounter==1000000:
			break

		errorlistzero=[]
		errorlistone=[]
		errorlisttwo=[]
		errorlistthree=[]

		#xvalues=dataset[0,:]

		for i in range (len(xvalues)):


			inputvariable=float(xvalues[i])
			outputvariable=float(yvalues[i])

			#print 'input variable', inputvariable
			
			prediction= thetazero + (thetaone*inputvariable) + (thetatwo * inputvariable*inputvariable)# + (thetathree * inputvariable * inputvariable * inputvariable)
			error=prediction - (outputvariable)

			#print 'Error', error

			errorzeroholder=error
			#print 'errorzeroholder', errorzeroholder
			errorlistzero.append(errorzeroholder)
			#print errorlistzero

			erroroneholder=error*inputvariable
			#print 'erroroneholder', erroroneholder
			errorlistone.append(erroroneholder)
			#print errorlistone

			errortwoholder=error*(inputvariable*inputvariable)
			#print 'errortwoholder', errortwoholder
			errorlisttwo.append(errortwoholder)
			#print errorlisttwo

			#errorthreeholder=error*(inputvariable*inputvariable*inputvariable)
			#print 'errorthreeholder', errorthreeholder
			#errorlistthree.append(errorthreeholder)
			#print errorlistthree

		thetazero = thetazero - alpha*(1/(float(len(xvalues))))*sum(errorlistzero)
		thetaone = thetaone - alpha*(1/(float(len(xvalues))))*sum(errorlistone)
		thetatwo = thetatwo - alpha*(1/(float(len(xvalues))))*sum(errorlisttwo)
		#thetathree = thetathree - alpha*(1/(float(len(xvalues))))*sum(errorlistthree)

		print [thetazero, thetaone, thetatwo]#, thetathree]

		meanerror=sum(errorlistzero)/float(len(xvalues))
		meanerror2=sum(errorlistone)/float(len(xvalues))
		meanerror3=sum(errorlisttwo)/float(len(xvalues))
		#meanerror4=sum(errorlistthree)/float(len(xvalues))

		meanerrorcollection[meanerror]=[thetazero, thetaone, thetatwo, thetathree]
		iterationcounter += 1


	#return [thetazero, thetaone, thetatwo]#, thetathree]


	if (abs(meanerror) <= 0.00000001) or (abs(meanerror2) <= 0.00000001):

		print "I'm Perfect!"
		return [thetazero, thetaone, thetatwo, thetathree]

	else:

		listoferrors=meanerrorcollection.keys()
		listoferrors.sort()
		keytoanswer=listoferrors[-1]
		answer=meanerrorcollection[keytoanswer]
		return [answer, iterationcounter]