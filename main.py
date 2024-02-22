import time
from nba_api.stats.endpoints import leagueleaders, leaguegamelog, teamgamelog, teamestimatedmetrics, boxscoreadvancedv2, boxscoreadvancedv3, playerestimatedmetrics, leaguedashplayerptshot
import pandas as pd
import git
from datetime import date

def LideresAnotadoresLiga(temporada, tipo_temporada, tipoModo):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = leagueleaders.LeagueLeaders(season=temporada,
                                            season_type_all_star=tipo_temporada,
                                            per_mode48=tipoModo,
                                            )
    df = datos_api.league_leaders.get_data_frame()
    return df

def LeagueGameLog(direction, id_league, temporada, tipo_temporada):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = leaguegamelog.LeagueGameLog(
        direction=direction,
        league_id=id_league,
        season=temporada,
        season_type_all_star=tipo_temporada)
    df_standings = datos_api.league_game_log.get_data_frame()
    return df_standings

def teamGameLog(temporada, tipo_temporada, id_team):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = teamgamelog.TeamGameLog(
        season=temporada,
        season_type_all_star=tipo_temporada,
        team_id=id_team,
        )
    df = datos_api.team_game_log.get_data_frame()
    return df

def TeamEstimatedMetrics(id_league, temporada, tipo_temporada):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = teamestimatedmetrics.TeamEstimatedMetrics(
        league_id=id_league,
        season=temporada,
        season_type=tipo_temporada,
        )
    df = datos_api.team_estimated_metrics.get_data_frame()
    return df

def boxScoreAdvanced2(id_partido):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = boxscoreadvancedv2.BoxScoreAdvancedV2(
        game_id=id_partido
        )
    df = datos_api.player_stats.get_data_frame()
    return df

def boxScoreAdvanced3(id_partido):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = boxscoreadvancedv3.BoxScoreAdvancedV3(
        game_id=id_partido
        )
    df = datos_api.player_stats.get_data_frame()
    return df

def PlayerEstimatedMetrics(id_liga, temporada, tipo_temporada):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = playerestimatedmetrics.PlayerEstimatedMetrics(
        league_id=id_liga,
        season=temporada,
        season_type=tipo_temporada,
        )
    df = datos_api.player_estimated_metrics.get_data_frame()
    return df

def playerShot(id_liga, per_mode, temporada, tipo_temporada):
    # Agregar un retraso de 6 segundos
    time.sleep(6)
    datos_api = leaguedashplayerptshot.LeagueDashPlayerPtShot(
        league_id=id_liga,
        per_mode_simple=per_mode,
        season=temporada,
        season_type_all_star=tipo_temporada,
        )
    df = datos_api.league_dash_ptshots.get_data_frame()
    return df

def subir_dataframe_a_github(dataframe, nombre_archivo, repositorio_local):
  hoy = date.today()
  fecha_formateada = hoy.strftime("%d/%m/%Y")
  """
  Sube un dataframe a un repositorio de Github.

  Args:
    dataframe: El dataframe a subir.
    nombre_archivo: El nombre del archivo a crear en Github.
    repositorio_local: La ruta al repositorio local clonado.
  """

  # Convertir el dataframe a csv
  dataframe.to_csv(f"{repositorio_local}/{nombre_archivo}.csv", index=False)

  # Agregar el archivo al repositorio
  repo = git.Repo(repositorio_local)
  repo.index.add(f"{nombre_archivo}.csv")

  # Hacer un commit y push
  repo.commit(message=f"{fecha_formateada}: Archivo {nombre_archivo}")
  repo.remote().push()

repositorio_local = "C:\\ProyectoGrado2"
#dataframe = LideresAnotadoresLiga('2023-24', 'Regular Season', 'PerGame')
#dataframe2 = LeagueGameLog('DESC', '00', '2023-24', 'Regular Season') #Historial de todos los partidos jugados hasta la fecha
#dataframe3 = teamGameLog(temporada='2023-24', tipo_temporada='Regular Season', id_team='1610612744') #Estadisticas de un equipo de cada partido
#dataframe4 = TeamEstimatedMetrics(id_league='00' ,temporada='2023-24', tipo_temporada='Regular Season') #Metricas avanzadas por equipo GENERAL
#dataframe6 = boxScoreAdvanced3(id_partido='0022300051') #Boxscore de estadisticas avanzadas por jugador o equipo POR PARTIDO
dataframe7 = PlayerEstimatedMetrics(id_liga='00', temporada='2023-24', tipo_temporada='Regular Season') #Boxscore de estadisticas avanzadas por jugador o equipo POR PARTIDO
dataframe8 = playerShot(id_liga='00',per_mode='PerGame', temporada='2023-24', tipo_temporada='Regular Season') #Datos de tiros de jugadores
subir_dataframe_a_github(dataframe7, "lideres_anotadores", repositorio_local)
# Subir dataframe de tiros de jugadores
subir_dataframe_a_github(dataframe8, "tiros_jugadores", repositorio_local)