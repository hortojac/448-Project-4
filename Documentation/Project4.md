#### Estimation of Person-Hours/Accounted Person-Hours: 
https://docs.google.com/spreadsheets/d/1lUsOUC2fbRDljCjvxWwighowklgWpwoVV_gzfDf-2TM/edit#gid=1967042640

#### Project 4 Documentation: 
https://docs.google.com/document/d/1Y1f8yEngeXtnqst9F6WEZM8Fzxa15KDxY3OeZn9bmt8/edit?usp=sharing

### Defect Tracking Tool:
https://docs.google.com/spreadsheets/d/1Zfy883qJayRSzOiYt2UFosgWxxOhcStMqA-susdaAoQ/edit#gid=0

### Video

https://youtu.be/08DgjTpNVIM

# Our Project: Game Suite
We are developing a game suite, stocked with 5 fun and exciting games to play:
 - BlackJack 
 - Connect 4 
 - Tic-Tac-Toe 
 - Wordle 
 - Rock Paper Scissors Lizard Spock 


### Story Point Estimation

| 1 | 2 | 3 | 5 | 8 | 13 | 
| :-- | :-- | :-- | :-- | :-- | :-- | 
|Assign Games|RPSLS Check Wins |Code Review|Write up Documentation(Code Integration)|Connect 4 Gui|Blackjack AI|
|Determining Projected Tasks|Tic-Tac-Toe set up Board|RPSLS Check Wins|Integrate code into main branch once finished |Write up Documentation( Deployment Plan, Maintenance Plan) |Wordle get Letter Colors|
|Installing proper libraries|Wordle show Incorrect|Blackjack check wins|Tic Tac Toe check wins|Test Suite|Connect 4 check wins|

#### Reasoning for estimation:
- We set each story point to have a time value of 40 minutes
- Since project 4 is the implementation of the prototype we had earlier, we knew it would take much longer to do than project 3. Each game was broken down into some main components/functions, and we assigned those points based on our battleship Game and how long it took us to implement similar functions there.


### Integration Strategy

All of our games are individualized and do not share much code between each other. The one thing each game does share is the GUI library called Tkinter for python. Tkinter uses “frames” to show widgets suchs as labels and buttons which hold information or when clicked can call a function. This means that games or software is heavily button based. For example: Tic Tac Toe: Click a button where you want your piece to be, either an X or O. BlackJack: Click a button for Hit, Deal Cards, and Stand. RPSLS: Click your option for either Rock, Paper, Scissors, Lizard, or Spock. Connect4: Click which column you would like your colored piece to go. Wordle: The only exception to button pressing. During gameplay, the use of the keyboard is how you play. Our main menus could be of similarity with similar code structure. We all could have a play or start button, rules, or exit button. These all perform similar functions. The integration strategy our team used for each of our games would be the Top-Down Integration. Based on the graph in the lecture slides. Artifact A would be the main menu when you run our main.py. file. When a button to play a certain game is clicked, that game file is then run, this would be artifacts B, C, D, etc. This would be the next level down. Each game is made up of a frame or multiple frames, that are cycled through with buttons showing different information, each frame in order, would be the next level in Top-Down Integration. Without Frame 1 and its button to call the raise function for frame 2, we can’t show the information on frame 2.

### Deployment Plan

There are several routes we can take to deploy our project, but the most ideal platforms would be mobile as an app (cross-platform) and desktop- on the App Store, Microsoft, and Web. To deploy it on the iOS app store, we need to prepare the project for distribution in line with apple’s requirements and do the same for Play.

To develop the app for iOS. It needs to be coherent with apple’s deployment requirements. In order to meet those requirements, We need to enroll in Apple’s Developer Program, Create an iOS distribution provision profile and distribution certificate, Create an App Store Connect record for the app, Configure the app’s metadata and other details in App Store’s Connect record, and finally submit the app for review and wait for the approval. The cost to distribute on apple’s platform will cost $99 every year.

 More can be read here:[ How to Submit Your App to the App Store in 2022 | Instabug Blog](https://instabug.com/blog/how-to-submit-app-to-app-store/)

Similarly, for Android deployment, we need to create a Google Developer Account, then Link the account to Merchant Account for in-app purchases, Configure the app for Google’s technical requirements, upload it to the google console, and finally publish the app. Overall cost for Google’s play store is one time payment of $25.

More can be read here:[ Preparing Your App for Distribution | Apple Developer Documentation](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution)

To get the app in Microsoft Store, We need to first configure the app with the Configuration Manager Client (online version) from Microsoft, then Provision the windows app packages for all users, Register to Azure AD tenant, Set up synchronization, Upload the app, and finally Manage the app. The overall cost for Microsoft Deployment is $20.

More can be read here:  [Microsoft Store apps - Configuration Manager | Microsoft Docs](https://docs.microsoft.com/en-us/mem/configmgr/apps/deploy-use/manage-apps-from-the-windows-store-for-business)

To deploy our arcade games for the web, we need to develop a website interface, find a hosting server that would cost about 10$ monthly, purchase a domain name that costs around $20 a year, then move the website to the server. We would also need to hire front-end developers as well and we’re estimating it would take about a week to complete the front end, the cost associated with that is around $2000 dollars (40 hours * $50 per hour = 2000). The overall cost is estimated to be around 2300$ to start and $140/yearly.

Overall, the costliest would be the deployment for the web as compared to the iOS, Android, or Microsoft Store. To combat the cost, we can include in-app purchases later with updates, charge customers to download the app, or/and add advertisements.

The potential market for our arcade game consists of family entertainment, teenagers, and arcades since our game arcade is entirely all age-friendly. Our games like Tic-Tac-Toe, Connect Four, and Rock Paper Scissors Lizard Spock are meant to attract young people, 13 and younger. While games like Wordle and Blackjack are focused on the older population, 13 and up.

We intend to advertise our game on the web on platforms such as YouTube and other apps.

### Maintenance Plan

In order to maintain our product for the next year we would need to hire some software developers. Since our product consists of 5 different games the best way to support our product would be to hire a software developer for each game. Having a clear role for each developer would lead to more organization and structure for the team. Being that we are a small startup the base salary would be $80,000 for each developer for the first year. The main role of each developer would be to maintain the code by fixing bugs and making improvements to the game. When hiring developers it is important that we hire people who are interested in our product. In order to create a successful team it is crucial that the team members feel that they are working on something important to them. In addition to the five developers, I think it would be important to hire a marketing agent. The job of the developers is to make improvements to our product, but without any customer feedback this would be difficult. In order to make our product known and accessible we need a marketing agent to advertise our game. Advertising and promoting our product is also crucial in order to increase sales, since at the end of the day we need money to pay our employees and maintain our product. The base salary for the marketing agent would be $40,000. The last person to hire would be a project manager. This person would oversee all other employees and approve any new improvements or changes to the product. They would meet with clients and present the feedback to the rest of the team. They would lead all meetings as well. The project manager base salary would be $100,000. Total cost of paying employees would be $540,000. Our game would be put on the app store and available for download. For the first year our game will initially be free to download. In the beginning, the main form of revenue will be from any ads that we put on the game. Initially, it is important to make our game well known and popular before charging users money. In addition, we would have a premium membership that customers could pay for as a monthly subscription of $6.99. The premium version would remove all ads and allow users to play any game an unlimited amount of times a day. Another important role of the software developers is not just to maintain the current version of the game but receive feedback on what users enjoy in order to create more games. Eventually there would be more game options and some exclusive games that only premium members would have access to. Another role of the software developers would be to enhance any of the two person games to have an ai. This feature could bring in more revenue since we could add a feature to allow customers to bet money against the ai. For example, you could bet real money against the dealer playing blackjack or the ai in rock paper scissors. For the two person games such as connect 4 or tic-tac-toe the developers could also add a feature to play against someone on a different phone. Having a diverse set of features makes our game attract a larger audience, leading to more revenue as well as necessary money for maintenance and salaries.  

### Code Review

#### RPSLS

![](https://media.discordapp.net/attachments/934294285883428875/968009916411437107/unknown.png)


* The error was an “Image not Found” error for every image used in RPSLS.
* This error occurred 7 times 
    * 7 images used for RPSLS game
    * Error occurred once in each code section to load an image
* Luca StockWil was assigned to fix it
* Faults fixed by correcting the file path used in the Image.open() lines of code.
    * Since the images used were stored inside a folder in Assets called “rpsls”, the correct asset path for each image should be “assets/rpsls/[image_name].jpeg”.
* After changing relative file paths, all images loaded and worked correctly for this game.

#### Blackjack

![](https://media.discordapp.net/attachments/934294285883428875/968010258712768512/unknown.png)

* The error was an Ace card needed to be converted to a 1 if the total of all cards equated to more than 21.
* This error occurred only when dealt an Ace.
* Jacob Horton was assigned to fix it.
* Fault fixed by enumerating through player_card_index and setting the Ace card to 1 in the player_card_index list. New player_total would be calculated. Then if total is > 21 then player busts else if total = 21, player wins. 

#### Tic-Tac-Toe

```python
   def checkWin(scores):
       place = len(scores)
       if(place<3):
           return 0
       else:
           for i in range(place):
               for j in range(place):
                   for k in range(place):
                           total = scores[i] + scores[j] + scores[k]

                           if(total == 15 and (scores[i] != scores[j]) and (scores[j] != scores[k]) and (scores[i] != scores[k])):
                               return 1

```

* This function checks for all cases of “won” after third click for each player. This function produced an error for some cases and was outputting wins even for cases that wasn’t considered win.
* It was reported by Bikash on the 20th and fixed the same day by him
* The cause was each loop was looking at the index twice and returning the sum.
    * For example if the values in P1 list was [1,2,3,4], 1 was looked at and added by each variable like 1(i) + 1(j) + 1(k)
* The solution was to add check conditions **<code>(scores[i] != scores[j]) and (scores[j</code></strong> to make sure the same index wasn’t being added when looping through it again using another variable and finding the sum.

#### Connect 4

```python
if(col<4 and col>0 and row>0 and row<5 ):
       if (label_ids[row][col].cget('fg')=='red'
       and label_ids[row+1][col+1].cget('fg')=='red'
       and label_ids[row+2][col+2].cget('fg')=='red'
       and label_ids[row-1][col-1].cget('fg')=='red'):
           label_frame2.destroy()
           win_frame.grid(row=0, column=0)
           disable()
       if (label_ids[row][col].cget('fg')=='blue'
       and label_ids[row+1][col+1].cget('fg')=='blue'
       and label_ids[row+2][col+2].cget('fg')=='blue'
       and label_ids[row-1][col-1].cget('fg')=='blue'):
           win_frame.configure(text="Player 2 wins!!!")
           win_frame.grid(row=0, column=0)
           label_frame2.destroy()
           disable()

```

* This code segment shows one of the checks to see if a player has won the game by getting 4 in a row diagonally. The check takes the current index of the last dropped piece and checks if there is one piece of the same color above and two pieces of the same color below in a negative slope. When testing this code snippet there sometimes would be an index out of range error. 
* Julia Nichols was assigned to fix this error
* The fault was fixed after realizing that the initial if statement was incorrect. The rows and cols should have been flipped around since the only options for rows was 0-5 but if row 4 was passed in as a parameter then row+2 would cause an index error. 

#### Wordle

![](https://cdn.discordapp.com/attachments/934294285883428875/968010731951886346/unknown.png)

This code block calculates the array of colors to be passed to the GUI handler to change the colors of the letters according to the game rules (green is the correct spot, yellow is in the wrong spot, gray is not in the word). Letters would change to the wrong colors at times (e.g. if there was a double letter like **lorry**, a guess with **rears** would not have the first **r** turn the correct color, yellow). Tram-Anh was assigned to fix this, and it was fixed by adding an additional boolean array to track what letters were already handled and adding an additional helper function, <code>get_first_unique_occurance</code></strong>, which would find the first unique occurrence of a letter, which would help with checking doubles. 


### Test Suite

* Implemented as a semi-automatic algorithm that ensures each game launches and exits properly
* To run, launch main.py and click the “Test Suite” button
* This button will procedurally open each game
* To test, close each game as they pop up
* Console will display results of each game
    * Closing the game within 5 seconds of it popping up will signify the game launches and exits successfully, and the test will be passed
    * If it takes the user longer than 5 seconds to close the game, that likely signifies a  program error or delays caused by the local machine–both undesired results for our program.
    * Console displays if the game passed or failed the 5-second test
    * Console displays total  runtime of the game
