import pandas as pd  # https://pandas.pydata.org/docs/getting_started/overview.html


def series_test():
    # https://pandas.pydata.org/docs/reference/series.html
    items = [10, 20, 30]
    labels = ["First Label", "Second Label", "Third Label"]
    my_series = pd.Series(items, labels)

    assert len(my_series) == 3
    assert my_series.index[0] == labels[0]


def data_frame_test():
    titanic_table = pd.read_csv("./tests/titanic.csv")
    assert titanic_table is not None

    cols = titanic_table.columns
    assert cols is not None
    assert len(cols) == 12
    assert "PassengerId" in cols

    top_ten_rows = titanic_table.head(10)
    assert top_ten_rows is not None
    assert len(top_ten_rows) == 10

    bottom_ten_rows = titanic_table.tail(10)
    assert bottom_ten_rows is not None
    assert len(bottom_ten_rows) == 10
