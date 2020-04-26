# Runlength compression Algorithm

def compress(s):
	# Beging run as empty string
	
	r = ""
	l = len(s)

	# check for the length 0

	if l == 0:
	    return ""

	# check for length 1 
	
	if l == 1:
	    return  s + '1'

	# intialize the values

	last = s[0]
	cnt  = 1
	i  = 1

	while i < l:
		# check to see if it is the same letter
		if s[i] == s[i-1]:
		    # add count if same as previous
		    cnt += 1
		else:
			# otherwise store the previous data
			r = r +s[i-1] + str(cnt)
			cnt = 1
	# add index count to terminate while loop
		i += 1
	#put erverthing back into run 
	r = r + ss[i-1] + str(cnt)
	return r
compress('AAAAABBBBCCCC')


