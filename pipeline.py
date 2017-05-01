# -*- coding: utf-8 -*-


def without(columns, with_no):
    return list(set(columns).difference(with_no))



class TestPipe(object):

    def transform(self, test):

        testdf = common_pipe(test)
        return testdf[without(testdf.columns, ['price_doc', 'id'])].values, test.id.values


class TrainPipe(object):

    def transform(self, train):

        traindf = common_pipe(train)
        # Wyciąganie X i y
        X = traindf[without(traindf.columns, ['price_doc', 'id'])].values

        y = traindf.price_doc.values

        return X, y



def common_pipe(data):
    # Wartości yes/no
    yes_no = [col for col in data if any(data[col].isin(['yes', 'no']))]

    # Wartości 0/1
    zero_one = [col for col in data if data[col].unique().tolist() == [0, 1]]

    # Wartości 0, 1 ,2
    zero_two = [col for col in data if data[col].unique().tolist() == [0, 1, 2]]

    # Wartości typu str
    strings = [col for col in data if isinstance(data[col].unique().tolist()[-1], str)]

    strings = without(strings, yes_no)

    # Zamiana wszystkich kategorii na 0 i 1
    for yn in yes_no:
        data[yn] = data[yn].apply(lambda x: 0 if x == 'no' else 1)

    data.product_type = data.product_type.apply(lambda x: 0 if x == "Investment" else 1)

    data.ecology = data.ecology.apply(lambda x: {'no data': 0, 'poor': 1,
                                                   'satisfactory': 2, 'good': 3,
                                                   'excellent': 4}[x])

    # Zamiana time_stamp
    data['year'] = data.timestamp.str[:4]
    data['month'] = data.timestamp.str[5:7].apply(int)

    # Usunięcie kolumny timestamp i fillna
    tcols = without(data.columns, ['timestamp', 'sub_area'])
    data = data[tcols].fillna(0)

    return data