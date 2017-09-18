"""
File made by Cathy Lefebvre
v 1.2
To be used to extract pledge and brother preference lists from csv files titled
BigListChoices.csv
AND
LittleListChoices.csv
"""
import csv

class data():
    def __init__(self):
        with open('BigListChoices.csv', 'rb') as pledgeLists:
            self.pledgeprefers = {}
            pledgeListR = csv.reader(pledgeLists)
            for row in pledgeListR:
                list = []
                for name in (row[x] for x in range(1, len(row))):
                    if (not name == '') and name is not 'None':
                        list.append(name)
                if list is not []:
                    self.pledgeprefers[row[0]] = list
        with open('LittleListChoices.csv', 'rb') as littleLists:
            self.brosprefers = {}
            broListR = csv.reader(littleLists)
            for row in broListR:
                list = []
                if row[1] == 'Yes':
                    for name in (row[x] for x in range(2, len(row))):
                        if not(name == '' or name == 'None' or name == 'Hayden Zelle' or name == 'Alexis Wilson'):
                            list.append(name)
                self.brosprefers[row[0]] = list

        self.pledges = sorted(self.pledgeprefers.keys())
        self.bros = sorted(self.brosprefers.keys())

    def getPledges(self):
        return self.pledges
    def getBros(self):
        return self.bros
    def getBroPreferences(self):
        return self.brosprefers
    def getPledgePreferences(self):
        return self.pledgeprefers
    def changePledges(self, bro, old, new):
        broPrefList = self.getPreferenceList(bro)
        if broPrefList.index(old) > broPrefList.index(new):
            return True # new pledge is smaller num on list therefor bro wants to change pledges
        else:
            return False
    def preferredPledge(self, bro, pledges):
        broPrefList = self.getPreferenceList(bro)
        pref = None
        for p in pledges:
            if pref is None:
                pref = p
            else:
                if broPrefList.index(p) < broPrefList.index(pref):
                    pref = p
        return pref
    def getPreferenceList(self, person):
        try:
            if self.pledgeprefers[person] is not None:
                return self.pledgeprefers[person]
        except KeyError:
            try:
                if self.brosprefers[person] is not None:
                    return self.brosprefers[person]
            except KeyError:
                return [ ]