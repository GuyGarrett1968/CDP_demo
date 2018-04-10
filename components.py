import pandas as pd

class ComponentsList(object):

    def __init__(self):

        self.df = pd.DataFrame([{'company': 'J&J',   'component': 'socialmedia', 'provider': 'Facebook',  'library': 'api_providerA.py'},
                                {'company': 'J&J',   'component': 'ide',         'provider': 'PyCharm',   'library': 'api_providerB.py'},
                                {'company': 'Roche', 'component': 'news',        'provider': 'NYT',       'library': 'api_NYT.py'}
                               ])

print('[NOTE]: Components list was imported.')


