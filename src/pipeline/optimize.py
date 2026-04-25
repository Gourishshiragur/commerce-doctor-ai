def optimize(df):

    df = df.repartition(4)
    df.cache()

    return df