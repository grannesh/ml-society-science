import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas

class NameBanker:
    
    # Fit the model to the data.  You can use any model you like to do
    # the fit, however you should be able to predict all class
    # probabilities
    def fit(self, X, y):
        
        self.data = [X, y]
        self.model = LogisticRegression().fit(X, y)
        
        return

    # set the interest rate
    def set_interest_rate(self, rate):
        self.rate = rate
        return

    # Predict the probability of creditworthiness for a specific person with data x
    def predict_proba(self, x):

        predict_pb = self.model.predict_proba(x)[0][0]
        self.prediction = self.model.predict(x)[0]
    
    # Prediction 1 = good
    # Prediction 2 = bad

        if (self.prediction == 1):
            pred_good = predict_pb
        elif (self.prediction == 2) :
            pred_good = 1 - predict_pb
        else:
            pred_good = 0

        return pred_good
        

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
    # exptected loss and expected profit
    
        elif (action == 1) :
            probability_loss = (1-self.predict_proba(x))
            probability_profit = 1 - probability_loss

            utility = probability_profit*loan_amount*pow(1+self.rate, length_of_loan) - probability_loss*loan_amount 

        return utility
                     
    # Return the best action. This is normally the one that maximises expected utility.
    # However, you are allowed to deviate from this if you can justify the reason.
    def get_best_action(self, x):

        utility_deny = self.expected_utility(x, 0)
        utiliy_approve = self.expected_utility(x, 1)

        if (utiliy_approve >= utility_deny) :
            action = 1
        else:
            action = 0

        return action
