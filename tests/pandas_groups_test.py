import pytest  # https://docs.pytest.org
import pandas as pd  # https://pandas.pydata.org/docs/getting_started/overview.html


FILE_PATH = "./tests/titanic.csv"


@pytest.fixture
def df():
    df = pd.read_csv(FILE_PATH)
    return df


def data_frame_value_count_test(df):
    subset_copy: pd.DataFrame = df.iloc[0:10].copy()
    data_grouped = subset_copy.groupby("Sex")

    assert len(data_grouped) == 2
    for name, group in data_grouped:
        assert name in ["male", "female"]
        assert len(group) == 5
        assert group["Age"].min() > 0
