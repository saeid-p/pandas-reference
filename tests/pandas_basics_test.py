import pytest  # https://docs.pytest.org
import pandas as pd  # https://pandas.pydata.org/docs/getting_started/overview.html


def series_test():
    # https://pandas.pydata.org/docs/reference/series.html
    items = [10, 20, 30]
    labels = ["First Label", "Second Label", "Third Label"]
    my_series = pd.Series(items, labels)

    assert len(my_series) == 3
    assert my_series.index[0] == labels[0]


FILE_PATH = "./tests/titanic.csv"


def data_frame_test():
    columns = ["PassengerId", "Name", "Age"]
    titanic_df = pd.read_csv(FILE_PATH, index_col=columns[0], usecols=columns)
    assert titanic_df is not None

    cols = titanic_df.columns
    assert cols is not None
    assert len(cols) == 2
    assert "PassengerId" not in cols
    assert "Name" in cols

    top_ten_rows = titanic_df.head(10)
    assert top_ten_rows is not None
    assert len(top_ten_rows) == 10

    bottom_ten_rows = titanic_df.tail(10)
    assert bottom_ten_rows is not None
    assert len(bottom_ten_rows) == 10

    age_with_id_df = titanic_df[["Age"]]
    age_series = age_with_id_df["Age"]
    age_array = pd.unique(age_series)
    assert len(age_array) == 89


@pytest.fixture
def df():
    df = pd.read_csv(FILE_PATH)
    return df


def data_frame_value_count_test(df):
    gender_counts = df["Sex"].value_counts()
    assert gender_counts["male"] == 577
    assert gender_counts["female"] == 314

    male_passengers = df["Sex"] == "male"
    male_passengers_counts = male_passengers.value_counts()
    assert male_passengers_counts[True] == 577
    assert male_passengers_counts[False] == 314


def data_frame_data_selection_test(df):
    # Finds by row range based on a query and column label.
    row_range = df["PassengerId"] == 10
    col_name = "Name"

    specific_row_by_loc = df.loc[row_range, col_name]

    assert len(specific_row_by_loc) == 1
    assert specific_row_by_loc.item() == "Nasser, Mrs. Nicholas (Adele Achem)"

    # Finds by row range and col indices.
    col_indexes = [0, 3, 5]
    specific_row_by_position = df.iloc[0:10, col_indexes]

    assert len(specific_row_by_position) == 10

    # Finds by row index and col name.
    specific_row_by_at = df.at[10, col_name]
    assert specific_row_by_at == "Sandstrom, Miss. Marguerite Rut"


def data_frame_data_process_test(df):
    ages = df["Age"]
    ticket_fares = df["Fare"]

    multiplication: pd.Series = ages * ticket_fares
    assert multiplication is not None
    assert multiplication.at[0] == 159.5

    assert multiplication.max() > 0  # Max value in series.
    # Returns the row index of the max value.
    assert multiplication.idxmax() > 0
    assert multiplication.min() == 0  # Min value in series.
