number = input()
goto check

label: negative
print "negative"
goto end

label: check
if number < 0: goto negative
if number % 2 == 0:
   print "even"
else:
   print "odd"
goto end

label: end
print "all done"
