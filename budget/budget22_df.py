import json

import pandas


def get_df(filename):
    df = pandas.read_csv(f'./data/acc/{filename}', header=None)
    return df


def read_csv_files():
    with open('./data/acc/data22.json') as json_file:
        data = json.load(json_file)
        return data


def parse_eur(eur):
    eur = eur.replace('€', '')
    eur_n = float(eur)
    return eur_n


def format_price(x: str):
    return x.replace(',', '.').replace('−', '-')


def wrangle_data(df: pandas.DataFrame):
    df[0] = df[0].fillna(method='ffill')
    df[2] = df[2].apply(format_price).map(parse_eur)

    return df


def get_dfs_combined():
    csv_contents = read_csv_files()

    dfs = [get_df(csv_content) for csv_content in csv_contents]

    df = pandas.concat(dfs)
    df = wrangle_data(df)

    return df
