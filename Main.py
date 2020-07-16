from Utilities import Utils
from GamesManagement import GamesManager

default_config = {
    "input_path": "C:\\Users\\Juan Carlos Solano\\Documents\\Mine\\The Jackbox Party Pack 5",
    "output_path": "",
    "games_path": "games\\",
    "language": "es",
    "localization_forced_ins": {
        'LANGUAGE_NAME': 'Español',
        'BACK': 'ATRAS',
        'CLOSE': 'CERRAR',
        'ON': 'ENCENDIDO',
        'BACK_TO_PACK': 'ATRAS',
        'GO_TO': 'VE A',
        'PRESS': 'PULSA',
        'EVERYBODYS_IN': 'TODOS LISTOS',
        'UNHIDE': 'MOSTRAR',
        "SETTINGS_VOLUME_DESCRIPTION": "Haz que el juego suene ALTO o BAJO.",
        'VOLUME_DESCRIPTION': 'Haz que el juego suene ALTO o BAJO.',
        'TWITCH_REQUIRED': 'Requerir cuenta en TWITCH',
        "LEADERBOARD": "Tabla de Puntos",
        "BADGE_TITLE_FAMILY_MODE": "APTO PARA TODA LA FAMILIA",
        "QUIT": "SALIR"
    },
    "localization_skip_words": ['twitter', 'spice girls', 'sub-zero', 'none', 'a', 'true', 'false', 'superman', 'frozen'],
    "games": {
        "PartyPack": {
            "path": "games\\PartyPack",
            "translate": False,
            "filenames": {}
        },
        "PatentlyStupid": {
            "path": "games\\PatentlyStupid",
            "translate": False,

            "filenames": {
                'PatentlyStupidGeneDrawing': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['Title'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": None,
                    "v": [1, 2],
                    "s": [],
                    "episodeid": 1230
                },
                'PatentlyStupidShortie': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['decoys', 'prompt'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": None,
                    "v": [1, 2],
                    "s": [3],
                    "episodeid": 1368
                }
            }
        },
        "SplitTheRoom": {
            "path": "games\\SplitTheRoom",
            "translate": True,

            "filenames": {
                'SplitTheRoomFinal': {
                    'single_structure': True,
                    'skip_values': ['true', 'false'],
                    "translate": True,
                    "has_folder": True,
                    "strings": ['answerText', 'scenarioText', 'decoys', 'category', 'questionText'],
                    "dicts": [],
                    "dict_arrays": [['<', '>'], ['[', ']']],
                    "special_characters": None,
                    "episodeid": 1353
                },
                'SplitTheRoomLater': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['answerText', 'scenarioText', 'decoys', 'category', 'questionText'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [3, 5, 7, 8, 9, 10, 12, 14],
                    "s": [15, 16, 17],
                    "episodeid": 1371
                },
                'SplitTheRoomShortie': {
                    "translate": True,
                    "has_folder": True,
                    "strings": ['answerText', 'scenarioText', 'decoys', 'category', 'questionText'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>'], ['[', ']']],
                    "v": [3, 5, 7, 9, 10, 12, 14],
                    "s": [15, 16, 17],
                    "episodeid": 1352
                }
            }
        },
        "SlingShoot": {
            "path": "games\\SlingShoot",
            "translate": True,

            "filenames": {
                'SSDifficulty': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['mission'],
                    "dicts": [],
                    "arrays": ['titles'],
                    "dict_arrays": [],
                    "special_characters": [['<', '>']],
                    "v": [],
                    "s": [],
                    "episodeid": 0
                },
                'SSEnemies': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['title'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>']],
                    "v": [3, 5, 7, 8, 9, 10, 12, 14],
                    "s": [15, 16, 17],
                    "episodeid": 0
                },
                'SSWeapons': {
                    "translate": True,
                    "has_folder": False,
                    "strings": ['title', 'description'],
                    "dicts": [],
                    "dict_arrays": [],
                    "special_characters": [['<', '>']],
                    "v": [],
                    "s": [],
                    "episodeid": 0
                }
            }
        }
    }
}

utils = Utils()
config = utils.create_config(default_config)
# utils.refresh_output(config['input_path'], config['output_path'])

for game in config['games'].keys():
    if config['games'][game]['translate']:
        print('Translating: {0}'.format(game))
        gamesManager = GamesManager(config, utils, game)
    else:
        print('{0} was skipped'.format(game))
