import pandas as pd
import numpy as np
from datetime import date, datetime
import warnings
warnings.filterwarnings("ignore")


def motivation_data(use_resp):
    use_resp = pd.DataFrame(use_resp)
    use_resp['Month'] = pd.to_datetime(use_resp.date).dt.strftime("%b")
    use_resp['Mot_lev'] = np.where(use_resp.morale > 2, "Motivated", "Not Motivated")
    use_resp = use_resp.drop_duplicates(subset='id', keep='last')
    groups = use_resp.groupby('Month'). \
        mean().reset_index()[['Month', 'morale']].sort_values('Month')
    groups['morale'] = round(groups.morale / 5 * 100)
    groups["Month2"] = pd.to_datetime(groups.Month, format='%b', errors='coerce').dt.month
    groups = groups.sort_values(by='Month2')

    use_resp = use_resp.groupby(['Month', 'Mot_lev']).count().reset_index()[['Month', 'Mot_lev', 'id']]
    motivated = use_resp[use_resp['Mot_lev'] == 'Motivated'][use_resp['Month'] == str(datetime.now().strftime('%b')) ]
    not_motivated = use_resp[use_resp['Mot_lev'] != 'Motivated'][use_resp['Month'] == str(datetime.now().strftime('%b') )]

    return groups,motivated,not_motivated
