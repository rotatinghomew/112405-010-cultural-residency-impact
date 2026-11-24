import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELATIONS = [["participation.csv", "application_id", "applications.csv", "application_id"], ["works.csv", "application_id", "applications.csv", "application_id"], ["adoptions.csv", "work_id", "works.csv", "work_id"]]

class MaterialTests(unittest.TestCase):
    def table(self, name):
        with (ROOT / 'data' / name).open(encoding='utf-8', newline='') as handle:
            return list(csv.DictReader(handle))

    def test_tables_have_records_and_stable_headers(self):
        paths = sorted((ROOT / 'data').glob('*.csv'))
        self.assertGreaterEqual(len(paths), 3)
        for path in paths:
            with self.subTest(table=path.name):
                rows = self.table(path.name)
                self.assertTrue(rows)
                self.assertTrue(all(set(row) == set(rows[0]) for row in rows))
                self.assertTrue(all(any(value.strip() for value in row.values()) for row in rows))

    def test_declared_references_resolve(self):
        for child, child_key, parent, parent_key in RELATIONS:
            with self.subTest(relation=(child, child_key, parent, parent_key)):
                child_values = {row[child_key] for row in self.table(child) if row[child_key]}
                parent_values = {row[parent_key] for row in self.table(parent) if row[parent_key]}
                self.assertLessEqual(child_values, parent_values)

    def test_source_rows_are_not_accidentally_duplicated(self):
        for name in (ROOT / 'data').glob('*.csv'):
            rows = self.table(name.name)
            values = [tuple(row.items()) for row in rows]
            self.assertEqual(len(values), len(set(values)), name.name)

if __name__ == '__main__':
    unittest.main()
