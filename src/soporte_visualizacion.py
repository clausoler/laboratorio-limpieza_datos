def calcular_porcentaje(df, columna_grupo1, columna_grupo2):
    """
    Calcula el porcentaje de empleados con y sin atrición para cada combinación de categorías en las columnas especificadas.

    Parameters:
    -----------
    df : DataFrame
        El DataFrame que contiene los datos de los empleados.
    columna_grupo1 : str
        El nombre de la primera columna de agrupación.
    columna_grupo2 : str
        El nombre de la segunda columna de agrupación.

    Returns:
    --------
    DataFrame
        Un nuevo DataFrame que contiene el porcentaje de empleados con y sin atrición para cada combinación de categorías en las columnas especificadas.
    """
    df_count = df.groupby([columna_grupo1, columna_grupo2])["EmployeeId"].count()
    df_porcentaje = (df_count / df_count.groupby(level=0).transform('sum') * 100).round(2).reset_index()
    return df_porcentaje
