#Teorema Bayes
def cal_bayes(prior_A, prob_B_dado_A, proba_B):
    return (prior_A * prob_B_dado_A) / proba_B

if __name__ == '__main__':

    #Probabilidades en el evento
    prob_cancer = 1 / 100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer

    #Calculo de P(E)-- Probabilidad de tener cancer dado un sintoma
    prob_sintoma = (prob_sintoma_dado_cancer *  prob_cancer) + (prob_no_cancer * prob_sintoma_dado_no_cancer)

    prob_cancer_dado_sintoma = cal_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)

    print(prob_cancer_dado_sintoma)
