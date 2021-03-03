from scipy import stats

def correl_spearman(matriz1, matriz2):
    try:    
        coef, p = stats.spearmanr(matriz1, matriz2)
        print("Coeficiente de correlação: " + str(coef))
        print("Valor p: " + str(p))
    except:
        print("Erro ao calcular correlação de Spearman.")

    return coef