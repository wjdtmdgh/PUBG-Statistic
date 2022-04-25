FILE_PATH = 'dataset/PUBG.csv'

column_prefix = {
    "solo": "solo_",
    "duo": "duo_",
    "squad": "squad_"
}

headers = {
    "solo": {
        "per_game_target": [
            'solo_KillDeathRatio',
            'solo_WinRatio',
            'solo_WinTop10Ratio',
            'solo_Top10Ratio',
        ],
        "per_game_columns": [
            'solo_DamagePg',
            'solo_HeadshotKillsPg',
            'solo_HealsPg',
            'solo_KillsPg',
            'solo_MoveDistancePg',
            # 'solo_RevivesPg', # 솔로 매치는 부활 불가능
            'solo_RoadKillsPg',
            'solo_TeamKillsPg',
            'solo_TimeSurvivedPg',
            'solo_Top10sPg'
        ]
    },
    "duo": {
        "per_game_target": [
            'duo_KillDeathRatio',
            'duo_WinRatio',
            'duo_WinTop10Ratio',
            'duo_Top10Ratio',
        ],
        "per_game_columns": [
            'duo_DamagePg',
            'duo_HeadshotKillsPg',
            'duo_HealsPg',
            'duo_KillsPg',
            'duo_MoveDistancePg',
            'duo_RevivesPg',
            'duo_RoadKillsPg',
            'duo_TeamKillsPg',
            'duo_TimeSurvivedPg',
            'duo_Top10sPg'
        ]
    },
    "squad": {
        "per_game_target": [
            'squad_KillDeathRatio',
            'squad_WinRatio',
            'squad_WinTop10Ratio',
            'squad_Top10Ratio',
        ],
        "per_game_columns": [
            'squad_DamagePg',
            'squad_HeadshotKillsPg',
            'squad_HealsPg',
            'squad_KillsPg',
            'squad_MoveDistancePg',
            'squad_RevivesPg',
            'squad_RoadKillsPg',
            'squad_TeamKillsPg',
            'squad_TimeSurvivedPg',
            'squad_Top10sPg'
        ]
    }
}
