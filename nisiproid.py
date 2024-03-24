def write_cleaned(data_, filename):
    """
    Write the cleaned data to a csv file.

    Args:
        data_: The cleaned data.
        filename: The name of the file to write the data to.
    """

    data_.to_csv(filename, index=False)

