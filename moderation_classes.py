class Categories:
    def __init__(self, harassment, harassment_threatening, hate, hate_threatening, self_harm, self_harm_instructions, self_harm_intent, sexual, sexual_minors, violence, violence_graphic):
        self.harassment = harassment
        self.harassment_threatening = harassment_threatening
        self.hate = hate
        self.hate_threatening = hate_threatening
        self.self_harm = self_harm
        self.self_harm_instructions = self_harm_instructions
        self.self_harm_intent = self_harm_intent
        self.sexual = sexual
        self.sexual_minors = sexual_minors
        self.violence = violence
        self.violence_graphic = violence_graphic

class CategoryScores:
    def __init__(self, harassment, harassment_threatening, hate, hate_threatening, self_harm, self_harm_instructions, self_harm_intent, sexual, sexual_minors, violence, violence_graphic):
        self.harassment = harassment
        self.harassment_threatening = harassment_threatening
        self.hate = hate
        self.hate_threatening = hate_threatening
        self.self_harm = self_harm
        self.self_harm_instructions = self_harm_instructions
        self.self_harm_intent = self_harm_intent
        self.sexual = sexual
        self.sexual_minors = sexual_minors
        self.violence = violence
        self.violence_graphic = violence_graphic

class Moderation:
    def __init__(self, categories, category_scores, flagged):
        self.categories = categories
        self.category_scores = category_scores
        self.flagged = flagged
