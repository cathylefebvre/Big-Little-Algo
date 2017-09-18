import data as d

INFO = d.data()

def makeDefaultMatches(info = INFO):
    pledges = info.getPledges()
    matches = {p: None for p in pledges}
    i = 0
    while None in matches.values(): # while any pledge doesn't have a match
        for p in pledges: # iterate through pledges
            pPref = info.getPreferenceList(p)
            for bro in pPref:
                if p in info.getPreferenceList(bro):
                    if bro not in matches.values():
                        matches[p] = bro
                        break
        if i > 5:
            print 'oops: someone never got an initial match'
            break
        i+=1
    return matches

def checkStability(matches, info = INFO):
    # check if both pledge and another bro would rather be together
    # check pledge list for every bro from 1 to match if they would switch
    if matches is None:
        return [False, "no matches have been made"]
    alreadyMatchedBros = []
    for p in info.getPledges():
        if p in matches.keys():
            if matches[p] in alreadyMatchedBros:
                return [False, "brother %s is matched to more than one pledges" %matches[p]]
            alreadyMatchedBros.append(matches[p])
            for bro in info.getPreferenceList(p):
                if bro == matches[p]:
                    # pledge prefers someone more who also prefers them more than their current match
                    if p in info.getPreferenceList(bro):
                        break
                    else:
                        return [False, "brother %s doesn't wish to be matched with pledge %s" %(bro, p)]
                else:
                    # p and bro not matched but do they want to
                    if p in info.getPreferenceList(bro): # if pledge on bro's preference list
                        for p2 in info.getPreferenceList(bro): # check their little list
                            if matches[p2] == bro: # if bro is match
                                if info.changePledges(bro, p2, p): # if bro would change from p2 to p
                                    #both brother bro and pledge p would prefer to be matched
                                    return [False, "both brother %s and pledge %s would prefer to be matched" %(bro, p)]
        else: # a pledge isn't in keys
            return [False, "pledge %s doesn't have a match" %p]
    return [True, "everyone should be happy"]

def improveMatches(matches, info = INFO):
    if matches is None:
        matches = makeDefaultMatches()
    alreadyMatchedBros =[]
    for p in info.getPledges():
        if p in matches.keys():
            if matches[p] in alreadyMatchedBros:
                doubleMatched = matches[p]
                sameBig = [p]
                for p2 in matches.keys():
                    if matches[p2] == matches[p]:
                        sameBig.append(p2)
                preferPledge = info.preferredPledge(doubleMatched, sameBig)
                for pledge in sameBig:
                    newBig = None
                    if not (pledge == preferPledge):
                        #assign new big
                        prefList = info.getPreferenceList(pledge)
                        passedOld = False
                        for bro in prefList:
                            if passedOld:
                                littlePrefList = info.getPreferenceList(bro)
                                if bro not in matches.values():
                                    if pledge in littlePrefList:
                                        newBig = bro
                                        break
                            else:
                                if bro == doubleMatched:
                                    passedOld = True
                        if newBig is None:
                            print ('Error no match to be made for %s' %pledge)
                        else:
                            matches[pledge] = newBig
                            alreadyMatchedBros.append(newBig)
            else:
                for bro in info.getPreferenceList(p):
                    if bro is matches[p]:
                        # pledge prefers someone more who also prefers them more than their current match
                        if p in info.getPreferenceList(bro):
                            break
                        else:
                            big = None
                            for bro2 in info.getPreferenceList(p):
                                littlePrefList = info.getPreferenceList(bro)
                                if bro2 not in matches.values():
                                    if pledge in littlePrefList:
                                        big = bro2
                                        break
                            if big is None:
                                print ('Error no match to be made for %s' %pledge)
                            else:
                                matches[p] = big
                                alreadyMatchedBros.append(big)
                    else:
                        if p in info.getPreferenceList(bro):  # if pledge on bro's preference list
                            for p2 in info.getPledges():  # check other pledge
                                if matches[p2] == bro:  # if bro is match
                                    if info.changePledges(bro, p2, p):  # if bro would change from p2 to p
                                        # both brother bro and pledge p would prefer to be matched
                                        newBig2 = None
                                        for bro2 in info.getPreferenceList(p2):
                                            if bro2 not in matches.values():
                                                if p2 in info.getPreferenceList(bro2):
                                                    newBig2 = bro2
                                                    break
                                        if newBig2 is not None:
                                            matches[p] = bro
                                            matches[p2] = newBig2
                                            alreadyMatchedBros.append(newBig2)
        else:
            pPref = info.getPreferenceList()
            for bro in pPref:
                if p in info.getPreferenceList(bro):
                    matches[p] = bro
        alreadyMatchedBros.append(matches[p])
    return matches

print 'PLEDGES'
print '--------------'
for p in INFO.getPledges():
    print p
    print INFO.getPreferenceList(p)
print 'BROS'
print '--------------'
for b in INFO.getBros():
    print b
    print INFO.getPreferenceList(b)
matches = makeDefaultMatches()
stabilityResult = checkStability(matches)
print 'Default Matches ----'
print matches
print stabilityResult[1]
i = 1
while not stabilityResult[0]:
    matches = improveMatches(matches)
    stabilityResult = checkStability(matches)
    print ('after run %i ----') %i
    print matches
    print stabilityResult[1]
    i+=1
    if i > 10:
        break
if stabilityResult[0]:
    for match in matches:
        print ('%s matched with %s' %(match, matches[match]))