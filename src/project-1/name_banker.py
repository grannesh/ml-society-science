import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas

class NameBanker:
    
    # Fit the model to the data.  You can use any model you like to do
    # the fit, however you should be able to predict all class
    # probabilities
    def fit(self, X, y):
        self.data = [X, y]
        model = LogisticRegression().fit(X, y)
        return model

    # set the interest rate
    def set_interest_rate(self, rate):
        self.rate = rate
        return

    # Predict the probability of failure for a specific person with data x
    def predict_proba(self, x):
        return model.predict_proba(x)
        

    # THe expected utility of granting the loan or not. Here there are two actions:
    # action = 0 do not grant the loan
    # action = 1 grant the loan
    #
    # Make sure that you extract the length_of_loan from the
    # 2nd attribute of x. Then the return if the loan is paid off to you is amount_of_loan*(1 + rate)^length_of_loan
    # The return if the loan is not paid off is -amount_of_loan.
    def expected_utility(self, x, action):

        loan_amount = x["amount"]
        length_of_loan = x["duration"]
        utility = 0

    # When action is 0 (declined) there is no loss nor profit. 
    # set utility to zero 
    
        if (action == 0):
            utility = 0

    # Action is 1 (approved) the expected utility is 
    # exptected loss and exptected profit
    
        elif (action == 1) :
            probability_loss = (1-predict_proba(x))
            probability_profit = 1 - probability_loss

            utility = probability_profit*loan_amount*(1+rate)^length_of_loan - probability_loss*loan_amount 

        return utility
                     
    # Return the best action. This is normally the one that maximises expected utility.
    # However, you are allowed to deviate from this if you can justify the reason.
    def get_best_action(self, x):
        return np.random.choice(2,1)[0]
