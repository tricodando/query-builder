import sqlite3
import os

class Build:
    def __init__(self, table):
        self.table = table
        self.con = sqlite3.connect(os.path.join("data.db"))
        self.cur = self.con.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id TEXT,
                name TEXT,
                password TEXT
            )
        """)

    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
        
    def _execute(self, query, values=[]):
        self.cur.row_factory = self._dict_factory
        self.cur.execute(query, list(values))
        rows = self.cur.fetchall()
        self.con.commit()
        return rows
    
    def _insert(self, values: dict):
        # INSERT INTO tableName (field1, field2, field3) VALUES (?,?,?)
        fields = ','.join(values)
        binds = ','.join(len(values)*['?'])
        query = f'INSERT INTO {self.table} ({fields}) VALUES ({binds})'
        self._execute(query, values.values())
    
    def _select(self, fields='*', where=''):
        # SELECT * FROM tableName WHERE condition
        where = f'WHERE {where}' if where != '' else ''
        query = f'SELECT {fields} FROM {self.table} {where}'
        return self._execute(query)
    
    def _update(self, where, values: dict):
        # UPDATE tableName SET field1=?, field2=? WHERE condition
        fields = '=?,'.join(values)
        where = f'WHERE {where}' if where != '' else ''
        query = f'UPDATE {self.table} SET {fields}=? {where}'
        self._execute(query, values.values())

    def _delete(self, where=''):
        # DELETE FROM tableName WHERE condition
        where = f'WHERE {where}' if where != '' else ''
        query = f'DELETE FROM {self.table} {where}'
        self._execute(query)

    def findMany(self):
        return self._select()

    def findUnique(self, key):
        return self._select(where=f"id='{key}'")

    def create(self, obj):
        self._insert(obj)

    def update(self, obj):
        self._update(f"id='{obj['id']}'", obj)
    
    def delete(self, id):
        self._delete(f"id='{id}'")