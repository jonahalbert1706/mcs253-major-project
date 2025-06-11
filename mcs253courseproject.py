class VARK:

    #Creating first dictionary of questions with options
    questions=[{"question_text":"1.You are helping someone who wants to go to your airport,town centre or railway station.You would:",
                 "options":["a)go with her.","b)tell her the directions.","c)write down the directions.","d)draw, or give her a map."]},
                {"question_text":"2.You are not sure whether a word should be spelled `dependent' or `dependant'.You would:",
                 "options":["a)see the words in your mind and choose by the way they look.","b)think about how each word sounds and choose one.","c)find it in a dictionary.","d)write both words on paper and choose one."]},
                {"question_text":"3.You are planning a holiday for a group.You want some feedback from them about the plan.You would:",
                 "options":["a)describe some of the highlights.","b)use a map or website to show them the places.","c)give them a copy of the printed itinerary.","d)phone, text or email them."]},
                {"question_text":"4.You are going to cook something as a special treat for your family.You would:",
                 "options":["a)cook something you know without the need for instructions.","b)ask friends for suggestions.","c)look through the cookbook for ideas from the pictures.","d)use a cookbook where you know there is a good recipe."]},
                {"question_text":"5.A group of tourists want to learn about the parks or nature reserves in your area.You would:",
                 "options":["a)talk about, or arrange a talk for them about parks or nature reserves.","b)show tnet pictres, photographs or picture books.","c)take them to a park or nature reserve and walk with them.","d)give them a book or pamphlets about the parks or nature reserves."]},
                {"question_text":"6.You are about to purchase a digital camera or mobile phone.Other than price,what would most influence your decision?:",
                 "options":["a)Trying or testing it.","b)Reading the details about its features.","c)It is a modernu design and looks good.","d)The salesperson telling me about its features."]},
                {"question_text":"7.Remember a time when you learned how to do something new.Try to avoid choosing a physical skill, e.g. riding a bike. You learned best by:",
                 "options":["a)watching a demonstration.","b)listening to somebody explaining it and asking questions.","c)diagrams and charts - visual clues.","d)written instructions – e.g. a manual or textbook."]},
                {"question_text":"8.You have a problem with your knee.You would prefer that the doctor:",
                 "options":["a)gave you a web address or something to read about it.","b)used a plastic model of a knee to show what was wrong.","c)described what was wrong.","d)showed you a diagram of what was wrong."]},
                {"question_text":"9.You want to learn a new programme,skill or game on a computer.You would:",
                 "options":["a)read the written instructions that came with the programme.","b)talk with people who know about the programme.","c)use the controls or keyboard.","d)follow the diagrams in the book that came with it."]},
                {"question_text":"10.I like websites that have:",
                 "options":["a)things I can click on, shift or try.","b)interesting design and visual features.","c)interesting written descriptions, lists and explanations.","d)audio channels where I can hear music, radio programmes or interviews."]},
                {"question_text":"11.Other than price,what would most influence your decision to buy a new non-fiction book?",
                 "options":["a)The way it looks is appealing.","b)Quickly reading parts of it.","c)A friend talks about it and recommends it.","d)It has real-life stories, experiences and examples."]},
                {"question_text":"12.You are using a book, DVD or website to learn how to take photos with your new digital camera.You would like to have:",
                 "options":["a)a chance to ask questions and talk about the camera and its features","b)clear written instructions with lists and bullet points about what to do","c)diagrams showing the camera and what it each part does","d)many examples on good and poor photos and how to improve them"]},
                {"question_text":"13.Do you prefer a trainer or a presenter who uses:",
                 "options":["a)demonstrations, models or practical sessions.","b)question and answer, talk, group discussion, or guest speakers.","c)handouts, books, or readings.","d)diagrams, charts or graphs."]},
                {"question_text":"14.You have finished a competition or test and would like some feedback.You would like to have feedback:",
                 "options":["a)using examples from what you have done.","b)using a written description of your results.","c)from somebody who talks it through with you.","d)using graphs showing what you had achieved."]},
                {"question_text":"15.You are going to choose food at a restaurant or cafe.You would:",
                 "options":["a)choose something that you have had there before.","b)listen to the waiter or ask friends to recommend choices.","c)choose from the descriptions in the menu.","d)look at what others are eating or look at pictures of each dish."]},
                {"question_text":"16.You have to make an important speech at a conference or special occasion.You would:",
                 "options":["a)make diagrams or get graphs to help explain things.","b)write a few key words and practice saying your speech over and over.","c)write out your speech and learn from reading it over several times.","d)gather many examples and stories to make the talk real and practical."]}
                ]    

    #Creating second dictionary from options in questions to VARK scorng chart
    scoring_chart={
        1:{"A":"K","B":"A","C":"R","D":"V"},
        2:{"A":"V","B":"A","C":"R","D":"K"},
        3:{"A":"K","B":"V","C":"R","D":"A"},
        4:{"A":"K","B":"A","C":"V","D":"R"},
        5:{"A":"A","B":"V","C":"K","D":"R"},
        6:{"A":"K","B":"R","C":"V","D":"A"},
        7:{"A":"K","B":"A","C":"V","D":"R"},
        8:{"A":"R","B":"K","C":"A","D":"V"},
        9:{"A":"R","B":"A","C":"K","D":"V"},
        10:{"A":"K","B":"V","C":"R","D":"A"},
        11:{"A":"V","B":"R","C":"A","D":"K"},
        12:{"A":"A","B":"R","C":"V","D":"K"},
        13:{"A":"K","B":"A","C":"R","D":"V"},
        14:{"A":"K","B":"R","C":"A","D":"V"},
        15:{"A":"K","B":"A","C":"R","D":"V"},
        16:{"A":"V","B":"A","C":"R","D":"K"}
    }

    for question in questions:
       print(question["question_text"])

       for option in question["options"]:
           print(option) 
       print()      

    def __init__(self):
        self.responses={"V":0,"A":0,"R":0,"K":0}

    def ask_question(self, q_num):
         if q_num not in self.scoring_chart:
             raise ValueError(f"Invalid question number: {q_num}")
         print(f"\nQuestion {q_num}:") 
         print("A) Option A") 
         print("B) Option B") 
         print("C) Option C")
         print("D) Option D") 
         print("You may choose one or two answers (e.g.,A or AC):")
         
         while True:
             response=input("Enter your choice(s):").upper().strip()
            
             #Check if input is 1 or 2 letters and all are valid choices
             if (len(response)in [1,2])and all(c in['A','B','C','D']for c in response):
                 if len(set(response))!=len(response):#Optional: prevent duplicate letters like "AA"
                     print("Duplicate choices detected.Please choose different options.")
                     continue
                 break
             else:
                 print("Invalid input.Please enter one or two letters from A,B,C or D.")

         categories=self.scoring_chart[q_num]   
         for choice in response:
             selected_category=categories[choice]
             self.responses[selected_category]+=1

    def calculate_scores(self):
        total = sum(self.responses.values()) 
        if total == 0:
             raise ValueError("No responses recorded. Please answer all questions.")
        print("\nYour VARK Scores:")
        for category, score in self.responses.items(): 
            print(f"{category}: {score}") 
        return self.responses 
    
    def determine_preference(self): 
        scores = self.calculate_scores() 
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_score = sorted_scores[0][1] 
        top_categories = [category for category, score in sorted_scores if score == top_score] 
        if len(top_categories) == 1: 
            print(f"\nYour primary learning preference is: {top_categories[0]}") 
        else: 
            print(f"\nYou have a multimodal learning preference: {', '.join(top_categories)}") 
    
    def run(self): 
        try:
          for i in range(1, 17): 
              self.ask_question(i) 
              self.determine_preference() 
        except ValueError as e:
              print(f"Error: {e}") 
        
if __name__ == "__main__": 
    vark_test = VARK() 
    vark_test.run()            