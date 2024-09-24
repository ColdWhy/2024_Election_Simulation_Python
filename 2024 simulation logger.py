import random
# pip install tabulate
from tabulate import tabulate
import os

last_update = '23-Sep-2024'

simulations = 100000

stat_dem_win_national = 0
stat_rep_win_national = 0
stat_tie_national = 0

log_electoral_votes_dem = []
log_electoral_votes_rep = []

stat_dem_win_AZ = 0
stat_rep_win_AZ = 0

stat_dem_win_NV = 0
stat_rep_win_NV = 0

stat_dem_win_GA = 0
stat_rep_win_GA = 0

stat_dem_win_NC = 0
stat_rep_win_NC = 0

stat_dem_win_PA = 0
stat_rep_win_PA = 0

stat_dem_win_WI = 0
stat_rep_win_WI = 0

stat_dem_win_MI = 0
stat_rep_win_MI = 0

# State_dem_chance = % of dem polling * 10
# State_rep_chance = % of rep polling * 10
# State = [Dem chance, Rep chance, Electoral votes]

AZ_dem_chance = 468
AZ_rep_chance = 483
AZ = [range(1, (AZ_dem_chance + 1)), range((AZ_dem_chance + 1), (AZ_dem_chance + AZ_rep_chance + 1)), 11]

NV_dem_chance = 484
NV_rep_chance = 472
NV = [range(1, (NV_dem_chance + 1)), range((NV_dem_chance + 1), (NV_dem_chance + NV_rep_chance + 1)), 6]

GA_dem_chance = 470
GA_rep_chance = 483
GA = [range(1, (GA_dem_chance + 1)), range((GA_dem_chance + 1), (GA_dem_chance + GA_rep_chance + 1)), 16]

NC_dem_chance = 476
NC_rep_chance = 480
NC = [range(1, (NC_dem_chance + 1)), range((NC_dem_chance + 1), (NC_dem_chance + NC_rep_chance + 1)), 16]

PA_dem_chance = 489
PA_rep_chance = 474
PA = [range(1, (PA_dem_chance + 1)), range((PA_dem_chance + 1), (PA_dem_chance + PA_rep_chance + 1)), 19]

WI_dem_chance = 497
WI_rep_chance = 475
WI = [range(1, (WI_dem_chance + 1)), range((WI_dem_chance + 1), (WI_dem_chance + WI_rep_chance + 1)), 10]
# WI = [range(1, 1001), range(0), 10]

MI_dem_chance = 492
MI_rep_chance = 468
MI = [range(1, (MI_dem_chance + 1)), range((MI_dem_chance + 1), (MI_dem_chance + MI_rep_chance + 1)), 15]
# MI = [range(1, 1001), range(0), 15]

# Polling source: Silver Bulletin

# ================================================================================================
# ================================================================================================
# ================================================================================================

def tossUp():
    tossup = random.randint(1, 2)
    return tossup


print('')
print(f'Simulating elections...')
for _ in range(simulations):
    dem_electoral_votes = 226
    rep_electoral_votes = 219

    state_election = random.randint(1, 1000)
    if state_election in AZ[0]:
        outcome = 1
    elif state_election in AZ[1]:
        outcome = 2
    else:
        outcome = tossUp()
    if outcome == 1:
        dem_electoral_votes += AZ[2]
        stat_dem_win_AZ += 1
    elif outcome == 2:
        rep_electoral_votes += AZ[2]
        stat_rep_win_AZ += 1

    state_election = random.randint(1, 1000)
    if state_election in NV[0]:
        outcome = 1
    elif state_election in NV[1]:
        outcome = 2
    else:
        outcome = tossUp()
    if outcome == 1:
        dem_electoral_votes += NV[2]
        stat_dem_win_NV += 1
    elif outcome == 2:
        rep_electoral_votes += NV[2]
        stat_rep_win_NV += 1

    state_election = random.randint(1, 1000)
    if state_election in GA[0]:
        outcome = 1
    elif state_election in GA[1]:
        outcome = 2
    else:
        outcome = tossUp()
    if outcome == 1:
        dem_electoral_votes += GA[2]
        stat_dem_win_GA += 1
    elif outcome == 2:
        rep_electoral_votes += GA[2]
        stat_rep_win_GA += 1

    state_election = random.randint(1, 1000)
    if state_election in NC[0]:
        outcome = 1
    elif state_election in NC[1]:
        outcome = 2
    else:
        outcome = tossUp()
    if outcome == 1:
        dem_electoral_votes += NC[2]
        stat_dem_win_NC += 1
    elif outcome == 2:
        rep_electoral_votes += NC[2]
        stat_rep_win_NC += 1

    state_election = random.randint(1, 1000)
    if state_election in PA[0]:
        outcome = 1
    elif state_election in PA[1]:
        outcome = 2
    else:
        outcome = tossUp()
    if outcome == 1:
        dem_electoral_votes += PA[2]
        stat_dem_win_PA += 1
    elif outcome == 2:
        rep_electoral_votes += PA[2]
        stat_rep_win_PA += 1

    state_election = random.randint(1, 1000)
    if state_election in WI[0]:
        outcome = 1
    elif state_election in WI[1]:
        outcome = 2
    else:
        outcome = tossUp()
    if outcome == 1:
        dem_electoral_votes += WI[2]
        stat_dem_win_WI += 1
    elif outcome == 2:
        rep_electoral_votes += WI[2]
        stat_rep_win_WI += 1

    state_election = random.randint(1, 1000)
    if state_election in MI[0]:
        outcome = 1
    elif state_election in MI[1]:
        outcome = 2
    else:
        outcome = tossUp()
    if outcome == 1:
        dem_electoral_votes += MI[2]
        stat_dem_win_MI += 1
    elif outcome == 2:
        rep_electoral_votes += MI[2]
        stat_rep_win_MI += 1

    if dem_electoral_votes >= 270:
        stat_dem_win_national += 1
    elif rep_electoral_votes >= 270:
        stat_rep_win_national += 1
    else:
        stat_tie_national += 1

    log_electoral_votes_dem.append(dem_electoral_votes)
    log_electoral_votes_rep.append(rep_electoral_votes)

# ================================================================================================
# ================================================================================================
# ================================================================================================


dem_win_percent = stat_dem_win_national / simulations * 100
rep_win_percent = stat_rep_win_national / simulations * 100
tie_percent = stat_tie_national / simulations * 100

file_name = f'{last_update} simulation.txt'
file_path = os.path.join(os.getcwd(), file_name)

with open(file_path, 'w') as file:
    file.write(f'{simulations} elections simulated\n')
    file.write('\n')
    file.write(f'Democrats win the election in {dem_win_percent:.2f}% of the simulations ({stat_dem_win_national})\n')
    file.write(f'Republicans win the election in {rep_win_percent:.2f}% of the simulations ({stat_rep_win_national})\n')
    file.write(f'The electoral college ties in {tie_percent:.2f}% of the simulations ({stat_tie_national})\n')
    file.write('\n')

    file.write('Arizona:\n')
    file.write(f'Dem: {stat_dem_win_AZ} victories\n')
    file.write(f'Rep: {stat_rep_win_AZ} victories\n')
    file.write(f'Polls D: {AZ_dem_chance / 10}%, R: {AZ_rep_chance / 10}%\n')
    file.write('\n')

    file.write('Nevada:\n')
    file.write(f'Dem: {stat_dem_win_NV} victories\n')
    file.write(f'Rep: {stat_rep_win_NV} victories\n')
    file.write(f'Polls D: {NV_dem_chance / 10}%, R: {NV_rep_chance / 10}%\n')
    file.write('\n')

    file.write('Georgia:\n')
    file.write(f'Dem: {stat_dem_win_GA} victories\n')
    file.write(f'Rep: {stat_rep_win_GA} victories\n')
    file.write(f'Polls D: {GA_dem_chance / 10}%, R: {GA_rep_chance / 10}%\n')
    file.write('\n')

    file.write('North Carolina:\n')
    file.write(f'Dem: {stat_dem_win_NC} victories\n')
    file.write(f'Rep: {stat_rep_win_NC} victories\n')
    file.write(f'Polls D: {NC_dem_chance / 10}%, R: {NC_rep_chance / 10}%\n')
    file.write('\n')

    file.write('Pennsylvania:\n')
    file.write(f'Dem: {stat_dem_win_PA} victories\n')
    file.write(f'Rep: {stat_rep_win_PA} victories\n')
    file.write(f'Polls D: {PA_dem_chance / 10}%, R: {PA_rep_chance / 10}%\n')
    file.write('\n')

    file.write('Wisconsin:\n')
    file.write(f'Dem: {stat_dem_win_WI} victories\n')
    file.write(f'Rep: {stat_rep_win_WI} victories\n')
    file.write(f'Polls D: {WI_dem_chance / 10}%, R: {WI_rep_chance / 10}%\n')
    file.write('\n')

    file.write('Michigan:\n')
    file.write(f'Dem: {stat_dem_win_MI} victories\n')
    file.write(f'Rep: {stat_rep_win_MI} victories\n')
    file.write(f'Polls D: {MI_dem_chance / 10}%, R: {MI_rep_chance / 10}%\n')
    file.write('\n')

    table_data_dem = []
    table_data_rep = []
    bar_sizer = 1
    while True:
        if simulations / bar_sizer <= 1000:
            break
        else:
            bar_sizer *= 10

    for x in sorted(set(log_electoral_votes_dem)):
        count_votes_dems = log_electoral_votes_dem.count(x)
        count_votes_dems_percent = count_votes_dems / simulations * 100
        bar = ''
        bar += '|' * int(count_votes_dems / bar_sizer)
        table_data_dem.append([x, count_votes_dems, f'{count_votes_dems_percent:.2f}%', bar])

    for x in sorted(set(log_electoral_votes_rep)):
        count_votes_reps = log_electoral_votes_rep.count(x)
        count_votes_reps_percent = count_votes_reps / simulations * 100
        bar = ''
        bar += '|' * int(count_votes_reps / bar_sizer)
        table_data_rep.append([x, count_votes_reps, f'{count_votes_reps_percent:.2f}%', bar])

    file.write('How many times Harris gets each electoral college result:\n')
    file.write(tabulate(table_data_dem, headers=['Electoral Votes', 'Count', 'Percentage', ''], tablefmt='grid'))
    file.write('\n')
    file.write('\n')
    file.write('How many times Trump gets each electoral college result:\n')
    file.write(tabulate(table_data_rep, headers=['Electoral Votes', 'Count', 'Percentage', ''], tablefmt='grid'))
    file.write('\n')

    file.write('Polls source: Silver Bulletin\n')
    file.write(f'Last update: {last_update}\n')