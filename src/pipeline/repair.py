def repair(df):

    df = df.filter("amount >= 0")
    df = df.filter("customer_id IS NOT NULL")
    df = df.dropDuplicates(["order_id"])

    return df