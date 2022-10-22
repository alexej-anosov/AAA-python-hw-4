from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestFitTransform(unittest.TestCase):
    def test_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_cities_unique(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        cities_unique = list(set(cities))
        transformed_cities = fit_transform(cities)
        for city in cities_unique:
            self.assertIn(city, list(map(list, zip(*transformed_cities)))[0])

    def test_colors(self):
        cities = ['green', 'green', 'red']
        exp_transformed_colors = [
            ('green', [0, 1]),
            ('green', [0, 1]),
            ('red', [1, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_colors)

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()
