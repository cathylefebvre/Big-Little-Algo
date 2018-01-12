# Big-Little-Algo
This is the big-little matching algo used for the Psi Upsilon fraternity at the Gamma Tau Chapter.
The ideas behind this come from the idea that matching bigs and littles is much like the stable marriage problem, and the principles of Gale-Shapley algorithm to pair pledges with brother; however, in this case, pledges' prefrences do take precedence.
If you are the current VP of Member Ed needing help running the big-little algo, ask Cathy Lefebvre or a previous Member Ed. 

## Steps to Run the Algo
1. When getting the lists try to minimize spelling errors every name must be spelled the EXACT same way (capitalization does matter). Pledge list should be bigger with larger pledge classes or smaller brotherhoods.
2. Make sure you have python downloaded on your computer (https://www.python.org/downloads/) and the path set-up appropriately as well.  
	+ Almost any CS (and some non-CS majors) major can help you with this.  
3. Create BigListChoices.csv and LittleListChoices.csv (USE THESE EXACT NAMES)  
  a. These are comma seperated value files  
  b. Do not put in a header/title line  
  c. For BigListChoices.csv, add every pledges list, with every line being:
    * Pledge, (Bro Choice 1), (Bro Choice 2), (Bro Choice 3), etc.    
    * Ozzie Ozburn, Emily Huskins, Cathy Lefebvre, Henry Leung, etc.  
 d. For LittleListChoices.csv, add every bro’s list and whether they want a little at all, with every line being:  
    * Brother, (Yes/No), (Pledge Choice 1), (Pledge Choice 2), (Pledge Choice 3), etc.    
    * Cathy Lefebvre, Yes, Ozzie Ozburn, Emily Gardner, Alexis Wilson, etc.  
    * The brothers list can have as many or few pledge name as the brother wishes.  
4. **_If a pledge has been depledged or dropped and therefore do not have a list or need a big, make sure their name is not on any of the brother’s list._**
5. Open command line in the folder where you have the csv files, data.py and matching.py
6. Enter “python matching.py”
7. The code should run and the final matches should show up in the format:  
	-(Pledge) matched with (Brother)  
	-Double check nothing went crazy by looking at lists in terms of matches  
8. If it doesn’t show up with matches in above format or says error at all, contact Cathy Lefebvre.
