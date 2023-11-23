import pandas as pd
import datetime

# NAO TO SABENDO SE USO LIST COMPREHENSION OU AS INDENTACOES C FOR LOOP PRA DESTRINCHAR OS DADOS DO INPUT E ENTAO
# ADICIONALOS A DATABASE.
def armazenar_dados_exercicios():
    training_date = datetime.date.today()
    # df.loc[training_date, 'TENIS'] = 'flat'

    # linha_a_modificar = df[df['TENIS'] == 'flat'].index
    # df.loc[linha_a_modificar, 'MEIA'] = 'cano alto'
    # df.insert(0, 'DATA TREINO', [training_date])

    user_input = input('Copie e cole os dados do treino. Ex.: excio1 weight1-reps,reps,reps-weight2-reps. excio2...\n') #raw
    #separo infos. na ordem nome exercicio, weight, quan reps sets 1 a x (quan series varia, geralmente 2 <= 5)
    training_session = user_input.split('.')
    weighted_exercises = [exercise.split() for exercise in training_session if '-' in exercise]
    other_types = [exercise.split() for exercise in training_session if '-' not in exercise] #the ones who do not use weights, such as planck, abs, cardio in general, calisthenics.
    all_exercises = weighted_exercises + other_types
    weights = []
    exercise_names = []
    amount_of_sets = []
    reps_total = []
    weight_changes = []
    repss = []
    for exercise in weighted_exercises:
        exercise_name = exercise[0] #This will always be the case (the name of the given exercise will always be in the position index 0, AS LONG AS the user input respects the format 'name_exercise weight1-#reps_serie1,#reps_serie2...'
        exercise_names.append(exercise_name)
        # como eu mostro o exercicio apenas uma vez (uma linha e so), mas se ele tiver tido mudanca de carga, ele tenha mais colunas preenchidas
        # print(f'____________________{exercise_name.upper()}____________________:')
        index_position = 1  # because zero index is always where the name or identified of the exercise will be, as explained before.
        times_weight_changed = len(exercise)
        while index_position < times_weight_changed:

                weight = int(exercise[index_position].split('-')[0])
                series = exercise[index_position].split('-')[1]
                reps = [int(item) for item in (series.split(','))]  # list with integers representing the number of reps performed in a given exercise.
                quan_total_series = len(reps)  # Logically, the lenght of that list above will represent exaclty the amount of sets performed with the given weight.
                # print(f'{weight} kg with {quan_total_series} sets of {reps} reps, in order.')
                index_position += 1

                weights.append(weight)
                amount_of_sets.append(quan_total_series)
                reps_total.append(reps)
                weight_changes.append(times_weight_changed-1)
                print(weight_changes)
                repss.append(reps)
                # df.at[-1, 'QUANT SERIES'] = int(quan_total_series)

        dict_exercicio1 = {'NAME': exercise_names,
                           'WEIGHT (kg)': weights,
                           'REPS': repss,
                           'WEIGHT CHANGES': weight_changes}

        df = pd.DataFrame(dict_exercicio1)

        df.insert(0, 'SESSION DATE', '') # Cria nova coluna chamada SESSION DATE mas deixando-a vazia(senão a data vai ser escrita em todas as linhas e nao precisa.)
        df.loc[-1, 'SESSION DATE'] = training_date #INSERIR a data apenas na última linha da nova coluna.
        print(df)

    # dict_exercicio = {'NAME': exercise_names,
    #                   'WEIGHT': weights,
    #                   'REPS': reps_total
    #                   }
    #
    # df2 = pd.DataFrame(dict_exercicio)
    # df3 = pd.concat([df, df2], ignore_index = True)
    # df3.reset_index()
    # print(df3)


        # if len(exercise) == 2: # ou seja, pra os casos em que so foi utilizada uma weight pra varias series (nao houve o metodo drop ou o de aumento progressivo NO exercicio)
        #     weight = int(exercise[1].split('-')[0])
        #     # print(weight)
        #     series = exercise[1].split('-')[1]
        #     reps = [int(item) for item in (series.split(','))] #list with integers representing the number of reps performed in a given exercise.
        #     quan_total_series = len(reps) #Logically, the lenght of that list above will represent exaclty the amount of sets performed with the given weight.
        #     # print(series, reps)
        #     #end of analysis. (all pieces of information from the raw input are now separed and stored as a variable.)

        # else:
        #     print(f'____________________{exercise_name.upper()}____________________:')
        #     index_position = 1 #because zero index is always where the name or identified of the exercise will be, as explained before.
        #     times_weight_changed = len(exercise)
        #     while index_position < times_weight_changed:
        #         weight = int(exercise[index_position].split('-')[0])
        #         series = exercise[index_position].split('-')[1]
        #         reps = [int(item) for item in (series.split(
        #             ','))]  # list with integers representing the number of reps performed in a given exercise.
        #         quan_total_series = len(reps)  # Logically, the lenght of that list above will represent exaclty the amount of sets performed with the given weight.
        #         print(f'{weight} kg with {quan_total_series} sets of {reps} reps, in order.')
        #         index_position+=1

                # print(e[i])
                # weight_e_series = e[i].split('-')
                # weight = weight_e_series[0]
                # print(weight)
            # reps = [e[1][1].split('-') for rep in e[1][1]]
            # print(f'weight de {weight}kg e feitas as reps {reps}')
        # if len(e) > 2:
        #     print(f'no exercicio {e} vc usou mais de uma weight. ou fez drop ou aumentou.')
        #     print(e[len(e)-1])
        # series_weight1 = e[1].split('-')[1]
        # print(series_weight1)

    # df = pd.DataFrame(weighted_exercises)
    # datas = pd.concat([df, data_treino])
    # print(df)
    # print(datas)


    # for e in treino:
    #     exercicio_realizado = {
    #         'DATA': data_treino,
    #         'CONT EXERCICIOS': len(treino) + 1,
    #         'DIV/GRUPO MUSCULAR': 'variavel a criar',
    #         'NOME': treino[0],
    #         'weight': treino[0],
    #         'REPS': treino[0]
    #     }
    #     df = pd.DataFrame(exercicio_realizado)
        # pd.concat([df, ecio], ignore_index=True, sort=False)

        # pd.concat([df, ecio], ignore_index=True, sort=False)
    # print(df)

    # print(f'TOTAL: {len(weighted_exercises)} exercicios feitos neste treino.')
    # exercicios_contagem = [f'#{numero+1}' for numero in range(len(weighted_exercises))]
    # df['CONT EXERCICIOS'] = exercicios_contagem
    # df['DATA'] = data_treino
    # print(df)
    # for i in range(len(weighted_exercises)):
    #     exercicios_contagem = [f'#{i + 1}']
    #     print(exercicios_contagem)
    #     # df['CONT EXERCICIOS'] = exercicios_contagem
    #
    #     exercise = weighted_exercises[i]
    #     nome = exercise[0]
    #     dados_raw = exercise[1:]
    #     total_reps_por_exercicio = 0
    #     df['NOME'] = exercise[0]
    #     print(df)
    #     for i in range(len(dados_raw)):
    #         dados = dados_raw[i].split('-')
    #         weight_kg = int(dados[0])
    #         # series = int(dados[1])
    #         # reps = series.split(',')
    #         # print(f'{len(reps)} series de {reps} repeticoes com {weight_kg} kg')
    #
    #         for rep in reps:
    #             total_reps_por_exercicio += int(rep)
    #     print(total_reps_por_exercicio)
    #


#
# nomes = ['a', 'b']
# df['nova coluna'] = nomes
# print(df)

        # weight1 = (e[1].split('-'))[0]
        # reps =
        # print(weight1)
        # quan_series = (len(e)-1)

        # try:
        #     nome = e[0]
        #     weight1 = e[1]
        #     reps1 = int(e[2])
        #     reps2 = int(e[3])
        #     print(f'voce fez o excio {nome}, {reps1+reps2} repeticoes com weight {weight1}.')
        # except IndexError:
        #     pass

armazenar_dados_exercicios()