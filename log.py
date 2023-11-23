import pandas as pd
import datetime

def store_training_session():
    training_date = datetime.date.today()
    dict_exercicio = {'DATE': '',
                      'EXERCISE': ''}

    df = pd.DataFrame(columns=dict_exercicio)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df.at[0, 'DATE'] = training_date
    user_input = input('Copie e cole os dados do treino. Ex.: excio1 weight1-reps,reps,reps-weight2-reps. excio2...\n') #raw
    #separo infos. na ordem nome exercicio, weight, quan reps sets 1 a x (quan series varia, geralmente 2 <= 5)
    weighted = [exercise.split() for exercise in user_input.split('.') if '-' in exercise] # separa nome do exercicio de respectivas cargas e series.
    other_types = [exercise.split() for exercise in user_input.split('.') if '-' not in exercise] #the ones who do not use weights, such as planck, abs, cardio in general, calisthenics.
    all_exercises = weighted + other_types
    names = [exercise[0] for exercise in weighted] #This will always be the case (the name of the given exercise will always be in the position index 0, AS LONG AS the user input respects the format 'name_exercise weight1-#reps_serie1,#reps_serie2...'

    for index, exercise in enumerate(weighted):
        name = exercise[0]
        df.loc[index, 'EXERCISE'] = name
        qtdd_cargas_usadas = len(exercise)-1

        for i in (range(qtdd_cargas_usadas)):
            sets_by_weight = exercise[i+1].split('-')
            sets = sets_by_weight[1].split(',')
            names_col_weights = f'WEIGHT #{i+1}'
            df.loc[index, names_col_weights] = sets_by_weight[0]
            # df.loc[index, names_col_sets] = (
            for i in range(len(sets)):
                names_col_sets = f'SETS #{i + 1}'
                df.loc[index, names_col_sets] = sets[i]

            #parei aqui, tentando alocar 1 coluna pra cada serie, tipo 15kg - 9reps 8reps..
            # for n in range(len(sets)):
            #     df.loc[index, n] = sets[n]



#marcus deu a dica do index (q depois adaptei acima):
    # for index, exercise in enumerate(weighted):
    #     sets_by_weight = exercise[1].split('-')
    #     weight = int(sets_by_weight[0])
    #
    #     sets = sets_by_weight[1].split(',')
    #     print(f'qtdd cargas usadas {len(exercise)-1}')
    #     df.loc[index, 'EXERCISE'] = exercise[0]  # nome.
    #     qtdd_cargas_usadas = len(exercise)
    #     for i in (range(qtdd_cargas_usadas)):
    #         names_col_sets = f'SET#{i+1}'
    #         names_col_weights = f'WEIGHT #{i+1}'
    #         # df.loc[index, names_col_weights] = sets_by_weight[i]
    #         # df.loc[index, names_col_sets] = sets_by_weight[i+1]

            # for i in range(len(sets)):
            #     df.loc[index, 'REPS2'] = sets[i]
        print(df)


store_training_session()