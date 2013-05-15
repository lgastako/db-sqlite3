import db
import db_sqlite3


class TestSqlite3x:

    def test_from_url(self):
        mem_db = db.from_url("sqlite3:///:memory:")
        mem_db.do("CREATE TABLE foo_tfu (bar)")
        sql = "SELECT COUNT(*) AS n FROM foo_tfu"
        assert mem_db.item(sql).n == 0

    def test_paramstyle_set_properly(self):
        mem_db = db.from_url("sqlite3:///:memory:")
        mem_db.do("CREATE TABLE foo_psp (bar)")
        sql = "SELECT COUNT(*) AS n FROM foo_psp WHERE bar = %X"
        assert mem_db.item(sql, "baz").n == 0
